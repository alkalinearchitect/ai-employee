#!/usr/bin/env python3
"""Build the Owl white paper PDF: 'Non-Human Intelligence' — black bg, white text, high-detail."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, NextPageTemplate, PageBreak, KeepTogether)
from reportlab.pdfgen import canvas

INK   = colors.HexColor("#ffffff")
SOFT  = colors.HexColor("#a8a8b0")
MUTED = colors.HexColor("#7c7c85")
GREEN = colors.HexColor("#16a35a")
GREEN_RING = colors.HexColor("#5fbf8a")
BG    = colors.HexColor("#000000")
SURF  = colors.HexColor("#141414")
BORDER= colors.HexColor("#242424")

PW, PH = A4
ML = MR = 20*mm
FRAME_W = PW - ML - MR

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop("parent", styles["Normal"])
    return ParagraphStyle(name, parent=base, **kw)

st_title = S("t", fontName="Helvetica-Bold", fontSize=34, leading=38, textColor=INK, spaceAfter=8, alignment=TA_LEFT)
st_kick  = S("k", fontName="Helvetica", fontSize=10, leading=14, textColor=GREEN, spaceAfter=10)
st_h1    = S("h1", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=INK, spaceBefore=18, spaceAfter=8)
st_h2    = S("h2", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=GREEN_RING, spaceBefore=12, spaceAfter=5)
st_body  = S("b", fontName="Helvetica", fontSize=10.5, leading=16, textColor=SOFT, alignment=TA_JUSTIFY, spaceAfter=8)
st_quote = S("q", fontName="Helvetica-Oblique", fontSize=12.5, leading=18, textColor=INK, spaceBefore=10, spaceAfter=10, leftIndent=6)
st_small = S("s", fontName="Helvetica", fontSize=8.5, leading=12, textColor=MUTED)
st_bull  = S("bu", fontName="Helvetica", fontSize=10.5, leading=15, textColor=SOFT, leftIndent=12, spaceAfter=4, bulletIndent=2)

def hr():
    t = Table([[""]], colWidths=[FRAME_W], rowHeights=[1])
    t.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),0.6,BORDER)]))
    return t

def page_footer(c, doc):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,PW,PH,fill=1,stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(ML, 12*mm, "OWL — Non-Human Intelligence")
    c.drawRightString(PW-MR, 12*mm, "Page %d" % doc.page)
    c.setStrokeColor(BORDER); c.setLineWidth(0.5)
    c.line(ML, 15*mm, PW-MR, 15*mm)
    c.restoreState()

def page_one_bg(c, doc):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,PW,PH,fill=1,stroke=0)
    c.setFillColor(GREEN); c.circle(ML, PH-40*mm, 5)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(INK)
    c.drawString(ML+10*mm, PH-42*mm, "OWL")
    c.setFont("Helvetica", 8); c.setFillColor(MUTED)
    c.drawRightString(PW-MR, PH-42*mm, "Managed AI Employee · UK-First")
    c.restoreState()

doc = BaseDocTemplate("/root/ai-employee/owl-non-human-intelligence.pdf",
                      pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=22*mm, bottomMargin=20*mm,
                      title="Owl — Non-Human Intelligence", author="Owl")
frame = Frame(ML, 20*mm, FRAME_W, PH-42*mm, id="main")
cover = Frame(ML, 22*mm, FRAME_W, PH-64*mm, id="cover")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[cover], onPage=page_one_bg),
    PageTemplate(id="body", frames=[frame], onPage=page_footer),
])

E = []
# ---------- COVER ----------
E.append(Spacer(1, 26*mm))
E.append(Paragraph("NON-HUMAN", st_kick))
E.append(Paragraph("Intelligence", st_title))
E.append(Paragraph("The operating model for the AI employee your business runs but never hires.", st_body))
E.append(Spacer(1, 8*mm))
E.append(hr())
E.append(Spacer(1, 6*mm))
E.append(Paragraph("A field paper from Owl — the managed AI employee for UK small and mid-sized businesses (£1M–£2M turnover). Flat £5,000/month. Live in 48 hours.", st_small))
E.append(Spacer(1, 4*mm))
E.append(Paragraph("© Owl. This document describes the Owl operating model. No personal names, no third-party brands.", st_small))
E.append(NextPageTemplate("body"))
E.append(PageBreak())

# ---------- 1. THE SHIFT ----------
E.append(Paragraph("01 — The shift", st_h1))
E.append(Paragraph("For a century, a business was bottlenecked by people: one person per task, one task per hour, one sick day at a time. That constraint is ending. Not because humans are replaceable, but because a large class of recurring work — the work that keeps a company small — does not require a human. It requires an agent that never sleeps, never forgets, and never asks for a raise.", st_body))
E.append(Paragraph("We call this class of system <b>non-human intelligence</b>: software that owns a workflow end to end, operates inside your business, and delivers the outcome — not a suggestion, not a draft, the result.", st_body))
E.append(Paragraph("“Your best hire this year won't be a person.”", st_quote))
E.append(hr())

# ---------- 2. WHAT IT IS ----------
E.append(Paragraph("02 — What non-human intelligence is", st_h1))
E.append(Paragraph("Non-human intelligence is not a chatbot. A chatbot waits for a prompt. An AI employee owns the job. The distinction is the difference between a tool you operate and a worker you manage.", st_body))
rows = [
    ["", "Chatbot / LLM tool", "Managed AI employee (Owl)"],
    ["Initiative", "Waits for your prompt", "Owns a workflow autonomously"],
    ["Where it lives", "A window you open", "Your Slack, Telegram, email, calendar"],
    ["Who runs it", "You", "We run it — fully managed"],
    ["Output", "A response", "The work, done"],
    ["You touch the tech?", "Yes", "No"],
]
tbl = Table(rows, colWidths=[FRAME_W*0.28, FRAME_W*0.34, FRAME_W*0.38])
tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),SURF),
    ("TEXTCOLOR",(0,0),(-1,0),GREEN_RING),
    ("TEXTCOLOR",(0,1),(0,-1),SOFT),
    ("TEXTCOLOR",(1,1),(1,-1),MUTED),
    ("TEXTCOLOR",(2,1),(2,-1),INK),
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
    ("FONTNAME",(0,1),(0,-1),"Helvetica-Bold"),
    ("FONTSIZE",(0,0),(-1,-1),9),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("LINEBELOW",(0,0),(-1,-1),0.5,BORDER),
    ("LINEAFTER",(0,0),(0,-1),0.5,BORDER),
    ("LINEAFTER",(1,0),(1,-1),0.5,BORDER),
]))
E.append(tbl)
E.append(Spacer(1, 4*mm))
E.append(Paragraph("An Owl agent is a managed employee with a full operating stack: one central brain directs four specialist agents — one finds and chases leads, one follows up and closes, one produces your content and assets, one does the fulfilment work.", st_body))
E.append(hr())

# ---------- 3. THE EIGHT PARTS ----------
E.append(Paragraph("03 — The eight parts", st_h1))
E.append(Paragraph("Miss one and it is a toy, not a worker. Every Owl agent is built on eight components:", st_body))
parts = [
    ("01 Its own computer", "A dedicated server for your agent alone. No shared tenant, no neighbour noise, no other client's data near yours."),
    ("02 Its own email", "A domain address in your name. It sends and receives as a real member of your team."),
    ("03 A live line", "A working Telegram line. Message it, it answers. Reachable, not a black box."),
    ("04 Your channels", "Wired into your Slack or Telegram. It works where your team already talks."),
    ("05 Real tools", "It uses your systems — files, the web, the terminal behind it. It does the job, not just describes it."),
    ("06 Simple billing", "One invoice, one price, every month. No per-seat maths, no usage surprises."),
    ("07 A memory of your business", "One governed knowledge layer — one fact, one home. Pricing, customers, do-and-don'ts, all in a single source. This is the edge: it stays accurate because it knows you, not the open internet."),
    ("08 Watching it", "Health checks run constantly and alert us before your customer ever notices."),
]
for n, txt in parts:
    E.append(Paragraph(f"<b>{n} — {n.split()[1]} {n.split()[2] if len(n.split())>2 else ''}</b> {txt}", st_bull))
E.append(hr())

# ---------- 4. WHY IT PAYS ----------
E.append(Paragraph("04 — Why it pays", st_h1))
E.append(Paragraph("A decent UK employee runs £30k–£45k before National Insurance, onboarding, and the three-month ramp to usefulness. Then they take leave, they quit, they have off days. Owl is £5,000 a month — no recruitment, no employment law, no maternity leave, no complaints, and it never clocks out.", st_body))
E.append(Paragraph("The real maths is not headcount. It is the leads your old process drops. A business taking 200 enquiries a month and losing 30% of them at £500 average value is leaving £24,000 a year on the table. An Owl agent that recovers 80% of that gap returns £19,200 a year from one workflow — and it scales to the next workflow, and the next.", st_body))
E.append(Paragraph("“The question isn't 'why pay £5k for an AI agent?' It's 'why pay far more for a human to do the work an agent does better, 24/7?'”", st_quote))
E.append(hr())

# ---------- 5. THE GUARANTEES ----------
E.append(Paragraph("05 — The guarantees", st_h1))
for g in [
    ("Live in 48 hours.", "Or the first month is refunded — automatically, no form, no debate."),
    ("Saves you more than £5k/month.", "Measured at day 30 against the human hours it replaced. If not, first month refunded."),
    ("Your data stays yours.", "Isolated environment, scoped — not blanket — access. Portable on exit."),
    ("No contract. Cancel anytime.", "Month to month. Stay because it works, not because you're trapped."),
]:
    E.append(Paragraph(f"<b>{g[0]}</b> {g[1]}", st_bull))
E.append(Spacer(1, 4*mm))
E.append(Paragraph("Every client gets a live dashboard showing the work done, the leads chased, and the hours reclaimed — measured against the human cost it replaced. On the call we walk you through a live client dashboard in your exact industry, end to end, so you see the proof before you decide.", st_body))
E.append(hr())

# ---------- 6. RESALE / FLEET ----------
E.append(Paragraph("06 — From one agent to a fleet", st_h1))
E.append(Paragraph("Start with one workflow — lead follow-up. Then we expand to the next, then the next. Before long you have a fleet of agents, each owning a piece of the operation. And the agent that runs your business can be offered to your own customers under your label. That covers Owl several times over, so it is not a cost — it is a profit line. It is also why clients do not churn: Owl becomes part of what you sell.", st_body))
E.append(Spacer(1, 6*mm))
E.append(Paragraph("Owl is built to be resold. You offer the agent under your own name; it becomes a revenue line, not a bill.", st_small))
E.append(Spacer(1, 8*mm))
E.append(hr())
E.append(Spacer(1, 4*mm))
E.append(Paragraph("Bring one workflow to a 20-minute call. Leave with a one-page scope statement — no obligation, no pitch.", st_body))
E.append(Paragraph("owl · managed AI employee · £5,000/month · live in 48 hours or refunded", st_small))

doc.build(E)
print("PDF built: /root/ai-employee/owl-non-human-intelligence.pdf")
