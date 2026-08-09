#!/usr/bin/env python3
import html, subprocess, os
OUT = "/root/ai-employee/revenue-os/out_build"

CSS = """
@font-face{font-family:'Inter';src:url('file:///root/fonts/Inter-Regular.ttf') format('truetype');font-weight:400;font-style:normal;}
@font-face{font-family:'Inter';src:url('file:///root/fonts/Inter-Medium.ttf') format('truetype');font-weight:500;font-style:normal;}
@font-face{font-family:'Inter';src:url('file:///root/fonts/Inter-Bold.ttf') format('truetype');font-weight:700;font-style:normal;}
*{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
@page{size:9in 12in;margin:0;}
html,body{background:#000;}
.page{position:relative;width:864px;height:1152px;background:#000000;color:#FFFFFF;overflow:hidden;page-break-after:always;padding:96px 88px 92px 88px;display:flex;flex-direction:column;}
.page:last-child{page-break-after:auto;}
.wm{position:absolute;right:40px;bottom:110px;font-size:250px;font-weight:700;color:#8b5cf6;opacity:0.09;letter-spacing:-10px;line-height:1;}
.wm.tr{right:40px;top:150px;bottom:auto;font-size:220px;}
.kicker{font-size:30px;font-weight:500;color:#8b5cf6;letter-spacing:5px;text-transform:uppercase;line-height:1.4;}
.rule{width:150px;height:5px;background:#8b5cf6;margin:34px 0 40px 0;border-radius:3px;}
h1{font-size:92px;font-weight:700;line-height:1.1;letter-spacing:-3px;color:#FFFFFF;}
.body{font-size:42px;font-weight:400;line-height:1.5;color:#EDEDED;margin-top:44px;max-width:660px;}
.pnum{position:absolute;right:88px;bottom:60px;font-size:26px;font-weight:500;color:#6b6b73;letter-spacing:3px;}
.foot{position:absolute;left:88px;bottom:60px;font-size:26px;font-weight:400;color:#6b6b73;letter-spacing:1px;}
.spacer{flex:1;}
.cover-title{font-size:120px;font-weight:700;line-height:1.02;letter-spacing:-5px;}
.cover-sub{font-size:46px;font-weight:400;line-height:1.45;color:#EDEDED;margin-top:46px;max-width:670px;}
ul{list-style:none;margin-top:40px;}
li{font-size:42px;font-weight:400;line-height:1.42;color:#EDEDED;margin-bottom:26px;padding-left:44px;position:relative;}
li:before{content:"";position:absolute;left:0;top:24px;width:20px;height:5px;background:#8b5cf6;border-radius:3px;}
.big{font-size:150px;font-weight:700;letter-spacing:-6px;line-height:1;color:#FFFFFF;}
.big span{color:#8b5cf6;font-size:64px;letter-spacing:-2px;}
.num{font-size:30px;font-weight:700;color:#8b5cf6;letter-spacing:5px;}
"""

def page(inner, num, total, foot="OWL &nbsp;·&nbsp; NON-HUMAN INTELLIGENCE", wm="NHI", wmtr=False):
    cls = "wm tr" if wmtr else "wm"
    return (f'<div class="page"><div class="{cls}">{wm}</div>{inner}'
            f'<div class="foot">{foot}</div>'
            f'<div class="pnum">{num:02d} / {total:02d}</div></div>')

def std(kicker, h1, body="", bullets=None, num=1, total=8, wmtr=False):
    s = f'<div class="kicker">{kicker}</div><div class="rule"></div><h1>{h1}</h1>'
    if body: s += f'<div class="body">{body}</div>'
    if bullets:
        s += '<ul>' + ''.join(f'<li>{b}</li>' for b in bullets) + '</ul>'
    s += '<div class="spacer"></div>'
    return page(s, num, total, wmtr=wmtr)

def doc(pages):
    return ("<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + CSS +
            "</style></head><body>" + "".join(pages) + "</body></html>")

# ---------------- DECK A ----------------
T = 8
A = []
A.append(page(
    '<div class="kicker">Owl &nbsp;·&nbsp; Non-Human Intelligence</div><div class="rule"></div>'
    '<div class="spacer"></div>'
    '<div class="cover-title">Pricing<br>&amp; Scope</div>'
    '<div class="cover-sub">One price. Everything included.<br>£5,000 a month.</div>'
    '<div class="spacer"></div>', 1, T, foot="HUMAN ARCHITECT", wm="OWL"))

A.append(std("Positioning", "Owl is not<br>software.",
    "Software waits to be used. Owl works. It is Non-Human Intelligence &mdash; a hired mind with its own computer, its own email, and a line you can talk to.",
    num=2, total=T))

A.append(page(
    '<div class="kicker">The Price</div><div class="rule"></div>'
    '<div class="big">£5,000<span>/mo</span></div>'
    '<div class="body">Flat. Build, hosting, onboarding and operation included. '
    'No setup fee. No per-seat. No usage add-ons.</div><div class="spacer"></div>', 3, T))

