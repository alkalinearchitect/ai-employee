#!/usr/bin/env python3
"""Build 2 Owl PDFs (How It Works, White-Label Partner Brief).

Mandatory design system:
- full-bleed solid #000000, @page { size: 9in 12in; margin: 0; }
- white / #EDEDED text, ONE violet #8b5cf6 accent. No other hue/gradient.
- Inter embedded via @font-face local file://, used for EVERYTHING.
- type scale: kicker 30, headline 92, body 42, cover-title 120, cover-sub 46,
  num 30, foot 26. line-height 1.5-1.6. body never < 38px.
- subtle violet NHI watermark corner, thin violet rule under headlines,
  page numbers bottom-right muted grey. print-color-adjust: exact.
- audit with fitz: (a) rect==648x864, (b) Inter not Liberation,
  (c) no span clipped within page, (d) full-bleed black.
"""
import subprocess, os, sys, re

OUT = "/root/ai-employee/revenue-os/out_build"
os.makedirs(OUT, exist_ok=True)
CHROME = "/usr/bin/google-chrome"

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0;
    -webkit-print-color-adjust: exact; print-color-adjust: exact; }
@page { size: 9in 12in; margin: 0; }
html, body { background: #000000; }
@font-face { font-family: 'Inter'; src: url('file:///root/fonts/Inter-Regular.ttf') format('truetype'); font-weight: 400; }
@font-face { font-family: 'Inter'; src: url('file:///root/fonts/Inter-Medium.ttf') format('truetype'); font-weight: 500; }
@font-face { font-family: 'Inter'; src: url('file:///root/fonts/Inter-Bold.ttf') format('truetype'); font-weight: 700; }
.page {
  position: relative; overflow: hidden;
  width: 9in; height: 12in; background: #000000;
  page-break-after: always;
  display: flex; flex-direction: column; justify-content: center;
  padding: 110px 100px;
  font-family: 'Inter', sans-serif; color: #FFFFFF;
}
.page:last-child { page-break-after: auto; }
.wm {
  position: absolute; top: 46px; right: 30px;
  font-family: 'Inter', sans-serif; font-weight: 700;
  font-size: 190px; line-height: 1; letter-spacing: -.04em;
  color: rgba(139,92,246,0.06); z-index: 0; pointer-events: none;
  user-select: none;
}
.content { position: relative; z-index: 1; }
.kicker {
  font-family: 'Inter', sans-serif; font-weight: 700;
  color: #8b5cf6; letter-spacing: .24em; text-transform: uppercase;
  font-size: 30px; margin-bottom: 46px;
}
.headline {
  font-family: 'Inter', sans-serif; font-weight: 700;
  font-size: 92px; line-height: 1.08; letter-spacing: -.02em;
  color: #FFFFFF; max-width: 15ch; margin-bottom: 0;
}
.rule { width: 96px; height: 5px; background: #8b5cf6; margin: 44px 0; border-radius: 3px; }
.body {
  font-family: 'Inter', sans-serif; font-weight: 400;
  font-size: 42px; line-height: 1.55; color: #EDEDED;
  max-width: 30ch;
}
.cover-title {
  font-family: 'Inter', sans-serif; font-weight: 700;
  font-size: 120px; line-height: 1.04; letter-spacing: -.025em;
  color: #FFFFFF; max-width: 13ch; margin-bottom: 0;
}
.cover-sub {
  font-family: 'Inter', sans-serif; font-weight: 400;
  font-size: 46px; line-height: 1.5; color: #EDEDED;
  max-width: 26ch; margin-top: 50px;
}
.num {
  font-family: 'Inter', sans-serif; font-weight: 700;
  color: #8b5cf6; font-size: 30px; letter-spacing: .14em;
  margin-bottom: 30px;
}
.foot {
  font-family: 'Inter', sans-serif; font-weight: 400;
  font-size: 26px; color: #8a8a92; letter-spacing: .03em;
  margin-top: 56px; z-index: 1;
}
.pagenum {
  position: absolute; bottom: 38px; right: 44px; z-index: 1;
  font-family: 'Inter', sans-serif; font-weight: 400;
  font-size: 26px; color: #555560; letter-spacing: .06em;
}
"""

def page(content_html, wm="NHI", num=None, is_cover=False):
    foot = ("<div class='foot'>Operated by Human Architect &middot; beacons.ai/humanarchitect</div>"
            if is_cover else "")
    pn = f"<div class='pagenum'>{num} / 06</div>" if (num and not is_cover) else \
         (f"<div class='pagenum'>{num} / 05</div>" if num else "")
    return (f"<div class='page'>\n"
            f"  <div class='wm'>{wm}</div>\n"
            f"  <div class='content'>{content_html}</div>\n"
            f"  {foot}\n  {pn}\n</div>")

def cover(kicker, title, sub):
    c = (f"<div class='kicker'>{kicker}</div>"
         f"<div class='cover-title'>{title}</div>"
         f"<div class='rule'></div>"
         f"<div class='cover-sub'>{sub}</div>")
    return page(c, is_cover=True)

# ── DECK A: How It Works (6pp) ─────────────────────────
HOW = []
HOW.append(cover(
    "Owl &middot; Non-Human Intelligence",
    "How it actually works.",
    "No code to learn. No dashboard to watch. One brain, four specialists, and a stack that arrives with its own desk."))
HOW.append(page(
    "<div class='kicker'>The architecture</div>"
    "<div class='headline'>One brain.<br>Four specialists.</div>"
    "<div class='rule'></div>"
    "<div class='body'>A single brain directs four agents &mdash; outbound, sales follow-up, content, and support. They pass work between themselves, so the job closes without a human in the loop.</div>",
    num="01"))
HOW.append(page(
    "<div class='kicker'>The stack</div>"
    "<div class='headline'>It shows up with its own desk.</div>"
    "<div class='rule'></div>"
    "<div class='body'>Its own computer. Its own email. A live messaging line and a seat where your team already works. Real tools, simple billing, one clean memory, health checks that never sleep. Eight parts. One worker.</div>",
    num="02"))
HOW.append(page(
    "<div class='kicker'>Where it runs</div>"
    "<div class='headline'>Your data stays in its own box.</div>"
    "<div class='rule'></div>"
    "<div class='body'>Owl runs on an isolated server with access scoped to exactly what the job needs. Nothing else. Your data never leaves your control, and it travels with you if you leave. Private by construction.</div>",
    num="03"))
HOW.append(page(
    "<div class='kicker'>Who it serves</div>"
    "<div class='headline'>Four industries. One workflow each.</div>"
    "<div class='rule'></div>"
    "<div class='body'>Trades. Clinics. Law firms. E-commerce. For each, Owl owns one recurring workflow &mdash; the quote, the intake, the follow-up, the support &mdash; and runs it end to end.</div>",
    num="04"))
HOW.append(page(
    "<div class='kicker'>The speed</div>"
    "<div class='headline'>Live in forty-eight hours.</div>"
    "<div class='rule'></div>"
    "<div class='body'>The stack is already built. We deploy it to your server and hand you a running workflow inside two days. If we miss, your first month is free. Speed is the product.</div>",
    num="05"))

# ── DECK B: White-Label Partner Brief (5pp) ────────────
WL = []
WL.append(cover(
    "Owl &middot; White-Label Partner Brief",
    "Sell it under your name.",
    "White-label Owl and turn a cost you carry into a revenue line your clients pay for. Single tier. No recruitment."))
WL.append(page(
    "<div class='kicker'>The model</div>"
    "<div class='headline'>Your brand. Our engine.</div>"
    "<div class='rule'></div>"
    "<div class='body'>Your clients see your name, not ours. The Non-Human Intelligence works under your label while we build, host, and run it. One clean option. Nothing else to buy.</div>",
    num="01"))
WL.append(page(
    "<div class='kicker'>Why it wins</div>"
    "<div class='headline'>No recruitment. No payroll.</div>"
    "<div class='rule'></div>"
    "<div class='body'>White-label is single-tier. You add an AI employee to your offer without hiring, training, or managing anyone. It becomes a product on your shelf, not a line on your cost sheet.</div>",
    num="02"))
WL.append(page(
    "<div class='kicker'>The economics</div>"
    "<div class='headline'>Recurring revenue, not overhead.</div>"
    "<div class='rule'></div>"
    "<div class='body'>You bill your clients monthly for an Owl you deliver through us. They pay you. We run it. The margin is yours, and it renews. The same five-thousand-pound engine becomes your income.</div>",
    num="03"))
WL.append(page(
    "<div class='kicker'>How to start</div>"
    "<div class='headline'>One call builds the instance.</div>"
    "<div class='rule'></div>"
    "<div class='body'>Book a scoping call at beacons.ai/humanarchitect. We stand up a white-label instance on your brand, live in forty-eight hours. You start selling Non-Human Intelligence under your name.</div>",
    num="04"))

DECKS = {"how-it-works": HOW, "white-label": WL}

def render(html, name):
    html_path = os.path.join(OUT, f"{name}.html")
    pdf_path = os.path.join(OUT, f"{name}.pdf")
    doc = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(html)}</body></html>"
    open(html_path, "w").write(doc)
    cmd = [CHROME, "--headless", "--no-sandbox", "--disable-gpu",
           "--no-pdf-header-footer",
           f"--print-to-pdf={pdf_path}", f"file://{html_path}"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise SystemExit("chrome failed: " + r.stderr[-500:])
    if not os.path.exists(pdf_path):
        raise SystemExit("no pdf produced")
    return html_path, pdf_path

if __name__ == "__main__":
    names = sys.argv[1:] or list(DECKS.keys())
    for n in names:
        hp, pp = render(DECKS[n], n)
        print("RENDERED", pp)
