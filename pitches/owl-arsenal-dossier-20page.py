#!/usr/bin/env python3
"""
Generate a 20-page OWL Arsenal dossier/brochure PDF.

- 3:4 ratio: 180mm x 240mm
- Black #0a0a0a background, orange #ff5c1f accents
- Carousel readability: one idea per page, large text
- Aligned to Arsenal Research Engineer job description
- Production AI framing, not chatbot
- No Hermes/Dewey in client copy
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

MARGIN = 20 * mm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

BG = HexColor("#0a0a0a")
ACCENT = HexColor("#ff5c1f")
WHITE = HexColor("#ffffff")
LIGHT = HexColor("#cccccc")
GRAY = HexColor("#aaaaaa")
DARK_GRAY = HexColor("#2a2a2a")
CARD_BG = HexColor("#141418")

TITLE_SIZE = 36
HEADING_SIZE = 22
BODY_SIZE = 15
CAPTION_SIZE = 11
HEADER_SIZE = 11
SMALL_SIZE = 10

OUT_PATH = "/root/ai-employee/pitches/owl-arsenal-dossier-20page.pdf"

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
    c.drawString(MARGIN, PAGE_HEIGHT - 12 * mm, "OWL  |  ARSENAL FC  |  CONFIDENTIAL")
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
    c.setFillColor(ACCENT)
    c.setFont(BOLD_FONT, TITLE_SIZE)
    c.drawString(MARGIN, y, text)
    c.setStrokeColor(DARK_GRAY)
    c.setLineWidth(1.2)
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


def draw_card(c, x, y, w, h, title, body):
    c.setFillColor(CARD_BG)
    c.roundRect(x, y - h + 6, w, h, 6, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#252528"))
    c.setLineWidth(0.8)
    c.roundRect(x, y - h + 6, w, h, 6, fill=0, stroke=1)
    c.setFillColor(ACCENT)
    c.rect(x + 8, y - 12, 2.5, h - 18, fill=1, stroke=0)
    ty = y - 20
    c.setFillColor(WHITE)
    c.setFont(BOLD_FONT, HEADING_SIZE - 2)
    c.drawString(x + 18, ty, title)
    ty -= 20
    c.setFillColor(LIGHT)
    c.setFont(BODY_FONT, BODY_SIZE - 1)
    c.drawString(x + 18, ty, body)
    return y - h


# ---------------------------------------------------------------------------
# Pages mapped to Arsenal job description
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
    c.drawString(MARGIN, y, "FOR ARSENAL FC")
    y -= 20 * mm
    c.setFillColor(LIGHT)
    c.setFont(BOLD_FONT, 16)
    c.drawString(MARGIN, y, "MANAGED AI RESEARCH ENGINEER")
    y -= 26 * mm
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, y, "Embedded with your First Team analysis department.")
    y -= 10 * mm
    c.drawString(MARGIN, y, "Builds, deploys, and supports — 48 hours.")
    y -= 28 * mm
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, CAPTION_SIZE)
    c.drawString(MARGIN, y, "AUGMENTATION, NOT REPLACEMENT.")
    draw_footer(c, 1)


def page_2_research_to_production(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "RESEARCH → PRODUCTION", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Not just models. Software coaches actually use.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Turn research into production applications.",
        "Deploy ML into matchday workflows.",
        "Bridge analysts and engineering.",
        "Validated against real fixtures.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 2)


def page_3_fullstack(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "FULL-STACK APPLICATIONS", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Design, develop, maintain data-driven applications for club stakeholders.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Python backend with SQL pipelines.",
        "React/TypeScript frontends for analysts and coaches.",
        "Scalable, reliable, efficient systems.",
        "Evolves with club data and workflows.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 3)


def page_4_automation(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "AUTOMATED ANALYSIS", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Streamline critical processes using engineering and applied ML.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Event tagging and clip generation.",
        "Scouting shortcuts and opponent profiles.",
        "Repetitive analyst labour removed.",
        "Quality control built into every pipeline.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 4)


def page_5_collaboration(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "ANALYST COLLABORATION", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Deeply understand analyst processes. Plan and implement solutions.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Translates coaching needs into engineering tasks.",
        "Proactively refines existing workflows.",
        "Bridges data and decisions.",
        "Adapts to training and matchday intensity.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 5)


def page_6_ai_specialist(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "APPLIED AI SPECIALIST", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "AI techniques applied to football analysis. Not LLMs everywhere.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "xG/xA, passing networks, PPDA, transition metrics.",
        "Set-piece optimisation and opposition profiling.",
        "Computer vision and sequence models where appropriate.",
        "R&D translated into production tooling.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 6)


def page_7_impact(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "MAXIMISE RESEARCH IMPACT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Grounded in coaching needs. Built for real constraints.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    bullets = [
        "Prioritises work that changes decisions.",
        "Validates models against known fixtures.",
        "Analysts can action outputs immediately.",
        "Iterates from match and training feedback.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, ">", b, MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 8
    draw_footer(c, 7)


def page_8_stack(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "CAPABILITIES", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Confirmed components. No black-box claims.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    items = [
        ("PYTHON / SQL / JS", "Full-stack apps with React/TypeScript frontends."),
        ("PYDATA", "numpy, pandas/polars, matplotlib/Altair for analysis and visuals."),
        ("COMPUTER USE", "Operates software, fills forms, generates reports."),
        ("MESSAGING", "Telegram, iMessage, Slack for analysts and coaches."),
        ("MODELS", "Advanced reasoning layer tuned for sports data."),
    ]
    for title, desc in items:
        card_h = 36 * mm
        y = draw_card(c, MARGIN, y, CONTENT_WIDTH, card_h, title, desc)
        y -= 6
    draw_footer(c, 8)


def page_9_football_systems(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "FOOTBALL INTELLIGENCE SYSTEM", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "How OWL turns raw inputs into coaching decisions.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    pipeline = [
        ("INPUT", "Match footage, event data, tracking, scouting exports."),
        ("PROCESS", "Feature extraction, model inference, memory retrieval."),
        ("REASONING", "Pattern matching, historical comparison, constraint checking."),
        ("OUTPUT", "Visualisations, reports, briefing cards, explanations."),
        ("DELIVERY", "Coach dashboard, Telegram/iMessage/Slack, archive."),
    ]
    for title, desc in pipeline:
        y = draw_bullet_line(c, ">", f"{title}: {desc}", MARGIN, y, CONTENT_WIDTH, leading=24)
        y -= 6
    draw_footer(c, 9)


def page_10_usecases(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "USE CASES", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Built for elite football operations.",
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
    draw_footer(c, 10)


def page_11_deployment(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "48-HOUR DEPLOYMENT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "From discovery call to first briefing card. No recruiting delay.",
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
    y = draw_big_text(c, "No new logins. No new workflows.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    channels = [
        ("TELEGRAM / iMessage", "Threaded comms with analysts and coaches."),
        ("SLACK", "Embedded support in existing channels."),
        ("EMAIL", "Digest and alert distribution."),
        ("DASHBOARD", "Coach-facing web app for matchday."),
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
    for b in proofs:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 13)


def page_14_wont_do(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "WHAT OWL WILL NOT DO", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Honest boundaries.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm
    cannot = [
        "Replace head of analysis or coaching staff.",
        "Guarantee match outcomes without data and buy-in.",
        "Operate without secure access to exports.",
        "Make medical or IR decisions.",
        "Control player access or dressing-room integration.",
    ]
    for b in cannot:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
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
        "Role-based access. Audit log for every action.",
        "Performance data never leaves your environment.",
        "On-prem or VPC option available.",
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 15)


def page_16_support(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "SUPPORT", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Real humans behind the system.",
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


def page_18_terms(c):
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
    ]
    for b in bullets:
        y = draw_bullet_line(c, "-", b, MARGIN, y, CONTENT_WIDTH, leading=22)
        y -= 6
    draw_footer(c, 18)


def page_19_faq(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "FAQs", PAGE_HEIGHT - 50 * mm)
    y -= 10 * mm
    faqs = [
        ("Q: Can you integrate with our existing video platform?", "A: Yes — exports, timestamps, metadata."),
        ("Q: Is our data used to train shared models?", "A: No. Your data stays in your environment."),
        ("Q: What happens after 48 hours?", "A: Live operation plus weekly iterations."),
        ("Q: Is this a chatbot?", "A: No. Production AI systems embedded with your analysts."),
    ]
    for q, a in faqs:
        y = draw_bullet_line(c, "Q:", q, MARGIN, y, CONTENT_WIDTH, leading=22)
        y = draw_bullet_line(c, "A:", a, MARGIN + 6 * mm, y, CONTENT_WIDTH - 6 * mm, leading=22)
        y -= 10
    draw_footer(c, 19)


def page_20_close(c):
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
    c.roundRect(MARGIN, y - 44 * mm, CONTENT_WIDTH, 30 * mm, 6, fill=1, stroke=0)
    c.setFillColor(BG)
    c.setFont(BOLD_FONT, HEADING_SIZE - 2)
    c.drawString(MARGIN + 10 * mm, y - 14 * mm, "BOOK NOW")
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN + 10 * mm, y - 24 * mm, "beacons.ai/humanarchitect")
    y -= 52 * mm
    y = draw_big_text(c, "Response within 24 hours. No obligation.",
                      MARGIN, y, CONTENT_WIDTH, leading=24)
    draw_footer(c, 20)


def build():
    c = canvas.Canvas(OUT_PATH, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    pages = [
        page_1_cover,
        page_2_research_to_production,
        page_3_fullstack,
        page_4_automation,
        page_5_collaboration,
        page_6_ai_specialist,
        page_7_impact,
        page_8_stack,
        page_9_football_systems,
        page_10_usecases,
        page_11_deployment,
        page_12_integration,
        page_13_proof,
        page_14_wont_do,
        page_15_security,
        page_16_support,
        page_17_scope,
        page_18_terms,
        page_19_faq,
        page_20_close,
    ]
    for fn in pages:
        fn(c)
        c.showPage()
    c.save()
    print("Generated:", OUT_PATH)


if __name__ == "__main__":
    build()
