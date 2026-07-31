#!/usr/bin/env python3
"""
Generate a 20-page OWL sports dossier/brochure PDF.

Forensic alignment to Arsenal Research Engineer JD:
- Full-stack build
- Applied ML
- Analyst/coach collaboration
- Production tooling
- Football-specific outputs
- Matchday intensity

- 3:4 ratio: 180mm x 240mm
- Black background #000000, accent #00b4ff
- One idea per page, carousel text
- No Hermes/Dewey mentions
- No hallucinated stats
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

MARGIN = 18 * mm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

BG = HexColor("#000000")
ACCENT = HexColor("#00b4ff")
WHITE = HexColor("#ffffff")
LIGHT = HexColor("#cccccc")
GRAY = HexColor("#aaaaaa")
DARK_GRAY = HexColor("#333333")

TITLE_SIZE = 36
HEADING_SIZE = 22
BODY_SIZE = 15
CAPTION_SIZE = 11
HEADER_SIZE = 11
SMALL_SIZE = 10

OUT_PATH = "/root/ai-employee/pitches/owl-sports-dossier-20page.pdf"

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
    c.setStrokeColor(DARK_GRAY)
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_HEIGHT - 14 * mm, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 14 * mm)


def draw_footer(c, page_num, total=20):
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, SMALL_SIZE)
    c.drawRightString(PAGE_WIDTH - MARGIN, 10 * mm, f"{page_num} / {total}")
    c.setStrokeColor(DARK_GRAY)
    c.setLineWidth(0.5)
    c.line(MARGIN, 12 * mm, PAGE_WIDTH - MARGIN, 12 * mm)


def draw_big_title(c, text, y):
    c.setFillColor(WHITE)
    c.setFont(BOLD_FONT, TITLE_SIZE)
    c.drawString(MARGIN, y, text)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(MARGIN, y - 4 * mm, MARGIN + 70 * mm, y - 4 * mm)
    return y - 14 * mm


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
    c.drawString(MARGIN, y, "FOR ARSENAL FIRST TEAM")
    y -= 20 * mm
    c.setFillColor(LIGHT)
    c.setFont(BOLD_FONT, 16)
    c.drawString(MARGIN, y, "APPLIED AI ENGINEER")
    y -= 26 * mm
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, y, "Embedded with Men's First Team Analysis.")
    y -= 10 * mm
    c.drawString(MARGIN, y, "Builds, deploys, and supports — 48 hours.")
    y -= 28 * mm
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, CAPTION_SIZE)
    c.drawString(MARGIN, y, "AUGMENTATION, NOT REPLACEMENT.")
    draw_footer(c, 1)


def page_2_problem(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "THE PROBLEM", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "The gap between analysis need and engineering delivery costs wins.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    pains = [
        ("01", "ENGINEER SHORTAGE", "Hard to hire applied ML engineers who understand football."),
        ("02", "MANUAL GRIND", "Analysts repeat pulls, wrangling, and reporting instead of analysing."),
        ("03", "SLOW INSIGHTS", "Tactical questions unanswered by matchday press conference."),
        ("04", "FRAGMENTED DATA", "Scouting, medical, tracking, and video stuck in silos."),
    ]
    for num, title, desc in pains:
        y = draw_bullet_line(c, num, f"{title} — {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 12
    draw_footer(c, 2)


def page_3_roi(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "WHY OWL OVER A RESEARCH ENGINEER HIRE?", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Same build capability. Lower cost. Zero recruiting delay.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    rows = [
        ("", "RESEARCH ENGINEER", "OWL"),
        ("COST", "£45-65K/year + benefits", "£5K/month flat"),
        ("DEPLOY TIME", "6-10 weeks hire + onboard", "48 hours"),
        ("SCHEDULE FLEX", "Monday-Friday, office-bound", "Always on, matchday-ready"),
        ("CONTEXT LOSS", "High — holiday, sick, turnover", "None — persistent memory"),
        ("OUTPUT", "Human-limited batch work", "Continuous automation + briefing cards"),
    ]
    col1 = CONTENT_WIDTH * 0.45
    col2 = CONTENT_WIDTH * 0.30
    col3 = CONTENT_WIDTH * 0.25
    row_h = 24 * mm
    x = MARGIN
    for i, row in enumerate(rows):
        if i == 0:
            c.setFillColor(ACCENT)
            c.roundRect(x, y - row_h, CONTENT_WIDTH, row_h, 4, fill=1, stroke=0)
            c.setFillColor(BG)
            c.setFont(BOLD_FONT, BODY_SIZE + 1)
            c.drawString(x + 8, y - 12 * mm, row[0])
            c.drawString(x + col1 + 8, y - 12 * mm, row[1])
            c.drawString(x + col1 + col2 + 8, y - 12 * mm, row[2])
        else:
            c.setFillColor(HexColor("#050505"))
            c.roundRect(x, y - row_h, CONTENT_WIDTH, row_h, 4, fill=1, stroke=0)
            c.setStrokeColor(DARK_GRAY)
            c.setLineWidth(0.5)
            c.roundRect(x, y - row_h, CONTENT_WIDTH, row_h, 4, fill=0, stroke=1)
            c.setFillColor(WHITE if i % 2 == 1 else LIGHT)
            c.setFont(BOLD_FONT if i % 2 == 1 else BODY_FONT, BODY_SIZE)
            c.drawString(x + 8, y - 12 * mm, row[0])
            c.setFillColor(LIGHT)
            c.setFont(BODY_FONT, BODY_SIZE)
            c.drawString(x + col1 + 8, y - 12 * mm, row[1])
            c.drawString(x + col1 + col2 + 8, y - 12 * mm, row[2])
        y -= row_h
    draw_footer(c, 3)


def page_4_design_build(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "DESIGN AND DEVELOP FULL-STACK APPLICATIONS", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Production-grade internal products for the Men's First Team.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "End-to-end data-driven applications for analysts and coaches.",
        "Efficient, reliable, scalable interfaces for football workflows.",
        "React/TypeScript frontends with Python/SQL backends.",
        "Schema-aligned exports from Opta, tracking, video, and scouting.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 4)


def page_5_streamline(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "STREAMLINE CRITICAL PROCESSES", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Full-stack engineering plus applied ML, aimed at real football tasks.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Automate repetitive analysis tasks: tagging, clipping, reporting.",
        "Applied ML for event detection, player tracking, and pattern recognition.",
        "Reduce analyst workload so they focus on interpretation, not wrangling.",
        "Ship proven automation in days, not quarters.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 5)


def page_6_collaborate(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "COLLABORATE WITH FOOTBALL ANALYSIS", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Deep process understanding before any code.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Work directly with analysts to understand real workflows.",
        "Proactively plan and implement technical solutions.",
        "Augment, refine, and improve existing processes.",
        "Available around training and matchday schedules.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 6)


def page_7_applied_ai(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "APPLIED AI SPECIALIST", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Subject matter expert at the intersection of AI and football analysis.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Drive adoption of state-of-the-art AI in coaching workflows.",
        "Identify new applied research opportunities.",
        "Translate coaching needs into production systems.",
        "Bridge the gap between analysts and engineers.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 7)


def page_8_research_impact(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "MAXIMISE RESEARCH IMPACT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Every build grounded in coaching need, every output matchday-ready.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Ensure research is grounded in concrete coaching and analysis needs.",
        "Account for real-world constraints: time, data quality, staff availability.",
        "Deliver dashboards and briefings that coaches actually use.",
        "Measure impact by decision speed and consistency, not paper metrics.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 8)


def page_9_stack(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "THE STACK", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Exact match to the Research Engineer requirements.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    items = [
        ("PYTHON / SQL / JS", "Python backend, SQL pipelines, React/TypeScript frontends."),
        ("PYDATA", "numpy, Pandas/Polars, matplotlib/seaborn/Altair."),
        ("APPLIED ML", "End-to-end applied ML for football tasks."),
        ("DEEP LEARNING", "PyTorch, JAX, TensorFlow for event and pattern models."),
        ("COMPUTER USE", "Operates software, fills forms, generates reports."),
        ("MESSAGING", "Telegram, iMessage, Slack for analysts and coaches."),
    ]
    for title, desc in items:
        y = draw_bullet_line(c, ">", f"{title}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6
    draw_footer(c, 9)


def page_10_usecases(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "FOOTBALL USE CASES", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Built for the Men's First Team Analysis department.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    cases = [
        ("MATCH ANALYSIS", "Post-match insight cards within 60 minutes."),
        ("SCOUTING SHORTCUTS", "Automated tagging, clip search, opponent profiles."),
        ("PERFORMANCE BRIEFS", "Weekly readiness and load digests for coaches."),
        ("SET-PIECE DESIGN", "Corner/free-kick threat maps by zone."),
        ("STAFF SUPPORT", "Telegram/iMessage/Slack bot embedded with analysts."),
    ]
    for title, desc in cases:
        y = draw_bullet_line(c, ">", f"{title}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6
    draw_footer(c, 10)


def page_11_deployment(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "48-HOUR DEPLOYMENT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "From kickoff to live briefing. No recruiting delay.",
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
    draw_footer(c, 11)


def page_12_integration(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "INTEGRATION", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Adapts to training and matchday schedules.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    channels = [
        ("TELEGRAM / iMessage", "Threaded comms with analysts and coaches."),
        ("SLACK", "Embedded support in existing channels."),
        ("EMAIL", "Digest and alert distribution."),
        ("VOICE", "Fast outbriefs when text isn't enough."),
    ]
    for channel, desc in channels:
        y = draw_bullet_line(c, ">", f"{channel}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6
    draw_footer(c, 12)


def page_13_proof(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "PROOF", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Verified public signals only.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    proofs = [
        "Managed AI employee model is live. Confirmed client revenue.",
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
        "Replace the Head of Analysis or coaching staff.",
        "Guarantee match outcomes without data and staff buy-in.",
        "Operate without secure access to exports.",
    ]
    for line in cannot:
        y = draw_bullet_line(c, "-", line, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 4
    draw_footer(c, 13)


def page_14_pricing(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "PRICING", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Three models. Same outcome.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    models = [
        ("SINGLE TEAM", "£5,000 / month", "One team. One workflow."),
        ("CLUB / ORG", "£12,000 / month", "Multiple departments. Shared agent."),
        ("RESELL / WHITE-LABEL", "£8,000 / month + 20% rev share", "You sell it. We run it."),
    ]
    for name, price, desc in models:
        c.setFillColor(HexColor("#050505"))
        c.roundRect(MARGIN, y - 40 * mm, CONTENT_WIDTH, 34 * mm, 6, fill=1, stroke=0)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.2)
        c.roundRect(MARGIN, y - 40 * mm, CONTENT_WIDTH, 34 * mm, 6, fill=0, stroke=1)
        c.setFillColor(ACCENT)
        c.rect(MARGIN + 8, y - 14, 2.5, 24, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BOLD_FONT, HEADING_SIZE - 2)
        c.drawString(MARGIN + 18, y - 10 * mm, name)
        c.setFillColor(ACCENT)
        c.setFont(BOLD_FONT, TITLE_SIZE - 14)
        c.drawString(MARGIN + 18, y - 20 * mm, price)
        c.setFillColor(LIGHT)
        c.setFont(BODY_FONT, BODY_SIZE - 1)
        c.drawString(MARGIN + 18, y - 30 * mm, desc)
        y -= 48 * mm
    draw_footer(c, 14)


def page_15_security(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "SECURITY", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Enterprise posture from day one.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Dedicated environment per client. No shared tenants.",
        "Encryption at rest and in transit.",
        "Role-based access. Audit log for every agent action.",
        "PII and performance data never used outside your environment.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 15)


def page_16_support(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "SUPPORT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Real humans behind the agent.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Named success contact.",
        "Weekly delivery review with analysts.",
        "Same-day critical fix SLA.",
        "Knowledge capture from every interaction.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 16)


def page_17_scope(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "IN SCOPE", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "What we own together.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Data ingestion from existing club exports.",
        "Model deployment, tuning, and validation.",
        "Insight delivery into existing comms channels.",
        "Weekly improvements driven by real requests.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 17)


def page_18_out_of_scope(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "OUT OF SCOPE", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "What stays with your staff.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Final coaching decisions.",
        "Medical clearance and player welfare calls.",
        "Purchasing new data sources or hardware.",
        "IR and PR communications.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 18)


def page_19_terms(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "TERMS", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Simple, non-binding starter terms.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Minimum term: 3 months.",
        "Exit: 30-day notice after minimum term.",
        "IP: client owns data and outputs; OWL owns the system.",
        "Price lock: guaranteed for the first 12 months.",
        "Application deadline response within 48 hours.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 19)


def page_20_close(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "NEXT STEP", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Application closes Thursday 6th August 2026.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 12 * mm
    y = draw_big_text(c, "We reserve the right to close early if volumes are high.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 12 * mm
    y = draw_big_text(c, "Get your application in sooner rather than later.",
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
    draw_footer(c, 20)


def build():
    c = canvas.Canvas(OUT_PATH, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    pages = [
        page_1_cover,
        page_2_problem,
        page_3_roi,
        page_4_design_build,
        page_5_streamline,
        page_6_collaborate,
        page_7_applied_ai,
        page_8_research_impact,
        page_9_stack,
        page_10_usecases,
        page_11_deployment,
        page_12_integration,
        page_13_proof,
        page_14_pricing,
        page_15_security,
        page_16_support,
        page_17_scope,
        page_18_out_of_scope,
        page_19_terms,
        page_20_close,
    ]
    for fn in pages:
        fn(c)
        c.showPage()
    c.save()
    print("Generated:", OUT_PATH)


if __name__ == "__main__":
    build()
