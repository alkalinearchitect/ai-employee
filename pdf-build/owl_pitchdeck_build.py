#!/usr/bin/env python3
# owl_pitchdeck_build.py — generate Owl pitch deck PDF
import sys
sys.path.insert(0, "/root/ai-employee/pdf-build")
from owl_unified_content_spec import COVER_PITCH, PITCH_SLIDES, URLS
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.styles import ParagraphStyle

BG = colors.HexColor("#101214")
INK = colors.HexColor("#f2f3f5")
SOFT = colors.HexColor("#8a8f94")
SURFACE = colors.HexColor("#171a1d")
ACC = colors.HexColor("#ffffff")
BORDER = colors.HexColor("#262a2e")

SC = 1.55
def sz(base):
    return int(base * SC)

ss = {
    'eyebrow': ParagraphStyle('eyebrow', fontName='Helvetica-Bold', fontSize=sz(9), textColor=SOFT, leading=sz(13), spaceAfter=6, letterSpacing=2),
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=sz(26), textColor=INK, leading=sz(31), spaceAfter=12),
    'sub': ParagraphStyle('sub', fontName='Helvetica', fontSize=sz(13), textColor=SOFT, leading=sz(19), spaceAfter=10),
    'p': ParagraphStyle('p', fontName='Helvetica', fontSize=sz(12), textColor=INK, leading=sz(17), spaceAfter=10),
    'li': ParagraphStyle('li', fontName='Helvetica', fontSize=sz(12), textColor=INK, leading=sz(17), leftIndent=16, bulletIndent=4, spaceAfter=8),
    'callout': ParagraphStyle('callout', fontName='Helvetica-Bold', fontSize=sz(13), textColor=BG, leading=sz(19), leftIndent=12, spaceBefore=8, spaceAfter=12),
    'quote': ParagraphStyle('quote', fontName='Helvetica-Oblique', fontSize=sz(13), textColor=SOFT, leading=sz(18), spaceBefore=8, spaceAfter=10),
    'label': ParagraphStyle('label', fontName='Helvetica-Bold', fontSize=sz(10), textColor=ACC, leading=sz(14), spaceAfter=4),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=sz(9), textColor=SOFT, leading=sz(13)),
    'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=sz(9), textColor=INK, leading=sz(13)),
    'cellh': ParagraphStyle('cellh', fontName='Helvetica-Bold', fontSize=sz(9), textColor=BG, leading=sz(13)),
    'foot': ParagraphStyle('foot', fontName='Helvetica', fontSize=sz(8), textColor=SOFT, leading=sz(10)),
}

page_w, page_h = landscape(A4)
LM = RM = 18 * mm
TM = BM = 14 * mm
fw = page_w - LM - RM
fh = page_h - TM - BM

def bg(c, d):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,page_w,page_h,fill=1,stroke=0)
    c.setFillColor(SURFACE); c.rect(LM, BM, fw, fh, fill=1, stroke=0)
    c.setStrokeColor(BORDER); c.setLineWidth(0.7)
    c.rect(LM, BM, fw, fh, fill=0, stroke=1)
    c.setFillColor(SOFT); c.setFont('Helvetica', sz(8))
    c.drawString(LM, BM-6*mm, 'HUMAN ARCHITECT  ·  PITCH v1.0')
    c.drawRightString(page_w-RM, BM-6*mm, 'Slide %d' % d.page)
    c.restoreState()

def cover_bg(c, d):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,page_w,page_h,fill=1,stroke=0)
    c.setFillColor(ACC); c.setFillAlpha(0.10)
    c.circle(page_w*0.5, page_h*0.55, 280, fill=1, stroke=0)
    c.circle(page_w*0.5, page_h*0.55, 380, fill=1, stroke=0)
    c.setFillAlpha(1)
    c.restoreState()

