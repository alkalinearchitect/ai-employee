#!/usr/bin/env python3
"""Owl deck renderer v3 — RED TEAM design system. Grid layout (no overlap),
Inter embedded, monogram SVG, corner ticks, cards, node motif, 3:4 full-bleed black/violet."""
import subprocess, os, sys

OUT = "/root/ai-employee/revenue-os/out_v3"
os.makedirs(OUT, exist_ok=True)
CHROME = "/usr/bin/google-chrome"

MONO = """<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16 17 L20.5 8.5 L27 14.5" stroke="#8b5cf6" stroke-width="2" stroke-linejoin="round"/>
<path d="M48 17 L43.5 8.5 L37 14.5" stroke="#8b5cf6" stroke-width="2" stroke-linejoin="round"/>
<circle cx="32" cy="34" r="22" stroke="#8b5cf6" stroke-width="2"/>
<circle cx="24" cy="31" r="7" stroke="#8b5cf6" stroke-width="2"/>
<circle cx="24" cy="31" r="2.4" stroke="#FFFFFF" stroke-width="2"/>
<circle cx="40" cy="31" r="7" stroke="#8b5cf6" stroke-width="2"/>
<circle cx="40" cy="31" r="2.4" stroke="#FFFFFF" stroke-width="2"/>
<path d="M32 38 L32 44.5" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round"/>
</svg>"""
NODE = """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
<line x1="50" y1="50" x2="50" y2="16" stroke="#8b5cf6" stroke-width="1.2"/>
<line x1="50" y1="50" x2="84" y2="50" stroke="#8b5cf6" stroke-width="1.2"/>
<line x1="50" y1="50" x2="50" y2="84" stroke="#8b5cf6" stroke-width="1.2"/>
<line x1="50" y1="50" x2="16" y2="50" stroke="#8b5cf6" stroke-width="1.2"/>
<circle cx="50" cy="50" r="7" stroke="#8b5cf6" stroke-width="2"/>
<circle cx="50" cy="16" r="4" stroke="#8b5cf6" stroke-width="1.5"/>
<circle cx="84" cy="50" r="4" stroke="#8b5cf6" stroke-width="1.5"/>
<circle cx="50" cy="84" r="4" stroke="#8b5cf6" stroke-width="1.5"/>
<circle cx="16" cy="50" r="4" stroke="#8b5cf6" stroke-width="1.5"/>
<circle cx="50" cy="50" r="24" stroke="#8b5cf6" stroke-width="0.8" opacity="0.5"/>
<circle cx="50" cy="50" r="34" stroke="#8b5cf6" stroke-width="0.8" opacity="0.3"/>
</svg>"""

