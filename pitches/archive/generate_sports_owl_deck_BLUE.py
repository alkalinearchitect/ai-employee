#!/usr/bin/env python3
"""
Generate a 10-page BLUE TEAM pitch deck PDF for OWL targeting sports teams.

VARIANT B - "PREMIUM DARK":
- 3:4 ratio: 180mm x 240mm
- Background: #0a0a0a, cards: #141418
- Accent: orange #ff5c1f
- Instagram carousel style: large text, one idea per page, high readability
"""

from reportlab.lib.pagesizes import portrait
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

WIDTH_MM = 180
HEIGHT_MM = 240
PAGE_WIDTH = WIDTH_MM * mm
PAGE_HEIGHT = HEIGHT_MM * mm

MARGIN = 16 * mm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

BG = HexColor("#0a0a0a")
ACCENT = HexColor("#ff5c1f")
WHITE = HexColor("#ffffff")
LIGHT = HexColor("#cccccc")
GRAY = HexColor("#888888")
DARK_GRAY = HexColor("#2a2a2a")
CARD_BG = HexColor("#141418")

# Carousel-style sizing: big, bold, readable on phone
TITLE_SIZE = 36
HEADING_SIZE = 22
BODY_SIZE = 15
CAPTION_SIZE = 10
HEADER_SIZE = 9
SMALL_SIZE = 8

OUT_PATH = "/root/ai-employee/pitches/sports-owl-10page-BLUE.pdf"

try:
    pdfmetrics.registerFont(TTFont("Helvetica", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"))
    BODY_FONT = "Helvetica"
except Exception:
    BODY_FONT = "Helvetica"

try:
    pdfmetrics.registerFont(TTFont("Helvetica-Bold", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"))
    BOLD_FONT = "Helvetica-Bold"
except Exception:
    BOLD_FONT = BODY_FONT


def draw_background(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)


def draw_header(c):
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, HEADER_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 12 * mm, "OWL  |  SPORTS  |  CONFIDENTIAL")
    c.setStrokeColor(HexColor("#1f1f1f"))
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_HEIGHT - 14 * mm, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 14 * mm)
    c.setFillColor(ACCENT)
    c.circle(MARGIN + 100, PAGE_HEIGHT - 12 * mm, 1.2, fill=1, stroke=0)


def draw_footer(c, page_num, total=10):
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, SMALL_SIZE)
    c.drawRightString(PAGE_WIDTH - MARGIN, 10 * mm, f"{page_num} / {total}")
    c.setStrokeColor(HexColor("#1f1f1f"))
    c.setLineWidth(0.5)
    c.line(MARGIN, 12 * mm, PAGE_WIDTH - MARGIN, 12 * mm)


def draw_big_title(c, text, y):
    c.setFillColor(ACCENT)
    c.setFont(BOLD_FONT, TITLE_SIZE)
    c.drawString(MARGIN, y, text)
    c.setStrokeColor(DARK_GRAY)
    c.setLineWidth(1.2)
    c.line(MARGIN, y - 4 * mm, MARGIN + 70 * mm, y - 4 * mm)
    return y - 14 * mm


def draw_big_heading(c, text, y):
    c.setFillColor(WHITE)
    c.setFont(BOLD_FONT, HEADING_SIZE)
    c.drawString(MARGIN, y, text)
    return y - 10 * mm


def draw_big_text(c, text, x, y, max_width, leading=24):
    words = text.split()
    line = ""
    c.setFont(BODY_FONT, BODY_SIZE)
    c.setFillColor(WHITE)
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, BODY_FONT, BODY_SIZE) <= max_width:
            line = test
        else:
            if line:
                c.drawString(x, y, line)
                y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullet_line(c, bullet, text, x, y, max_width, leading=24):
    c.setFillColor(ACCENT)
    c.setFont(BOLD_FONT, BODY_SIZE)
    c.drawString(x, y, bullet)
    y = draw_big_text(c, text, x + 14 * mm, y, max_width - 14 * mm, leading=leading)
    y -= 10
    return y


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def page_1_cover(c):
    draw_background(c)
    draw_header(c)
    y = PAGE_HEIGHT - 70 * mm
    c.setFillColor(WHITE)
    c.setFont(BOLD_FONT, TITLE_SIZE + 10)
    c.drawString(MARGIN, y, "OWL")
    y -= 22 * mm
    c.setFillColor(ACCENT)
    c.setFont(BOLD_FONT, TITLE_SIZE - 4)
    c.drawString(MARGIN, y, "FOR SPORTS TEAMS")
    y -= 20 * mm
    c.setFillColor(LIGHT)
    c.setFont(BOLD_FONT, 16)
    c.drawString(MARGIN, y, "MANAGED AI ENGINEER")
    y -= 26 * mm
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, y, "Your forward-deployed engineer.")
    y -= 10 * mm
    c.drawString(MARGIN, y, "Builds, automates, and supports — 48 hours.")
    y -= 28 * mm
    c.setFillColor(DARK_GRAY)
    c.setFont(BODY_FONT, CAPTION_SIZE)
    c.drawString(MARGIN, y, "AUGMENTATION, NOT REPLACEMENT.")
    draw_footer(c, 1)


