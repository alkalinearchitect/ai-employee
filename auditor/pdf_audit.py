"""NOHUMA Auditor — PDF export.
Black/white, full-bleed, large-type deliverable (NOHUMA brief: no violet).
Builds a one-page-per-section audit PDF from the assess() result.
Used by app.py route /audit-pdf so the demo becomes a real deliverable.
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
        "eyebrow": ParagraphStyle("eyebrow", fontName="Helvetica-Bold",
            fontSize=9, textColor=SOFT, leading=12, spaceAfter=6, letterSpacing=2),
        "title": ParagraphStyle("title", fontName="Helvetica-Bold",
            fontSize=26, textColor=INK, leading=30, spaceAfter=10),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold",
            fontSize=16, textColor=INK, leading=20, spaceBefore=14, spaceAfter=8),
        "p": ParagraphStyle("p", fontName="Helvetica",
            fontSize=11.5, textColor=INK, leading=16, spaceAfter=8),
        "li": ParagraphStyle("li", fontName="Helvetica",
            fontSize=11.5, textColor=INK, leading=16, spaceAfter=5),
        "small": ParagraphStyle("small", fontName="Helvetica",
            fontSize=9, textColor=SOFT, leading=13, spaceBefore=8),
        "cell": ParagraphStyle("cell", fontName="Helvetica",
            fontSize=10, textColor=INK, leading=13),
        "cellh": ParagraphStyle("cellh", fontName="Helvetica-Bold",
            fontSize=10, textColor=BG, leading=13),
        "tag": ParagraphStyle("tag", fontName="Helvetica-Bold",
            fontSize=10, textColor=INK, leading=13),
    }


def _footer(c, d):
    c.saveState()
    c.setFillColor(BG); c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setStrokeColor(LINE); c.setLineWidth(0.5)
    c.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
    c.setFillColor(SOFT); c.setFont("Helvetica", 8)
    c.drawString(18 * mm, 9 * mm, "NOHUMA AUDIT  ·  demo deliverable  ·  no client data stored")
    c.drawRightString(A4[0] - 18 * mm, 9 * mm, "Page %d" % d.page)
    c.restoreState()


def build(r: dict, path: str):
    if not r.get("ok"):
        raise ValueError(r.get("reason", "audit failed"))
    ss = _styles()
    doc = BaseDocTemplate(path, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=18 * mm, bottomMargin=18 * mm,
        title="NOHUMA Audit — %s" % r.get("domain"))
    fw = doc.width
    doc.addPageTemplates([PageTemplate(id="p",
        frames=[Frame(doc.leftMargin, doc.bottomMargin, fw, doc.height, id="f")],
        onPage=_footer)])

    flow = []
    # Header
    flow.append(Paragraph("SITE AUDIT", ss["eyebrow"]))
    flow.append(Paragraph(r.get("title") or r.get("domain"), ss["title"]))
    flow.append(HRFlowable(width="40%", thickness=1.2, color=INK,
        spaceAfter=12, hAlign="LEFT"))

    # Fact strip
    facts = [
        ["Domain", r.get("domain", "—")],
        ["Industry", r.get("industry", "—")],
        ["Pages found", str(r.get("pages", 0))],
        ["Tech stack", ", ".join(r.get("stack", [])) or "unknown / custom"],
        ["Manual tasks found", str(len(r.get("manual_tells", [])))],
    ]
    rows = [[Paragraph(k, ss["cellh"]), Paragraph(v, ss["cellh"])] for k, v in facts]
    t = Table(rows, colWidths=[fw * 0.32, fw * 0.68])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), INK),
        ("TEXTCOLOR", (0, 0), (-1, -1), BG),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, BG),
    ]))
    flow.append(t)
    flow.append(Spacer(1, 10))

    # Bottleneck
    flow.append(Paragraph("THEIR BOTTLENECK", ss["h2"]))
    flow.append(Paragraph(r.get("bottleneck", "—"), ss["p"]))

    # Manual tells
    if r.get("manual_tells"):
        flow.append(Paragraph("WHAT A PERSON DOES BY HAND", ss["h2"]))
        items = [ListItem(Paragraph(x, ss["li"]), leftIndent=10)
                 for x in r["manual_tells"]]
        flow.append(ListFlowable(items, bulletType="bullet",
            start="•", leftIndent=14, bulletColor=INK))

    # How we help
    flow.append(Paragraph("HOW A NOHUMA WORKER HELPS", ss["h2"]))
    items = [ListItem(Paragraph(x, ss["li"]), leftIndent=10)
             for x in r.get("how_we_help", [])]
    flow.append(ListFlowable(items, bulletType="bullet",
        start="•", leftIndent=14, bulletColor=INK))

    # Honesty note
    flow.append(Paragraph(
        "Industry, pages and stack above are read live from the site. The "
        "bottleneck and 'how we help' wording is our reasoned assessment from "
        "those signals — not a claim about the company. " + r.get("stack_note", ""),
        ss["small"]))

    doc.build(flow)
    return path
