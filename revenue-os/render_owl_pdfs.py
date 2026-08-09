#!/usr/bin/env python3
"""Render Owl PDFs via chrome print-to-pdf (pdf-dossier-builder pipeline).
Aesthetic: black canvas, white Helvetica, violet #8b5cf6 accent, massive whitespace.
Usage: python3 render_owl_pdf.py <name>
  name = pricing | objection | onboarding
Reads /root/owl-<name>... source md, but we inline the HTML per deck here for control.
"""
import subprocess, os, sys

OUT = "/root/ai-employee/revenue-os/out"
os.makedirs(OUT, exist_ok=True)
CHROME = "/usr/bin/google-chrome"

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
@page { size: 9in 12in; margin: 0; }
html, body { background: #000; }
.page { width: 9in; height: 12in; background: #000; page-break-after: always;
  display: flex; flex-direction: column; justify-content: center;
  padding: 95px 90px; }
.page:last-child { page-break-after: auto; }
.kicker { color: #8b5cf6; letter-spacing: .22em; text-transform: uppercase;
  font-size: 26px; font-weight: 700; margin-bottom: 44px; }
.headline { font-family: Helvetica, Arial, sans-serif; font-weight: 700; font-size: 76px; line-height: 1.06; letter-spacing: -.01em;
  margin-bottom: 40px; max-width: 18ch; }
.body { font-size: 34px; line-height: 1.6; color: #dcdcdc; max-width: 38ch; }
.rule { width: 90px; height: 6px; background: #8b5cf6; margin: 50px 0; border-radius: 3px; }
.foot { margin-top: 56px; font-size: 22px; color: #9a9aa2; letter-spacing: .04em; }
.cover-title { font-family: Helvetica, Arial, sans-serif; font-weight: 700; font-size: 96px; line-height: 1.02; letter-spacing: -.02em;
  margin-bottom: 38px; max-width: 16ch; }
.cover-sub { font-size: 38px; line-height: 1.5; color: #dcdcdc; max-width: 36ch; }
.num { color: #8b5cf6; font-weight: 700; font-size: 26px; letter-spacing: .1em; margin-bottom: 28px; }
"""

def render(html, name):
    html_path = os.path.join(OUT, f"_{name}_src.html")
    pdf_path = os.path.join(OUT, f"owl-{name}.pdf")
    open(html_path, "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html}</body></html>")
    cmd = [CHROME, "--headless", "--no-sandbox", "--disable-gpu",
           "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", f"file://{html_path}"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise SystemExit("chrome failed: " + r.stderr[-400:])
    if not os.path.exists(pdf_path):
        raise SystemExit("no pdf")
    return pdf_path

# ── DECKS ──────────────────────────────────────────────
PRICING = """
<div class="page">
  <div class="kicker">Owl · Non-Human Intelligence</div>
  <div class="cover-title">One price. One employee that isn't human.</div>
  <div class="cover-sub">A managed AI employee that owns one recurring workflow in your business. £5,000 a month, everything included. Live in 48 hours.</div>
  <div class="rule"></div>
  <div class="foot">Operated by Human Architect · beacons.ai/humanarchitect</div>
</div>
<div class="page">
  <div class="kicker">Pricing</div>
  <div class="headline">£5,000 a month. Everything included.</div>
  <div class="body">Build, hosting, onboarding, and daily operation sit in one flat fee. No setup charge, no per-seat pricing, no usage add-ons waiting to surprise you at month end.</div>
</div>
<div class="page">
  <div class="kicker">What's included</div>
  <div class="headline">It shows up with its own desk.</div>
  <div class="body">Its own computer, its own email, a live Telegram line, and a seat in your Slack or Telegram. One brain plus four specialists — outbound, sales follow-up, content, support — backed by real tools, simple billing, a memory that files one fact in one home, and constant health checks.</div>
</div>
<div class="page">
  <div class="kicker">Guarantee · 01</div>
  <div class="headline">Live in 48 hours, or your first month is free.</div>
  <div class="body">From the scoping call, your agent is built and running within two days. If it isn't, we refund the first month. No debate.</div>
</div>
<div class="page">
  <div class="kicker">Guarantee · 02</div>
  <div class="headline">If it hasn't paid for itself by day 30, you don't pay.</div>
  <div class="body">We measure the human hours it has returned. If it hasn't saved more than £5,000 in human time by day 30, the first month is refunded. The bar is your invoice, not our opinion.</div>
</div>
<div class="page">
  <div class="kicker">White-label</div>
  <div class="headline">Put your name on it. Make it a product, not a cost.</div>
  <div class="body">White-label is single-tier and asks no recruitment of you. It becomes a revenue line you sell to your own clients — billed under your brand, run by us.</div>
</div>
<div class="page">
  <div class="kicker">Terms</div>
  <div class="headline">Month to month. Your data leaves only when you do.</div>
  <div class="body">Cancel any time, no contract, no exit fee. Your agent runs on an isolated client VPS with scoped access — your data stays yours and travels with you on exit.</div>
</div>
<div class="page">
  <div class="kicker">Start</div>
  <div class="headline">Book a scoping call.</div>
  <div class="body">Book at beacons.ai/humanarchitect. Forty-eight hours later, your first non-human employee is at work.</div>
  <div class="foot">Operated by Human Architect</div>
</div>
"""

OBJECTION = """
<div class="page">
  <div class="kicker">Owl · Non-Human Intelligence</div>
  <div class="cover-title">Seven objections stand between interested and booked.</div>
  <div class="cover-sub">Owl owns one recurring workflow in your business. £5,000 a month. Everything included. Live in 48 hours. Here is the answer to each objection.</div>
  <div class="rule"></div>
  <div class="foot">Operated by Human Architect · beacons.ai/humanarchitect</div>
</div>
<div class="page">
  <div class="num">01</div>
  <div class="headline">Hiring is the expensive option.</div>
  <div class="body">A junior's salary is the smallest number on the bill. Add tax, software, training, and the months before they are useful. Owl is one flat £5,000 a month, live in 48 hours, owning one workflow from day one. You are not hiring. You are buying a result that pays for itself — or we refund the month.</div>
</div>
<div class="page">
  <div class="num">02</div>
  <div class="headline">It replaces the work, not the people.</div>
  <div class="body">Owl takes the recurring task your best person dreads — the quotes, the follow-ups, the admin that eats the day. Your team moves up to the work only humans should do. The Non-Human Intelligence handles the part that was always a tax on their time.</div>
</div>
<div class="page">
  <div class="num">03</div>
  <div class="headline">Your data never leaves its own box.</div>
  <div class="body">Owl runs on an isolated VPS with scoped access to only what it needs — nothing else. It is portable, so you take it with you. We cannot see what you have not permitted, and neither can anyone else.</div>
</div>
<div class="page">
  <div class="num">04</div>
  <div class="headline">If it breaks, you don't pay.</div>
  <div class="body">Owl is live in 48 hours or your first month is refunded. At day 30, if it has not saved you more than £5,000, we refund that month too. A Non-Human Intelligence that costs you money is not doing its job — so we don't charge you for it.</div>
</div>
<div class="page">
  <div class="num">05</div>
  <div class="headline">ChatGPT answers. Owl does.</div>
  <div class="body">ChatGPT waits for your team to type the right prompt and check the output. Owl owns one workflow end to end — it acts, it follows up, it closes the loop while you sleep. One is a tool on your desk. The other is a colleague that works.</div>
</div>
<div class="page">
  <div class="num">06</div>
  <div class="headline">Fast is the point, not the risk.</div>
  <div class="body">The 8-part stack is already built — one brain and four specialists, configured, not coded from zero. We deploy it to your isolated VPS and hand you a running workflow within 48 hours. If we miss, the first month is free. Speed is what you are paying for.</div>
</div>
<div class="page">
  <div class="num">07</div>
  <div class="headline">Leave anytime. Take it with you.</div>
  <div class="body">Cancel whenever you want — no contract, no notice period, no exit fee. Your Owl runs on a portable VPS, so the work and the setup travel with you. We keep you by being good, not by holding you.</div>
</div>
<div class="page">
  <div class="kicker">Close</div>
  <div class="headline">The first responder wins.</div>
  <div class="body">Harvard Business Review found buyers are 7x more likely to qualify a vendor they reached within the hour. And 78% buy from the first to respond. We answer fast because the data says so. Book the call. Live in 48 hours. beacons.ai/humanarchitect</div>
</div>
"""

ONBOARDING = """
<div class="page">
  <div class="kicker">Owl · Non-Human Intelligence</div>
  <div class="cover-title">What to expect after you say yes.</div>
  <div class="cover-sub">A clear timeline, hard guarantees, and no surprises. This is how a managed AI employee goes from signed to working in 48 hours — and what happens next.</div>
  <div class="rule"></div>
  <div class="foot">Operated by Human Architect · beacons.ai/humanarchitect</div>
</div>
<div class="page">
  <div class="num">01</div>
  <div class="headline">We learn your business before we touch a tool.</div>
  <div class="body">The discovery call is a conversation, not a pitch. You tell us the one recurring workflow you want off your plate. We ask, we listen, and we decide together whether a single Non-Human Intelligence can own it cleanly. Like hiring a real employee: we understand the role before we fill it.</div>
</div>
<div class="page">
  <div class="num">02</div>
  <div class="headline">Live in forty-eight hours, or your first month is free.</div>
  <div class="body">From the moment the call ends, Owl builds. One brain and four specialists stand up the workflow, wire the real tools, and stage everything on an isolated VPS with access scoped only to what the job needs. If Owl is not running inside 48 hours, the first month is refunded.</div>
</div>
<div class="page">
  <div class="num">03</div>
  <div class="headline">Your new hire arrives where your team already talks.</div>
  <div class="body">Owl onboards into your Slack or Telegram — the place your people already work. You get a dedicated messaging line, a real email, and a presence your team can see and message. No new portal. No dashboard to babysit.</div>
</div>
<div class="page">
  <div class="num">04</div>
  <div class="headline">Thirty days in, the math has to be obvious.</div>
  <div class="body">Good looks like this: the workflow runs without you thinking about it, and your people stop doing the part they resented. On day 30 we sit down and count what Owl saved. If it is not more than £5,000 in real terms, we refund the month. No argument.</div>
</div>
<div class="page">
  <div class="num">05</div>
  <div class="headline">We watch it so you don't have to.</div>
  <div class="body">Owl runs constant health checks across the whole stack — its own computer, its email, its messaging line, the tools it uses, and the memory it keeps. If something breaks, we know before you do, and we fix it. The monitoring is part of the flat £5,000. Never an add-on.</div>
</div>
<div class="page">
  <div class="num">06</div>
  <div class="headline">When one workflow is owned, the next one is easy.</div>
  <div class="body">Owl is built to own a single recurring workflow and own it completely. Once yours runs without you, we stand up the next job you want gone with the same 48-hour build, the same handover, and the same guarantees. No new contract to decode.</div>
</div>
<div class="page">
  <div class="num">07</div>
  <div class="headline">Put your name on it.</div>
  <div class="body">Owl runs white-label, single tier. Your clients see your brand, not ours — the Non-Human Intelligence works under your name. It is one clean option, available whenever you are ready, with nothing else to buy.</div>
  <div class="foot">Flat £5,000/month. Everything included. Cancel anytime. Operated by Human Architect.</div>
</div>
"""

AWARENESS = """
<div class="page">
  <div class="kicker">Owl · Non-Human Intelligence</div>
  <div class="cover-title">The employee who never sleeps.</div>
  <div class="cover-sub">A new kind of worker owns your recurring tasks. It does not take holiday. It does not resign. It replies in the first hour — every time.</div>
  <div class="rule"></div>
  <div class="foot">Operated by Human Architect · beacons.ai/humanarchitect</div>
</div>
<div class="page">
  <div class="kicker">The cost of slow</div>
  <div class="headline">The first to reply wins the work.</div>
  <div class="body">Harvard Business Review found buyers are seven times more likely to qualify a vendor they reached within the hour. And seventy-eight percent buy from the first to respond. Slow is not a style. Slow is lost revenue.</div>
</div>
<div class="page">
  <div class="kicker">The category</div>
  <div class="headline">This is not software you babysit.</div>
  <div class="body">Non-Human Intelligence owns one workflow in your business and runs it. A chatbot waits to be prompted. Owl logs in, does the work, and remembers it. The difference is the difference between a tool and a colleague.</div>
</div>
<div class="page">
  <div class="kicker">The offer</div>
  <div class="headline">One flat fee. One workflow owned.</div>
  <div class="body">Owl is a managed Non-Human Intelligence for five thousand pounds a month, everything included. Live in forty-eight hours. If it has not paid for itself by day thirty, the first month is refunded. Start at beacons.ai/humanarchitect.</div>
</div>
"""

HOWITWORKS = """
<div class="page">
  <div class="kicker">Owl · Non-Human Intelligence</div>
  <div class="cover-title">How it actually works.</div>
  <div class="cover-sub">No code. No dashboard to babysit. One brain, four specialists, and a stack that shows up with its own desk.</div>
  <div class="rule"></div>
  <div class="foot">Operated by Human Architect · beacons.ai/humanarchitect</div>
</div>
<div class="page">
  <div class="kicker">The architecture</div>
  <div class="headline">One brain. Four specialists.</div>
  <div class="body">A central brain directs four agents — outbound lead generation, sales follow-up, content and assets, and support or fulfilment. They hand work to each other so the workflow closes without a human in the loop.</div>
</div>
<div class="page">
  <div class="kicker">The stack</div>
  <div class="headline">It arrives with its own desk.</div>
  <div class="body">Its own computer, its own email, a live Telegram line, and a seat in your Slack or Telegram. Real tools, simple billing, a memory that files one fact in one home, and constant health checks. Eight parts, one worker.</div>
</div>
<div class="page">
  <div class="kicker">Where it runs</div>
  <div class="headline">Your data stays in its own box.</div>
  <div class="body">Owl runs on an isolated client server with access scoped only to what the job needs. Your data never leaves your control, and it travels with you if you leave. Self-hosted, portable, private.</div>
</div>
<div class="page">
  <div class="kicker">Who it serves</div>
  <div class="headline">Four industries. One workflow each.</div>
  <div class="body">Trades and services, clinics and health, law and professional firms, and e-commerce. For each, Owl owns one recurring workflow — quote requests, intake, follow-up, or support — and runs it end to end.</div>
</div>
<div class="page">
  <div class="kicker">The speed</div>
  <div class="headline">Live in forty-eight hours.</div>
  <div class="body">The stack is already built. We deploy it to your server and hand you a running workflow within two days. If we miss, the first month is free. Speed is what you are paying for.</div>
</div>
"""

WHITELABEL = """
<div class="page">
  <div class="kicker">Owl · Non-Human Intelligence</div>
  <div class="cover-title">Sell it under your name.</div>
  <div class="cover-sub">White-label Owl and turn a cost you carry into a revenue line your clients pay for. Single tier. No recruitment.</div>
  <div class="rule"></div>
  <div class="foot">Operated by Human Architect · beacons.ai/humanarchitect</div>
</div>
<div class="page">
  <div class="kicker">The model</div>
  <div class="headline">Your brand. Our engine.</div>
  <div class="body">Your clients see your name, not ours. The Non-Human Intelligence works under your label while we build, host, and run it. One clean option, nothing else to buy.</div>
</div>
<div class="page">
  <div class="kicker">Why it wins</div>
  <div class="headline">No recruitment. No payroll.</div>
  <div class="body">White-label is single-tier. You add an AI employee to your offer without hiring, training, or managing anyone. It becomes a product on your shelf, not a line on your cost sheet.</div>
</div>
<div class="page">
  <div class="kicker">The economics</div>
  <div class="headline">Recurring revenue, not overhead.</div>
  <div class="body">You bill your clients monthly for an Owl you deliver through us. They pay you. We run it. The margin is yours and it renews. The same five-thousand-pound engine becomes your recurring income.</div>
</div>
<div class="page">
  <div class="kicker">How to start</div>
  <div class="headline">One call builds the instance.</div>
  <div class="body">Book a scoping call at beacons.ai/humanarchitect. We stand up a white-label instance on your brand, live in forty-eight hours. You start selling Non-Human Intelligence under your name.</div>
</div>
"""

DECKS = {"pricing": PRICING, "objection": OBJECTION, "onboarding": ONBOARDING,
         "awareness": AWARENESS, "howitworks": HOWITWORKS, "whitelabel": WHITELABEL}

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "pricing"
    if name not in DECKS:
        print("choose: pricing | objection | onboarding"); sys.exit(2)
    path = render(DECKS[name], name)
    print("RENDERED", path)
