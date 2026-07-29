SITE="https://alkalinearchitect.github.io/ai-employee/"
BOOK="https://beacons.ai/humanarchitect"
SUB="https://substack.com/@humanarchitect"

COVER={
 "eyebrow":"HUMAN ARCHITECT  ·  OWL DOSSIER",
 "title":"THE FULFILLMENT LAYER",
 "sub":"The managed-AI-employee playbook for UK operators. Model, methodology, objections, case studies, and adoption-ready use cases.",
 "tag":"Sell an outcome, not a tool. Charge rent on the loop.",
 "foot":"Compiled by OWL | VERIFIED 2026-07-29 | Internal strategy dossier",
}
PAGES=[]

# --- 1 ---
PAGES.append({"n":2,"eyebrow":"THE MODEL","title":"What a managed AI employee is",
 "blocks":[
  ("p","A managed AI employee is a deployed AI worker that owns a defined body of work for your business — operated by you, not by the client — for one flat monthly fee. **The client pays to receive an outcome, not to own a tool they have to figure out.**"),
  ("callout","Price: £5,000 per client, per month. Includes: unlimited agents, unlimited usage, unlimited updates. Managed end-to-end. If it breaks, you fix it fast."),
  ("p","Nick Vasilescu runs this model publicly. Corey Ganim verified it and copied it. Market is early. Margin is ~90%. The moat is not the model — it is the fulfillment layer."),
  ("quote","The agent is leverage. You are still the architect."),
 ]})

# --- 2 ---
PAGES.append({"n":3,"eyebrow":"THE ACQUISITION FUNNEL","title":"How to close £5k/mo clients",
 "blocks":[
  ("li","<b>1 · Foot in the door:</b> lead with a £999 AI audit. Cold prospects say no to £5k. The audit pays you to learn their business AND surfaces the exact pain to solve."),
  ("li","<b>2 · Pick ONE specialised agent</b> from the audit — the one with the most obvious ROI. One sharp agent beats ten half-built ones."),
  ("li","<b>3 · Price £5,000/mo, all-in.</b> Unlimited usage, unlimited updates, fully managed."),
  ("li","<b>4 · Ship by day two.</b> Same-day or next-day delivery changes the entire sales dynamic."),
  ("li","<b>5 · B2B2B retention:</b> help the client resell the agent to THEIR customers — churn dies."),
  ("callout","Speed-to-value rule: the same day a client wires money, ship them something. Agent live by day two."),
 ]})

# --- 3 ---
PAGES.append({"n":4,"eyebrow":"THE MATH","title":"Why the margin is ~90%",
 "blocks":[
  ("p","10 clients × £5,000 = <b>£50,000/month recurring.</b>"),
  ("p","Overhead per client ≈ workspace costs plus modest compute. Self-hosted keeps this tiny."),
  ("callout","Key insight: almost no client needs an army of agents — they need one or two very specialised ones. That is why \"unlimited\" is safe to promise."),
  ("quote","Build once. Fulfill forever. Charge rent on the loop."),
 ]})

# --- 4 ---
PAGES.append({"n":5,"eyebrow":"THE 8-PART FRAMEWORK","title":"What every AI employee needs",
 "blocks":[
  ("li","<b>1. Computer</b> — isolated env: VPS/container per client"),
  ("li","<b>2. Email</b> — real inbox the agent can send/receive"),
  ("li","<b>3. Phone/IM</b> — Telegram/Slack (client-facing)"),
  ("li","<b>4. Comms channel</b> — where the client talks to it"),
  ("li","<b>5. Tools/connectors</b> — skills + terminal/file/web"),
  ("li","<b>6. Card/payment</b> — client billing + agent spend rails"),
  ("li","<b>7. Knowledge base</b> — markdown \"one fact, one home\""),
  ("li","<b>8. Observability</b> — health checks + Telegram alerts"),
  ("callout","Miss one and it is a toy, not a worker."),
 ]})

# --- 5 ---
PAGES.append({"n":6,"eyebrow":"THE ARCHITECTURE","title":"Orchestrator + Swarm",
 "blocks":[
  ("p","One orchestrator handles the client relationship. Specialised sub-agents execute: outbound, sales follow-up, content, support."),
  ("p","Why split? <b>Minimise blast radius.</b> One broken sub-agent must never take down the others."),
  ("callout","Rule: never tell the client \"the agent builds itself.\" Say: \"I have a build system. You get the agent by Friday.\""),
  ("p","Repeatable delivery: <b>Build → Onboard → Fulfill → Pay.</b> Hands-off every month."),
 ]})

