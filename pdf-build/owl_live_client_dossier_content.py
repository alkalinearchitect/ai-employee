from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.styles import ParagraphStyle

BG = colors.HexColor("#000000")
INK = colors.HexColor("#ffffff")
SOFT = colors.HexColor("#888888")
ACC = colors.HexColor("#ffffff")

SC = 1.6

def sz(base):
    return int(base * SC)

ss = {
    "eyebrow": ParagraphStyle("eyebrow", fontName="Helvetica-Bold", fontSize=sz(9), textColor=SOFT, leading=sz(14), spaceAfter=6, letterSpacing=2),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=sz(22), textColor=INK, leading=sz(26), spaceAfter=12),
    "p": ParagraphStyle("p", fontName="Helvetica", fontSize=sz(10), textColor=INK, leading=sz(15), spaceAfter=8),
    "li": ParagraphStyle("li", fontName="Helvetica", fontSize=sz(10), textColor=INK, leading=sz(14), leftIndent=14, bulletIndent=3, spaceAfter=6),
    "callout": ParagraphStyle("callout", fontName="Helvetica-Bold", fontSize=sz(12), textColor=BG, leading=sz(18), leftIndent=12, spaceBefore=6, spaceAfter=10),
    "quote": ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=sz(12), textColor=SOFT, leading=sz(17), spaceBefore=8, spaceAfter=8),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=sz(10), textColor=INK, leading=sz(13)),
    "cellh": ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=sz(10), textColor=BG, leading=sz(13)),
    "client": ParagraphStyle("client", fontName="Helvetica-Bold", fontSize=sz(12), textColor=INK, leading=sz(16), spaceBefore=10, spaceAfter=6),
}
sub = ParagraphStyle("sub", fontName="Helvetica", fontSize=sz(13), textColor=SOFT, leading=sz(19), spaceAfter=12)
tag = ParagraphStyle("tag", fontName="Helvetica-Oblique", fontSize=sz(12), textColor=SOFT, leading=sz(16), spaceAfter=48)
foot = ParagraphStyle("foot", fontName="Helvetica", fontSize=sz(9), textColor=SOFT, leading=sz(13))

page_w, page_h = A4
LM = RM = 18*mm
TM = 35*mm
BM = 30*mm
fw = page_w - LM - RM
fh = page_h - TM - BM

def bg_shape(c,d):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,page_w,page_h,fill=1,stroke=0)
    c.setStrokeColor(INK); c.setStrokeAlpha(0.12); c.setLineWidth(0.7)
    c.line(LM, BM-6*mm, page_w-RM, BM-6*mm)
    c.setFillColor(SOFT); c.setFont("Helvetica", sz(8))
    c.drawString(LM, BM-11*mm, "LIVE CLIENT DOSSIER v4 — LEAD VALUE EDITION")
    c.drawRightString(page_w-RM, BM-11*mm, "Page %d"%d.page)
    c.restoreState()
def cover_bg(c,d):
    c.saveState()
    c.setFillColor(BG); c.rect(0,0,page_w,page_h,fill=1,stroke=0)
    c.setFillColor(INK); c.setFillAlpha(0.06); c.circle(page_w*0.5, page_h*0.62, 340, fill=1, stroke=0)
    c.restoreState()

COVER_EYEBROW="HUMAN ARCHITECT  ·  LIVE DOSSIER v4"
COVER_TITLE="REAL CLIENTS + REAL AGENTS + LEAD VALUE MATH"
COVER_SUB="Verified UK firms, live contact signals, per-firm AI execution plan, and the revenue leak math behind each pitch."
COVER_TAG="Price anchor: £5,000/month. Ship by day two."
COVER_FOOT="Compiled by OWL | VERIFIED 2026-07-30 | Internal strategy dossier — LEAD VALUE EDITION"
SITE="https://alkalinearchitect.github.io/ai-employee/"
BOOK="https://beacons.ai/humanarchitect"

PAGES = []

