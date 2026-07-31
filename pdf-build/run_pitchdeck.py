import importlib.util, pathlib
p=pathlib.Path('/root/ai-employee/pdf-build/owl_pitchdeck_content.py')
code=p.read_text()
exec(compile(code, p, 'exec'), globals())  # populate slides, ss, etc.
# Build PDF inline
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.pagesizes import landscape, A4
page_w, page_h = landscape(A4)
LM = 18; RM = 18; TM = 14; BM = 14
fw = page_w - LM - RM; fh = page_h - TM - BM
BG = colors.HexColor('#101214')
SURFACE = colors.HexColor('#171a1d')
BORDER = colors.HexColor('#262a2e')
INK = colors.HexColor('#f2f3f5')
SOFT = colors.HexColor('#8a8f94')
ACC = colors.HexColor('#ffffff')
SC = 1.55
def sz(base): return int(base * SC)

def bg(c,d):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,page_w,page_h,fill=1,stroke=0)
    c.setFillColor(SURFACE); c.rect(LM, BM, fw, fh, fill=1, stroke=0)
    c.setStrokeColor(BORDER); c.setLineWidth(0.7)
    c.rect(LM, BM, fw, fh, fill=0, stroke=1)
    c.setFillColor(SOFT); c.setFont('Helvetica', sz(8))
    c.drawString(LM, BM-6, 'HUMAN ARCHITECT  ·  PITCH v1.0')
    c.drawRightString(page_w-RM, BM-6, 'Slide %d' % d.page)
    c.restoreState()

path='/root/ai-employee/pdf-build/owl_pitchdeck.pdf'
out=BaseDocTemplate(path, pagesize=landscape(A4), leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM)
out.addPageTemplates([PageTemplate(id='slide', frames=[Frame(LM,BM,fw,fh,id='f')], onPage=bg)])
doc=[]
c=0
for s in slides:
    c += 1
    if c > 1: doc.append(PageBreak())
    doc.append(Paragraph(s['eyebrow'], ss['eyebrow']))
    doc.append(Spacer(1, 3))
    doc.append(Paragraph(s['title'], ss['title']))
    doc.append(HRFlowable(width='35%', thickness=1, color=ACC, spaceAfter=10, spaceBefore=0, hAlign='LEFT'))
    for kind, txt in s['blocks']:
        if kind == 'p':
            doc.append(Paragraph(txt, ss['p']))
        elif kind == 'li':
            doc.append(Paragraph('•  ' + txt, ss['li']))
        elif kind == 'callout':
            t=Table([[Paragraph(txt, ss['callout'])]], colWidths=[fw])
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1), ACC.clone(alpha=0.88)),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
            doc.append(t); doc.append(Spacer(1,4))
        elif kind == 'quote':
            doc.append(Paragraph('\u201c' + txt + '\u201d', ss['quote']))
        elif kind == 'table':
            rows = [[Paragraph(c, ss['cellh'] if i==0 else ss['cell']) for c in r] for i,r in enumerate(txt)]
            col_w=[fw*0.34, fw*0.34, fw*0.32]
            if len(rows[0])==2: col_w=[fw*0.4, fw*0.6]
            tw = Table(rows, colWidths=col_w)
            tw.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0), INK),('ROWBACKGROUNDS',(0,1),(-1,-1), [BG, SURFACE]),('GRID',(0,0),(-1,-1), 0.5, INK.clone(alpha=0.25)),('VALIGN',(0,0),(-1,-1), 'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            doc.append(tw); doc.append(Spacer(1,4))
        elif kind == 'sub':
            doc.append(Paragraph(txt, ss['sub']))
        elif kind == 'label':
            doc.append(Paragraph(txt, ss['label']))
        elif kind == 'small':
            doc.append(Paragraph(txt, ss['small']))
    doc.append(Spacer(1,6))
out.build(doc)
print('PDF ->', path)