CSS = """
@font-face { font-family:'Inter'; src:url('file:///root/fonts/Inter-Regular.ttf') format('truetype'); font-weight:400; font-style:normal; }
@font-face { font-family:'Inter'; src:url('file:///root/fonts/Inter-Medium.ttf')  format('truetype'); font-weight:500; font-style:normal; }
@font-face { font-family:'Inter'; src:url('file:///root/fonts/Inter-Bold.ttf')    format('truetype'); font-weight:700; font-style:normal; }
@page { size:9in 12in; margin:0; }
* { box-sizing:border-box; margin:0; padding:0; }
html, body { background:#000; }
body { font-family:'Inter', sans-serif; color:#FFFFFF; -webkit-font-smoothing:antialiased; print-color-adjust:exact; -webkit-print-color-adjust:exact; }
.page { position:relative; width:9in; height:12in; background:#000; overflow:hidden;
  display:grid; grid-template-rows:1fr auto; grid-template-areas:'main' 'footrow';
  padding:84px 95px 34px; page-break-after:always; break-after:page; }
.page:last-child { page-break-after:auto; break-after:auto; }
.main { grid-area:main; display:flex; flex-direction:column; justify-content:flex-start; min-height:0; overflow:hidden; }
.footrow { grid-area:footrow; display:flex; justify-content:space-between; align-items:baseline; gap:24px; padding-top:18px; border-top:1px solid #2a2a2e; }
.foot { font-size:20pt; color:#b5b5be; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:calc(100% - 56px); }
.pnum { font-size:20pt; color:#8a8a92; white-space:nowrap; }
.page.cover { padding-top:84px; }
.tick { position:absolute; width:28px; height:28px; pointer-events:none; }
.tick.tl { top:40pt; left:40pt;  border-top:2px solid #8b5cf6; border-left:2px solid #8b5cf6; }
.tick.tr { top:40pt; right:40pt; border-top:2px solid #8b5cf6; border-right:2px solid #8b5cf6; }
.tick.bl { bottom:40pt; left:40pt;  border-bottom:2px solid #8b5cf6; border-left:2px solid #8b5cf6; }
.tick.br { bottom:40pt; right:40pt; border-bottom:2px solid #8b5cf6; border-right:2px solid #8b5cf6; }
.monogram { position:absolute; top:78px; right:95px; width:64pt; height:64pt; }
.monogram svg { width:100%; height:100%; display:block; }
.railidx { position:absolute; top:82px; left:95px; font-size:20pt; font-weight:500; letter-spacing:.10em; color:#8b5cf6; }
.kicker { font-size:26pt; font-weight:500; letter-spacing:.16em; text-transform:uppercase; color:#8b5cf6; }
.rule { width:100pt; height:6pt; background:#8b5cf6; margin:22px 0 30px; }
.hairline { width:100%; height:1px; background:#2a2a2e; margin:26px 0 30px; }
.cover-title { font-size:72pt; font-weight:700; line-height:1.02; letter-spacing:-.025em; color:#FFFFFF; }
.cover-sub { font-size:38pt; font-weight:400; line-height:1.28; color:#EDEDED; max-width:14ch; }
.headline { font-size:62pt; font-weight:700; line-height:1.06; letter-spacing:-.02em; color:#FFFFFF; }
.body { font-size:38pt; font-weight:400; line-height:1.34; color:#EDEDED; }
.body + .body { margin-top:26px; }
.dim { color:#9a9aa2; }
.accent { color:#8b5cf6; }
.void { flex:1 1 auto; min-height:0; }
.cover .main > .kicker { margin-bottom:26px; }
.cards { display:grid; gap:22px; }
.cards.two   { grid-template-columns:1fr 1fr; }
.cards.one   { grid-template-columns:1fr; }
.cards.three { grid-template-columns:1fr 1fr 1fr; }
.card { border:1px solid #2a2a2e; background:none; padding:18px 18px 20px; min-height:0; }
.cards.four { grid-template-columns:1fr 1fr 1fr 1fr; }
.stackc .card { padding:14px 18px; }
.stackc .card .t { font-size:30pt; }
.card.on { border-color:#8b5cf6; }
.card .n { font-size:22pt; font-weight:700; color:#8b5cf6; letter-spacing:.06em; display:block; margin-bottom:8px; }
.card .t { font-size:28pt; font-weight:500; line-height:1.12; color:#FFFFFF; }
.card .d { font-size:19pt; font-weight:400; line-height:1.25; color:#b5b5be; margin-top:8px; }
.stat { border-left:2px solid #8b5cf6; padding-left:26px; }
.stat .big { font-size:62pt; font-weight:700; line-height:1; }
.stat .lab { font-size:26pt; color:#9a9aa2; margin-top:10px; }
.node-emblem { position:absolute; bottom:96px; right:95px; width:86pt; height:86pt; opacity:.85; }
.node-bg { position:absolute; bottom:-120px; right:-120px; width:560px; height:560px; opacity:.10; pointer-events:none; }
.node-emblem svg, .node-bg svg { width:100%; height:100%; display:block; }
"""

def frame(inner_main, foot_left, foot_mid, pnum, cover=False, rail=None, node=False, nodebg=False):
    ticks = '<div class="tick tl"></div><div class="tick tr"></div><div class="tick bl"></div><div class="tick br"></div>'
    mono = f'<div class="monogram">{MONO}</div>'
    railhtml = f'<div class="railidx">{rail}</div>' if rail else ''
    nodehtml = f'<div class="node-emblem">{NODE}</div>' if node else ''
    nodebghtml = f'<div class="node-bg">{NODE}</div>' if nodebg else ''
    cls = 'page cover' if cover else 'page'
    mids = f'<div class="foot dim">{foot_mid}</div>' if foot_mid else ''
    return f'<section class="{cls}">{ticks}{mono}{railhtml}{nodehtml}{nodebghtml}<div class="main">{inner_main}</div><div class="footrow"><div class="foot">{foot_left}</div>{mids}<div class="pnum">{pnum}</div></div></section>'

def cover(kicker, title, sub, pnum, foot="Owl — Operated by Human Architect"):
    main = f'<div class="kicker">{kicker}</div><h1 class="cover-title">{title}</h1><div class="rule"></div><p class="cover-sub">{sub}</p><div class="void"></div>'
    return frame(main, foot, None, pnum, cover=True, nodebg=True)