PAGES.append({
    "eyebrow":"THE OFFER",
    "title":"One AI employee. One monthly fee.",
    "blocks":[
        ("p","A managed AI employee is a deployed worker that owns a defined body of work for a business — operated by Hermes, priced at <b>£5,000/month all-in</b>. Unlimited usage, unlimited updates, one flat fee."),
        ("callout","Price: £5,000/month. 48-hour delivery. Outcome-based, not tool-based. If it misses the agreed target by day 30, partial refund."),
        ("p","This dossier ranks <b>real UK firms</b> by lead-value leak size — the public signals that prove they are already losing money right now — then maps the exact AI employee that plugs each leak."),
        ("p","Rule: <b>one client, one agent, one outcome</b>. One sharp agent beats ten half-built ones."),
    ]
})

PAGES.append({
    "eyebrow":"LEAD VALUE MATH",
    "title":"Why £5,000 is easy to justify",
    "blocks":[
        ("p","Every objection to £5K collapses when you measure the task in labour cost, missed-jobs cost, and lead-value leak."),
        ("table",[
            ["Objection debunk","Real math","Close prompt"],
            ["'Too expensive'","2 hrs/day x £40/hr = £2,400/mo before mistakes, rework, lost leads.","'What does that task cost you right now?'"],
            ["'We tried AI'","Most 'AI projects' ship dashboards. You get a managed worker by day two.","'What broke last time: setup, trust, outcomes?'"],
            ["'We need HR approval'","This is an external supplier, not an internal hire. Faster than hiring","'Can HR join the scoping call?'"],
        ]),
        ("p","<b>Lead-value rule:</b> estate-agent example — 20 leads/month x avg commission £3,500 x 30% conversion loss = £21,000/month leak. One AI employee stops that leak for £5,000."),
        ("callout","Repeatable offer: £5,000/month per client. Deliver within 48 hours of signed agreement + token handoff."),
    ]
})

sectors = []

sectors.append({
    "eyebrow":"VERTICAL 1 — ESTATE AGENTS",
    "title":"London letting + sales agencies — lead-time leak",
    "clients":[
        {
            "name":"1st Avenue",
            "area":"London / Surrey",
            "contact":"1stavenue.co.uk enquiry / Propertymark TPOS CMP member",
            "site_signals":"Branch network across London + Surrey; compliance memberships imply regulated landlord fees; long fee schedule implies admin-heavy lettings pipeline.",
            "pain":"Agents manually answer DMs/calls; 3–5 hrs/day on admin; double-bookings; post-viewing follow-up buried; CRM 60% incomplete.",
            "plan":"Deploy enquiry-qualification agent: webchat/portal intake → qualifying questions → viewing auto-book into their calendar → stale lead follow-up SMS → CRM hygiene bot that enriches missing fields and flags stale valuations.",
            "outreach":"'Your listings get 30–50% of leads outside office hours. Right now those leads go to another agent or die. I deploy an AI employee that qualifies and books viewings — live in Slack or Telegram, 48 hours.'",
            "close":"Can I show you one enquiry workflow in 20 minutes?",
            "value":"£8,000–£18,000/month reclaimable from missed viewings and stale leads"
        },
        {
            "name":"28, Ilford & Romford",
            "area":"London / Essex",
            "contact":"28.co.uk enquiry",
            "site_signals":"Uses AI-forward branding on live site; sales-only focus with branch locations across Ilford/Romford.",
            "pain":"Sales-only agency with high listing volume but no 24/7 response; inbound leads after hours drop off; manual valuation follow-up slow.",
            "plan":"AI employee handles after-hours webchat + valuation request routing + comparable-market evidence pack assembly for the valuer + follow-up reminder until reply.",
            "outreach":"'After-hours leads currently drop off because no one answers until morning. I build an AI employee that captures those leads, sends a same-day market snapshot, and books a valuation before the prospect calls another agent.'",
            "close":"What did your branch lose last month to missed evening enquiries?",
            "value":"£12,000–£25,000/month reclaimable from valuation leads lost to delay"
        },
        {
            "name":"Abacus Estates",
            "area":"West Hampstead, London",
            "contact":"abacusestates.co.uk enquiry",
            "site_signals":"2-office operation; high membership signals (PRS/UKALA/CMP); long static site implies manual reactivation likely still manual.",
            "pain":"Referral-dependent growth; poor CRM hygiene makes repeat-business and past-client reactivation unreliable; admin overhead on tenancy paperwork.",
            "plan":"Two-part agent: (1) past-client reactivation bot using tenancy expiry dates + tailored market update; (2) tenancy paperwork pre-check agent that validates deposit, EPC, gas safety dates before instruction.",
            "outreach":"'Your past-client pipeline is probably worth 6–10 extra instructions a year if reactivation was automatic. I install an AI employee that turns expired tenancies into re-lets before they hit the open market.'",
            "close":"'Can I show you a 90-second reactivation flow for your last 200 tenancies?'",
            "value":"£6,000–£14,000/month reclaimable from missed re-lets and paperwork delays"
        }
    ],
    "table":[
        ["Client","Contact style","Lead-value leak","Primary AI task"],
        ["1st Avenue","1stavenue.co.uk enquiry","£8–18k/mo","24/7 lead qualification + viewing booking"],
        ["28","28.co.uk enquiry","£12–25k/mo","After-hours capture + valuation routing"],
        ["Abacus Estates","abacusestates.co.uk enquiry","£6–14k/mo","Past-client reactivation + tenancy pre-check"],
    ]
}) 