# --- 6 ---
PAGES.append({"n":7,"eyebrow":"KNOWLEDGE FIRST","title":"Lead with the KB, not the bot",
 "blocks":[
  ("p","Before any agent is useful it needs a governed knowledge base. This is the step most operators skip. Don't."),
  ("li","Organised by function: Company / Customers / Offers / Sales / Ops / Finance."),
  ("li","Every fact carries provenance, owner, sensitivity, review date."),
  ("li","Protected tier for credentials; agents get scoped boundaries."),
  ("li","Pipeline: raw inputs → wiki → outputs. Maintenance is part of the product."),
  ("callout","A governed KB is one of the few moats left in the AI age. Sell it as a service for £5k+."),
 ]})

# --- 7 use cases ---
PAGES.append({"n":8,"eyebrow":"USE CASES","title":"Adoption-ready client use cases",
 "blocks":[
  ("p","Real-world use cases mapped to client language and outcome metrics. Each is a standalone conversation starter on a discovery call."),
  ("callout","Rule: pick ONE agent per client. One sharp agent beats ten half-built ones."),
  ("table",[
    ["Sector","Exact AI task","Manual pain","Outcome","Monthly value"],
    ["Design agency","Pitch deck + brand research + mood board from brief","Designers spend 6–10 hrs/pitch scanning assets and assembling slides","60–75% faster pitch turnaround","£2,800–£4,500"],
    ["Real estate","24/7 lead qualification + auto-booking viewings + agent handoff","Agents manually answer DMs; low-quality leads waste 3–5 hrs/day; double-bookings","80%+ leads qualified/booked; no-shows cut 30%","£3,200–£5,500"],
    ["Private clinic","AI scribe: transcribes consultations, drafts notes, files to records","Clinicians spend 1.5–2 hrs/day typing notes; burnout","Notes in real time; review cut from 90 mins to <15 mins","£3,000–£5,000"],
    ["Coaching / wellness","Intake agent: pre-qualifies, books discovery calls, intake forms + reminders","Owner handles all scheduling; 30–40% leads go cold before first call","Booking rate lifts 35–55%; admin drops 10–15 hrs/week","£1,800–£3,500"],
    ["Trades","After-hours phone/SMS agent: diagnostics, quotes, books emergency visits","40–60% of callers hit voicemail after hours; lost jobs","60–80% jobs booked without a human; out-of-hours capture 3×","£2,500–£4,500"],
    ["Professional services","Document-review agent: reads contracts/invoices, flags anomalies, drafts summaries","Associates spend 40–60% of billable hours on prep; rework from errors","First-pass review cut 70–85%; 10–15 hrs/week to advisory","£4,500–£7,500"],
    ["B2B SaaS","Support + CSM agent: tier-1 onboarding, setup walkthroughs, escalation routing","Tickets pile up after launches; CSMs buried; NPS drops","First response <90 sec; 50–65% tickets resolved without human","£2,500–£5,000"],
    ["E-commerce","Customer-service + returns handler: answers queries, processes returns, upsells","CS team drowned in order-status/return tickets; abandoned carts","60–75% tickets solved without human; AOV lifts 5–12%","£1,800–£3,500"],
    ["Logistics","Dispatch + exception agent: auto-assigns drivers, optimises routes, delay alerts","Dispatcher spends all day on rider queries; routing by gut feel; late SLA","Route density +15–25%; failed-delivery rate -20–35%","£3,000–£5,500"],
    ["Property management","Tenant-support agent: answers tenancy questions, logs maintenance, routes contractors","20–40 calls/emails/day per manager; emergency delays; compliance stacks","55–70% tenant queries self-serve; emergency SLA from 4 hrs to 1 hr","£2,800–£4,500"],
    ["All sectors","HR agent: policy answers, holiday/OOO tracking, offer/exit letters, compliance","Founder interrupted constantly with policy/admin work; clunky processes","HR admin cut 60–75%; answers instant; compliance risk reduced","£1,500–£2,800"],
    ["IFA / Accountancy","Client-intake + KYC agent: fact-find, Open Banking pull, client folders, gap alerts","3–6 hrs per new client on admin, paperwork, chasing docs","Onboarding from 2 days to same-day; missing-doc turnaround hours not days","£2,500–£4,000"],
    ["Performance marketing","Reporting agent: pulls Ads/GA4/social APIs, writes narrative reports, anomaly alerts","Account managers spend 6–10 hrs/week on decks; client calls become screenshares","Reporting time cut 80%; calls reallocated to strategy","£2,200–£4,000"],
    ["Recruitment / staffing","CV screen + candidate-engagement agent: ranks applicants, books interviews, chases feedback","Recruiters spend 60% time reading CVs/admin; candidate ghosting rises","Time-to-shortlist cut 70%; response rate +30–40%","£2,000–£4,000"],
    ["Tech consultancy","Project assistant: status from Jira/Notion, client updates, blocker flags, rebalance","PM spends half the day chasing updates, writing recaps, rescheduling meetings","Status-report time drops 85%; blockers surfaced in hours","£2,000–£3,800"],
  ]),
 ]})