def content(kicker, rail, headline, inner_after, pnum, section, node=False):
    main = f'<div class="kicker">{kicker}</div><div class="rule"></div><h2 class="headline">{headline}</h2><div class="hairline"></div>{inner_after}<div class="void"></div>'
    return frame(main, "Owl — Operated by Human Architect", section, pnum, rail=rail, node=node)

# ---------- DECK COPY ----------
PRICING = [
cover("Owl · Non-Human Intelligence", "Stop losing the lead you almost had.", "Every slow reply, every missed message, every hour of admin is work you paid someone to lose. Owl does it.", "01"),
content("The cost of one week", "02 / 08", "A lead cools in the time it takes to finish your coffee.", '<p class="body">HBR: firms that reply within the hour are 7x more likely to qualify a lead. 78% buy from the first to respond. Most businesses answer same-day, if at all.</p>', "02", "The gap", node=True),
content("The fix", "03 / 08", "One employee that never stops.", '<p class="body">Owl is a managed Non-Human Intelligence that owns one recurring workflow in your business — quotes, follow-up, intake, support. It replies in the first hour. Every time.</p>', "03", "The fix"),
content("What you get", "04 / 08", "One flat fee. Everything built, hosted, run.", '<div class="cards two"><div class="card on"><span class="n">01</span><div class="t">Its own desk</div><div class="d">Computer, email, live Telegram, your Slack.</div></div><div class="card"><span class="n">02</span><div class="t">One brain, four specialists</div><div class="d">Outbound, follow-up, content, support.</div></div><div class="card"><span class="n">03</span><div class="t">Live in 48 hours</div><div class="d">Or the first month is free.</div></div><div class="card"><span class="n">04</span><div class="t">Day-30 proof</div><div class="d">More than £5k saved or you don\'t pay.</div></div></div>', "04", "The offer"),
content("The price", "05 / 08", "£5,000 a month. That is the whole invoice.", '<p class="body">No setup. No per-seat. No usage add-ons. One number covers build, hosting, onboarding, and daily operation. The cost of one junior, for a worker that never sleeps.</p>', "05", "The price"),
content("The guarantee", "06 / 08", "If it hasn't paid for itself, you don't.", '<p class="body">We measure the human hours it returns. If it hasn\'t saved more than £5,000 in human time by day 30, the first month is refunded. Live in 48 hours or the first month is free.</p>', "06", "The guarantee"),
content("Proof it works", "07 / 08", "This is not a science experiment.", '<div class="stat"><div class="big accent">456k</div><div class="lab">Autonomous coding agents have already authored 456,000 pull requests across 61,000 repositories and 47,000 developers. The model class is proven at scale. Owl applies it to your workflow. Source: arxiv SE 3.0.</div></div>', "07", "Proof"),
content("Your data, your call", "08 / 08", "Isolated. Scoped. Portable. Yours.", '<p class="body">Runs on its own server with access only to the job. Cancel any time, no contract, no exit fee. The work and the setup travel with you.</p>', "08", "The terms"),
content("Start", "09 / 09", "Book the call. Watch it work.", '<div class="stat"><div class="big accent">48h</div><div class="lab">From scoping call to running workflow. Your first non-human employee, live in 48 hours. Book at beacons.ai/humanarchitect. Operated by Human Architect.</div></div>', "09", "Start"),
]

