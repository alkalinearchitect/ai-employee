"""NOHUMA Auditor — demo web app. Dark chrome UI, paste a company URL, get a plain-English
audit: what they do, their bottleneck, and how a managed AI employee helps.
Real scraped signals + clearly-labelled assessment. Run: python3 app.py"""

from flask import Flask, render_template_string, request
from assessor import assess

app = Flask(__name__)

PAGE = """
<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NOHUMA Auditor</title>
<style>
:root{--bg:#0a0a0c;--surface:#131318;--border:#232329;--text:#f6f6f8;--text-2:#c4c6cf;--text-3:#9a9ca6;--steel:#aeb4c0;--green:#3ad389}
*{box-sizing:border-box}html,body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:60rem;margin:0 auto;padding:0 20px}
header{display:flex;align-items:center;justify-content:space-between;padding:22px 0;border-bottom:1px solid var(--border)}
.brand{font-weight:600;font-size:1.05rem;letter-spacing:-.01em}
.lm{background:linear-gradient(100deg,#8b909c,#eef1f6 16%,#6b707b 30%,#f6f8fb 47%,#9aa0ad 60%,#fff 73%,#aab0bc 84%,#e9ebf0);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;font-weight:700}
main{padding:48px 0 96px}
h1{font-weight:300;font-size:clamp(2.1rem,5vw,3.4rem);line-height:1.05;letter-spacing:-.03em;margin:0 0 10px;max-width:18ch}
.sub{color:var(--text-2);max-width:52ch;margin:0 0 34px}
form{display:flex;gap:10px;max-width:42rem;flex-wrap:wrap}
input{flex:1;min-width:240px;background:var(--surface);border:1px solid var(--border-2,#34343d);border-radius:980px;color:var(--text);padding:14px 20px;font-size:1rem;outline:none}
input:focus{border-color:var(--steel)}
button{background:linear-gradient(180deg,#f6f8fb,#cfd3dc);color:#0a0a0c;border:none;border-radius:980px;font-weight:600;font-size:.98rem;padding:14px 26px;cursor:pointer}
button:hover{transform:translateY(-2px)}
.err{color:#ff8a8a;margin-top:16px;font-size:.95rem}
.card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:30px;margin-top:38px}
.tag{display:inline-block;font-family:ui-monospace,monospace;font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--steel);border:1px solid var(--border);border-radius:980px;padding:5px 12px;margin-bottom:18px}
.kicker{color:var(--text-3);font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;margin:26px 0 8px}
.big{font-size:clamp(1.3rem,3vw,1.9rem);font-weight:300;letter-spacing:-.02em;line-height:1.2;margin:0 0 6px}
.facts{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 4px}
.fact{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:10px 14px;font-size:.9rem;color:var(--text-2)}
.fact b{color:var(--text);font-weight:600}
.help li{margin:0 0 12px;color:var(--text-2);line-height:1.5}
.help li b{color:var(--text)}
.assess{font-size:.78rem;color:var(--text-3);margin-top:22px;border-top:1px solid var(--border);padding-top:14px}
.und{color:var(--green);font-weight:600}
footer{color:var(--text-3);font-size:.8rem;border-top:1px solid var(--border);padding:26px 0 60px;text-align:center}
</style></head><body>
<header class="wrap"><div class="brand"><span class="lm">NOHUMA</span> &middot; Auditor</div></header>
<main class="wrap">
  <h1>See where a business is losing time.</h1>
  <p class="sub">Paste any company website. We read what they actually do, spot the manual work an AI employee can own, and show how NOHUMA would run it. Real signals from their live site.</p>
  <form method="post">
    <input name="url" placeholder="https://example.com" value="{{url}}" required>
    <button type="submit">Run audit</button>
  </form>
  {% if err %}<div class="err">{{err}}</div>{% endif %}
  {% if r %}
  <div class="card">
    <span class="tag">{{r.industry}}{% if r.underserved %} &middot; <span class="und">under-served by AI</span>{% endif %}</span>
    <div class="kicker">What they do</div>
    <p class="big">{{r.title}}</p>
    <div class="facts">
      <div class="fact">Site: <b>{{r.domain}}</b></div>
      <div class="fact">Pages: <b>{{r.pages}}</b></div>
      <div class="fact">Stack: <b>{{', '.join(r.stack)}}</b></div>
      <div class="fact">Manual tells found: <b>{{r.manual_tells|length}}</b></div>
    </div>
    <div class="kicker">Their bottleneck</div>
    <p class="big" style="font-weight:400">{{r.bottleneck}}</p>
    <div class="kicker">How a NOHUMA agent helps</div>
    <ul class="help">{% for h in r.how_we_help %}<li>{{h}}</li>{% endfor %}</ul>
    <p class="assess">Assessment: the industry, tells and numbers above are read live from the site. The bottleneck and "how we help" wording is our reasoned assessment from those signals — not a claim about the company. {{r.stack_note}}</p>
  </div>
  {% endif %}
  <p class="sub" style="margin-top:40px;color:var(--text-3);font-size:.92rem">Try an industry that hasn't adopted AI yet — a dentist, solicitor, accountant, estate agent, garage, or care provider.</p>
</main>
<footer class="wrap">NOHUMA is a managed Non-Human Intelligence by Human Architect &middot; demo only, no data stored</footer>
</body></html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    r, err, url = None, None, ""
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url.startswith("http"):
            url = "https://" + url
        try:
            r = assess(url)
        except Exception as e:
            err = f"Could not analyse that site: {type(e).__name__}"
        if r and not r.get("ok"):
            err = r.get("reason", "analysis failed")
            r = None
    return render_template_string(PAGE, r=r, err=err, url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=False)
