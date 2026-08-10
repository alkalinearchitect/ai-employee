"""Zernio verdict PDF — black/white, full-bleed, no violet (NOHUMA brief).
Builds a plain-English assessment of whether Zernio is worth using for OWL/Dewey.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, ListFlowable, ListItem, PageBreak
)
from reportlab.lib.styles import ParagraphStyle

BG = colors.HexColor("#000000")
INK = colors.HexColor("#ffffff")
SOFT = colors.HexColor("#9a9ca6")
LINE = colors.HexColor("#34343d")


def _styles():
    return {
        "eyebrow": ParagraphStyle("eyebrow", fontName="Helvetica-Bold", fontSize=9,
            textColor=SOFT, leading=12, spaceAfter=6, letterSpacing=2),
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24,
            textColor=INK, leading=28, spaceAfter=8),
        "verdict": ParagraphStyle("verdict", fontName="Helvetica-Bold", fontSize=15,
            textColor=INK, leading=20, spaceBefore=6, spaceAfter=10),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=14,
            textColor=INK, leading=18, spaceBefore=14, spaceAfter=6),
        "p": ParagraphStyle("p", fontName="Helvetica", fontSize=11,
            textColor=INK, leading=15.5, spaceAfter=8),
        "li": ParagraphStyle("li", fontName="Helvetica", fontSize=11,
            textColor=INK, leading=15, spaceAfter=4),
        "small": ParagraphStyle("small", fontName="Helvetica", fontSize=9,
            textColor=SOFT, leading=13, spaceBefore=8),
        "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=10,
            textColor=INK, leading=13),
        "cellh": ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=10,
            textColor=BG, leading=13),
        "ok": ParagraphStyle("ok", fontName="Helvetica-Bold", fontSize=10,
            textColor=INK, leading=13),
    }


def _footer(c, d):
    c.saveState()
    c.setFillColor(BG); c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setStrokeColor(LINE); c.setLineWidth(0.5)
    c.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
    c.setFillColor(SOFT); c.setFont("Helvetica", 8)
    c.drawString(18 * mm, 9 * mm, "OWL INTEL  ·  ZERNIO VERDICT  ·  verified 2026-08-10")
    c.drawRightString(A4[0] - 18 * mm, 9 * mm, "Page %d" % d.page)
    c.restoreState()


def build(path: str):
    ss = _styles()
    doc = BaseDocTemplate(path, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=18 * mm, bottomMargin=18 * mm, title="Zernio Verdict")
    fw = doc.width
    doc.addPageTemplates([PageTemplate(id="p",
        frames=[Frame(doc.leftMargin, doc.bottomMargin, fw, doc.height, id="f")],
        onPage=_footer)])

    f = []
    f.append(Paragraph("IS ZERNIO ANY GOOD?", ss["eyebrow"]))
    f.append(Paragraph("Verdict on a unified 15-channel messaging API for OWL / Dewey", ss["title"]))
    f.append(HRFlowable(width="40%", thickness=1.2, color=INK, spaceAfter=10, hAlign="LEFT"))

    # Verdict box
    vb = Table([[Paragraph(
        "VERDICT: LEGIT. Use as a candidate comms layer — after a free-tier check. "
        "It is the cleanest fix for Dewey's missing multi-channel comms, and it is "
        "MCP-native so Hermes can drive it. Do NOT spend or sign up without T's go.",
        ss["verdict"])]], colWidths=[fw])
    vb.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), INK),
        ("TEXTCOLOR", (0, 0), (-1, -1), BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    f.append(vb)

    # What it is
    f.append(Paragraph("WHAT IT IS (verified from live site + docs)", ss["h2"]))
    f.append(Paragraph(
        "Zernio (formerly getlate.dev) is one API + one MCP server that lets software "
        "post, message, run ads, and read analytics across 15 channels: X, Instagram, "
        "TikTok, LinkedIn, Facebook, YouTube, Threads, Reddit, Pinterest, Bluesky, "
        "Snapchat, Google Business, WhatsApp, Telegram, Discord. It handles OAuth "
        "logins, WhatsApp number KYC in 54 countries, and retry-on-failure. Official "
        "APIs only — no ban risk. SOC 2 + GDPR listed on trust.zernio.com.", ss["p"]))

    # Evidence table
    rows = [
        [Paragraph("Claim", ss["cellh"]), Paragraph("Status", ss["cellh"]), Paragraph("Source", ss["cellh"])],
        [Paragraph("Live product, not vaporware", ss["cell"]), Paragraph("CONFIRMED", ss["ok"]), Paragraph("zernio.com HTTP 200; real docs", ss["cell"])],
        [Paragraph("Official MCP server for AI agents", ss["cell"]), Paragraph("CONFIRMED", ss["ok"]), Paragraph("docs.zernio.com/mcp; 496 tools", ss["cell"])],
        [Paragraph("Free tier exists", ss["cell"]), Paragraph("CONFIRMED", ss["ok"]), Paragraph("'first 2 accounts free, no card'", ss["cell"])],
        [Paragraph("15+ channels as stated", ss["cell"]), Paragraph("CONFIRMED", ss["ok"]), Paragraph("platform list on site", ss["cell"])],
        [Paragraph("SOC2 / GDPR compliant", ss["cell"]), Paragraph("CLAIMED", ss["cell"]), Paragraph("trust.zernio.com (unverified by us)", ss["cell"])],
        [Paragraph("'409k posts this week'", ss["cell"]), Paragraph("THEIR MARKETING", ss["cell"]), Paragraph("not independently verified", ss["cell"])],
    ]
    t = Table(rows, colWidths=[fw * 0.42, fw * 0.22, fw * 0.36])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BG, colors.HexColor("#0d0d10")]),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    f.append(t)

    f.append(Paragraph("HOW IT FITS OWL / DEWEY (the 8-part model)", ss["h2"]))
    f.append(Paragraph(
        "Component 4 of the Dewey model is 'phone and comms.' Our free-stack clone has "
        "Telegram + Slack but no proper outbound layer across the channels a client's "
        "customers actually use. Zernio is the ready-made comms layer:", ss["p"]))
    items = [
        ListItem(Paragraph("Closes the 'phone is the interface' gap — a WhatsApp number, KYC done, live in minutes, no iMessage dependency.", ss["li"]), leftIndent=10),
        ListItem(Paragraph("Closes the 'OWL drafts, you send' limit — with Zernio + MCP, OWL can actually POST and REPLY, not just write.", ss["li"]), leftIndent=10),
        ListItem(Paragraph("It sits ON TOP as a distribution layer; it does not replace anything we have.", ss["li"]), leftIndent=10),
    ]
    f.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=14, bulletColor=INK))

    f.append(Paragraph("WHY USE IT (my honest read)", ss["h2"]))
    f.append(Paragraph(
        "Yes, as a candidate. It is the most direct fix for Dewey's missing comms layer, "
        "and MCP-native means Hermes can use it in plain language ('Post this to LinkedIn "
        "and WhatsApp'). The free tier (2 accounts, no card) means we can trial with zero "
        "spend and zero risk.", ss["p"]))

    f.append(Paragraph("WHY NOT YET / NOT BLIND (boss-protocol)", ss["h2"]))
    items2 = [
        ListItem(Paragraph("It is a paid SaaS. Rule: free-stack-only unless T approves spend. No API key held, not signed up.", ss["li"]), leftIndent=10),
        ListItem(Paragraph("Must verify before recommending money: read MCP + API docs, check free-tier limits, confirm Hermes compatibility via MCP, check SOC2/GDPR claims on trust.zernio.com.", ss["li"]), leftIndent=10),
        ListItem(Paragraph("Trial on a TEST account first — never wire into a paying client on day one.", ss["li"]), leftIndent=10),
        ListItem(Paragraph("'409k posts this week' is their marketing, not verified. Treat all volume claims as unconfirmed.", ss["li"]), leftIndent=10),
    ]
    f.append(ListFlowable(items2, bulletType="bullet", start="•", leftIndent=14, bulletColor=INK))

    f.append(Paragraph("BOTTOM LINE", ss["h2"]))
    f.append(Paragraph(
        "Zernio is the cleanest way to give OWL/Dewey real multi-channel comms without "
        "building 15 integrations by hand. Use it after a verified free-tier check — as "
        "the comms component in the client-agent factory, not as a core dependency. "
        "I will not sign up or spend without your go.", ss["p"]))

    f.append(Paragraph(
        "Verification note: site, docs, MCP page and platform list confirmed live on "
        "2026-08-10. SOC2/GDPR and volume metrics are vendor claims, not independently "
        "verified. No purchase made. No account created.", ss["small"]))

    doc.build(f)
    return path