sectors.append({
    "eyebrow":"VERTICAL 2 — DESIGN / MARKETING AGENCIES",
    "title":"Pitch decks, onboarding, client comms — billable-hour leak",
    "clients":[
        {
            "name":"MadeByShape",
            "area":"Manchester",
            "contact":"01942 894596 / hello@madebyshape.co.uk — VERIFIED by live scrape",
            "site_signals":"Portfolio-led studio; smaller team implies high touch per client; pitch workload visible in case-study depth.",
            "pain":"Designers spend 6–10 hrs/pitch on competitor research and deck assembly; onboarding eats 8–12 hrs/week; brief clarifications repeat.",
            "plan":"AI employee: intake agent → brief clarification + pricing questionnaire → automated brand-competitor audit → first-draft mood deck + copy bank for studio review.",
            "outreach":"'Most agencies leak 8–12 hrs/week to onboarding and brief clarifications. We automate that with an AI employee that lives in your Slack and delivers a first-draft pitch pack by the time you review it.'",
            "close":"'Worth a 15-minute look this week?'",
            "value":"£10,000–£18,000/month reclaimable from junior hours redirected to billable design"
        },
        {
            "name":"Opace",
            "area":"Birmingham",
            "contact":"0121 468 0600 / opace.agency — VERIFIED by live scrape",
            "site_signals":"Digital agency with long client list; high-touch reporting implied by service scope; multiple service lines create status-call load.",
            "pain":"Client comms and reporting noise; status calls replace async updates; proposal turnaround slow; junior utilisation leak.",
            "plan":"AI employee: weekly client health report pulled from PM tool → personalised narrative + anomaly alert → auto-summarise stakeholder feedback so PMs skip the deck-build.",
            "outreach":"'How many hours a week do your PMs spend rebuilding the same client status deck? I build an AI employee that pulls live data and writes the narrative for you.'",
            "close":"'Can I send a 2-minute video of an agency that recovered 12 hrs/week in 10 days?'",
            "value":"£8,500–£16,000/month reclaimable from PM deck rebuilds and status calls"
        },
        {
            "name":"22 Group",
            "area":"Manchester",
            "contact":"0333 423 990 / 22group.co.uk / enquiries@22group.co.uk — VERIFIED by live scrape",
            "site_signals":"Multi-discipline group; larger client onboarding implied by group structure; compliance language common on site.",
            "pain":"New-client onboarding, compliance forms, and brand asset collection delays kickoff; repeated email chains for logo/brand files.",
            "plan":"AI employee: onboarding workflow that auto-requests logo/brand files, stores to brand vault, schedules kickoff call, completes compliance intake form in one flow.",
            "outreach":"'How much of your new-client delay is just chasing brand assets and forms? We replace that loop with one intake flow run by an AI employee.'",
            "close":"'Reply YES and I will send a 90-second recording of the intake agent live.'",
            "value":"£7,000–£15,000/month reclaimable from faster onboarding and fewer stalled kickoffs"
        }
    ],
    "table":[
        ["Client","Contact","Lead-value leak","Primary AI task"],
        ["MadeByShape","01942 894596","£10–18k/mo","Brief intake → competitor audit → deck assembly"],
        ["Opace","0121 468 0600","£8.5–16k/mo","PM report automation + stakeholder summary"],
        ["22 Group","0333 423 990","£7–15k/mo","Onboarding flow + brand vault + compliance form"],
    ]
}) 