OBJECTION = [
cover("Owl · Non-Human Intelligence", "Seven objections. One answer.", "One recurring workflow owned. £5,000 a month. Live in 48 hours.", "01"),
content("Objection 01", "02 / 09", "Hiring is the expensive option.", '<p class="body">A junior\'s salary is the smallest number on the bill. Add tax, software, training, and the months before they are useful. Owl is one flat five thousand a month, live in 48 hours.</p>', "02", "Obj 01"),
content("Objection 02", "03 / 09", "It replaces the work, not the people.", '<p class="body">Owl takes the recurring task your best person dreads — the quotes, the follow-ups, the admin that eats the day. Your team moves up to the work only humans should do.</p>', "03", "Obj 02"),
content("Objection 03", "04 / 09", "Your data never leaves its own box.", '<p class="body">Owl runs on an isolated server with scoped access to only what it needs. Portable, so you take it with you. We cannot see what you have not permitted.</p>', "04", "Obj 03"),
content("Objection 04", "05 / 09", "If it breaks, you don't pay.", '<p class="body">Owl is live in 48 hours or your first month is refunded. At day 30, if it has not saved you more than £5,000, we refund that month too.</p>', "05", "Obj 04"),
content("Objection 05", "06 / 09", "ChatGPT answers. Owl does.", '<p class="body">ChatGPT waits for your team to type the right prompt and check the output. Owl owns one workflow end to end — it acts, follows up, closes the loop while you sleep.</p>', "06", "Obj 05"),
content("Objection 06", "07 / 09", "Fast is the point, not the risk.", '<p class="body">The stack is already built — one brain and four specialists, configured, not coded from zero. We deploy it within two days. If we miss, the first month is free.</p>', "07", "Obj 06"),
content("Objection 07", "08 / 09", "Leave anytime. Take it with you.", '<p class="body">Cancel whenever you want — no contract, no notice, no exit fee. Your Owl runs on a portable server, so the work and the setup travel with you.</p>', "08", "Obj 07"),
content("Close", "09 / 09", "The first responder wins.", '<div class="stat"><div class="big accent">7x</div><div class="lab">HBR: firms replying within an hour are 7x more likely to qualify a lead. 78% buy from the first to respond. Book the call. Live in 48 hours.</div></div>', "09", "Close"),
]

ONBOARDING = [
cover("Owl · Non-Human Intelligence", "What to expect after you say yes.", "A clear timeline and hard guarantees. Working in 48 hours.", "01"),
content("Step 01", "02 / 08", "We learn your business before we touch a tool.", '<p class="body">The discovery call is a conversation, not a pitch. You tell us the one recurring workflow you want off your plate. We decide together whether one Non-Human Intelligence can own it cleanly.</p>', "02", "Step 01"),
content("Step 02", "03 / 08", "Live in 48 hours, or your first month is free.", '<p class="body">From the moment the call ends, Owl builds. One brain and four specialists stand up the workflow, wire the tools, and stage it on an isolated server. If not running in two days, the first month is refunded.</p>', "03", "Step 02"),
content("Step 03", "04 / 08", "Your new hire arrives where your team talks.", '<p class="body">Owl onboards into your Slack or Telegram — the place your people already work. A dedicated line, a real email, a presence your team can message. No new portal.</p>', "04", "Step 03"),
content("Step 04", "05 / 08", "Thirty days in, the math has to be obvious.", '<p class="body">The workflow runs without you thinking about it. On day 30 we count what Owl saved. If it is not more than £5,000, we refund the month.</p>', "05", "Step 04"),
content("Step 05", "06 / 08", "We watch it so you don't have to.", '<p class="body">Owl runs constant health checks across the whole stack. If something breaks, we know before you do. It is part of the flat fee.</p>', "06", "Step 05"),
content("Step 06", "07 / 08", "When one workflow is owned, the next is easy.", '<p class="body">Owl is built to own a single recurring workflow completely. Once yours runs without you, we stand up the next with the same build and the same guarantees.</p>', "07", "Step 06"),
content("Step 07", "08 / 08", "Put your name on it.", '<p class="body">Owl runs white-label, single tier. Your clients see your brand, not ours. One clean option, available whenever you are ready.</p><p class="body dim">Flat £5,000/month · Cancel anytime · Human Architect</p>', "08", "Step 07"),
]

AWARENESS = [
cover("Owl · Non-Human Intelligence", "The employee who never sleeps.", "A new kind of worker. It does not take holiday. It does not resign. It replies in the first hour — every time.", "01"),
content("The gap you feel", "02 / 04", "You are losing work you never knew you had.", '<p class="body">HBR: firms that reply within the hour are 7x more likely to qualify a lead. 78% buy from the first to respond. Your slow reply is the competitor\'s closed deal.</p>', "02", "The gap", node=True),
content("The shift", "03 / 04", "Software waits to be used. This works.", '<p class="body">Non-Human Intelligence owns one workflow in your business and runs it. A chatbot waits to be prompted. Owl logs in, does the work, and remembers it. The difference between a tool and a colleague.</p>', "03", "The category"),
content("The offer", "04 / 04", "One flat fee. One workflow owned.", '<div class="stat"><div class="big accent">£5k</div><div class="lab">A month, everything included. Live in 48 hours. If it has not paid for itself by day 30, the first month is refunded. Book at beacons.ai/humanarchitect.</div></div>', "04", "The offer"),
]