def page_2_problem(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "THE PROBLEM", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Your team bleeds on the same four bottlenecks every week.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    pains = [
        ("01", "TALENT GAPS", "Too few analysts. Blind spots between training and matchday."),
        ("02", "MANUAL GRIND", "Hours lost to pulls, wrangling, and reporting."),
        ("03", "SLOW INSIGHTS", "Questions answered after the press conference."),
        ("04", "FRAGMENTED DATA", "Scouting, medical, performance stuck in silos."),
    ]
    for num, title, desc in pains:
        y = draw_bullet_line(c, num, f"{title} — {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 12

    draw_footer(c, 2)


def page_3_what(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "WHAT OWL DOES", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "A verified managed AI employee. Not a chatbot.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    rows = [
        ("DATA", "Pulls and normalises Opta, tracking, video, medical, scouting exports."),
        ("MODELS", "xG/xA, passing networks, PPDA, transition, set-piece maps."),
        ("INSIGHTS", "Flags anomalies and suggests focuses. Coaching-ready."),
        ("AUTOMATION", "Tags events, generates clips, builds reports, schedules."),
        ("DELIVERY", "Briefing cards to Telegram, iMessage, or Slack with archive."),
    ]
    for title, desc in rows:
        y = draw_bullet_line(c, ">", f"{title}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8

    draw_footer(c, 3)


def page_4_stack(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "THE STACK", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Confirmed components only. No black-box claims.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    items = [
        ("PYTHON / SQL / JS", "Python backend, SQL pipelines, React/TypeScript frontends."),
        ("PYDATA", "numpy, pandas/polars, matplotlib/Altair."),
        ("COMPUTER USE", "Operates software, fills forms, generates reports."),
        ("MESSAGING", "Telegram, iMessage, Slack for analysts and coaches."),
        ("ORGO + 13 MCPs", "AgentMail, AgentPhone, AgentCard, Composio, Latitude, Honcho, Obsidian."),
        ("MODELS", "gpt-5.5 / gpt-5.6-sol class reasoning, swappable."),
    ]
    for title, desc in items:
        y = draw_bullet_line(c, ">", f"{title}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6

    draw_footer(c, 4)


def page_5_usecases(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "USE CASES", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Built for real sports operations.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    cases = [
        ("MATCH ANALYSIS", "Post-match insight cards within 60 minutes."),
        ("SCOUTING SHORTCUTS", "Automated tagging, clip search, opponent profiles."),
        ("PERFORMANCE BRIEFS", "Weekly readiness and load digests for coaches."),
        ("SET-PIECE DESIGN", "Corner/free-kick threat maps by zone."),
        ("STAFF SUPPORT", "Telegram/iMessage/Slack bot for analysts."),
    ]
    for title, desc in cases:
        y = draw_bullet_line(c, ">", f"{title}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6

    draw_footer(c, 5)


def page_6_deployment(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "DEPLOYMENT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "From now to first briefing card in 48 hours.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    steps = [
        ("0-4H", "Access provisioning: data exports, video, schemas."),
        ("4-12H", "Schema mapping and club-specific alignment."),
        ("12-24H", "Warm-start on last season data."),
        ("24-36H", "Validation against known fixtures."),
        ("36-48H", "Go-live. First briefing card sent."),
    ]
    for step, desc in steps:
        y = draw_bullet_line(c, step, desc, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8

    draw_footer(c, 6)


def page_7_integration(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "INTEGRATION", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "No new logins. No new workflows.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    channels = [
        ("TELEGRAM / IMessage", "Threaded comms with analysts and coaches."),
        ("SLACK", "Embedded support in existing channels."),
        ("EMAIL", "Digest and alert distribution."),
        ("VOICE", "Fast outbriefs when text isn't enough."),
    ]
    for channel, desc in channels:
        y = draw_bullet_line(c, ">", f"{channel}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6

    draw_footer(c, 7)


def page_8_proof(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "PROOF", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Verified public signals only.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    proofs = [
        "Managed AI employee is live. $5,000/month confirmed client.",
        "Agent builds and onboards client systems autonomously.",
        "Customer support runs without human intervention.",
        "Stack proven: agent mail, phone, card, observability, vault.",
        "B2B2B path proven: resell lowers churn.",
    ]
    for line in proofs:
        y = draw_bullet_line(c, "-", line, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    y -= 12

    c.setFillColor(WHITE)
    c.setFont(BOLD_FONT, HEADING_SIZE)
    c.drawString(MARGIN, y, "WHAT OWL WON'T DO")
    y -= 10 * mm
    cannot = [
        "Replace your head of analysis or coaching staff.",
        "Guarantee outcomes without your data and buy-in.",
        "Operate without secure access to your exports.",
    ]
    for line in cannot:
        y = draw_bullet_line(c, "-", line, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 4

    draw_footer(c, 8)


def page_9_pricing(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "PRICING", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Three models. Same outcome.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    models = [
        ("SINGLE TEAM", "£5,000 / month", "One team. One workflow. Flat fee."),
        ("CLUB / ORG", "£12,000 / month", "Multiple departments. Shared agent."),
        ("RESELL / WHITE-LABEL", "£8,000 / month + 20% rev share", "You sell it. We run it."),
    ]

    for name, price, desc in models:
        c.setFillColor(CARD_BG)
        c.roundRect(MARGIN, y - 48 * mm, CONTENT_WIDTH, 40 * mm, 6, fill=1, stroke=0)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.2)
        c.roundRect(MARGIN, y - 48 * mm, CONTENT_WIDTH, 40 * mm, 6, fill=0, stroke=1)
        c.setFillColor(ACCENT)
        c.rect(MARGIN + 8, y - 14, 3, 30, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BOLD_FONT, HEADING_SIZE - 2)
        c.drawString(MARGIN + 18, y - 12 * mm, name)
        c.setFillColor(ACCENT)
        c.setFont(BOLD_FONT, TITLE_SIZE - 12)
        c.drawString(MARGIN + 18, y - 24 * mm, price)
        c.setFillColor(LIGHT)
        c.setFont(BODY_FONT, BODY_SIZE - 1)
        c.drawString(MARGIN + 18, y - 34 * mm, desc)
        y -= 56 * mm

    draw_footer(c, 9)


def page_10_close(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "NEXT STEP", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Only 3 Club/Organization slots left for Q3.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 12 * mm
    y = draw_big_text(c, "Next Single Team cohort starts Monday.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 12 * mm
    y = draw_big_text(c, "Lock your price before Q4 launch.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 20 * mm

    c.setFillColor(ACCENT)
    c.roundRect(MARGIN, y - 40 * mm, CONTENT_WIDTH, 28 * mm, 6, fill=1, stroke=0)
    c.setFillColor(BG)
    c.setFont(BOLD_FONT, HEADING_SIZE - 2)
    c.drawString(MARGIN + 10 * mm, y - 14 * mm, "BOOK NOW")
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN + 10 * mm, y - 24 * mm, "beacons.ai/humanarchitect")
    y -= 48 * mm
    y = draw_big_text(c, "Response within 24 hours. No obligation.",
                      MARGIN, y, CONTENT_WIDTH, leading=24)
    draw_footer(c, 10)


def build():
    c = canvas.Canvas(OUT_PATH, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    pages = [
        page_1_cover,
        page_2_problem,
        page_3_what,
        page_4_stack,
        page_5_usecases,
        page_6_deployment,
        page_7_integration,
        page_8_proof,
        page_9_pricing,
        page_10_close,
    ]
    for fn in pages:
        fn(c)
        c.showPage()
    c.save()
    print("Generated:", OUT_PATH)


if __name__ == "__main__":
    build()