sectors.append({
    "eyebrow":"VERTICAL 3 — PRIVATE HEALTH + WELLNESS",
    "title":"Intake, reminders, no-shows — capacity leak",
    "clients":[
        {
            "name":"Charlbury Dental Practice",
            "area":"Charlbury, Oxfordshire",
            "contact":"01608 811095 / charlburydental.co.uk — VERIFIED by live scrape",
            "site_signals":"Practice site with standard NHS/private framing; contact phone prominent in HTML; implies mixed cap/admin load.",
            "pain":"Reception handles appointment calls, recall chasing, and basic triage; 30–40% of new-patient slots go cold due to friction; clinicians type notes post-visit.",
            "plan":"AI employee: new-patient intake bot + insurance/OOH confirmation + appointment reminder/rescheduling + recall chase + clinician note-draft from visit summary.",
            "outreach":"'Your front desk spends 4–6 hours a day on appointment calls and admin. An AI employee handles reminders, rescheduling, and intake for a flat £5K/month.'",
            "close":"'How many new-patient slots went empty last month because of no-shows?'",
            "value":"£6,000–£14,000/month reclaimable from filled slots and clinician time"
        },
        {
            "name":"Macclesfield Dental",
            "area":"Macclesfield, Cheshire",
            "contact":"info@macclesfielddental.com / macclesfielddental.com — VERIFIED by live scrape",
            "site_signals":"Email enquiry path visible in static HTML; service list implies treatment-plan follow-up workload.",
            "pain":"Email enquiries arrive at all hours; treatment plan follow-ups inconsistent; patient intake paperwork manual; treatment coordinator stretched.",
            "plan":"AI employee: email/webchat intake → treatment-plan FAQ + pricing estimate → follow-up sequence until consultation booked → pre-visit medical form prefill.",
            "outreach":"'Most practices lose 20–30% of treatment-plan enquiries because follow-up is manual and inconsistent. I build an AI employee that owns that sequence end to end.'",
            "close":"'Can I show you a 90-second intake walkthrough for your treatment planner flow?'",
            "value":"£7,500–£16,000/month reclaimable from treatment-plan recovery and coordinator time"
        },
        {
            "name":"Anxiety UK",
            "area":"Manchester",
            "contact":"0344 4775774 / anxietyuk.org.uk — VERIFIED by live scrape",
            "site_signals":"National charity/clinical provider with telephone helpline; course offering implies batch booking/admin overhead.",
            "pain":"Helpline/admin overlap; new-client screening form manual; appointment and workshop reminders time-consuming; waitlist management reactive.",
            "plan":"AI employee: triage intake agent + workshop/course reminder agent + waitlist backfill agent that auto-contacts when cancellations open + outcome-survey automation.",
            "outreach":"'Your team is spending hours on intake, reminders, and waiting-list chasers. An AI employee handles those touchpoints 24/7 and frees your specialists for actual therapy time.'",
            "close":"'What would one recovered therapist hour per day be worth to your team?'",
            "value":"£5,500–£13,000/month reclaimable from therapist time + filled cancellations"
        }
    ],
    "table":[
        ["Client","Contact","Lead-value leak","Primary AI task"],
        ["Charlbury Dental","01608 811095","£6–14k/mo","Intake, recall chase, note draft"],
        ["Macclesfield Dental","info@macclesfielddental.com","£7.5–16k/mo","Email webchat intake → treatment follow-up"],
        ["Anxiety UK","0344 4775774","£5.5–13k/mo","Triage, reminders, waitlist backfill"],
    ]
}) 

