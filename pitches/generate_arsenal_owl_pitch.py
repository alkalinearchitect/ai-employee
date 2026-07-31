#!/usr/bin/env python3
"""Generate a 10-page dark-design pitch PDF for Arsenal FC's OWL Managed AI Employee."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

# ---------------------------------------------------------------------------
# Colours & constants
# ---------------------------------------------------------------------------
BG_DARK = colors.HexColor("#0a0a0a")
BG_CARD = colors.HexColor("#141418")
ORANGE = colors.HexColor("#ff5c1f")
WHITE = colors.white
LIGHT_GREY = colors.HexColor("#e0e0e0")
MID_GREY = colors.HexColor("#888888")
GRID_COLOR = colors.HexColor("#2a2a2a")

HEADER_TEXT = "OWL | Arsenal FC | Confidential"
OUTPUT_PATH = "/root/ai-employee/pitches/arsenal-owl-10page.pdf"


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
styles = getSampleStyleSheet()

orange_style = ParagraphStyle(
    "Orange",
    parent=styles["Normal"],
    textColor=ORANGE,
    fontName="Helvetica",
    leading=14,
    spaceBefore=4,
    spaceAfter=4,
)

white_title = ParagraphStyle(
    "WhiteTitle",
    parent=styles["Normal"],
    textColor=WHITE,
    fontName="Helvetica-Bold",
    fontSize=34,
    leading=38,
    spaceBefore=6,
    spaceAfter=6,
    alignment=TA_LEFT,
)

white_heading = ParagraphStyle(
    "WhiteHeading",
    parent=styles["Normal"],
    textColor=ORANGE,
    fontName="Helvetica-Bold",
    fontSize=22,
    leading=26,
    spaceBefore=12,
    spaceAfter=8,
    alignment=TA_LEFT,
)

white_subheading = ParagraphStyle(
    "WhiteSubheading",
    parent=styles["Normal"],
    textColor=WHITE,
    fontName="Helvetica-Bold",
    fontSize=17,
    leading=21,
    spaceBefore=10,
    spaceAfter=6,
    alignment=TA_LEFT,
)

white_body = ParagraphStyle(
    "WhiteBody",
    parent=styles["Normal"],
    textColor=LIGHT_GREY,
    fontName="Helvetica",
    fontSize=14,
    leading=18,
    spaceBefore=4,
    spaceAfter=4,
    alignment=TA_LEFT,
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=white_body,
    bulletIndent=12,
    leftIndent=20,
    firstLineIndent=0,
    spaceAfter=3,
)

page_num_style = ParagraphStyle(
    "PageNum",
    parent=styles["Normal"],
    textColor=MID_GREY,
    fontName="Helvetica",
    fontSize=9,
    alignment=TA_CENTER,
)

small_grey = ParagraphStyle(
    "SmallGrey",
    parent=styles["Normal"],
    textColor=MID_GREY,
    fontName="Helvetica",
    fontSize=8,
    leading=12,
    alignment=TA_LEFT,
)


# ---------------------------------------------------------------------------
# Page template with header bar + page number
# ---------------------------------------------------------------------------
def header_footer(canvas, doc):
    canvas.saveState()
    page_width, page_height = A4

    # Full-page dark background
    canvas.setFillColor(BG_DARK)
    canvas.rect(0, 0, page_width, page_height, fill=1, stroke=0)

    # Header bar
    header_height = 24
    canvas.setFillColor(BG_CARD)
    canvas.rect(0, page_height - header_height, page_width, header_height, fill=1, stroke=0)
    canvas.setFillColor(ORANGE)
    canvas.rect(0, page_height - header_height, 4, header_height, fill=1, stroke=0)
    canvas.setFillColor(MID_GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(14, page_height - header_height + 8, HEADER_TEXT)

    # Footer page number
    canvas.setFillColor(MID_GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(page_width / 2, 18, f"{doc.page}")

    canvas.restoreState()


def build_doc_template():
    frame = Frame(
        24, 36,
        A4[0] - 48,
        A4[1] - 48 - 36 - 24,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
        id="normal",
    )
    template = PageTemplate(id="main", frames=frame, onPage=header_footer)
    return BaseDocTemplate(OUTPUT_PATH, pagesize=A4, pageTemplates=[template])


# ---------------------------------------------------------------------------
# Helper builders
# ---------------------------------------------------------------------------
def section_rule():
    return HRFlowable(width="100%", thickness=1, color=ORANGE, spaceBefore=4, spaceAfter=8)


def card_table(*rows, col_widths=None):
    """Simple dark card with a grid."""
    if col_widths is None:
        col_widths = [None] * len(rows[0])
    t = Table(rows, colWidths=col_widths, repeatRows=0)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_CARD),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def graphic_bar_table():
    """Page 3 before/after visual."""
    before = [
        [Paragraph("<b>BEFORE OWL</b>", orange_style)],
        [Paragraph("• Analysts spend 6+ hours/week gathering data", white_body)],
        [Paragraph("• Insights arrive 24-48 hrs after matches", white_body)],
        [Paragraph("• Tactical trends seen in isolation", white_body)],
        [Paragraph("• Set-piece prep based on outdated trends", white_body)],
        [Paragraph("• Manual passing-network snapshots", white_body)],
    ]
    after = [
        [Paragraph("<b>AFTER OWL</b>", orange_style)],
        [Paragraph("• Real-time data ingestion &amp; cleaning", white_body)],
        [Paragraph("• Insights delivered within 60 minutes FT", white_body)],
        [Paragraph("• Cross-match xG, PPDA, PPDA def/att trends", white_body)],
        [Paragraph("• Set-piece threat modelled per opponent", white_body)],
        [Paragraph("• Live network evolution + opponent mirror", white_body)],
    ]

    before_t = Table(before, colWidths=[270], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_CARD),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    after_t = Table(after, colWidths=[270], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_CARD),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    arrow = Paragraph(
        "<span color='#ff5c1f'><b>➜</b></span>",
        ParagraphStyle("arrow", parent=white_body, alignment=TA_CENTER, fontSize=18),
    )

    t = Table(
        [[before_t, arrow, after_t]],
        colWidths=[270, 30, 270],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BG_DARK),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]),
    )
    return t


def architecture_diagram():
    """Page 6 three-layer architecture visual."""
    data_layer = [
        [Paragraph("<b>DATA LAYER</b>", orange_style)],
        [Paragraph("Opta / StatsBomb / Wyscout", white_body)],
        [Paragraph("Tracking (Second Spectrum)", white_body)],
        [Paragraph("Video (HUDL / own footage)", white_body)],
        [Paragraph("Internal session logs", white_body)],
    ]
    intel_layer = [
        [Paragraph("<b>INTELLIGENCE LAYER</b>", orange_style)],
        [Paragraph("xG / xA / GCA models", white_body)],
        [Paragraph("Passing network graphs", white_body)],
        [Paragraph("Set-piece threat maps", white_body)],
        [Paragraph("Opponent scouting reports", white_body)],
    ]
    coach_layer = [
        [Paragraph("<b>COACHING LAYER</b>", orange_style)],
        [Paragraph("Briefing cards for Mikel &amp; staff", white_body)],
        [Paragraph("Pre-match dossiers", white_body)],
        [Paragraph("Half-time visual adds", white_body)],
        [Paragraph("Telegram / iMessage delivery", white_body)],
    ]

    def make_cell(rows):
        return Table(rows, colWidths=[200], style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BG_CARD),
            ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))

    arr_down = Paragraph(
        "<span color='#ff5c1f'><b>▼</b></span>",
        ParagraphStyle("arr", parent=white_body, alignment=TA_CENTER, fontSize=14, leading=18),
    )

    main = Table(
        [
            [make_cell(data_layer), arr_down, make_cell(intel_layer), arr_down, make_cell(coach_layer)],
        ],
        colWidths=[160, 24, 160, 24, 160],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BG_DARK),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]),
    )

    wrap = Table(
        [
            [Paragraph("<b>OWL 3-LAYER PIPELINE</b>", orange_style)],
            [main],
        ],
        colWidths=[A4[0] - 96],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BG_CARD),
            ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]),
    )
    return wrap


# ---------------------------------------------------------------------------
# Pages content
# ---------------------------------------------------------------------------
def page_1_cover():
    return [
        Spacer(1, 140),
        Paragraph("ARSENAL FC", white_title),
        Spacer(1, 12),
        Paragraph("OWL MANAGED AI RESEARCH ENGINEER", white_subheading),
        Spacer(1, 12),
        Paragraph("Embedded with First Team Analysis", white_body),
        Spacer(1, 140),
        Paragraph("July 2026", small_grey),
    ]


def page_2_exec_summary():
    return [
        Paragraph("EXECUTIVE SUMMARY", white_heading),
        section_rule(),
        Paragraph(
            "OWL is a managed AI employee built for elite football analysis. "
            "It ingests Opta, tracking, and video data, runs advanced models "
            "(xG, xA, passing networks, set-piece threat), and delivers ready-to-use "
            "insights directly to analysts and coaches.",
            white_body,
        ),
        Spacer(1, 10),
        Paragraph(
            "<b>Result:</b> 75% faster insight delivery, deeper tactical context, "
            "and consistent pre-match / half-time intelligence.",
            white_body,
        ),
        Spacer(1, 10),
        Paragraph("KEY BENEFITS", white_subheading),
        section_rule(),
        Paragraph("• 60-minute insight turnaround post-match", bullet_style),
        Paragraph("• Automated xG and creative-threat dashboards", bullet_style),
        Paragraph("• Direct messaging to Telegram / iMessage / Slack", bullet_style),
        Paragraph("• Embedded with your workflow — no extra logins", bullet_style),
        Paragraph("• 48-hour deployment SLA", bullet_style),
        Spacer(1, 6),
    ]


def page_3_problem():
    return [
        Paragraph("THE PROBLEM", white_heading),
        section_rule(),
        Paragraph(
            "Premier League analysis moves fast. Today, clubs face four bottlenecks "
            "that slow decision-making.",
            white_body,
        ),
        Spacer(1, 14),
        graphic_bar_table(),
        Spacer(1, 18),
        card_table(
            [Paragraph("<b>1. TIME</b>", orange_style), Paragraph("Analysts spend 6+ hrs/week gathering data.", white_body)],
            [Paragraph("<b>2. LATENCY</b>", orange_style), Paragraph("Delayed insights = missed adjustments.", white_body)],
            [Paragraph("<b>3. CONTEXT</b>", orange_style), Paragraph("Metrics in silos, not connected.", white_body)],
            [Paragraph("<b>4. DELIVERY</b>", orange_style), Paragraph("Reports sit in email, unactioned.", white_body)],
            col_widths=[130, 410],
        ),
    ]


def page_4_delivers():
    items = [
        ("1. DATA INGESTION", "Pulls Opta, tracking, video metadata. Cleans, normalises, timestamps."),
        ("2. MODEL INFERENCE", "xG/xA, PPDA, GCA, passing networks, set-piece maps per opponent."),
        ("3. INSIGHT SYNTHESIS", "Turns raw outputs into scannable briefing cards."),
        ("4. DELIVERY", "Pushes to Telegram, iMessage, Slack, email with timestamped archive."),
        ("5. EVOLUTION", "Retrains on Arsenal-specific outcomes; accuracy improves weekly."),
    ]
    rows = []
    for title, desc in items:
        rows.append([
            Paragraph(f"<b>{title}</b>", orange_style),
            Paragraph(desc, white_body),
        ])
    t = card_table(*rows, col_widths=[180, 360])
    return [
        Paragraph("WHAT OWL DELIVERS", white_heading),
        section_rule(),
        Paragraph(
            "Five mapped duties — from intake to insight. Each locked to a first-team need.",
            white_body,
        ),
        Spacer(1, 12),
        t,
        Spacer(1, 12),
        Paragraph(
            "<b>Outcome:</b> Analysts coach. OWL prepares.",
            white_body,
        ),
    ]


def page_5_capability():
    return [
        Paragraph("APPLIED AI SPECIALIST CAPABILITY", white_heading),
        section_rule(),
        card_table(
            [Paragraph("<b>xG / xA</b>", orange_style), Paragraph("Shoot quality + chance creation context", white_body)],
            [Paragraph("<b>PASSING NETWORKS</b>", orange_style), Paragraph("Live evolution + opponent mirror", white_body)],
            [Paragraph("<b>SET PIECES</b>", orange_style), Paragraph("Corner / free-kick threat maps by zone", white_body)],
            [Paragraph("<b>PPDA</b>", orange_style), Paragraph("Pressing intensity by phase", white_body)],
            [Paragraph("<b>TRANSITION</b>", orange_style), Paragraph("Speed-of-play and verticality metrics", white_body)],
            col_widths=[170, 320],
        ),
        Spacer(1, 14),
        Paragraph(
            "OWL doesn’t dump raw numbers. It structures them for coaches: "
            "highlight zones, flag anomalies, and suggest attacking / defensive focuses.",
            white_body,
        ),
        Spacer(1, 6),
        Paragraph(
            "<b>Example:</b> Before the North London derby, OWL delivers a 1-page "
            "set-piece threat map covering opponent’s near-post runs + Arsenal’s "
            "defensive shape gaps.",
            white_body,
        ),
    ]


def page_6_architecture():
    return [
        Paragraph("ARCHITECTURE", white_heading),
        section_rule(),
        architecture_diagram(),
        Spacer(1, 14),
        Paragraph(
            "Three clean stages. Plugs into existing tooling. "
            "No rip-and-replace required.",
            white_body,
        ),
    ]


def page_7_deployment():
    return [
        Paragraph("DEPLOYMENT", white_heading),
        section_rule(),
        Paragraph("<b>48-HOUR MODEL</b>", white_subheading),
        section_rule(),
        Paragraph("• Hour 0-4: Credentialed access provisioning (Opta / tracking / video)", bullet_style),
        Paragraph("• Hour 4-12: Schema mapping + Arsenal-specific label alignment", bullet_style),
        Paragraph("• Hour 12-24: Model warm-start on last season's data", bullet_style),
        Paragraph("• Hour 24-36: Validation against known fixtures", bullet_style),
        Paragraph("• Hour 36-48: Go-live + first briefing card sent", bullet_style),
        Spacer(1, 12),
        card_table(
            [Paragraph("<b>SLA</b>", orange_style), Paragraph("<b>TARGET</b>", orange_style), Paragraph("<b>DELIVERED</b>", orange_style)],
            [Paragraph("Deployment window", white_body), Paragraph("72 hrs", white_body), Paragraph("48 hrs", white_body)],
            [Paragraph("Uptime", white_body), Paragraph("99.5%", white_body), Paragraph("99.9%", white_body)],
            [Paragraph("Response time (support)", white_body), Paragraph("< 2 hrs", white_body), Paragraph("< 30 min", white_body)],
            col_widths=[200, 170, 170],
        ),
        Spacer(1, 12),
        Paragraph(
            "OWL runs on secure, dedicated infrastructure. "
            "No PII shared outside Arsenal’s environment.",
            white_body,
        ),
    ]


def page_8_integration():
    return [
        Paragraph("INTEGRATION", white_heading),
        section_rule(),
        Paragraph(
            "Analysts and coaches live in Telegram, iMessage, and Slack. "
            "OWL meets them there.",
            white_body,
        ),
        Spacer(1, 14),
        card_table(
            [Paragraph("TELEGRAM", orange_style), Paragraph("Group threads + direct chats. Rich cards with thumbnails.", white_body)],
            [Paragraph("IMESSAGE", orange_style), Paragraph("Apple ecosystem native. Quick-look summaries.", white_body)],
            [Paragraph("SLACK", orange_style), Paragraph("Workspace channels for analysts + performance.", white_body)],
            col_widths=[140, 400],
        ),
        Spacer(1, 14),
        Paragraph("<b>HOW IT WORKS</b>", white_subheading),
        section_rule(),
        Paragraph("• Coach requests: 'Opponent set-pieces vs low block' → OWL pushes 1-pager in 90 seconds.", bullet_style),
        Paragraph("• Scheduled: Pre-match at T-24h, T-12h, T-1h.", bullet_style),
        Paragraph("• Post-match: Full insight recap + trend delta within 60 minutes FT.", bullet_style),
        Paragraph("• QA loop: Analyst thumbs-up / feedback feeds back to model.", bullet_style),
        Spacer(1, 6),
    ]


def page_9_proof_pricing():
    return [
        Paragraph("PROOF & PRICING", white_heading),
        section_rule(),
        card_table(
            [Paragraph("<b>PROOF</b>", orange_style), Paragraph("DETAIL", white_body)],
            [Paragraph("Validated on 3 clubs", white_body), Paragraph("Premier League + Championship, full season data.", white_body)],
            [Paragraph("Accuracy uplift", white_body), Paragraph("+18% xG calibration over baseline public models.", white_body)],
            [Paragraph("Adoption", white_body), Paragraph("100% of analysts used OWL daily by end of week 1.", white_body)],
            col_widths=[180, 360],
        ),
        Spacer(1, 16),
        Paragraph("<b>PRICING</b>", white_subheading),
        section_rule(),
        card_table(
            [Paragraph("<b>TIER</b>", orange_style), Paragraph("<b>SCOPE</b>", orange_style), Paragraph("<b>INCLUDES</b>", orange_style), Paragraph("<b>PRICE</b>", orange_style)],
            [Paragraph("Embedded", white_body), Paragraph("1st team, weekly", white_body), Paragraph("All deliverables + Telegram/iMessage/Slack", white_body), Paragraph("£6,500/mo", white_body)],
            [Paragraph("Squad", white_body), Paragraph("1st + U21s", white_body), Paragraph("All deliverables + squad-wide scouting", white_body), Paragraph("£9,900/mo", white_body)],
            col_widths=[110, 130, 210, 100],
        ),
        Spacer(1, 8),
        Paragraph(
            "No long-term lock-in. Cancel anytime. Setup: one-time £1,200 onboarding.",
            white_body,
        ),
    ]


def page_10_contact():
    return [
        Spacer(1, 180),
        Paragraph("NEXT STEP", white_heading),
        section_rule(),
        Paragraph("• 30-minute working session with head of analysis", bullet_style),
        Paragraph("• Live OWL demo using your latest opponent footage", bullet_style),
        Paragraph("• 48-hour pilot after sign-off", bullet_style),
        Spacer(1, 30),
        Paragraph("contact@owl-ai.tech", orange_style),
        Paragraph("+44 (0)20 7946 0321", white_body),
        Spacer(1, 40),
        Paragraph("OWL © 2026 — Confidential Arsenal FC proposal.", small_grey),
    ]


# ---------------------------------------------------------------------------
# Build the document
# ---------------------------------------------------------------------------
def build_pdf():
    doc = build_doc_template()
    story = []
    pages = [
        page_1_cover(),
        page_2_exec_summary(),
        page_3_problem(),
        page_4_delivers(),
        page_5_capability(),
        page_6_architecture(),
        page_7_deployment(),
        page_8_integration(),
        page_9_proof_pricing(),
        page_10_contact(),
    ]
    for i, content in enumerate(pages):
        story.extend(content)
        if i < len(pages) - 1:
            story.append(PageBreak())

    doc.build(story)
    print(f"PDF written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
