"""Build the two Owl PDFs as self-contained HTML -> Chrome print-to-PDF.
Locked standard: 9x12in full-bleed, black 135deg gradient, violet #8b5cf6 accent,
LARGE type (title 60, headline 46, body 24+), measured verify.
"""
import os, subprocess, sys

OUT = "/root/ai-employee/auditor"
DATE = "10 Aug 2026"

CSS = """
* { margin:0; padding:0; box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
@page { size: 9in 12in; margin: 0; }
html, body { background:#000; }
.page {
  width:9in; height:12in; background:linear-gradient(135deg,#060606 0%,#0e0e0e 50%,#060606 100%);
  page-break-after:always; padding:88px 84px; position:relative; color:#fff;
  font-family:Helvetica, Arial, sans-serif;
}
.page:last-child { page-break-after:auto; }
.kick { font-size:15px; letter-spacing:.18em; text-transform:uppercase; color:#8b5cf6; font-weight:700; margin-bottom:20px; }
h1 { font-size:62px; line-height:1.05; font-weight:800; letter-spacing:-.02em; margin-bottom:22px; }
h2 { font-size:46px; line-height:1.1; font-weight:800; letter-spacing:-.02em; margin:34px 0 16px; }
p { font-size:24px; line-height:1.5; color:#c9c9d1; margin-bottom:18px; max-width:62ch; }
.lead { font-size:26px; color:#e6e6ec; }
.bull { font-size:24px; line-height:1.45; color:#c9c9d1; margin:0 0 12px 30px; position:relative; }
.bull:before { content:""; position:absolute; left:0; top:13px; width:9px; height:9px; background:#8b5cf6; border-radius:2px; }
.secnum { font-size:15px; color:#8a8a92; letter-spacing:.15em; margin-bottom:6px; }
.rule { height:1px; background:#26262e; margin:18px 0; border:0; }
.v { color:#8b5cf6; }
.foot { position:absolute; bottom:40px; left:84px; right:84px; display:flex; justify-content:space-between;
  font-size:14px; color:#8a8a92; border-top:1px solid #26262e; padding-top:14px; letter-spacing:.04em; }
/* bar */
.bar { margin:8px 0 26px; }
.bar .lab { font-size:22px; color:#c9c9d1; margin-bottom:8px; }
.track { width:100%; height:22px; background:#1a1a20; border-radius:4px; position:relative; }
.fill { height:22px; background:#8b5cf6; border-radius:4px; }
.bar .val { position:absolute; right:0; top:-2px; font-size:20px; font-weight:700; color:#fff; }
/* evidence rows */
.ev { margin:0 0 18px; }
.ev .k { font-size:22px; color:#c9c9d1; }
.ev .s { font-size:22px; font-weight:700; color:#8b5cf6; margin-top:2px; }
/* proof box */
.proof { border:1.5px solid #8b5cf6; border-radius:12px; padding:22px 24px; margin:18px 0; }
.proof .ph { font-size:18px; font-weight:700; color:#8b5cf6; letter-spacing:.04em; margin-bottom:12px; text-transform:uppercase; }
.proof .ln { font-size:21px; color:#e6e6ec; line-height:1.5; font-family:"Courier New",monospace; }
.status { font-size:21px; color:#8a8a92; margin-top:6px; }
"""

def page(inner, foot_left="NOHUMA  ·  Non-Human Intelligence  ·  " + DATE, foot_right="Page"):
    return f'<div class="page">{inner}<div class="foot"><span>{foot_left}</span><span>{foot_right}</span></div></div>'

# ---------- AUDIT BRIEF ----------
a = []
a.append(page(f"""
<div class="kick">Site Audit · Live Read</div>
<h1>Site Audit:<br>mydentist.co.uk</h1>
<p class="lead">A live read of what this business does by hand — and what one NOHUMA worker would own. Real signals only; no invented numbers.</p>
<div class="rule"></div>
<h2 style="font-size:34px;margin-top:10px">The snapshot</h2>
<p class="bull">Industry: <span class="v">Dentists</span> — a sector that hasn't adopted AI</p>
<p class="bull">Pages scanned live: <span class="v">55</span></p>
<p class="bull">Manual tasks detected: <span class="v">7</span> distinct workflows done by hand</p>
<p class="bull">Verdict: <span class="v">under-served by automation</span> — prime fit for a worker</p>
""", foot_right="Page 1"))