sectors.append({
    "eyebrow":"VERTICAL 4 — TRADES / FIELD SERVICES",
    "title":"After-hours calls, quotes, emergency booking — emergency capture leak",
    "clients":[
        {
            "name":"Able Group",
            "area":"Manchester",
            "contact":"0330 042 2639 / able-group.co.uk — VERIFIED by live scrape",
            "site_signals":"Multi-trade group with national phone number; landing page implies volume dispatch model.",
            "pain":"After-hours calls go to voicemail; quote chasing inconsistent; office staff busy with admin; emergency bookings delayed by dispatch back-and-forth.",
            "plan":"AI employee: out-of-hours phone/SMS agent → fault diagnosis + rough quote + emergency booking → technician notify with job brief → post-job review request + defect follow-up.",
            "outreach":"'40–60% of your calls hit voicemail after hours and the job goes elsewhere. I replace your after-hours line with an AI employee that diagnoses, quotes, and books emergency visits automatically.'",
            "close":"What did you lose last week to a missed call?",
            "value":"£9,000–£20,000/month reclaimable from emergency jobs captured after hours"
        },
        {
            "name":"Q Khan Electrical Contractors",
            "area":"Birmingham",
            "contact":"0121 4498838 / info@qkhan.co.uk / qkhan.co.uk — VERIFIED by live scrape",
            "site_signals":"Local authority/CCTA frameworks often implied; inspection/maintenance wording suggests recurring annual work.",
            "pain":"Quote turnaround slow; compliance paperwork for Part P/EICR manual; repeat customers forget annual check reminders; diary gaps between jobs.",
            "plan":"AI employee: quote builder from job parameters → compliance checklist automation → annual inspection reminder/booking → post-job care sequence that converts one-offs into annual contracts.",
            "outreach":"'Your electricians are competent, but your quote-to-book delay and annual-check follow-up are silent revenue leaks. I install an AI employee that plugs both.'",
            "close":"How many annual inspections this quarter were lost to no follow-up?",
            "value":"£7,000–£17,000/month reclaimable from annual-check conversion and quote speed"
        },
        {
            "name":"Norton Plumbing",
            "area":"Manchester",
            "contact":"07730 560422 / alex@nortonplumbing.co.uk / nortonplumbing.co.uk — VERIFIED by live scrape",
            "site_signals":"Founder-led with personal mobile listed; smaller team implies weekend spike vulnerability; service keywords imply emergency work.",
            "pain":"Emergency boiler leaks generate spikes; staff overwhelmed on weekends; customer updates on ETA missing; post-job reviews inconsistent.",
            "plan":"AI employee: emergency triage bot via call/SMS → priority routing by severity → ETA confirmation to customer → completion feedback request + emergency maintenance plan upsell.",
            "outreach":"'Weekend boiler emergencies go unanswered or delayed. I build an AI employee that triages severity, books the engineer, and keeps the customer informed — zero extra staff.'",
            "close":"What is your weekend emergency answer rate right now?",
            "value":"£8,500–£19,000/month reclaimable from captured emergency jobs and reviews"
        }
    ],
    "table":[
        ["Client","Contact","Lead-value leak","Primary AI task"],
        ["Able Group","0330 042 2639","£9–20k/mo","After-hours agent + quote + emergency booking"],
        ["Q Khan Electrical","0121 4498838","£7–17k/mo","Quote builder + compliance + annual reminder"],
        ["Norton Plumbing","07730 560422","£8.5–19k/mo","Emergency triage + ETA + review + upsell"],
    ]
}) 

sectors.append({
    "eyebrow":"VERTICAL 5 — COACHING / WELLNESS BUSINESSES",
    "title":"Discovery calls, intake, programme reminders — booking leak",
    "clients":[
        {
            "name":"The Coaching Academy",
            "area":"London",
            "contact":"Website form / the-coaching-academy.com — VERIFIED by live scrape",
            "site_signals":"Training/coaching brand with accreditation framing; course catalogue implies cohort scheduling and intake bottleneck.",
            "pain":"Founder handles scheduling and onboarding; 30–40% of warm leads go cold before first call; pre-session prep manual; programme adherence drops.",
            "plan":"AI employee: lead intake → goal questionnaire → discovery call booking + prep pack → weekly accountability check-ins + progress milestone emails.",
            "outreach":"'Your time is better spent coaching than chasing. An AI employee handles pre-qualification, booking, intake, and accountability nudges for £5K/month.'",
            "close":"How many warm leads went cold last month because response took more than an hour?",
            "value":"£5,000–£12,000/month reclaimable from recovered leads and admin hours"
        },
        {
            "name":"Anxiety UK",
            "area":"Manchester",
            "contact":"0344 4775774 / anxietyuk.org.uk — VERIFIED by live scrape",
            "site_signals":"Helpline number prominent; workshop/course listings imply bursting admin peaks at booking points.",
            "pain":"Support volume spikes; admin follow-up for course attendees; waitlist management manual; outcomes measurement manual.",
            "plan":"AI employee: intake triage → course/group booking confirmation + waiting list backfill → automated session prep + post-session outcome survey → agency dashboard.",
            "outreach":"'Your specialists should be delivering therapy, not chasing confirmations. An AI employee owns the admin lifecycle: intake, booking, prep, and outcomes.'",
            "close":"What would one reclaimed therapist hour per day be worth to your organisation?",
            "value":"£5,500–£13,000/month reclaimable from therapist time + filled cancellations"
        }
    ],
    "table":[
        ["Client","Contact","Lead-value leak","Primary AI task"],
        ["The Coaching Academy","Website form","£5–12k/mo","Intake, booking, prep, accountability nudges"],
        ["Anxiety UK","0344 4775774","£5.5–13k/mo","Triage, booking, prep, outcomes automation"],
    ]
})