PAGES.append({"n":9,"eyebrow":"ADOPTION SIGNALS","title":"What the research says",
 "blocks":[
  ("p","UK SMB automation research points to fast payback when the AI owns a defined outcome rather than acting as a chatbot."),
  ("li","UK SMBs report saving £500–£2,000/month per focused automation (Insightful AI UK, 57% adoption rate)."),
  ("li","Professional-services ROI runs 280–370%, with 8–12-month payback (Samyotech, Forrester via Microsoft)."),
  ("li","Trade/logistics automation typically pays for itself within 2–4 months by preventing one missed job or failed delivery per week."),
  ("callout","The common failure mode is shipping a dashboard, not an employee. Outcome ownership is the differentiator."),
 ]})

# --- objections page shifts to 10 ---
PAGES.append({"n":10,"eyebrow":"OBJECTIONS","title":"12 objections + handlers",
 "blocks":[
  ("p","Objections are requests for reassurance, not rejection. Acknowledge, reframe, close."),
  ("table",[
    ["Objection","Handler","Close prompt"],
    ["£5,000 is too expensive","If the task takes 2 hours daily at £40/hr, it costs £2,400/month before mistakes. Owl pays for itself before your first two bad hires.","What does that task cost you right now?"],
    ["We don't do AI here","Most clients said the same. The agent lives in Slack. You don't touch code. You just watch the work get done.","Can we show you one workflow in 20 minutes?"],
    ["We already have tools","Tools are not the same as fulfillment. A dashboard is a job. Owl ships the work.","What task is still manual even though you have tools?"],
    ["We tried AI before","Most AI projects fail because they ship a toy, not a worker. Owl is managed execution, not a demo.","What broke last time — setup, trust, or outcomes?"],
    ["We're too small","SMBs at £1M–£2M+ pay faster and ask fewer questions. They value outcomes over novelty.","What task costs you 2+ hours every single day?"],
    ["We need custom","Every agent is custom by default — built from your knowledge, your workflow, your outputs.","Can we scope exactly one role in the next call?"],
    ["It will replace people","It replaces the manual work nobody wants to do. Your team moves to higher-value work.","What would your team do with 10 hours back this week?"],
    ["We need to test first","I agree. Start with one agent, one workflow. If it misses the target by day 30, partial refund.","What is the one task you would test first?"],
    ["Our data is sensitive","Your data stays within your environment. Controlled scope, not blanket access.","Do you have a data policy we should align with?"],
    ["We need HR approval","Good — HR protects the business. This is an external supplier system, not an internal hire.","Can HR join the scoping call?"],
    ["It's not a priority right now","That is usually because one painful task is stealing margin and attention.","What task would free you up to focus on growth?"],
    ["We need to think about it","The only risk is inaction. Margin bleeds while you wait. I will follow up Thursday. Does that work?","What would help you decide by Thursday?"],
  ]),
 ]})

# --- 8 objections ---
PAGES.append({"n":9,"eyebrow":"OBJECTIONS","title":"12 objections + handlers",
 "blocks":[
  ("p","Objections are requests for reassurance, not rejection. Acknowledge, reframe, close."),
  ("table",[
    ["Objection","Handler","Close prompt"],
    ["£5,000 is too expensive","If the task takes 2 hours daily at £40/hr, it costs £2,400/month before mistakes. Owl pays for itself before your first two bad hires.","What does that task cost you right now?"],
    ["We don't do AI here","Most clients said the same. The agent lives in Slack. You don't touch code. You just watch the work get done.","Can we show you one workflow in 20 minutes?"],
    ["We already have tools","Tools are not the same as fulfillment. A dashboard is a job. Owl ships the work.","What task is still manual even though you have tools?"],
    ["We tried AI before","Most AI projects fail because they ship a toy, not a worker. Owl is managed execution, not a demo.","What broke last time — setup, trust, or outcomes?"],
    ["We're too small","SMBs at £1M–£2M+ pay faster and ask fewer questions. They value outcomes over novelty.","What task costs you 2+ hours every single day?"],
    ["We need custom","Every agent is custom by default — built from your knowledge, your workflow, your outputs.","Can we scope exactly one role in the next call?"],
    ["It will replace people","It replaces the manual work nobody wants to do. Your team moves to higher-value work.","What would your team do with 10 hours back this week?"],
    ["We need to test first","I agree. Start with one agent, one workflow. If it misses the target by day 30, partial refund.","What is the one task you would test first?"],
    ["Our data is sensitive","Your data stays within your environment. Controlled scope, not blanket access.","Do you have a data policy we should align with?"],
    ["We need HR approval","Good — HR protects the business. This is an external supplier system, not an internal hire.","Can HR join the scoping call?"],
    ["It's not a priority right now","That is usually because one painful task is stealing margin and attention.","What task would free you up to focus on growth?"],
    ["We need to think about it","The only risk is inaction. Margin bleeds while you wait. I will follow up Thursday. Does that work?","What would help you decide by Thursday?"],
  ]),
 ]})