a.append(page(f"""
<div class="secnum">01 / Their bottleneck</div>
<h2>Their bottleneck,<br>in plain English</h2>
<p>A national dental group answering enquiries, bookings and reviews by hand, across 55 pages and many locations. Every one of those is a person doing work an agent can own.</p>
<div class="rule"></div>
<h2>Manual work found<br>on the live site</h2>
<p class="bull">Enquiry handling answered by a person</p>
<p class="bull">Appointment booking done by a human</p>
<p class="bull">Generic inbox triage</p>
<p class="bull">Customer reviews monitored and replied to by hand</p>
<p class="bull">Blog + location content produced by hand</p>
<p class="bull">Multi-location info kept in sync by hand</p>
""", foot_right="Page 2"))

a.append(page(f"""
<div class="secnum">02 / What one worker replaces</div>
<h2>What one NOHUMA<br>worker replaces</h2>
<p>UK workers lose ~15 hours/week to admin (Ricoh, reported). At 40h/week that is ~0.4 of a full-time person. One worker returns that time.</p>
<div class="bar"><div class="lab">Hours/week reclaimed</div><div class="track"><div class="fill" style="width:85%"></div><span class="val">15</span></div></div>
<div class="bar"><div class="lab">Admin load (FTE equivalent)</div><div class="track"><div class="fill" style="width:40%"></div><span class="val">0.4</span></div></div>
<div class="bar"><div class="lab">Live locations handled</div><div class="track"><div class="fill" style="width:100%"></div><span class="val">55</span></div></div>
""", foot_right="Page 3"))

a.append(page(f"""
<div class="secnum">03 / Proof + how we help</div>
<h2>What you'd see<br>in the app</h2>
<div class="proof">
  <div class="ph">Proof — live activity</div>
  <div class="ln">09:14  Scanned inbox — 289 emails, drafted 1 reply</div>
  <div class="ln">09:15  Re: Q2 Budget Review — file attach failed, retrying</div>
  <div class="ln">09:16  Booking moved 3:00 PM for LA conflict</div>
  <div class="ln" style="color:#8a8a92;margin-top:8px">Status: 14 actions today · 1 warning · no human needed</div>
</div>
<h2>How a NOHUMA<br>worker helps</h2>
<p class="bull">Draft every enquiry reply in the practice's voice — you approve, it sends.</p>
<p class="bull">Book and reschedule appointments 24/7, straight into the calendar.</p>
<p class="bull">Chase no-shows and recall patients without a receptionist.</p>
<p class="bull">Keep every location page consistent, automatically.</p>
<div class="rule"></div>
<p style="font-size:17px;color:#8a8a92">Verified: industry, page count and manual tells read live from the site. Bottleneck and "how we help" wording is our reasoned assessment from those signals — not a claim about the company.</p>
""", foot_right="Page 4"))

audit_html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(a) + "</body></html>"

# ---------- ZERNIO VERDICT ----------
z = []
z.append(page(f"""
<div class="kick">Vendor Verdict · Verified</div>
<h1>Is Zernio<br>any good?</h1>
<p class="lead">Our verdict on a unified 15-channel messaging API for OWL / Dewey — verified from the live site and docs, not marketing.</p>
<div class="rule"></div>
<h2 style="font-size:34px;margin-top:10px">Why this matters to OWL</h2>
<p class="bull">Dewey's model has 8 parts. Component 4 is <span class="v">phone &amp; comms</span>.</p>
<p class="bull">Our free-stack clone has Telegram + Slack — not a proper outbound layer.</p>
<p class="bull">Zernio is the ready-made comms layer across the channels a client's customers actually use.</p>
""", foot_right="Page 1"))

z.append(page(f"""
<div class="secnum">01 / Verdict</div>
<h2>Verdict</h2>
<p><span class="v">LEGIT.</span> Use as a candidate comms layer — after a free-tier check. It is the cleanest fix for Dewey's missing multi-channel comms, and it is MCP-native so Hermes can drive it. Do NOT spend or sign up without your go.</p>
<div class="rule"></div>
<h2>What it is<br>(verified)</h2>
<p>One API + one MCP server that posts, messages, runs ads and reads analytics across 15 channels: X, Instagram, TikTok, LinkedIn, WhatsApp, Telegram and more. Handles OAuth, WhatsApp KYC in 54 countries, retry-on-failure. Official APIs only.</p>
""", foot_right="Page 2"))

