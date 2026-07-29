#!/usr/bin/env python3
# owl_sales_manual_build.py — generate Owl closing training manual PDF
import sys
sys.path.insert(0, "/root/ai-employee/pdf-build")
from owl_sales_manual_content import PAGES, COVER, SITE, BOOK
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.styles import ParagraphStyle

BG = colors.HexColor("#0a0612")
INK = colors.HexColor("#ffffff")
SOFT = colors.HexColor("#b9aee0")
ACC = colors.HexColor("#8B5CFF")
RULE = colors.HexColor("#d1d1d6")

ss = {
    "eyebrow": ParagraphStyle("eyebrow", fontName="Helvetica-Bold", fontSize=9, textColor=ACC, leading=12, spaceAfter=4, letterSpacing=2),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=23, textColor=INK, leading=26, spaceAfter=10),
    "p": ParagraphStyle("p", fontName="Helvetica", fontSize=11, textColor=INK, leading=16, spaceAfter=7),
    "li": ParagraphStyle("li", fontName="Helvetica", fontSize=11, textColor=INK, leading=15, leftIndent=12, bulletIndent=2, spaceAfter=5),
    "callout": ParagraphStyle("callout", fontName="Helvetica-Bold", fontSize=11.5, textColor=INK, leading=16, leftIndent=10, spaceBefore=4, spaceAfter=8),
    "quote": ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=13, textColor=ACC, leading=18, spaceBefore=6, spaceAfter=6),
    "cover_eye": ParagraphStyle("ce", fontName="Helvetica-Bold", fontSize=11, textColor=ACC, leading=14, spaceAfter=10, letterSpacing=3),
    "cover_title": ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=40, textColor=INK, leading=44, spaceAfter=12),
    "cover_sub": ParagraphStyle("cs", fontName="Helvetica", fontSize=13, textColor=SOFT, leading=18, spaceAfter=24),
    "cover_tag": ParagraphStyle("ctg", fontName="Helvetica-Oblique", fontSize=12, textColor=ACC, leading=16, spaceAfter=40),
    "cover_foot": ParagraphStyle("cf", fontName="Helvetica", fontSize=9, textColor=SOFT, leading=13),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=13),
    "cellh": ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=9.5, textColor=BG, leading=13),
    "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8, textColor=SOFT, leading=10),
    "step_title": ParagraphStyle("step_title", fontName="Helvetica-Bold", fontSize=12.5, textColor=ACC, leading=15, spaceAfter=4),
    "step_body": ParagraphStyle("step_body", fontName="Helvetica", fontSize=11, textColor=INK, leading=15, spaceAfter=6, leftIndent=14),
}

def bg_shape(c, d):
    c.saveState()
    c.setFillColor(BG); c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setStrokeColor(RULE); c.setStrokeAlpha(0.15); c.setLineWidth(0.5)
    c.line(18*mm, 14*mm, A4[0]-18*mm, 14*mm)
    c.setFillColor(SOFT); c.setFont("Helvetica", 8); c.setFillAlpha(0.6)
    c.drawString(18*mm, 9*mm, "OWL CLOSING MANUAL · Human Architect")
    c.drawRightString(A4[0]-18*mm, 9*mm, "Page %d" % d.page)
    c.restoreState()

def cover_bg(c, d):
    c.saveState()
    c.setFillColor(BG); c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setFillColor(ACC); c.setFillAlpha(0.12)
    c.circle(A4[0]*0.5, A4[1]*0.62, 300, fill=1, stroke=0)
    c.setFillAlpha(1)
    c.setFillColor(ACC); c.rect(18*mm, A4[1]-150*mm, 26*mm, 2.4, fill=1, stroke=0); c.restoreState()

def build(path):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=18*mm, rightMargin=18*mm,
                          topMargin=20*mm, bottomMargin=18*mm)
    fw = doc.width
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[Frame(doc.leftMargin, doc.bottomMargin, fw, doc.height, id="c")], onPage=cover_bg),
        PageTemplate(id="body", frames=[Frame(doc.leftMargin, doc.bottomMargin, fw, doc.height, id="f")], onPage=bg_shape),
    ])
    st = []
    st.append(Spacer(1, 36*mm))
    st.append(Paragraph(COVER["eyebrow"], ss["cover_eye"]))
    st.append(Paragraph(COVER["title"], ss["cover_title"]))
    st.append(Paragraph(COVER["sub"], ss["cover_sub"]))
    st.append(Paragraph(COVER["tag"], ss["cover_tag"]))
    st.append(Paragraph(COVER["foot"], ss["cover_foot"]))
    st.append(Paragraph("Live: "+SITE+"<br/>Call: "+BOOK, ss["cover_foot"]))
    st.append(PageBreak())

    for pg in PAGES:
        st.append(Paragraph(pg["eyebrow"], ss["eyebrow"]))
        st.append(Paragraph(pg["title"], ss["title"]))
        st.append(HRFlowable(width="40%", thickness=1.2, color=ACC, spaceAfter=10, spaceBefore=0, hAlign="LEFT"))
        for kind, txt in pg["blocks"]:
            if kind == "p":
                st.append(Paragraph(txt, ss["p"]))
            elif kind == "li":
                st.append(Paragraph("• • "+txt, ss["li"]))
            elif kind == "callout":
                t = Table([[Paragraph(txt, ss["callout"])]], colWidths=[fw])
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0,0), (-1,-1), ACC.clone(alpha=0.12)),
                    ("LINEBEFORE", (0,0), (0,-1), 3, ACC),
                    ("LEFTPADDING", (0,0), (-1,-1), 10),
                    ("RIGHTPADDING", (0,0), (-1,-1), 10),
                    ("TOPPADDING", (0,0), (-1,-1), 8),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
                ]))
                st.append(t); st.append(Spacer(1,6))
            elif kind == "quote":
                st.append(Paragraph("“"+txt+"”", ss["quote"]))
            elif kind == "table":
                rows = [[Paragraph(c, ss["cellh"] if i==0 else ss["cell"]) for c in r] for i,r in enumerate(txt)]
                tb = Table(rows, colWidths=[fw*0.28, fw*0.36, fw*0.36])
                tb.setStyle(TableStyle([
                    ("BACKGROUND", (0,0), (-1,0), ACC),
                    ("ROWBACKGROUNDS", (0,1), (-1,-1), [BG, ACC.clone(alpha=0.06)]),
                    ("GRID", (0,0), (-1,-1), 0.5, ACC.clone(alpha=0.3)),
                    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                    ("LEFTPADDING", (0,0), (-1,-1), 7),
                    ("RIGHTPADDING", (0,0), (-1,-1), 7),
                    ("TOPPADDING", (0,0), (-1,-1), 6),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
                ]))
                st.append(tb); st.append(Spacer(1,6))
            elif kind == "step":
                st.append(Paragraph(txt, ss["step_body"]))
            elif kind == "step_title":
                st.append(Paragraph(txt, ss["step_title"]))
        st.append(PageBreak())

    doc.build(st)
    print("PDF written:", path)

if __name__ == "__main__":
    build("/root/ai-employee/pdf-build/owl-closing-manual.pdf")
