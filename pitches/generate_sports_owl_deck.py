#!/usr/bin/env python3
"""
Generate a 10-page dark pitch deck PDF for selling a managed AI employee
service called "OWL" to sports teams.

Requirements: reportlab
Output: /root/ai-employee/pitches/sports-owl-10page.pdf
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 20 * mm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

BG = HexColor("#0a0a0a")
ACCENT = HexColor("#ff5c1f")
WHITE = HexColor("#ffffff")
LIGHT = HexColor("#cccccc")
GRAY = HexColor("#888888")
DARK_GRAY = HexColor("#333333")
CARD_BG = HexColor("#141414")

TITLE_SIZE = 34
HEADING_SIZE = 22
BODY_SIZE = 14
CAPTION_SIZE = 10
HEADER_SIZE = 9
SMALL_SIZE = 8

OUT_DIR = "/root/ai-employee/pitches"
OUT_PATH = os.path.join(OUT_DIR, "sports-owl-10page.pdf")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------
try:
    pdfmetrics.registerFont(TTFont("Helvetica", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"))
    BODY_FONT = "Helvetica"
except Exception:
    BODY_FONT = "Helvetica"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))


def draw_header(c):
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, HEADER_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 15 * mm, "OWL | Sports Teams | Confidential")
    c.setStrokeColor(DARK_GRAY)
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_HEIGHT - 17 * mm, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 17 * mm)


def draw_footer(c, page_num, total=10):
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, SMALL_SIZE)
    c.drawRightString(PAGE_WIDTH - MARGIN, 12 * mm, f"{page_num} / {total}")
    c.setStrokeColor(DARK_GRAY)
    c.setLineWidth(0.5)
    c.line(MARGIN, 14 * mm, PAGE_WIDTH - MARGIN, 14 * mm)


def draw_background(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)


def draw_wrapped_text(c, text, x, y, max_width, leading):
    """Simple word-wrap text renderer."""
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


def draw_bullet_block(c, bullets, x, y, max_width, leading=20, bullet="•"):
    """Draw bullets with auto wrap. Returns new y after last line."""
    leading = 20
    for b in bullets:
        # bullet
        c.setFillColor(ACCENT)
        c.drawString(x, y, bullet)
        # text
        words = b.split()
        line = ""
        text_x = x + 8
        c.setFillColor(WHITE)
        max_y = y
        for word in words:
            test = (line + " " + word).strip()
            if c.stringWidth(test, BODY_FONT, BODY_SIZE) <= max_width - 8:
                line = test
            else:
                if line:
                    c.drawString(text_x, max_y, line)
                    max_y -= leading
                line = word
        if line:
            c.drawString(text_x, max_y, line)
            max_y -= leading
        y = max_y - 6
    return y


def draw_card(c, x, y, w, h, title_lines):
    c.setFillColor(CARD_BG)
    c.roundRect(x, y - h + 6, w, h, 6, fill=1, stroke=0)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.roundRect(x, y - h + 6, w, h, 6, fill=0, stroke=1)
    # small accent bar top
    c.setFillColor(ACCENT)
    c.rect(x + 2, y - 14, w - 4, 3, fill=1, stroke=0)
    y -= 22
    c.setFont(BODY_FONT, BODY_SIZE)
    c.setFillColor(WHITE)
    for tl in title_lines:
        c.drawString(x + 10, y, tl)
        y -= 18
    return y


# ---------------------------------------------------------------------------
# Page renderers
# ---------------------------------------------------------------------------

def page_1_cover(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(WHITE)
    c.setFont(BODY_FONT, TITLE_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 120 * mm, "OWL for Sports Teams")
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 150 * mm, "Managed AI Engineer")
    c.setFillColor(LIGHT)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 180 * mm, "Your forward-deployed engineer.")
    c.drawString(MARGIN, PAGE_HEIGHT - 200 * mm, "Builds, automates, and supports — 48 hours.")
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, CAPTION_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 240 * mm, "Augmentation, not replacement.")
    draw_footer(c, 1)


def page_2_problem(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "The Four Pain Points")
    c.setFillColor(WHITE)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 80 * mm,
                 "Every sports team bleeds money on the same four bottlenecks:")

    cards = [
        ["1. Talent Gaps", "Analysis staff shortages create blind spots between matchdays."],
        ["2. Manual Grind", "Hours lost to repetitive data pulls, wrangling, and reporting."],
        ["3. Slow Insights", "Tactical questions unanswered long after the press conference."],
        ["4. Fragmented Data", "Scouting, medical, and performance data stuck in silos."],
    ]

    y = PAGE_HEIGHT - 110 * mm
    for i in range(0, 4, 2):
        x1 = MARGIN
        x2 = MARGIN + (CONTENT_WIDTH / 2) + 10 * mm
        w1 = (CONTENT_WIDTH / 2) - 5 * mm
        w2 = (CONTENT_WIDTH / 2) - 5 * mm
        y1 = draw_card(c, x1, y, w1, 52 * mm, cards[i])
        if i + 1 < 4:
            draw_card(c, x2, y, w2, 52 * mm, cards[i + 1])
        y -= 60 * mm

    draw_footer(c, 2)


def page_3_what_owl_does(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "What OWL Actually Does")

    bullets = [
        "Automates ETL and repetitive quantification so analysts focus on strategy.",
        "Builds full-stack analytics applications on top of your existing infrastructure.",
        "Develops applied ML models grounded in coaching questions — not academic papers.",
        "Ships dashboards and visualizations faster than any human team can.",
        "Operates as a permanent embedded analyst. No bench. No holidays. No notice period.",
    ]
    y = PAGE_HEIGHT - 90 * mm
    y = draw_bullet_block(c, bullets, MARGIN, y, CONTENT_WIDTH, 20)

    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, BODY_SIZE)
    y -= 10 * mm
    c.drawString(MARGIN, y, "OWL does not replace your analysts. It gives them superpowers.")
    draw_footer(c, 3)


def page_4_stack(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "The Stack")

    items = [
        ("Python", "PyData: NumPy, Pandas, scikit-learn. xG pipelines, tracking-data ETL."),
        ("SQL", "Match event stores, player-wearable joins, scouting-dossier data."),
        ("JavaScript / TypeScript", "Web dashboards, coaching portals, live-match apps."),
        ("Data Visualization", "Expected-threat maps, transition heatmaps, passing-lane diagrams."),
        ("Full-Stack Development", "Production apps built and shipped inside your environment."),
        ("Computer-Use + Messaging", "Automates browser actions. Connects to Telegram, iMessage, and Slack."),
    ]

    y = PAGE_HEIGHT - 90 * mm
    w = CONTENT_WIDTH
    for tech, desc in items:
        h = 32 * mm if len(desc) > 60 else 26 * mm
        c.setFillColor(CARD_BG)
        c.roundRect(MARGIN, y - h + 4, w, h, 4, fill=1, stroke=0)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1)
        c.roundRect(MARGIN, y - h + 4, w, h, 4, fill=0, stroke=1)
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(MARGIN + 10, y - 10, tech)
        c.setFillColor(LIGHT)
        c.setFont(BODY_FONT, BODY_SIZE - 2)
        c.drawString(MARGIN + 10, y - 26, desc)
        y -= h + 8 * mm

    draw_footer(c, 4)


def page_5_use_cases(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "Five Real Sports Applications")

    use_cases = [
        "Pre-match opposition scouting and probability maps",
        "In-game transition and passing-lane heatmaps",
        "Player load monitoring and injury-risk trend detection",
        "Transfer / scout similarity and assessment engines",
        "Automated coaching-portal dashboards and daily reporting",
    ]

    cols = 3
    box_w = (CONTENT_WIDTH / cols) - 6 * mm
    box_h = 44 * mm
    y = PAGE_HEIGHT - 90 * mm
    x_positions = [MARGIN, MARGIN + box_w + 6 * mm, MARGIN + 2 * (box_w + 6 * mm)]

    row = 0
    for i, uc in enumerate(use_cases):
        col = i % cols
        if i > 0 and col == 0:
            row += 1
            y -= (box_h + 12 * mm)
        x = x_positions[col]
        c.setFillColor(CARD_BG)
        c.roundRect(x, y - box_h, box_w, box_h, 6, fill=1, stroke=0)
        c.setStrokeColor(DARK_GRAY)
        c.setLineWidth(1)
        c.roundRect(x, y - box_h, box_w, box_h, 6, fill=0, stroke=1)
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, BODY_SIZE)
        num = str(i + 1) + "."
        c.drawString(x + 10, y - 18, num)
        c.setFillColor(WHITE)
        words = uc.split()
        line = ""
        text_y = y - 36
        for word in words:
            test = (line + " " + word).strip()
            if c.stringWidth(test, BODY_FONT, BODY_SIZE - 2) <= box_w - 20:
                line = test
            else:
                c.drawString(x + 10, text_y, line)
                text_y -= 16
                line = word
        if line:
            c.drawString(x + 10, text_y, line)

    draw_footer(c, 5)


def page_6_deployment(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "48-Hour Deployment")

    timeline = [
        ("Hour 0-4", "Environment access, data contracts, API ingestion"),
        ("Hour 4-24", "First analytics app built, live, and tested"),
        ("Hour 24-36", "ML prototype deployed on a verified use case"),
        ("Hour 36-48", "Dashboard live. Team briefed. Reports running."),
    ]

    y = PAGE_HEIGHT - 90 * mm
    step_w = (CONTENT_WIDTH - 30 * mm) / 4
    for i, (t, d) in enumerate(timeline):
        x = MARGIN + i * (step_w + 10 * mm)
        # box
        c.setFillColor(CARD_BG)
        c.roundRect(x, y - 60 * mm, step_w, 60 * mm, 6, fill=1, stroke=0)
        c.setStrokeColor(DARK_GRAY)
        c.setLineWidth(1)
        c.roundRect(x, y - 60 * mm, step_w, 60 * mm, 6, fill=0, stroke=1)
        # time
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, BODY_SIZE - 2)
        c.drawString(x + 10, y - 18, t)
        # desc
        c.setFillColor(WHITE)
        words = d.split()
        line = ""
        text_y = y - 38
        for word in words:
            test = (line + " " + word).strip()
            if c.stringWidth(test, BODY_FONT, BODY_SIZE - 3) <= step_w - 20:
                line = test
            else:
                c.drawString(x + 10, text_y, line)
                text_y -= 14
                line = word
        if line:
            c.drawString(x + 10, text_y, line)
        # arrow
        if i < 3:
            ax = x + step_w + 2
            ay = y - 30 * mm
            c.setStrokeColor(ACCENT)
            c.setLineWidth(2)
            c.line(ax, ay, ax + 6 * mm, ay)
            c.line(ax + 6 * mm, ay, ax + 4 * mm, ay + 3)
            c.line(ax + 6 * mm, ay, ax + 4 * mm, ay - 3)

    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, y - 80 * mm, "Ship by Friday. Train Monday. Win by matchday.")
    draw_footer(c, 6)


def page_7_integration(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "How OWL Connects to Staff")

    channels = [
        ("Telegram", "Real-time alerts and on-demand queries."),
        ("iMessage", "Daily automated reports delivered to phones."),
        ("Slack", "Team channels, ops channels, coaching-portal updates."),
    ]

    y = PAGE_HEIGHT - 90 * mm
    w = CONTENT_WIDTH
    for ch, desc in channels:
        h = 40 * mm
        c.setFillColor(CARD_BG)
        c.roundRect(MARGIN, y - h, w, h, 8, fill=1, stroke=0)
        c.setStrokeColor(DARK_GRAY)
        c.setLineWidth(1)
        c.roundRect(MARGIN, y - h, w, h, 8, fill=0, stroke=1)
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(MARGIN + 12, y - 16, ch)
        c.setFillColor(WHITE)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(MARGIN + 12, y - 34, desc)
        y -= h + 10 * mm

    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, y - 10, "Zero training. Staff already know the apps.")
    draw_footer(c, 7)


def page_8_proof(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "Proof")

    proofs = [
        ("Cline", "8M+ installs", "Open-source coding agent. Validates demand."),
        ("Dewey Model", "$5K/mo", "Managed AI employee. Agent builds agent."),
        ("agentmarketcap.ai", "60-80% margins", "$200-500/mo delivery cost. Near-zero overhead."),
        ("Solo-founder trend", "36.3%", "Market trusts one-person agent businesses."),
    ]

    y = PAGE_HEIGHT - 90 * mm
    w = CONTENT_WIDTH
    for name, stat, desc in proofs:
        h = 38 * mm
        c.setFillColor(CARD_BG)
        c.roundRect(MARGIN, y - h, w, h, 6, fill=1, stroke=0)
        c.setStrokeColor(DARK_GRAY)
        c.setLineWidth(1)
        c.roundRect(MARGIN, y - h, w, h, 6, fill=0, stroke=1)
        # left accent bar
        c.setFillColor(ACCENT)
        c.rect(MARGIN + 4, y - h + 4, 4, h - 8, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(MARGIN + 16, y - 16, name)
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(MARGIN + 16, y - 30, stat)
        c.setFillColor(LIGHT)
        c.setFont(BODY_FONT, BODY_SIZE - 2)
        c.drawString(MARGIN + 16, y - 46, desc)
        y -= h + 8 * mm

    draw_footer(c, 8)


def page_9_pricing(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 55 * mm, "Pricing")

    col_w = (CONTENT_WIDTH - 30 * mm) / 3
    models = [
        {
            "name": "Single Team",
            "price": "£5,000/month",
            "features": [
                "One managed OWL instance",
                "Embedded with one team",
                "Standard integrations",
                "Weekly optimization",
            ],
            "highlight": False,
        },
        {
            "name": "Club / Organization",
            "price": "£12,000/month",
            "features": [
                "Multi-department access",
                "Priority deployment queue",
                "Custom skills stack",
                "Dedicated ops review",
            ],
            "highlight": True,
        },
        {
            "name": "Resell / White-Label",
            "price": "£8,000/month",
            "features": [
                "Your brand, OWL underneath",
                "20% revenue share",
                "Managed rollout support",
                "Optional add-ons included",
            ],
            "highlight": False,
        },
    ]

    y = PAGE_HEIGHT - 90 * mm
    h = 130 * mm
    for i, m in enumerate(models):
        x = MARGIN + i * (col_w + 15 * mm)
        # card fill
        bg = HexColor("#1a0f0a") if m["highlight"] else CARD_BG
        c.setFillColor(bg)
        c.roundRect(x, y - h, col_w, h, 8, fill=1, stroke=0)
        c.setStrokeColor(ACCENT if m["highlight"] else DARK_GRAY)
        c.setLineWidth(2 if m["highlight"] else 1)
        c.roundRect(x, y - h, col_w, h, 8, fill=0, stroke=1)
        # name
        c.setFillColor(WHITE)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(x + 12, y - 22, m["name"])
        # price
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, HEADING_SIZE - 2)
        c.drawString(x + 12, y - 46, m["price"])
        # divider
        c.setStrokeColor(DARK_GRAY)
        c.setLineWidth(0.5)
        c.line(x + 12, y - 58, x + col_w - 12, y - 58)
        # features
        c.setFillColor(LIGHT)
        c.setFont(BODY_FONT, BODY_SIZE - 2)
        fy = y - 78
        for feat in m["features"]:
            c.drawString(x + 12, fy, "• " + feat)
            fy -= 20

    # comparison table row
    table_y = y - h - 20 * mm
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN, table_y, "All plans include: 48-hour deployment | Embedded access | Telegram/Slack/iMessage support")
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, CAPTION_SIZE)
    c.drawString(MARGIN, table_y - 14, "Price in GBP. No setup fees. Upgrade or downgrade quarterly.")

    draw_footer(c, 9)


def page_10_close(c):
    draw_background(c)
    draw_header(c)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, TITLE_SIZE - 4)
    c.drawString(MARGIN, PAGE_HEIGHT - 90 * mm, "Stop Hiring. Start Embedding.")

    c.setFillColor(WHITE)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN, PAGE_HEIGHT - 120 * mm, "OWL is live.")
    c.drawString(MARGIN, PAGE_HEIGHT - 148 * mm, "Your team can embed a managed AI")
    c.drawString(MARGIN, PAGE_HEIGHT - 174 * mm, "engineer this week.")

    urgency = [
        "Only 3 Club/Organization slots left for Q3.",
        "Next Single Team cohort starts Monday.",
        "Lock your price before Q4 launch.",
    ]
    y = PAGE_HEIGHT - 210 * mm
    for u in urgency:
        c.setFillColor(ACCENT)
        c.setFont(BODY_FONT, BODY_SIZE)
        c.drawString(MARGIN + 10 * mm, y, "•")
        c.setFillColor(WHITE)
        c.drawString(MARGIN + 18 * mm, y, u)
        y -= 22

    # CTA box
    c.setFillColor(CARD_BG)
    c.roundRect(MARGIN, y - 60 * mm, CONTENT_WIDTH, 60 * mm, 8, fill=1, stroke=0)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2)
    c.roundRect(MARGIN, y - 60 * mm, CONTENT_WIDTH, 60 * mm, 8, fill=0, stroke=1)
    c.setFillColor(ACCENT)
    c.setFont(BODY_FONT, HEADING_SIZE)
    c.drawString(MARGIN + 20, y - 25, "Book your embed")
    c.setFillColor(WHITE)
    c.setFont(BODY_FONT, BODY_SIZE)
    c.drawString(MARGIN + 20, y - 46, "beacons.ai/humanarchitect")

    # footer trust line
    c.setFillColor(GRAY)
    c.setFont(BODY_FONT, CAPTION_SIZE)
    c.drawString(MARGIN, y - 80 * mm, "Managed AI employee. Augmentation-only. Your data stays in your environment.")

    draw_footer(c, 10)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    c = canvas.Canvas(OUT_PATH, pagesize=A4)
    c.setTitle("OWL for Sports Teams — Managed AI Engineer")
    c.setAuthor("OWL")
    c.setSubject("Pitch Deck")

    pages = [
        page_1_cover,
        page_2_problem,
        page_3_what_owl_does,
        page_4_stack,
        page_5_use_cases,
        page_6_deployment,
        page_7_integration,
        page_8_proof,
        page_9_pricing,
        page_10_close,
    ]

    for i, page_fn in enumerate(pages, 1):
        page_fn(c)
        c.showPage()

    c.save()
    print(f"Generated: {OUT_PATH}")


if __name__ == "__main__":
    main()
