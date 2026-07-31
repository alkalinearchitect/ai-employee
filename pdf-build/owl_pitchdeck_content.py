from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.styles import ParagraphStyle

BG = colors.HexColor('#101214')
SURFACE = colors.HexColor('#171a1d')
BORDER = colors.HexColor('#262a2e')
INK = colors.HexColor('#f2f3f5')
SOFT = colors.HexColor('#8a8f94')
ACC = colors.HexColor('#ffffff')

SC = 1.55
def sz(base): return int(base * SC)

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
}

page_w, page_h = landscape(A4)
LM = 18*mm; RM = 18*mm; TM = 14*mm; BM = 14*mm
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

slides = []
slides.append({
    'eyebrow':'HUMAN ARCHITECT',
    'title':'One AI employee.<br/>One monthly fee.',
    'blocks':[
        ('sub','Flat £5,000/month. Live in 48 hours. Managed outcome, not a chatbot.'),
        ('callout','Price: £5,000/month. 48-hour delivery. Outcome-based, not tool-based.'),
        ('p','I deploy an AI worker into your existing channel — Slack or Telegram — that owns one defined body of work. You measure output, not usage. No hiring. No HR. No sick leave.'),
    ]
})
slides.append({
    'eyebrow':'WHY',
    'title':'We refuse to accept avoidable admin cost.',
    'blocks':[
        ('p','Most UK SMBs bleed money on tasks humans do badly at 3am, on holidays, or under pressure. These are not strategy tasks — they are repetitive loops.'),
        ('quote','A managed AI employee is leverage, not replacement. You keep the architect. You get the hours back.'),
        ('p','The market is early. The margin runs around 90%. The moat is fulfillment — not the model.'),
    ]
})
slides.append({
    'eyebrow':'THE PAIN',
    'title':'The wound is small, daily, and visible.',
    'blocks':[
        ('p','Staff spend 10–20 hours a week on intake, follow-up, notes, or admin that needs consistency, not judgement.'),
        ('li','Missed enquiries: after-hours leads go elsewhere.'),
        ('li','Slow quotes: trade jobs lost to faster responders.'),
        ('li','No-shows: clinic or coach time disappears.'),
        ('li','Onboarding drag: agencies lose kickoff weeks to asset chasing.'),
        ('p','These leaks are not dramatic. They are daily. That is why they never get fixed.'),
    ]
})
slides.append({
    'eyebrow':'HOW',
    'title':'Outcome ownership, not tool deployment.',
    'blocks':[
        ('li','1 · Foot-in-the-door: £999 audit surfaces the highest-ROI task.'),
        ('li','2 · One agent, ONE job — the task with the most obvious payback.'),
        ('li','3 · Price flat at £5,000/month, all usage, all updates included.'),
        ('li','4 · Ship by day two after agreement + platform token.'),
        ('li','5 · Prove outcome fast. Use client language, not AI language.'),
        ('p','Speed wins. If you lead with AI, you lose. Lead with outcomes.'),
    ]
})
slides.append({
    'eyebrow':'PROOF MATH',
    'title':'Why £5,000 is easy to justify.',
    'blocks':[
        ('p','Every objection collapses when you measure hours, leads, or outcomes.'),
        ('li','2 hrs/day x £40/hr = £2,400/month before mistakes.'),
        ('li','20 missed leads/month x £3,500 commission = £21,000/month leak.'),
        ('li','1 recovered emergency job/week > £5,000 within 6–10 weeks.'),
        ('callout','Lead-value rule: the AI employee either pays for itself or misses target.'),
    ]
})
slides.append({
    'eyebrow':'PROOF POINTS',
    'title':'Verified operators, exact claims.',
    'blocks':[
        ('table',[
            ['Source','Claim','Date / context'],
            ['Nick Vasilescu / Corey Ganim','$5K/mo + fulfillment model','podcast + recap Jun 2026'],
            ['Linara Bozieva / Business Insider','27 agents, 5 clients, ~2 hrs/week oversight','post eBay layoff, 2026'],
            ['Boon Media / case studies','Barber no-shows 18%→4%; freight quote response 45min→5min','live page'],
        ]),
        ('small','Attribution note: the $5K/mo fulfillment quote originates from Corey Ganim’s recap of Nick Vasilescu — do not use unauthenticated.'),
    ]
})
slides.append({
    'eyebrow':'IMPLEMENTATION',
    'title':'Standard opener. No custom until proven.',
    'blocks':[
        ('li','Discovery call: one question — “What task drains your team every day?”'),
        ('li','Audit: map exact workflow + current tool stack.'),
        ('li','Scope: ONE agent, ONE outcome, ONE integration channel.'),
        ('li','Build: SOUL.md + knowledge vault + process map.'),
        ('li','Onboard: introduce into the client’s Slack/Telegram with live example.'),
        ('p','Do not scale until the first agent delivers by day 14.'),
    ]
})
slides.append({
    'eyebrow':'STACK',
    'title':'Your edge: self-hosted.',
    'blocks':[
        ('table',[
            ['Part','Reference paid','Self-hosted free'],
            ['Computer','Orgo','VPS / container'],
            ['Harness','OpenClaw/Hermes','Hermes Agent'],
            ['KB','Fresh vault','~/vault Obsidian'],
            ['Watch','Latitude','Cron → Telegram'],
        ]),
        ('p','Avoid Orgo/Composio/AgentMail/AgentPhone/Latitude/Honcho unless explicitly approved. The paid stack is a sales hook, not a requirement.'),
    ]
})
slides.append({
    'eyebrow':'B2B2B RETENTION',
    'title':'Churn reduction mode.',
    'blocks':[
        ('p','Once the agent runs, show the client how to resell access to THEIR customers. That changes churn psychology.'),
        ('li','They become less likely to cancel because it becomes revenue infrastructure.'),
        ('li','They become a case study.'),
        ('li','They introduce you to peers in the same vertical.'),
        ('callout','Do not sell an AI employee. Sell a margin loop they can resell.'),
    ]
})
slides.append({
    'eyebrow':'RISK CONTROL',
    'title':'Reduce risk before reducing price.',
    'blocks':[
        ('li','Fixed scope: one task per agent, one outcome.'),
        ('li','Fixed channel: one Slack or Telegram thread.'),
        ('li','Fixed deadline: live by day two after handoff.'),
        ('li','Fixed metric: what “done” looks like in 30 days.'),
        ('p','If it misses the agreed target by day 30, partial refund.'),
    ]
})
slides.append({
    'eyebrow':'ASSUME CLOSE',
    'title':'Close from the first touch.',
    'blocks':[
        ('quote','The risk is not testing one AI employee for one month. The risk is bleeding margin on a task that does not require a human.'),
        ('p','“If I could [exact outcome] in 48 hours at £5,000/month, which side of this are you on?”'),
        ('callout','Next action is a fixed call, not a vague follow-up.'),
    ]
})
slides.append({
    'eyebrow':'CONTACT',
    'title':'One next step.',
    'blocks':[
        ('p','Primary booking: beacons.ai/humanarchitect'),
        ('p','Offer site: alkalinearchitect.github.io/ai-employee/'),
        ('quote','One agent. One workflow. One outcome.'),
    ]
})