def build(path):
    doc = BaseDocTemplate(path, pagesize=landscape(A4),
                          leftMargin=LM, rightMargin=RM,
                          topMargin=TM, bottomMargin=BM)
    doc.addPageTemplates([
        PageTemplate(id='slides', frames=[Frame(LM,BM,fw,fh,id='f')], onPage=bg),
        PageTemplate(id='cover', frames=[Frame(LM,BM,fw,fh,id='c')], onPage=cover_bg),
    ])
    st = []
    c = 0
    for s in PITCH_SLIDES:
        c += 1
        if c == 1:
            st.append(Spacer(1, 8*mm))
            st.append(Paragraph(s['eyebrow'], ss['eyebrow']))
            st.append(Spacer(1, 3*mm))
            st.append(Paragraph(s['title'], ss['title']))
            st.append(HRFlowable(width='35%', thickness=1, color=ACC, spaceAfter=10, spaceBefore=0, hAlign='LEFT'))
            for blk in s['blocks']:
                kind = blk['t']
                txt = blk['text']
                if kind == 'sub':
                    st.append(Paragraph(txt, ss['sub']))
                elif kind == 'callout':
                    t = Table([[Paragraph(txt, ss['callout'])]], colWidths=[fw])
                    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1), ACC.clone(alpha=0.88)),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
                    st.append(t)
                    st.append(Spacer(1,4))
                elif kind == 'p':
                    st.append(Paragraph(txt, ss['p']))
            st.append(Spacer(1, 4))
            st.append(Paragraph(COVER_PITCH['foot'], ss['foot']))
            st.append(Paragraph('Live: ' + URLS['SITE'] + '<br/>Call: ' + URLS['BOOK'], ss['foot']))
            if c < len(PITCH_SLIDES):
                st.append(PageBreak())
            continue

        if c > 1:
            st.append(PageBreak())
        st.append(Paragraph(s['eyebrow'], ss['eyebrow']))
        st.append(Spacer(1, 3*mm))
        st.append(Paragraph(s['title'], ss['title']))
        st.append(HRFlowable(width='35%', thickness=1, color=ACC, spaceAfter=10, spaceBefore=0, hAlign='LEFT'))
        for blk in s['blocks']:
            kind = blk['t']
            txt = blk['text']
            if kind == 'p':
                st.append(Paragraph(txt, ss['p']))
            elif kind == 'li':
                st.append(Paragraph('•  ' + txt, ss['li']))
            elif kind == 'callout':
                t = Table([[Paragraph(txt, ss['callout'])]], colWidths=[fw])
                t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1), ACC.clone(alpha=0.88)),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,0),8)]))
                st.append(t)
                st.append(Spacer(1,4))
            elif kind == 'quote':
                st.append(Paragraph('\u201c' + txt + '\u201d', ss['quote']))
            elif kind == 'table':
                rows = txt
                table_rows = [[Paragraph(c, ss['cellh'] if i==0 else ss['cell']) for c in r] for i,r in enumerate(rows)]
                col_w = [fw * 0.34, fw * 0.34, fw * 0.32] if len(rows[0]) == 3 else [fw * 0.40, fw * 0.60]
                if len(rows[0]) == 2:
                    col_w = [fw * 0.34, fw * 0.66]
                tw = Table(table_rows, colWidths=col_w)
                tw.setStyle(TableStyle([
                    ('BACKGROUND',(0,0),(-1,0), INK),
                    ('ROWBACKGROUNDS',(0,1),(-1,-1), [BG, SURFACE]),
                    ('GRID',(0,0),(-1,-1), 0.5, INK.clone(alpha=0.25)),
                    ('VALIGN',(0,0),(-1,-1), 'TOP'),
                    ('LEFTPADDING',(0,0),(-1,-1),7), ('RIGHTPADDING',(0,0),(-1,-1),7),
                    ('TOPPADDING',(0,0),(-1,-1),7), ('BOTTOMPADDING',(0,0),(-1,-1),7),
                ]))
                st.append(tw)
                st.append(Spacer(1,4))
            elif kind == 'sub':
                st.append(Paragraph(txt, ss['sub']))
            elif kind == 'label':
                st.append(Paragraph(txt, ss['label']))
            elif kind == 'small':
                st.append(Paragraph(txt, ss['small']))
        st.append(Spacer(1, 4))

    doc.build(st)
    print('PDF ->', path)
    print('SLIDES', c)

if __name__ == "__main__":
    build("/root/ai-employee/pdf-build/owl_pitchdeck.pdf")