A.append(std("What&rsquo;s Included", "Eight parts.<br>One hire.", bullets=[
    "Its own computer", "Its own email", "A live Telegram line",
    "Your Slack or Telegram", "Real tools, real access",
    "Simple billing", "Memory: one fact, one home", "Constant health checks"],
    num=4, total=T, wmtr=True))

A.append(std("The Team Inside", "One brain.<br>Four specialists.",
    "Outbound. Sales follow-up. Content. Support. One mind coordinating all four, awake at every hour you are not.",
    num=5, total=T))

A.append(std("Guarantee &nbsp;/&nbsp; 48 Hours", "Live in 48 hours,<br>or month one<br>is free.",
    "Forty-eight hours from the scoping call. If we miss it, your first month is refunded. No argument.",
    num=6, total=T))

A.append(std("Guarantee &nbsp;/&nbsp; Day 30", "It pays for itself,<br>or it costs<br>nothing.",
    "On day thirty, if Owl has not saved you more than £5,000 in human hours, your first month is refunded.",
    num=7, total=T, wmtr=True))

A.append(page(
    '<div class="kicker">Yours, Not Ours</div><div class="rule"></div>'
    '<h1>White-label.<br>Cancel anytime.</h1>'
    '<ul><li>Runs on your own isolated, self-hosted server</li>'
    '<li>Scoped access &mdash; the data stays yours</li>'
    '<li>Portable on exit. You leave with everything</li>'
    '<li>Single tier. No recruitment. A revenue line, not a cost</li></ul>'
    '<div class="body" style="margin-top:56px">Book a scoping call:<br>'
    '<span style="color:#8b5cf6;font-weight:700">beacons.ai/humanarchitect</span></div>'
    '<div class="spacer"></div>', 8, T, wm="OWL"))

# ---------------- DECK B ----------------
T2 = 9
B = []
B.append(page(
    '<div class="kicker">Owl &nbsp;·&nbsp; Non-Human Intelligence</div><div class="rule"></div>'
    '<div class="spacer"></div>'
    '<div class="cover-title">Seven<br>Objections.</div>'
    '<div class="cover-sub">And the honest answer to each one.</div>'
    '<div class="spacer"></div>', 1, T2, foot="OBJECTION &amp; CLOSE PLAYBOOK", wm="OWL"))

objs = [
 ("01 &nbsp;·&nbsp; Too expensive", "A junior costs more<br>and sleeps.",
  "£5,000 a month, flat, is one salary &mdash; without recruitment, holiday, sickness or notice. And it works through the night.", False),
 ("02 &nbsp;·&nbsp; Replaces my team", "It does the work<br>nobody wanted.",
  "Follow-up. Chasing. Admin at midnight. Owl takes the load your people resent, so they do the work only people can do.", True),
 ("03 &nbsp;·&nbsp; Is my data safe", "Your data never<br>leaves your house.",
  "Owl lives on an isolated server that is yours, with scoped access only. Nothing is pooled. Nothing is sold.", False),
 ("04 &nbsp;·&nbsp; What if it breaks", "It checks itself,<br>constantly.",
  "Health checks run without being asked, and a human operator stands behind them. You have a live Telegram line to say so.", False),
 ("05 &nbsp;·&nbsp; We already use ChatGPT", "A chat window<br>is not a colleague.",
  "ChatGPT waits for you to type. Owl has its own computer, its own email, real tools and a memory &mdash; one fact, one home.", True),
 ("06 &nbsp;·&nbsp; 48 hours is too fast", "If it isn&rsquo;t live<br>in 48 hours,<br>you pay nothing.",
  "We have built this before. The scoping call is the hard part. If we miss the window, month one is refunded.", False),
 ("07 &nbsp;·&nbsp; Am I locked in", "Cancel anytime.<br>Leave with<br>everything.",
  "Single tier, month to month, white-label. On exit it is portable &mdash; the work, the memory, the setup all come with you.", False),
]
for i,(k,h,b,tr) in enumerate(objs, start=2):
    B.append(std(k, h, b, num=i, total=T2, wmtr=tr))

B.append(page(
    '<div class="kicker">The Close</div><div class="rule"></div>'
    '<h1>Speed decides<br>who wins.</h1>'
    '<ul><li>Reply within one hour: 7x more likely to qualify a lead (HBR)</li>'
    '<li>78% of buyers buy from whoever answers first</li>'
    '<li>Owl answers first. Every time.</li></ul>'
    '<div class="body" style="margin-top:56px">Book a scoping call:<br>'
    '<span style="color:#8b5cf6;font-weight:700">beacons.ai/humanarchitect</span></div>'
    '<div class="spacer"></div>', 9, T2, wm="OWL"))

for name, pages in (("owl-pricing-scope", A), ("owl-objection-close", B)):
    hp = f"{OUT}/{name}.html"
    open(hp, "w").write(doc(pages))
    subprocess.run(["/usr/bin/google-chrome","--headless","--no-sandbox","--disable-gpu",
                    "--no-pdf-header-footer",f"--print-to-pdf={OUT}/{name}.pdf",
                    f"file://{hp}"], check=True, capture_output=True)
    print("built", name)