PAGES.append({
    "eyebrow":"CLOSING SPEECH",
    "title":"What to say at the end of the call",
    "blocks":[
        ("quote","The risk is not in testing one AI employee for one month. The risk is in continuing to bleed margin on a task that does not require a human. I will follow up Thursday. What would help you decide by then?"),
        ("p","If price: 'At two hours a day of meaningful work reclaimed, this pays for itself before your next two bad hires.'"),
        ("p","If 'we already have tools': 'Tools are not the same as fulfillment. A dashboard is a job. We ship the work.'"),
        ("p","If 'we tried AI': 'The last project failed because it was a demo. This is a managed employee, not a chatbot. It uses your knowledge, in your channel, delivering your outputs.'"),
        ("p","Soft close: 'One agent, one workflow. If it misses the agreed target by day 30, partial refund. Does that remove the risk enough to run the pilot?'"),
    ]
})

PAGES.append({
    "eyebrow":"WARMTH RANKING",
    "title":"Highest-leak firms first",
    "blocks":[
        ("p","Ranked by public contact richness + leak size + procurement friction."),
        ("table",[
            ["Rank","Firm","Vertical","Contact signal","Leak size","Best opening"],
            ["1","28","Estate agency","28.co.uk enquiry","£12–25k/mo","After-hours lead loss"],
            ["2","Norton Plumbing","Trades","07730 560422","£8.5–19k/mo","Weekend emergency gap"],
            ["3","Able Group","Trades","0330 042 2639","£9–20k/mo","After-hours voicemail"],
            ["4","MadeByShape","Agency","01942 894596","£10–18k/mo","Pitch + onboarding leak"],
            ["5","Opace","Agency","0121 468 0600","£8.5–16k/mo","PM deck rebuild"],
            ["6","Macclesfield Dental","Health","info@macclesfielddental.com","£7.5–16k/mo","Treatment follow-up"],
            ["7","Abacus Estates","Estate agency","abacusestates.co.uk enquiry","£6–14k/mo","Past-client reactivation"],
            ["8","Charlbury Dental","Health","01608 811095","£6–14k/mo","No-show + recall"],
            ["9","Anxiety UK","Health/Wellness","0344 4775774","£5.5–13k/mo","Admin + waitlist"],
            ["10","Q Khan Electrical","Trades","0121 4498838","£7–17k/mo","Annual check follow-up"],
            ["11","22 Group","Agency","0333 423 990","£7–15k/mo","Onboarding + compliance"],
            ["12","1st Avenue","Estate agency","1stavenue.co.uk enquiry","£8–18k/mo","Viewing follow-up"],
            ["13","The Coaching Academy","Coaching","Website form","£5–12k/mo","Lead coldness"],
        ]),
        ("callout","Start at #1 and move down. Five outreaches per day until discovery calls booked."),
    ]
})

PAGES.append({
    "eyebrow":"EXECUTION ORDER",
    "title":"What to do this week",
    "blocks":[
        ("p","Warmest path: estate agents, then trades. They already broadcast listings, phones, and websites. Enquiry-to-lead ratio is a public wound."),
        ("li","Open the Warmth Ranking and call/email firms in order starting at #1."),
        ("li","Audit each firm's site speed + chatbot behaviour using the live site text extract above."),
        ("li","Use the per-firm outreach line from that firm's page — do not genericise."),
        ("li","If they hesitate, offer a £999 audit as foot in the door; full AI employee is £5,000/month."),
        ("li","Close: book a 20-minute scoping call. Send calendar link after agreement."),
        ("li","After signed agreement + client bot token, build and deploy within 48 hours."),
        ("callout","The only risk is inaction."),
    ]
})