path='/root/ai-employee/pdf-build/owl_pitchdeck.pdf'
out = BaseDocTemplate(path, pagesize=landscape(A4), leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM)
out.addPageTemplates([PageTemplate(id='slides', frames=[Frame(LM,BM,fw,fh,id='f')], onPage=bg)])

st=[]
c=0
for s in slides:
    c += 1
    if c > 1:
        st.append(PageBreak())
    st.append(Paragraph(s['eyebrow'], ss['eyebrow']))
    st.append(Spacer(1, 3*mm))
    st.append(Paragraph(s['title'], ss['title']))
    st.append(HRFlowable(width='35%', thickness=1, color=ACC, spaceAfter=10, spaceBefore=0, hAlign='LEFT'))
    for kind, txt in s['blocks']:
        if kind == 'p':
            st.append(Paragraph(txt, ss['p']))
        elif kind == 'li':
            st.append(Paragraph('•  ' + txt, ss['li']))
        elif kind == 'callout':
            t=Table([[Paragraph(txt, ss['callout'])]], colWidths=[fw])
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1), ACC.clone(alpha=0.88)),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
            st.append(t); st.append(Spacer(1,4))
        elif kind == 'quote':
            st.append(Paragraph('\u201c' + txt + '\u201d', ss['quote']))
        elif kind == 'table':
            rows = [[Paragraph(c, ss['cellh'] if i==0 else ss['cell']) for c in r] for i,r in enumerate(txt)]
            col_w=[fw*0.28, fw*0.40, fw*0.32] if len(rows[0])==3 else [fw*0.34, fw*0.33, fw*0.33]
            tw = Table(rows, colWidths=col_w[:len(rows[0])])
            tw.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0), INK),
                ('ROWBACKGROUNDS',(0,1),(-1,-1), [BG, SURFACE]),
                ('GRID',(0,0),(-1,-1), 0.5, INK.clone(alpha=0.25)),
                ('VALIGN',(0,0),(-1,-1), 'TOP'),
                ('LEFTPADDING',(0,0),(-1,-1),7), ('RIGHTPADDING',(0,0),(-1,-1),7),
                ('TOPPADDING',(0,0),(-1,-1),7), ('BOTTOMPADDING',(0,0),(-1,-1),7),
            ]))
            st.append(tw); st.append(Spacer(1,4))
        elif kind == 'sub':
            st.append(Paragraph(txt, ss['sub']))
        elif kind == 'label':
            st.append(Paragraph(txt, ss['label']))
        elif kind == 'small':
            st.append(Paragraph(txt, ss['small']))
    st.append(Spacer(1,6))

out.build(st)
print('PDF ->', path)
print('SLIDES', len(slides))