# --- 9 proof ---
PAGES.append({"n":10,"eyebrow":"PROOF POINTS","title":"Verifiable case studies + quotes",
 "blocks":[
  ("p","Publicly verifiable operators running managed AI employee / AI employee-for-hire models, with exact quotes."),
  ("table",[
    ["Source","Claim","Context"],
    ["Nick Vasilescu / Corey Ganim newsletter","$5K/mo + fulfillment model","Also confirmed on Build With AI podcast Jul 27 2026; Nick's verified reply: 'thanks for having me on again Corey'"],
    ["Nick Vasilescu / YouTube (BI-MNjm1tTQ)","Solo operator, managed agents","Demonstrates Dewey build + client deployment walkthrough"],
    ["Linara Bozieva / Business Insider","27 agents, 5 clients, ~2 hrs/week oversight","Launched after eBay layoff; could scale to 20–25 clients solo; costs under $1,000/month"],
    ["Corey Ganim / newsletter (corey-ganim.kit.com)","'10 clients, £50k/month, one person'","Explicit 90% margin math; overhead ~£200 Codex + Orgo workspace per client"],
    ["Corey Ganim / X post Jun 18 2026","Quantified $5K retainer justification","'if your time is worth £250/hr and admin is 5 hrs/week, that's £5,000/month you'll buy back'"],
    ["Boon Media / case studies","Barber: no-shows 18%→4%; SaaS reply 0.8%→6.2%; freight: quote response 45min→5min","Hard metrics from live case-study page"],
    ["Rebotify / case studies","Energy retailer: drafts days→<1 hr; higher ed: 24hr→1min response; telco: 60–70% automated containment","Enterprise AI employee deployments with public outcomes"],
    ["Agentive.au","Junior-accountant price benchmark + 24hr deployment","'A junior accountant costs £5,000/month minimum... Deploy in 24 hours... Available 24/7'"],
    ["Skool / Agent Empire","1.4k members","Free course on building/selling managed agents"],
  ]),
  ("callout","No standalone Nick post with the exact '$5k/mo fulfillment' phrase was found unauthenticated. The quote originates from Corey's recap thread + podcast. Attribute it right."),
 ]})

# --- 10 stack ---
PAGES.append({"n":11,"eyebrow":"THE STACK","title":"Your edge: self-hosted",
 "blocks":[
  ("p","Nick's reference stack is paid. T already owns the free equivalents on this VPS. Same result, higher margin, total control."),
  ("table",[
    ["Part","Nick pays","T owns free"],
    ["Computer","Orgo","This VPS, 24/7"],
    ["Harness","OpenClaw/Hermes","Hermes Agent"],
    ["Email","agentmail.to","Domain alias"],
    ["IM","agentphone.ai","Telegram gateway"],
    ["Tools","Composio","Hermes skills + native tools"],
    ["Knowledge","fresh vault","~/vault (Obsidian)"],
    ["Watch","latitude.so","cron → Telegram"],
  ]),
  ("callout","Never adopt the paid stack unless T approves a specific upgrade."),
 ]})

# --- 11 checklist ---
PAGES.append({"n":12,"eyebrow":"LAUNCH CHECKLIST","title":"Owl execution checklist",
 "blocks":[
  ("li","Foot in the door: offer £999 audit first."),
  ("li","Audit → pick ONE high-ROI agent per client."),
  ("li","Close at £5,000/mo all-in. Agent LIVE BY DAY TWO."),
  ("li","Target SMBs at £1M–£2M+ revenue."),
  ("li","B2B2B retention: help client resell to THEIR customers."),
  ("li","Self-hosted stack; keep overhead ~£200/mo or less."),
  ("li","Template knowledge layer: clients/<name>/context.md + discovery-call transcript."),
  ("li","Bonus: sell the AI Second Brain KB service for £5k."),
  ("li","Keep Dewey/Owl income SEPARATE from HumanitAI CIC."),
  ("li","Teach the model publicly on Substack/X to pull leads."),
 ]})