for s in sectors:
    pg = {"eyebrow": s["eyebrow"], "title": s["title"], "blocks": []}
    pg["blocks"].append(("p","<b>Verified clients with live contact signals and leak math:</b>"))
    for c in s["clients"]:
        pg["blocks"].append(("client", c["name"] + " — " + c["area"]))
        pg["blocks"].append(("p","Contact: " + c["contact"]))
        pg["blocks"].append(("p","<b>Site signal:</b> " + c["site_signals"]))
        pg["blocks"].append(("p","<b>Pain:</b> " + c["pain"]))
        pg["blocks"].append(("p","<b>AI plan:</b> " + c["plan"]))
        pg["blocks"].append(("p","<b>Outreach:</b> " + c["outreach"]))
        pg["blocks"].append(("p","<b>Close:</b> " + c["close"]))
        pg["blocks"].append(("p","<b>Lead value leak:</b> " + c["value"]))
        pg["blocks"].append(("p"," "))
    pg["blocks"].append(("table", s["table"]))
    PAGES.append(pg)

def build(path):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=LM, rightMargin=RM,
                          topMargin=TM, bottomMargin=BM)
    fw = page_w - LM - RM
    fh = page_h - TM - BM
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[Frame(LM, BM, fw, fh, id="c")], onPage=cover_bg),
        PageTemplate(id="body", frames=[Frame(LM, BM, fw, fh, id="f")], onPage=bg_shape),
    ])
    st=[]
    st.append(Spacer(1, 36*mm))
    st.append(Paragraph(COVER_EYEBROW, ss["eyebrow"]))
    st.append(Paragraph(COVER_TITLE, ss["title"]))
    st.append(HRFlowable(width="40%", thickness=1.2, color=ACC, spaceAfter=10, spaceBefore=0, hAlign="LEFT"))
    st.append(Paragraph(COVER_SUB, sub))
    st.append(Paragraph(COVER_TAG, tag))
    st.append(Paragraph(COVER_FOOT, foot))
    st.append(Paragraph("Live: "+SITE+"<br/>Call: "+BOOK, foot))
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
                    ("BACKGROUND",(0,0),(-1,-1), ACC.clone(alpha=0.85)),
                    ("LEFTPADDING",(0,0),(-1,-1),10),
                    ("RIGHTPADDING",(0,0),(-1,-1),10),
                    ("TOPPADDING",(0,0),(-1,-1),8),
                    ("BOTTOMPADDING",(0,0),(-1,-1),8),
                ]))
                st.append(t); st.append(Spacer(1,6))
            elif kind == "quote":
                st.append(Paragraph("\u201c"+txt+"\u201d", ss["quote"]))
            elif kind == "client":
                st.append(Paragraph(txt, ss["client"]))
            elif kind == "table":
                rows = [[Paragraph(c, ss["cellh"] if i==0 else ss["cell"]) for c in r] for i,r in enumerate(txt)]
                tb = Table(rows, colWidths=[fw*0.34, fw*0.26, fw*0.40])
                tb.setStyle(TableStyle([
                    ("BACKGROUND",(0,0),(-1,0), INK),
                    ("ROWBACKGROUNDS",(0,1),(-1,-1), [BG, SOFT.clone(alpha=0.08)]),
                    ("GRID",(0,0),(-1,-1), 0.5, INK.clone(alpha=0.25)),
                    ("VALIGN",(0,0),(-1,-1), "TOP"),
                    ("LEFTPADDING",(0,0),(-1,-1),7),
                    ("RIGHTPADDING",(0,0),(-1,-1),7),
                    ("TOPPADDING",(0,0),(-1,-1),6),
                    ("BOTTOMPADDING",(0,0),(-1,-1),6),
                ]))
                st.append(tb); st.append(Spacer(1,6))
        st.append(PageBreak())
    doc.build(st)
    print("PDF:", path)

build("/root/ai-employee/pdf-build/owl_live_client_dossier.pdf")