HOWITWORKS = [
cover("Owl · Non-Human Intelligence", "How it actually works.", "One brain, four specialists, a stack with its own desk.", "01"),
content("The architecture", "02 / 06", "One brain. Four specialists.", '<div class="cards two"><div class="card on"><span class="n">01</span><div class="t">Outbound</div><div class="d">Lead generation and replies.</div></div><div class="card"><span class="n">02</span><div class="t">Sales follow-up</div><div class="d">Nurture and booking.</div></div><div class="card"><span class="n">03</span><div class="t">Content</div><div class="d">Assets and posts.</div></div><div class="card"><span class="n">04</span><div class="t">Support</div><div class="d">Fulfilment and handover.</div></div></div>', "02", "Architecture", node=True),
content("The stack", "03 / 06", "It arrives with its own desk.", '<div class="cards two stackc"><div class="card"><span class="n">01</span><div class="t">Its own computer</div></div><div class="card"><span class="n">02</span><div class="t">Its own email</div></div><div class="card"><span class="n">03</span><div class="t">Live Telegram line</div></div><div class="card"><span class="n">04</span><div class="t">Your Slack / Telegram</div></div><div class="card"><span class="n">05</span><div class="t">Real tools</div></div><div class="card"><span class="n">06</span><div class="t">Simple billing</div></div><div class="card"><span class="n">07</span><div class="t">Memory: one fact, one home</div></div><div class="card"><span class="n">08</span><div class="t">Constant health checks</div></div></div>', "03", "The stack"),
content("Where it runs", "04 / 06", "Your data stays in its own box.", '<p class="body">Owl runs on an isolated client server with access scoped only to what the job needs. Your data never leaves your control, and it travels with you if you leave. Self-hosted, portable, private.</p>', "04", "Where it runs"),
content("Who it serves", "05 / 06", "Four industries. One workflow each.", '<div class="cards two"><div class="card on"><span class="n">01</span><div class="t">Trades &amp; services</div></div><div class="card"><span class="n">02</span><div class="t">Clinics &amp; health</div></div><div class="card"><span class="n">03</span><div class="t">Law &amp; professional</div></div><div class="card"><span class="n">04</span><div class="t">E-commerce</div></div></div>', "05", "Who it serves"),
content("The speed", "06 / 06", "Live in 48 hours.", '<p class="body">The stack is already built. We deploy it to your server and hand you a running workflow within two days. If we miss, the first month is free. Speed is what you are paying for.</p>', "06", "The speed"),
]

WHITELABEL = [
cover("Owl · Non-Human Intelligence", "Sell it under your name.", "Turn a cost you carry into a revenue line. Single tier. No recruitment.", "01"),
content("The model", "02 / 05", "Your brand. Our engine.", '<p class="body">Your clients see your name, not ours. The Non-Human Intelligence works under your label while we build, host, and run it. One clean option, nothing else to buy.</p>', "02", "The model"),
content("Why it wins", "03 / 05", "No recruitment. No payroll.", '<p class="body">White-label is single tier. You add an AI employee to your offer without hiring, training, or managing anyone. A product on your shelf, not a line on your cost sheet.</p>', "03", "Why it wins"),
content("The economics", "04 / 05", "Recurring revenue, not overhead.", '<p class="body">You bill your clients monthly for an Owl you deliver through us. They pay you. We run it. The margin is yours and it renews.</p>', "04", "The economics"),
content("How to start", "05 / 05", "One call builds the instance.", '<p class="body">Book a scoping call at beacons.ai/humanarchitect. We stand up a white-label instance on your brand, live in 48 hours.</p>', "05", "How to start"),
]

DECKS = {
    "owl-pricing-scope": PRICING,
    "owl-objection-close": OBJECTION,
    "owl-onboarding-guide": ONBOARDING,
    "owl-awareness": AWARENESS,
    "how-it-works": HOWITWORKS,
    "white-label": WHITELABEL,
}

def render(pages, name):
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(pages) + "</body></html>"
    hp = os.path.join(OUT, f"{name}.html"); pp = os.path.join(OUT, f"{name}.pdf")
    open(hp, "w").write(html)
    r = subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pp}", f"file://{hp}"], capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise SystemExit("chrome failed: " + r.stderr[-300:])
    return pp

if __name__ == "__main__":
    names = sys.argv[1:] or list(DECKS)
    for n in names:
        print("RENDERED", render(DECKS[n], n))
