#!/usr/bin/env python3
"""
Generate a 10-page RED TEAM pitch deck PDF for OWL targeting sports teams.

VARIANT A - "SHARP MINIMAL":
- 3:4 ratio: 180mm x 240mm
- Black background #000000
- Single accent: electric blue #00b4ff
- Instagram carousel style: giant text, one idea per page, instant readability
- No clutter, no fake stats, no Hermes/Dewey
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

TITLE_SIZE = 38
HEADING_SIZE = 24
BODY_SIZE = 15
CAPTION_SIZE = 11
HEADER_SIZE = 11
SMALL_SIZE = 10

OUT_PATH = "/root/ai-employee/pitches/sports-owl-10page-RED.pdf"

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


def draw_footer(c, page_num, total=10):
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
    c.setFillColor(GRAY)
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


def page_3_roi(c):
    draw_background(c)
    draw_header(c)
    y = draw_big_title(c, "WHY OWL OVER ONE MORE ANALYST?", PAGE_HEIGHT - 50 * mm)
    y = draw_big_text(c, "Same output. Lower cost. Zero recruiting delay.",
                      MARGIN, y, CONTENT_WIDTH, leading=26)
    y -= 14 * mm

    rows = [
        ("", "ANALYST", "OWL"),
        ("COST", "£35-45K/year + benefits", "£5K/month flat"),
        ("DEPLOY TIME", "4-8 weeks hire + onboard", "48 hours"),
        ("SCHEDULE FLEX", "Monday-Friday, 9-5", "Always on"),
        ("CONTEXT LOSS", "High — holiday, sick, turnover", "None — persistent memory"),
        ("OUTPUT", "Human-limited batch reports", "Continuous automation + briefing cards"),
    ]

    col1 = CONTENT_WIDTH * 0.55
    col2 = CONTENT_WIDTH * 0.30
    col3 = CONTENT_WIDTH * 0.15
    row_h = 26 * mm
    x = MARGIN
    y0 = y

    for i, row in enumerate rows):
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