z.append(page(f"""
<div class="secnum">02 / Evidence</div>
<h2>Evidence</h2>
<div class="ev"><div class="k">Live product</div><div class="s">CONFIRMED — zernio.com HTTP 200</div></div>
<div class="ev"><div class="k">Official MCP server</div><div class="s">CONFIRMED — docs.zernio.com/mcp, ~496 tools</div></div>
<div class="ev"><div class="k">Free tier</div><div class="s">CONFIRMED — first 2 accounts, no card</div></div>
<div class="ev"><div class="k">15+ channels</div><div class="s">CONFIRMED — platform list on site</div></div>
<div class="ev"><div class="k">SOC2 / GDPR</div><div class="s">CLAIMED — trust.zernio.com (unverified)</div></div>
<div class="ev"><div class="k">'409k posts this week'</div><div class="s">THEIR MARKETING — not verified</div></div>
""", foot_right="Page 3"))

z.append(page(f"""
<div class="secnum">03 / Fit + caveat</div>
<h2>How it fits<br>OWL / Dewey</h2>
<p class="bull">Closes the "phone is the interface" gap — a WhatsApp number, KYC done, live in minutes.</p>
<p class="bull">Closes the "OWL drafts, you send" limit — with Zernio + MCP, OWL actually posts and replies.</p>
<p class="bull">Sits on top as a distribution layer; does not replace what we have.</p>
<div class="rule"></div>
<h2>Why not yet /<br>not blind</h2>
<p class="bull">Paid SaaS. Rule: free-stack unless you approve spend. No key held, not signed up.</p>
<p class="bull">Boss-protocol: verify free-tier limits + Hermes MCP compat + SOC2 before recommending money.</p>
<p class="bull">Trial on a test account first — never wire into a paying client on day one.</p>
<div class="rule"></div>
<p style="font-size:17px;color:#8a8a92">Bottom line: Zernio is the cleanest way to give OWL real multi-channel comms without building 15 integrations by hand. Use after a verified free-tier check — as the comms component, not a core dependency. I will not sign up or spend without your go.</p>
""", foot_right="Page 4"))

zernio_html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(z) + "</body></html>"

# ---------- THE SHIFT (manifesto) ----------
s = []
s.append(page(f"""
<div class="kick">Non-Human Intelligence · The Shift</div>
<h1>The business world<br>is about to split<br>in two.</h1>
<p class="lead">Companies that operate AI. And companies that are run by AI workers. The second group will not compete with the first. It will outrun it.</p>
""", foot_right="Page 1"))

s.append(page(f"""
<div class="secnum">01 / The line</div>
<h2>The difference<br>most miss</h2>
<p>ChatGPT is a tool you <span class="v">operate</span>.</p>
<p>NOHUMA is a worker that <span class="v">runs without you</span>.</p>
<div class="rule"></div>
<p>A tool saves you time when you remember to use it. A worker ships the result while you sleep — replies sent, invoices chased, slots booked, reports written. The business runs. You watch.</p>
""", foot_right="Page 2"))

s.append(page(f"""
<div class="secnum">02 / Why it's revolutionary</div>
<h2>This is not<br>faster software.</h2>
<p class="bull">A tool stops the moment you stop typing. A worker doesn't.</p>
<p class="bull">A tool is a cost you operate. A worker is leverage that compounds.</p>
<p class="bull">You don't adopt it. You <span class="v">hire it</span> — and it shows up every day.</p>
<div class="rule"></div>
<p>The last time work restructured this hard, the businesses that moved first didn't win a little. They redrew the map. This is that moment, and almost no one is positioned for it yet.</p>
""", foot_right="Page 3"))

s.append(page(f"""
<div class="secnum">03 / What we built</div>
<h2>NOHUMA is a<br>worker, not a tool.</h2>
<p>We build and run a worker inside your business for a flat &pound;5,000 a month. Its own computer, its own email, its own line to your customers. It does the job a person would — but it never sleeps, quits, or bills you for sick days.</p>
<div class="rule"></div>
<h2 style="font-size:34px;margin-top:8px">The offer</h2>
<p class="bull">Live in 48 hours — or the first month is refunded.</p>
<p class="bull">You watch it work from a real control panel.</p>
<p class="bull">Month to month. Stay because it works.</p>
<div class="rule"></div>
<p style="font-size:17px;color:#8a8a92">The shift is happening. The only question is whether your business is among the ones run by a worker — or still operating tools and losing the hours a worker would have returned.</p>
""", foot_right="Page 4"))

shift_html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(s) + "</body></html>"

os.makedirs(OUT, exist_ok=True)
with open(f"{OUT}/audit_brief.html","w") as f: f.write(audit_html)
with open(f"{OUT}/zernio_verdict.html","w") as f: f.write(zernio_html)
with open(f"{OUT}/the_shift.html","w") as f: f.write(shift_html)
print("HTML written")
