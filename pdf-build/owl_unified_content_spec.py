"""
owl_unified_content_spec.py
============================
Canonical data model for the Human Architect AI-employee offer PDFs:
  • owl_dossier.pdf       (portrait dossier)
  • owl_brochure.pdf      (portrait brochure)
  • owl_sales_manual.pdf  (portrait sales manual)
  • owl_pitchdeck.pdf     (landscape pitch deck)

Style canon: black/white premium.
"""

# --------------------------------------------------------------------------- #
# 1. SHARED IDENTITY                                                          #
# --------------------------------------------------------------------------- #
URLS = {
    "SITE": "https://alkalinearchitect.github.io/ai-employee/",
    "BOOK": "https://beacons.ai/humanarchitect",
    "SUB":  "https://substack.com/@humanarchitect",
}

# --------------------------------------------------------------------------- #
# 2. VERBATIM STRONG BLOCKS                                                    #
# --------------------------------------------------------------------------- #
STRONG_BLOCKS = {
    "tagline": "Sell an outcome, not a tool. Charge rent on the loop.",
    "model_definition": (
        "A managed AI employee is a deployed AI worker that owns a defined body of work "
        "for your business — operated by you, not by the client — for one flat monthly fee. "
        "The client pays to receive an outcome, not to own a tool they have to figure out."
    ),
    "price_block": (
        "£5,000 per client, per month. Includes: unlimited agents, unlimited usage, "
        "unlimited updates. Managed end-to-end. If it breaks, you fix it fast."
    ),
    "refund_guarantee": "If the agent misses the agreed target by day 30, partial refund.",
    "delivery_speed": "Ship by day two. Same-day or next-day delivery changes the entire sales dynamic.",
    "one_agent_rule": "One sharp agent beats ten half-built ones.",
    "quote_fulfillment": "Build once. Fulfill forever. Charge rent on the loop.",
    "quote_leverage": "The agent is leverage. You are still the architect.",
    "quote_manual": "You brief. The agent delivers. The client keeps their result.",
    "quote_close": (
        "The risk is not testing one AI employee for one month. The risk is continuing to "
        "bleed margin on a task that does not require a human."
    ),
    "quote_first_mover": "First movers with a real fulfillment layer own the category.",
    "km_quote": (
        "A governed knowledge base is one of the few moats left in the AI age. "
        "Sell it as a service for £5k+."
    ),
    "rule_no_automated": (
        "If the client ever hears the term 'automated' as a reason to trust you less, "
        "you are describing the agent badly. Say 'managed system' or 'delivery layer'."
    ),
    "rule_burden_first": (
        "The client does not buy AI. They buy a removed burden. "
        "Lead with the burden, not the technology."
    ),
    "billboard_callout": (
        "Most operators have AI. Almost none have an agent that ships. "
        "The tool sits idle while you do the delivery by hand — and margin bleeds out "
        "every single week."
    ),
    "b2b2b_callout": "Do not sell an AI employee. Sell a margin loop they can resell.",
    "close_prompt_too_expensive": "What does that task cost you right now?",
    "close_prompt_tried_ai": "What broke last time — setup, trust, or outcomes?",
    "close_prompt_hr": "Can HR join the scoping call?",
    "close_prompt_no_ai": "Can we show you one workflow in 20 minutes?",
    "close_prompt_tools": "What task is still manual even though you have tools?",
    "close_prompt_custom": "Can we scope exactly one role in the next call?",
    "close_prompt_replace": "What would your team do with 10 hours back this week?",
    "close_prompt_test": "What is the one task you would test first?",
    "close_prompt_data": "Do you have a data policy we should align with?",
    "close_prompt_priority": "What task would free you up to focus on growth?",
    "close_prompt_think": "What would help you decide by Thursday?",
    "close_prompt_small": "What task costs you 2+ hours every single day?",
    "proof_nick_corey": (
        "Nick Vasilescu / Corey Ganim newsletter: $5K/mo + fulfillment model. "
        "Also confirmed on Build With AI podcast Jul 27 2026."
    ),
    "proof_corey_quote": (
        "Corey Ganim / X post Jun 18 2026: 'if your time is worth £250/hr and admin is "
        "5 hrs/week, that's £5,000/month you'll buy back'"
    ),
    "proof_boon": (
        "Boon Media / case studies: Barber no-shows 18%→4%; SaaS reply 0.8%→6.2%; "
        "freight quote response 45min→5min."
    ),
    "proof_rebotify": (
        "Rebotify / case studies: Energy retailer drafts days→<1 hr; higher ed 24hr→1min "
        "response; telco 60–70% automated containment."
    ),
    "proof_agentive": (
        "Agentive.au: 'A junior accountant costs £5,000/month minimum... Deploy in 24 "
        "hours... Available 24/7'"
    ),
    "proof_linara": "Linara Bozieva / Business Insider: 27 agents, 5 clients, ~2 hrs/week oversight.",
}

# --------------------------------------------------------------------------- #
# 3. TABLES — canonical schemas                                                #
# --------------------------------------------------------------------------- #

LEAD_MATH_TABLE = {
    "headers": ["Objection", "Real math", "Close prompt"],
    "rows": [
        [
            "£5,000 is too expensive",
            "2 hrs/day x £40/hr = £2,400/mo before mistakes, rework, lost leads.",
            STRONG_BLOCKS["close_prompt_too_expensive"],
        ],
        [
            "We tried AI before",
            "Most 'AI projects' ship dashboards. You get a managed worker by day two.",
            STRONG_BLOCKS["close_prompt_tried_ai"],
        ],
        [
            "We need HR approval",
            "This is an external supplier, not an internal hire. Faster than hiring.",
            STRONG_BLOCKS["close_prompt_hr"],
        ],
    ],
}

PROOF_POINTS_TABLE = {
    "headers": ["Source", "Claim", "Context", "Date"],
    "rows": [
        [
            "Nick Vasilescu / Corey Ganim newsletter",
            "$5K/mo + fulfillment model",
            "Confirmed on Build With AI podcast Jul 27 2026; Nick's verified reply",
            "Jul 2026",
        ],
        [
            "Corey Ganim / X post Jun 18 2026",
            "Quantified $5K retainer justification",
            "'if your time is worth £250/hr and admin is 5 hrs/week, that's £5,000/month'",
            "Jun 2026",
        ],
        [
            "Linara Bozieva / Business Insider",
            "27 agents, 5 clients, ~2 hrs/week oversight",
            "Launched after eBay layoff; could scale to 20–25 clients solo",
            "2026",
        ],
        [
            "Boon Media / case studies",
            "Barber no-shows 18%→4%; SaaS reply 0.8%→6.2%; freight quote 45min→5min",
            "Live case-study page with hard metrics",
            "Live",
        ],
        [
            "Rebotify / case studies",
            "Energy retailer drafts days→<1 hr; higher ed 24hr→1min; telco 60–70% containment",
            "Enterprise AI employee deployments with public outcomes",
            "Live",
        ],
        [
            "Agentive.au",
            "Junior-accountant price benchmark + 24hr deployment",
            "'A junior accountant costs £5,000/month minimum... Deploy in 24 hours'",
            "Live",
        ],
        [
            "Skool / Agent Empire",
            "1.4k members",
            "Free course on building/selling managed agents",
            "Live",
        ],
    ],
}

OBJECTIONS_TABLE = {
    "headers": ["Objection", "Acknowledge", "Handler", "Close"],
    "rows": [
        [
            "£5,000 is too expensive",
            "It feels steep if you compare it to a seat.",
            "This is a managed employee on a flat fee, not a tool. "
            "If the task costs £2,400/month in human hours, this pays for itself before your first two bad hires.",
            STRONG_BLOCKS["close_prompt_too_expensive"],
        ],
        [
            "We don't do AI here",
            "Most clients said the same.",
            "The agent lives in Slack. You don't touch code. You watch the work get done.",
            STRONG_BLOCKS["close_prompt_no_ai"],
        ],
        [
            "We already have tools",
            "Tools are not fulfillment.",
            "A dashboard still needs someone to do the work. Owl ships the outcome.",
            STRONG_BLOCKS["close_prompt_tools"],
        ],
        [
            "We tried AI before",
            "Past failure is useful data.",
            "Most AI projects fail because they ship a toy, not a worker. We ship managed execution.",
            STRONG_BLOCKS["close_prompt_tried_ai"],
        ],
        [
            "We're too small",
            "Size is relative to pain.",
            "SMBs at £1M–£2M+ pay faster and ask fewer questions. They value outcomes over novelty.",
            STRONG_BLOCKS["close_prompt_small"],
        ],
        [
            "We need custom",
            "Custom is expected.",
            "Every agent is custom by default — built from your knowledge, workflow, outputs.",
            STRONG_BLOCKS["close_prompt_custom"],
        ],
        [
            "It will replace people",
            "Workforce fear is real.",
            "It replaces the manual work nobody wants to do. Your team moves to higher-value work.",
            STRONG_BLOCKS["close_prompt_replace"],
        ],
        [
            "We need to test first",
            "Test mode is reasonable.",
            "Start with one agent, one workflow. If it misses target by day 30, partial refund.",
            STRONG_BLOCKS["close_prompt_test"],
        ],
        [
            "Our data is sensitive",
            "Security concern is valid.",
            "Your data stays within your environment. Controlled scope, not blanket access.",
            STRONG_BLOCKS["close_prompt_data"],
        ],
        [
            "We need HR approval",
            "Good — HR protects the team.",
            "This is an external supplier system, not an internal hire.",
            STRONG_BLOCKS["close_prompt_hr"],
        ],
        [
            "It's not a priority right now",
            "Priority follows pain.",
            "One painful task is stealing margin and attention right now.",
            STRONG_BLOCKS["close_prompt_priority"],
        ],
        [
            "We need to think about it",
            "Think is stall.",
            "The only risk is inaction. Margin bleeds while you wait. I will follow up Thursday.",
            STRONG_BLOCKS["close_prompt_think"],
        ],
    ],
}

# --------------------------------------------------------------------------- #
# 4. DESIGN RULES                                                             #
# --------------------------------------------------------------------------- #
DESIGN_RULES = (
    "1. Background: #101214 on every page. "
    "2. Primary ink: #f2f3f5 near-white for body text and table data. "
    "3. Soft text: #8a8f94 for eyebrow, subtext, footnote, and quote blocks. "
    "4. Accent: #ffffff solid for callout fill (alpha 0.85) and table header background. "
    "5. Scale: 1.55× everywhere (SC = 1.55). "
    "6. Margins: LM = RM = 18 mm, TM = BM = 14 mm (landscape too). "
    "7. Cover: eyebrow → title → 35-40% HR → sub → tag → foot → URL footer. "
    "8. Body pages: eyebrow → title → 35-40% HR → blocks → PageBreak. "
    "9. Callout: Table wrapper with ACC background (alpha 0.85), bold font, BG text color. "
    "10. Quote: wrap text in “ ”; italic (Helvetica-Oblique) or oblique; SOFT color. "
    "11. Table header: INK background, BG forecolor, bold. "
    "12. PageBreak after every page/slide except the last."
)

# --------------------------------------------------------------------------- #
# 5. PRODUCT PAGE DATA                                                         #
# --------------------------------------------------------------------------- #

COVER_DOSSIER = {
    "eyebrow": "HUMAN ARCHITECT  ·  OWL DOSSIER",
    "title": "THE FULFILLMENT LAYER",
    "sub": "The managed-AI-employee playbook for UK operators. Model, methodology, objections, case studies, and adoption-ready use cases.",
    "tag": "Sell an outcome, not a tool. Charge rent on the loop.",
    "foot": "Compiled by OWL | VERIFIED 2026-07-29 | Internal strategy dossier",
}
DOSSIER_PAGES = [
    {
        "n": 2, "eyebrow": "THE MODEL", "title": "What a managed AI employee is",
        "blocks": [
            {"t": "p", "text": STRONG_BLOCKS["model_definition"]},
            {"t": "callout", "text": STRONG_BLOCKS["price_block"]},
            {"t": "p", "text": "Nick Vasilescu runs this model publicly. Corey Ganim verified it and copied it. Market is early. Margin is ~90%. The moat is not the model — it is the fulfillment layer."},
            {"t": "quote", "text": STRONG_BLOCKS["quote_leverage"]},
        ]
    },
    {
        "n": 3, "eyebrow": "THE ACQUISITION FUNNEL", "title": "How to close £5k/mo clients",
        "blocks": [
            {"t": "li", "text": "<b>1 · Foot in the door:</b> lead with a £999 AI audit. Cold prospects say no to £5k. The audit pays you to learn their business AND surfaces the exact pain to solve."},
            {"t": "li", "text": "<b>2 · Pick ONE specialised agent</b> from the audit — the one with the most obvious ROI. One sharp agent beats ten half-built ones."},
            {"t": "li", "text": "<b>3 · Price £5,000/mo, all-in.</b> Unlimited usage, unlimited updates, fully managed."},
            {"t": "li", "text": "<b>4 · Ship by day two.</b> Same-day or next-day delivery changes the entire sales dynamic."},
            {"t": "li", "text": "<b>5 · B2B2B retention:</b> help the client resell the agent to THEIR customers — churn dies."},
            {"t": "callout", "text": "Speed-to-value rule: the same day a client wires money, ship them something. Agent live by day two."},
        ]
    },
    {
        "n": 4, "eyebrow": "THE MATH", "title": "Why the margin is ~90%",
        "blocks": [
            {"t": "p", "text": "10 clients × £5,000 = <b>£50,000/month recurring.</b>"},
            {"t": "p", "text": "Overhead per client ≈ workspace costs plus modest compute. Self-hosted keeps this tiny."},
            {"t": "callout", "text": "Key insight: almost no client needs an army of agents — they need one or two very specialised ones. That is why \"unlimited\" is safe to promise."},
            {"t": "quote", "text": STRONG_BLOCKS["quote_fulfillment"]},
        ]
    },
    {
        "n": 5, "eyebrow": "THE 8-PART FRAMEWORK", "title": "What every AI employee needs",
        "blocks": [
            {"t": "li", "text": "<b>1. Computer</b> — isolated env: VPS/container per client"},
            {"t": "li", "text": "<b>2. Email</b> — real inbox the agent can send/receive"},
            {"t": "li", "text": "<b>3. Phone/IM</b> — Telegram/Slack (client-facing)"},
            {"t": "li", "text": "<b>4. Comms channel</b> — where the client talks to it"},
            {"t": "li", "text": "<b>5. Tools/connectors</b> — skills + terminal/file/web"},
            {"t": "li", "text": "<b>6. Card/payment</b> — client billing + agent spend rails"},
            {"t": "li", "text": "<b>7. Knowledge base</b> — markdown \"one fact, one home\""},
            {"t": "li", "text": "<b>8. Observability</b> — health checks + Telegram alerts"},
            {"t": "callout", "text": "Miss one and it is a toy, not a worker."},
        ]
    },
    {
        "n": 6, "eyebrow": "THE ARCHITECTURE", "title": "Orchestrator + Swarm",
        "blocks": [
            {"t": "p", "text": "One orchestrator handles the client relationship. Specialised sub-agents execute: outbound, sales follow-up, content, support."},
            {"t": "p", "text": "Why split? <b>Minimise blast radius.</b> One broken sub-agent must never take down the others."},
            {"t": "callout", "text": "Rule: never tell the client \"the agent builds itself.\" Say: \"I have a build system. You get the agent by Friday.\""},
            {"t": "p", "text": "Repeatable delivery: <b>Build → Onboard → Fulfill → Pay.</b> Hands-off every month."},
        ]
    },
    {
        "n": 7, "eyebrow": "KNOWLEDGE FIRST", "title": "Lead with the KB, not the bot",
        "blocks": [
            {"t": "p", "text": "Before any agent is useful it needs a governed knowledge base. This is the step most operators skip. Don't."},
            {"t": "li", "text": "Organised by function: Company / Customers / Offers / Sales / Ops / Finance."},
            {"t": "li", "text": "Every fact carries provenance, owner, sensitivity, review date."},
            {"t": "li", "text": "Protected tier for credentials; agents get scoped boundaries."},
            {"t": "li", "text": "Pipeline: raw inputs → wiki → outputs. Maintenance is part of the product."},
            {"t": "callout", "text": STRONG_BLOCKS["km_quote"]},
        ]
    },
    {
        "n": 8, "eyebrow": "USE CASES", "title": "Adoption-ready client use cases",
        "blocks": [
            {"t": "p", "text": "Real-world use cases mapped to client language and outcome metrics. Each is a standalone conversation starter on a discovery call."},
            {"t": "callout", "text": STRONG_BLOCKS["one_agent_rule"]},
            {"t": "table", "text": [
                ["Sector", "Exact AI task", "Manual pain", "Outcome", "Monthly value"],
                ["Design agency", "Pitch deck + brand research + mood board from brief", "Designers spend 6–10 hrs/pitch scanning assets and assembling slides", "60–75% faster pitch turnaround", "£2,800–£4,500"],
                ["Real estate", "24/7 lead qualification + auto-booking viewings + agent handoff", "Agents manually answer DMs; low-quality leads waste 3–5 hrs/day; double-bookings", "80%+ leads qualified/booked; no-shows cut 30%", "£3,200–£5,500"],
                ["Private clinic", "AI scribe: transcribes consultations, drafts notes, files to records", "Clinicians spend 1.5–2 hrs/day typing notes; burnout", "Notes in real time; review cut from 90 mins to <15 mins", "£3,000–£5,000"],
                ["Coaching / wellness", "Intake agent: pre-qualifies, books discovery calls, intake forms + reminders", "Owner handles all scheduling; 30–40% leads go cold before first call", "Booking rate lifts 35–55%; admin drops 10–15 hrs/week", "£1,800–£3,500"],
                ["Trades", "After-hours phone/SMS agent: diagnostics, quotes, books emergency visits", "40–60% of callers hit voicemail after hours; lost jobs", "60–80% jobs booked without a human; out-of-hours capture 3×", "£2,500–£4,500"],
                ["Professional services", "Document-review agent: reads contracts/invoices, flags anomalies, drafts summaries", "Associates spend 40–60% of billable hours on prep; rework from errors", "First-pass review cut 70–85%; 10–15 hrs/week to advisory", "£4,500–£7,500"],
                ["B2B SaaS", "Support + CSM agent: tier-1 onboarding, setup walkthroughs, escalation routing", "Tickets pile up after launches; CSMs buried; NPS drops", "First response <90 sec; 50–65% tickets resolved without human", "£2,500–£5,000"],
                ["E-commerce", "Customer-service + returns handler: answers queries, processes returns, upsells", "CS team drowned in order-status/return tickets; abandoned carts", "60–75% tickets solved without human; AOV lifts 5–12%", "£1,800–£3,500"],
                ["Logistics", "Dispatch + exception agent: auto-assigns drivers, optimises routes, delay alerts", "Dispatcher spends all day on rider queries; routing by gut feel; late SLA", "Route density +15–25%; failed-delivery rate -20–35%", "£3,000–£5,500"],
                ["Property management", "Tenant-support agent: answers tenancy questions, logs maintenance, routes contractors", "20–40 calls/emails/day per manager; emergency delays; compliance stacks", "55–70% tenant queries self-serve; emergency SLA from 4 hrs to 1 hr", "£2,800–£4,500"],
                ["All sectors", "HR agent: policy answers, holiday/OOO tracking, offer/exit letters, compliance", "Founder interrupted constantly with policy/admin work; clunky processes", "HR admin cut 60–75%; answers instant; compliance risk reduced", "£1,500–£2,800"],
                ["IFA / Accountancy", "Client-intake + KYC agent: fact-find, Open Banking pull, client folders, gap alerts", "3–6 hrs per new client on admin, paperwork, chasing docs", "Onboarding from 2 days to same-day; missing-doc turnaround hours not days", "£2,500–£4,000"],
                ["Performance marketing", "Reporting agent: pulls Ads/GA4/social APIs, writes narrative reports, anomaly alerts", "Account managers spend 6–10 hrs/week on decks; client calls become screenshares", "Reporting time cut 80%; calls reallocated to strategy", "£2,200–£4,000"],
                ["Recruitment / staffing", "CV screen + candidate-engagement agent: ranks applicants, books interviews, chases feedback", "Recruiters spend 60% time reading CVs/admin; candidate ghosting rises", "Time-to-shortlist cut 70%; response rate +30–40%", "£2,000–£4,000"],
                ["Tech consultancy", "Project assistant: status from Jira/Notion, client updates, blocker flags, rebalance", "PM spends half the day chasing updates, writing recaps, rescheduling meetings", "Status-report time drops 85%; blockers surfaced in hours", "£2,000–£3,800"],
            ]},
        ]
    },
    {
        "n": 9, "eyebrow": "ADOPTION SIGNALS", "title": "What the research says",
        "blocks": [
            {"t": "p", "text": "UK SMB automation research points to fast payback when the AI owns a defined outcome rather than acting as a chatbot."},
            {"t": "li", "text": "UK SMBs report saving £500–£2,000/month per focused automation (Insightful AI UK, 57% adoption rate)."},
            {"t": "li", "text": "Professional-services ROI runs 280–370%, with 8–12-month payback (Samyotech, Forrester via Microsoft)."},
            {"t": "li", "text": "Trade/logistics automation typically pays for itself within 2–4 months by preventing one missed job or failed delivery per week."},
            {"t": "callout", "text": "The common failure mode is shipping a dashboard, not an employee. Outcome ownership is the differentiator."},
        ]
    },
    {
        "n": 10, "eyebrow": "OBJECTIONS", "title": "12 objections + handlers",
        "blocks": [
            {"t": "p", "text": "Objections are requests for reassurance, not rejection. Acknowledge, reframe, close."},
            {"t": "table", "text": [
                ["Objection", "Handler", "Close prompt"],
                ["£5,000 is too expensive", "If the task takes 2 hours daily at £40/hr, it costs £2,400/month before mistakes. Owl pays for itself before your first two bad hires.", STRONG_BLOCKS["close_prompt_too_expensive"]],
                ["We don't do AI here", "Most clients said the same. The agent lives in Slack. You don't touch code. You just watch the work get done.", STRONG_BLOCKS["close_prompt_no_ai"]],
                ["We already have tools", "Tools are not the same as fulfillment. A dashboard is a job. Owl ships the work.", STRONG_BLOCKS["close_prompt_tools"]],
                ["We tried AI before", "Most AI projects fail because they ship a toy, not a worker. Owl is managed execution, not a demo.", STRONG_BLOCKS["close_prompt_tried_ai"]],
                ["We're too small", "SMBs at £1M–£2M+ pay faster and ask fewer questions. They value outcomes over novelty.", STRONG_BLOCKS["close_prompt_small"]],
                ["We need custom", "Every agent is custom by default — built from your knowledge, your workflow, your outputs.", STRONG_BLOCKS["close_prompt_custom"]],
                ["It will replace people", "It replaces the manual work nobody wants to do. Your team moves to higher-value work.", STRONG_BLOCKS["close_prompt_replace"]],
                ["We need to test first", "I agree. Start with one agent, one workflow. If it misses the target by day 30, partial refund.", STRONG_BLOCKS["close_prompt_test"]],
                ["Our data is sensitive", "Your data stays within your environment. Controlled scope, not blanket access.", STRONG_BLOCKS["close_prompt_data"]],
                ["We need HR approval", "Good — HR protects the business. This is an external supplier system, not an internal hire.", STRONG_BLOCKS["close_prompt_hr"]],
                ["It's not a priority right now", "That is usually because one painful task is stealing margin and attention.", STRONG_BLOCKS["close_prompt_priority"]],
                ["We need to think about it", "The only risk is inaction. Margin bleeds while you wait. I will follow up Thursday. Does that work?", STRONG_BLOCKS["close_prompt_think"]],
            ]},
        ]
    },
    {
        "n": 11, "eyebrow": "PROOF POINTS", "title": "Verifiable case studies + quotes",
        "blocks": [
            {"t": "p", "text": "Publicly verifiable operators running managed AI employee / AI employee-for-hire models, with exact quotes."},
            {"t": "table", "text": [
                ["Source", "Claim", "Context"],
                ["Nick Vasilescu / Corey Ganim newsletter", "$5K/mo + fulfillment model", "Also confirmed on Build With AI podcast Jul 27 2026; Nick's verified reply: 'thanks for having me on again Corey'"],
                ["Nick Vasilescu / YouTube (BI-MNjm1tTQ)", "Solo operator, managed agents", "Demonstrates Dewey build + client deployment walkthrough"],
                ["Linara Bozieva / Business Insider", "27 agents, 5 clients, ~2 hrs/week oversight", "Launched after eBay layoff; could scale to 20–25 clients solo; costs under $1,000/month"],
                ["Corey Ganim / newsletter (corey-ganim.kit.com)", "'10 clients, £50k/month, one person'", "Explicit 90% margin math; overhead ~£200 Codex + Orgo workspace per client"],
                ["Corey Ganim / X post Jun 18 2026", "Quantified $5K retainer justification", STRONG_BLOCKS["proof_corey_quote"]],
                ["Boon Media / case studies", "Barber: no-shows 18%→4%; SaaS reply 0.8%→6.2%; freight: quote response 45min→5min", "Hard metrics from live case-study page"],
                ["Rebotify / case studies", "Energy retailer: drafts days→<1 hr; higher ed: 24hr→1min response; telco: 60–70% automated containment", "Enterprise AI employee deployments with public outcomes"],
                ["Agentive.au", "Junior-accountant price benchmark + 24hr deployment", STRONG_BLOCKS["proof_agentive"]],
                ["Skool / Agent Empire", "1.4k members", "Free course on building/selling managed agents"],
            ]},
            {"t": "callout", "text": "No standalone Nick post with the exact '$5k/mo fulfillment' phrase was found unauthenticated. The quote originates from Corey's recap thread + podcast. Attribute it right."},
        ]
    },
    {
        "n": 12, "eyebrow": "THE STACK", "title": "Your edge: self-hosted",
        "blocks": [
            {"t": "p", "text": "Nick's reference stack is paid. T already owns the free equivalents on this VPS. Same result, higher margin, total control."},
            {"t": "table", "text": [
                ["Part", "Nick pays", "T owns free"],
                ["Computer", "Orgo", "This VPS, 24/7"],
                ["Harness", "OpenClaw/Hermes", "Hermes Agent"],
                ["Email", "agentmail.to", "Domain alias"],
                ["IM", "agentphone.ai", "Telegram gateway"],
                ["Tools", "Composio", "Hermes skills + native tools"],
                ["Knowledge", "fresh vault", "~/vault (Obsidian)"],
                ["Watch", "latitude.so", "cron → Telegram"],
            ]},
            {"t": "callout", "text": "Never adopt the paid stack unless T approves a specific upgrade."},
        ]
    },
    {
        "n": 13, "eyebrow": "LAUNCH CHECKLIST", "title": "Owl execution checklist",
        "blocks": [
            {"t": "li", "text": "Foot in the door: offer £999 audit first."},
            {"t": "li", "text": "Audit → pick ONE high-ROI agent per client."},
            {"t": "li", "text": "Close at £5,000/mo all-in. Agent LIVE BY DAY TWO."},
            {"t": "li", "text": "Target SMBs at £1M–£2M+ revenue."},
            {"t": "li", "text": "B2B2B retention: help client resell to THEIR customers."},
            {"t": "li", "text": "Self-hosted stack; keep overhead ~£200/mo or less."},
            {"t": "li", "text": "Template knowledge layer: clients/<name>/context.md + discovery-call transcript."},
            {"t": "li", "text": "Bonus: sell the AI Second Brain KB service for £5k."},
            {"t": "li", "text": "Keep Dewey/Owl income SEPARATE from HumanitAI CIC."},
            {"t": "li", "text": "Teach the model publicly on Substack/X to pull leads."},
        ]
    },
]

COVER_BROCHURE = {
    "eyebrow": "HUMAN ARCHITECT  ·  OWL",
    "title": "THE FULFILLMENT LAYER",
    "sub": "How to close £5,000/month AI-employee clients, ship in 48 hours, and run fulfillment without writing code.",
    "tag": STRONG_BLOCKS["tagline"],
    "foot": "Internal strategy brochure · VERIFIED from live sources",
}
BROCHURE_PAGES = [
    {
        "n": 2, "eyebrow": "THE BUSINESS MODEL", "title": "A headcount replacement, not a dashboard",
        "blocks": [
            {"t": "p", "text": (
                "A managed AI employee is a deployed AI worker that handles one defined job for a client "
                "for a flat monthly fee. The client pays to receive an outcome, not to own software they "
                "have to figure out. That distinction is the whole business."
            )},
            {"t": "callout", "text": (
                "Most operators have AI. Almost none have an agent that ships. "
                "The tool sits idle while you do the delivery by hand — and margin bleeds out every single week."
            )},
            {"t": "p", "text": (
                "Owl charges <b>£5,000 per client, per month</b>. That includes unlimited usage, "
                "unlimited updates, and full management by us. Delivery target: live in their Slack within 48 hours."
            )},
            {"t": "callout", "text": (
                "Refund rule: if the agent misses the agreed target by day 30, the client gets a partial refund. "
                "We only win if they get value."
            )},
        ]
    },
    {
        "n": 3, "eyebrow": "WHAT THE CLIENT GETS", "title": "Built. Onboarded. Fulfilled.",
        "blocks": [
            {"t": "li", "text": "<b>A custom AI employee.</b> Built for the exact work the client needs, not a toy template."},
            {"t": "li", "text": "<b>It lives in Slack.</b> Your team talks to it where work already happens. No new app to learn."},
            {"t": "li", "text": "<b>Hands-off fulfillment.</b> Customer support, daily tasks, follow-ups — handled."},
            {"t": "li", "text": "<b>Health visibility.</b> Telegram alerts so the owner sees it working without babysitting."},
        ]
    },
    {
        "n": 4, "eyebrow": "THE ACQUISITION PLAYBOOK", "title": "How to close $5k/mo clients",
        "blocks": [
            {"t": "li", "text": "<b>1 · Lead with a £999 audit,</b> not the £5k retainer. The audit pays you to learn their business AND shows the exact pain to solve."},
            {"t": "li", "text": "<b>2 · Pick ONE specialised agent</b> from the audit — the one with the most obvious ROI."},
            {"t": "li", "text": "<b>3 · Price £5,000/mo, all-in.</b> Unlimited usage, unlimited updates, fully managed."},
            {"t": "li", "text": "<b>4 · Ship by day two.</b> Same-day or next-day delivery changes the sales dynamic."},
            {"t": "callout", "text": "The old model (charge £4k upfront, retain £350/mo) is dead. The new model is monthly recurring, delivered fast, with a value-back guarantee."},
        ]
    },
    {
        "n": 5, "eyebrow": "THE MATH", "title": "Why the margin is ~90%",
        "blocks": [
            {"t": "p", "text": "10 clients × £5,000 = <b>£50,000/month recurring.</b>"},
            {"t": "p", "text": "Overhead per client is roughly workspace costs plus modest compute. One person runs the whole operation with sub-agents executing deep work under an orchestrator."},
            {"t": "callout", "text": "Key insight: almost no client needs an army of agents — they need one or two specialised ones. That is why \"unlimited\" is safe to promise."},
            {"t": "quote", "text": STRONG_BLOCKS["quote_fulfillment"]},
        ]
    },
    {
        "n": 6, "eyebrow": "THE ARCHITECTURE", "title": "Orchestrator + Swarm",
        "blocks": [
            {"t": "p", "text": "One orchestrator agent handles the client relationship. Specialised sub-agents do the work: outbound, sales follow-up, content, support. Split exists for one reason: <b>minimise blast radius.</b>"},
            {"t": "p", "text": "If one sub-agent breaks, the rest keep running. If one client task explodes, the others stay steady. Isolation is not optional."},
            {"t": "callout", "text": "The agent is leverage, not a sales pitch. Say: \"I have a build system. You get the agent by Friday.\""},
            {"t": "p", "text": "Delivery loop: <b>Build → Onboard → Fulfill → Pay.</b> Repeats every month, hands-off."},
        ]
    },
    {
        "n": 7, "eyebrow": "KNOWLEDGE FIRST", "title": "Lead with the knowledge layer",
        "blocks": [
            {"t": "p", "text": "Before any agent becomes useful, it needs a governed knowledge base. Use a simple schema: function-based folders, metadata on every fact, protected tier for credentials."},
            {"t": "li", "text": "Organised by function: Company / Customers / Offers / Sales / Ops / Finance."},
            {"t": "li", "text": "Every fact carries provenance, owner, sensitivity, and review date."},
            {"t": "li", "text": "Distillation pipeline: raw inputs → wiki → outputs. Maintenance is part of the product."},
            {"t": "callout", "text": STRONG_BLOCKS["km_quote"]},
        ]
    },
    {
        "n": 8, "eyebrow": "THE STACK", "title": "What we use and why",
        "blocks": [
            {"t": "p", "text": "Self-hosted takes more setup but pays back in margin and control. The agent does not need the fanciest model — it needs the right tool attached to the right workflow."},
            {"t": "callout", "text": "Rule: every component must justify its cost in margin or control. If a paid tool costs more than the value it extracts, replace it or remove it."},
            {"t": "table", "text": [
                ["Part", "Purpose", "Note"],
                ["Orchestrator", "Manage clients and delegate tasks", "One central Hermes agent"],
                ["Slack", "Primary comms channel", "Client never leaves their workspace"],
                ["Telegram", "Owner visibility + alerts", "Lightweight, low upkeep"],
                ["Knowledge base", "Client context + business rules", "Markdown, versioned"],
                ["Health checks", "Uptime + silent alerts", "Cron + Telegram fallback"],
            ]},
        ]
    },
    {
        "n": 9, "eyebrow": "THE CHECKLIST", "title": "Owl launch checklist",
        "blocks": [
            {"t": "li", "text": "<b>Target real businesses.</b> SMBs doing £1M–£2M+ revenue pay faster and ask fewer questions."},
            {"t": "li", "text": "<b>Foot in the door:</b> start with a £999 audit, not a £5k sell."},
            {"t": "li", "text": "<b>Discovery questions:</b> What task takes 2+ hours every day? What breaks when it slips? What would 24/7 coverage unlock?"},
            {"t": "li", "text": "<b>Ship fast:</b> same-day or next-day delivery changes the sales dynamic."},
            {"t": "li", "text": "<b>Retention:</b> help the client resell the agent to THEIR customers — B2B2B never churns."},
            {"t": "li", "text": "<b>Keep overhead tiny</b> and self-hosted. Margin compounds when you do."},
            {"t": "li", "text": "<b>Teach publicly</b> on Substack/X to pull inbound leads."},
        ]
    },
    {
        "n": 10, "eyebrow": "NEXT STEPS", "title": "What to do this week",
        "blocks": [
            {"t": "li", "text": "Publish one short post explaining the Fulfillment Layer in plain language."},
            {"t": "li", "text": "Run 5 discovery calls using the script in section 3."},
            {"t": "li", "text": "Close the first £999 audit within 7 days."},
            {"t": "li", "text": "Build the first live agent and ship by day two."},
            {"t": "li", "text": "Collect results, record a case study, publish again."},
            {"t": "callout", "text": "Repeat until the model is proven. Then scale with sub-agents, not more of you."},
            {"t": "li", "text": URLS["SITE"]},
            {"t": "li", "text": URLS["BOOK"]},
            {"t": "quote", "text": STRONG_BLOCKS["quote_first_mover"]},
        ]
    },
]

COVER_SALES = {
    "eyebrow": "HUMAN ARCHITECT  ·  OWL",
    "title": "THE CLOSING FIELD MANUAL",
    "sub": "A forensic training manual for selling managed AI employees. Scripts, objections, proof, roles, and close sequences.",
    "tag": "Teach the model. Close the deal. Own the loop.",
    "foot": "Internal training · VERIFIED 2026-07-29 · For operators only",
}
SALES_PAGES = [
    {
        "n": 2, "eyebrow": "PRIME DIRECTIVE", "title": "Operators close. Agents fulfill.",
        "blocks": [
            {"t": "p", "text": "This manual is not theory. It is a repeatable closing system for a £5,000/month managed AI employee offer. You either teach it or you outsource it. Never let the client feel the difference."},
            {"t": "callout", "text": STRONG_BLOCKS["rule_burden_first"]},
            {"t": "p", "text": "Every stage below is mapped to owner power and agent support. The owner owns the relationship and the close. The agent owns the follow-up, the proof, and the admin. If you mix these roles on a call, you lose leverage."},
            {"t": "quote", "text": STRONG_BLOCKS["quote_manual"]},
        ]
    },
    {
        "n": 3, "eyebrow": "MINDSET", "title": "How to think during the close",
        "blocks": [
            {"t": "p", "text": "The client is not saying no. They are calculating risk. Lower the risk faster than they can raise it."},
            {"t": "li", "text": "<b>You are not selling software.</b> You are selling a managed outcome. The price follows the outcome, not the tooling."},
            {"t": "li", "text": "<b>Speed beats perfection.</b> The first operator to show up with a credible plan wins. Credibility comes from specificity, not polish."},
            {"t": "li", "text": "<b>Objections are requests for reassurance,</b> not rejection. Answer the fear behind the sentence, not the sentence itself."},
            {"t": "li", "text": "<b>Close is not a moment.</b> It is a sequence. Discovery → fit → proof → terms → next step."},
            {"t": "li", "text": "<b>The agent is your leverage, not your sales pitch.</b> Say: 'I have a build system.' Do not say: 'the agent builds itself.'"},
        ]
    },
    {
        "n": 4, "eyebrow": "ROLES", "title": "Owner vs agent during the sale",
        "blocks": [
            {"t": "p", "text": "Clear role split prevents confusion and protects trust."},
            {"t": "table", "text": [
                ["Owner does", "Agent does", "Client sees"],
                ["Discovery calls", "Follow-up emails", "Fast, personal replies"],
                ["Price framing + close", "Proof assembly + case-drop calendar", "Consistent evidence"],
                ["Scoping conversation", "Knowledge-base intake forms", "Structured intake without rework"],
                ["Live demo or workflow review", "Health checks + readiness tests", "Reliable delivery timeline"],
                ["Objection handling", "Objection handler library + snippets", "Confident answers in chat/email"],
                ["Relationship ownership", "Appointment scheduling + reminders", "No dropped balls"],
            ]},
            {"t": "callout", "text": STRONG_BLOCKS["rule_no_automated"]},
        ]
    },
    {
        "n": 5, "eyebrow": "SCRIPT", "title": "Discovery call script",
        "blocks": [
            {"t": "step_title", "text": "1 · Opener"},
            {"t": "step", "text": "'Thanks for making the time. The goal of this call is simple: find out whether there is a clear, painful task we can take off your plate in 48 hours. I will do less talking than you.'"},
            {"t": "step_title", "text": "2 · Pain discovery"},
            {"t": "step", "text": "'What task costs your team two or more hours every single day?'"},
            {"t": "step", "text": "'What happens when that task slips?'"},
            {"t": "step", "text": "'Who currently owns it, and what are they not doing because of it?'"},
            {"t": "step", "text": "'If this was handled 24/7 without you managing it, what would that unlock next month?'"},
            {"t": "step_title", "text": "3 · Fit"},
            {"t": "step", "text": "'Based on what you just said, I can see one agent that fits: [exact task]. It would live in your Slack, handle [workflow], and report to [owner/channel].'"},
            {"t": "step", "text": "'Price is flat £5,000/month. Managed, unlimited, by day two. Does that feel worth solving?'"},
            {"t": "step_title", "text": "4 · Close"},
            {"t": "step", "text": "'I can send onboarding instructions today. We will have a live demo by [day]. Shall I set it up?'"},
        ]
    },
    {
        "n": 6, "eyebrow": "PROOF SYSTEM", "title": "How to prove it without bragging",
        "blocks": [
            {"t": "p", "text": "Clients do not need more evidence. They need the right evidence, at the right moment, in their language."},
            {"t": "li", "text": "<b>Anchor with the model first,</b> not your CV. 'Operators are running this at £5k/month with one person.'"},
            {"t": "li", "text": "<b>Then drop one relevant case.</b> Pick the sector closest to theirs."},
            {"t": "li", "text": "<b>Then show the stack.</b> One slide. One architecture sentence: 'Orchestrator plus sub-agents, Slack-native, self-hosted.'"},
            {"t": "li", "text": "<b>Then show the calendar.</b> 'Day one: signed agreement. Day two: live agent.' That is the close."},
            {"t": "callout", "text": "Rule: never show more than three proof points per call. More evidence weakens certainty, not strengthens it."},
        ]
    },
    {
        "n": 7, "eyebrow": "DEMO", "title": "The 20-minute live demo script",
        "blocks": [
            {"t": "step_title", "text": "Setup"},
            {"t": "step", "text": "Open a clean Slack workspace or dedicated Telegram thread so the client sees the agent from inside their own tool. No custom UI, no login portals."},
            {"t": "step_title", "text": "Minute 0–5 · The brief"},
            {"t": "step", "text": "'Here is the exact workflow we scoped on the call. The agent owns [task]. It reads from [knowledge folder]. It answers in [Slack/Telegram]. Here is how it starts.'"},
            {"t": "step_title", "text": "Minute 5–15 · Live execution"},
            {"t": "step", "text": "Send a real inbound message the agent should handle. Let it respond. Show the knowledge base. Show the fallback behaviour when it does not know."},
            {"t": "step_title", "text": "Minute 15–20 · What you own"},
            {"t": "step", "text": "'This is live now. You will see health alerts here. I will handle improvements. You handle the client relationship. If it misses the agreed target by day 30, partial refund.'"},
            {"t": "callout", "text": "Do not demo features. Demo outcome. Every minute should show ownership, not capability."},
        ]
    },
    {
        "n": 8, "eyebrow": "CLOSE SEQUENCE", "title": "The 5-step close",
        "blocks": [
            {"t": "step_title", "text": "1 · Summary"},
            {"t": "step", "text": "Repeat what they asked for using their words. 'You want a support agent in Slack that closes customer tickets without you in the middle.'"},
            {"t": "step_title", "text": "2 · Investment"},
            {"t": "step", "text": "'Flat £5,000/month. Managed. Unlimited usage. Live by day two. Partial refund if it misses the target by day 30.'"},
            {"t": "step_title", "text": "3 · Risk reversal"},
            {"t": "step", "text": "'I do not need a long-term commitment. Start with one agent, one workflow. If it does not earn its keep by day 30, we will make it right.'"},
            {"t": "step_title", "text": "4 · Next step"},
            {"t": "step", "text": "'I will send onboarding instructions and a simple intake form. You wire the first month. We start tomorrow.'"},
            {"t": "step_title", "text": "5 · Assumption close"},
            {"t": "step", "text": "'Great — does Tuesday or Wednesday work better for the scoping handoff?'"},
            {"t": "callout", "text": "If they hesitate on price, return to pain value: 'What does that manual task cost you per month right now?'"},
        ]
    },
    {
        "n": 9, "eyebrow": "OBJECTIONS", "title": "Field-tested handlers",
        "blocks": [
            {"t": "table", "text": OBJECTIONS_TABLE["rows"]},
        ]
    },
    {
        "n": 10, "eyebrow": "LIVE DEALS", "title": "How to run a live close",
        "blocks": [
            {"t": "p", "text": "A live deal is a pipeline with timestamps and ownership. Do not let a prospect float in 'we are thinking about it' forever."},
            {"t": "li", "text": "<b>Hour 0:</b> discovery call → scoping handoff email within 30 minutes."},
            {"t": "li", "text": "<b>Hour 1–4:</b> agent sends intake form; owner sends case-study PDF matching their sector."},
            {"t": "li", "text": "<b>Hour 4–24:</b> agent schedules the follow-up call; owner reviews intake and drafts agent brief."},
            {"t": "li", "text": "<b>Day 2:</b> live demo or delivery preview with exact workflow."},
            {"t": "li", "text": "<b>Day 3–7:</b> answer objections by email/Slack; keep proof in sight."},
            {"t": "li", "text": "<b>Day 7:</b> close or clear decision. If not closed, reduce price or scope, or move prospect to nurture for 14 days."},
            {"t": "callout", "text": "Do not extend hope without a defined decision. A deal without a next step is not a deal."},
        ]
    },
    {
        "n": 11, "eyebrow": "DEMO", "title": "Demo techniques that convert",
        "blocks": [
            {"t": "p", "text": "A demo is not a tour. It is a promise you keep in real time."},
            {"t": "li", "text": "<b>Start with pain,</b> not features: 'You described follow-up dropping off after day three. Here is the exact sequence your agent will own.'"},
            {"t": "li", "text": "<b>Use real data,</b> not synthetic examples: import one anonymised client message or ticket."},
            {"t": "li", "text": "<b>Show failure mode first:</b> ask the agent a question it cannot answer. Show the fallback. This builds trust faster than perfection."},
            {"t": "li", "text": "<b>End on outcome,</b> not roadmap: 'This is live on day two. You get the first complete set of results by Friday.'"},
        ]
    },
    {
        "n": 12, "eyebrow": "NEGOTIATION", "title": "How to negotiate without discounting",
        "blocks": [
            {"t": "p", "text": "Discount is a last resort. Change scope or value first."},
            {"t": "li", "text": "<b>Scope down, not price:</b> one agent, one workflow, 30-day start."},
            {"t": "li", "text": "<b>Payment cadence:</b> monthly first, then quarterly with a small discount only after 90 days."},
            {"t": "li", "text": "<b>Guarantee leverage:</b> 'I can offer a partial refund by day 30 if we miss the agreed target. That protects you without devaluing the work.'"},
            {"t": "li", "text": "<b>Add outcome terms:</b> specific target, milestone, or SLA attached to performance."},
            {"t": "li", "text": "<b>Framing:</b> 'This is priced for managed execution, not access. The alternative is hiring, which costs more and never guarantees outcome.'"},
        ]
    },
    {
        "n": 13, "eyebrow": "TEMPLATES", "title": "Scripts you can copy",
        "blocks": [
            {"t": "step_title", "text": "Post-call follow-up"},
            {"t": "step", "text": "'Quick recap: we scoped [agent name] to own [task] inside [Slack/Telegram]. Flat £5,000/month, managed, live by day two. Partial refund if we miss the target by day 30. I will send onboarding instructions and the intake form by 6pm GMT. Reply with the best scoping time for tomorrow and I will lock it in.'"},
            {"t": "step_title", "text": "Proof drop"},
            {"t": "step", "text": "'This case matches your sector: [sector]. Before/after metrics: [metric] to [metric]. The client now runs the agent solo with a 30-minute weekly review.'"},
            {"t": "step_title", "text": "Re-engagement nurture"},
            {"t": "step", "text": "'Still thinking about it. If the blocker is budget, we can start with one workflow at reduced scope and expand once it earns its keep. If it is trust, I can send a signed NDA and a 14-day pilot plan. What would help most?'"},
        ]
    },
    {
        "n": 14, "eyebrow": "METRICS", "title": "Measure what matters",
        "blocks": [
            {"t": "p", "text": "Track these every week until the model is proven."},
            {"t": "table", "text": [
                ["Metric", "Target", "Why it matters"],
                ["Discovery calls/week", "5+", "Top of funnel."],
                ["Audit-to-agent rate", "20%+", "Quality of fit."],
                ["Close rate", "15%+", "Conversion strength."],
                ["Day-two live rate", "90%+", "Speed-to-value."],
                ["Client NPS / testimonial rate", "1 per 3 clients", "Proof compounding."],
                ["Time to first value", "<7 days", "Retention predictor."],
            ]},
            {"t": "callout", "text": "If discovery calls are high but closes are low, fix the offer or the proof sequence. Do not increase traffic."},
        ]
    },
    {
        "n": 15, "eyebrow": "PLAYBOOK", "title": "Your first 30 days",
        "blocks": [
            {"t": "li", "text": "Day 1: publish one post on the Fulfillment Layer. Post one thread. Send five outreach messages."},
            {"t": "li", "text": "Day 2–7: complete five discovery calls using the script in this manual."},
            {"t": "li", "text": "Day 7: close one £999 audit. Build agent brief in your clients folder."},
            {"t": "li", "text": "Day 8–14: ship first live agent. Collect before/after metrics."},
            {"t": "li", "text": "Day 15–21: record a case study from the first client. Publish again."},
            {"t": "li", "text": "Day 22–30: raise price or scope once you have one proven outcome. Add sub-agents for support, not more of you."},
            {"t": "quote", "text": STRONG_BLOCKS["quote_fulfillment"]},
        ]
    },
]

COVER_PITCH = {
    "eyebrow": "HUMAN ARCHITECT",
    "title": "One AI employee.<br/>One monthly fee.",
    "sub": "Flat £5,000/month. Live in 48 hours. Managed outcome, not a chatbot.",
    "tag": "Price: £5,000/month. 48-hour delivery. Outcome-based, not tool-based.",
    "foot": "Internal strategy · VERIFIED 2026-07-29",
}
PITCH_SLIDES = [
    {
        "n": 1, "eyebrow": "HUMAN ARCHITECT", "title": "One AI employee.<br/>One monthly fee.",
        "blocks": [
            {"t": "sub", "text": "Flat £5,000/month. Live in 48 hours. Managed outcome, not a chatbot."},
            {"t": "callout", "text": "Price: £5,000/month. 48-hour delivery. Outcome-based, not tool-based."},
            {"t": "p", "text": "I deploy an AI worker into your existing channel — Slack or Telegram — that owns one defined body of work. You measure output, not usage. No hiring. No HR. No sick leave."},
        ]
    },
    {
        "n": 2, "eyebrow": "WHY", "title": "We refuse to accept avoidable admin cost.",
        "blocks": [
            {"t": "p", "text": "Most UK SMBs bleed money on tasks humans do badly at 3am, on holidays, or under pressure. These are not strategy tasks — they are repetitive loops."},
            {"t": "quote", "text": STRONG_BLOCKS["quote_leverage"]},
            {"t": "p", "text": "The market is early. The margin runs around 90%. The moat is fulfillment — not the model."},
        ]
    },
    {
        "n": 3, "eyebrow": "THE PAIN", "title": "The wound is small, daily, and visible.",
        "blocks": [
            {"t": "p", "text": "Staff spend 10–20 hours a week on intake, follow-up, notes, or admin that needs consistency, not judgement."},
            {"t": "li", "text": "Missed enquiries: after-hours leads go elsewhere."},
            {"t": "li", "text": "Slow quotes: trade jobs lost to faster responders."},
            {"t": "li", "text": "No-shows: clinic or coach time disappears."},
            {"t": "li", "text": "Onboarding drag: agencies lose kickoff weeks to asset chasing."},
            {"t": "p", "text": "These leaks are not dramatic. They are daily. That is why they never get fixed."},
        ]
    },
    {
        "n": 4, "eyebrow": "HOW", "title": "Outcome ownership, not tool deployment.",
        "blocks": [
            {"t": "li", "text": "1 · Foot-in-the-door: £999 audit surfaces the highest-ROI task."},
            {"t": "li", "text": "2 · One agent, ONE job — the task with the most obvious payback."},
            {"t": "li", "text": "3 · Price flat at £5,000/month, all usage, all updates included."},
            {"t": "li", "text": "4 · Ship by day two after agreement + platform token."},
            {"t": "li", "text": "5 · Prove outcome fast. Use client language, not AI language."},
            {"t": "p", "text": "Speed wins. If you lead with AI, you lose. Lead with outcomes."},
        ]
    },
    {
        "n": 5, "eyebrow": "PROOF MATH", "title": "Why £5,000 is easy to justify.",
        "blocks": [
            {"t": "p", "text": "Every objection collapses when you measure hours, leads, or outcomes."},
            {"t": "li", "text": "2 hrs/day x £40/hr = £2,400/month before mistakes."},
            {"t": "li", "text": "20 missed leads/month x £3,500 commission = £21,000/month leak."},
            {"t": "li", "text": "1 recovered emergency job/week > £5,000 within 6–10 weeks."},
            {"t": "callout", "text": "Lead-value rule: the AI employee either pays for itself or misses target."},
        ]
    },
    {
        "n": 6, "eyebrow": "PROOF POINTS", "title": "Verified operators, exact claims.",
        "blocks": [
            {"t": "table", "text": [
                ["Source", "Claim", "Date / context"],
                ["Nick Vasilescu / Corey Ganim", "$5K/mo + fulfillment model", "podcast + recap Jun 2026"],
                ["Linara Bozieva / Business Insider", "27 agents, 5 clients, ~2 hrs/week oversight", "post eBay layoff, 2026"],
                ["Boon Media / case studies", "Barber no-shows 18%→4%; freight quote response 45min→5min", "live page"],
            ]},
            {"t": "small", "text": "Attribution note: the $5K/mo fulfillment quote originates from Corey Ganim's recap of Nick Vasilescu — do not use unauthenticated."},
        ]
    },
    {
        "n": 7, "eyebrow": "IMPLEMENTATION", "title": "Standard opener. No custom until proven.",
        "blocks": [
            {"t": "li", "text": "Discovery call: one question — \"What task drains your team every day?\""},
            {"t": "li", "text": "Audit: map exact workflow + current tool stack."},
            {"t": "li", "text": "Scope: ONE agent, ONE outcome, ONE integration channel."},
            {"t": "li", "text": "Build: SOUL.md + knowledge vault + process map."},
            {"t": "li", "text": "Onboard: introduce into the client's Slack/Telegram with live example."},
            {"t": "p", "text": "Do not scale until the first agent delivers by day 14."},
        ]
    },
    {
        "n": 8, "eyebrow": "STACK", "title": "Your edge: self-hosted.",
        "blocks": [
            {"t": "table", "text": [
                ["Part", "Reference paid", "Self-hosted free"],
                ["Computer", "Orgo", "VPS / container"],
                ["Harness", "OpenClaw/Hermes", "Hermes Agent"],
                ["KB", "Fresh vault", "~/vault Obsidian"],
                ["Watch", "Latitude", "Cron → Telegram"],
            ]},
            {"t": "p", "text": "Avoid Orgo/Composio/AgentMail/AgentPhone/Latitude/Honcho unless explicitly approved. The paid stack is a sales hook, not a requirement."},
        ]
    },
    {
        "n": 9, "eyebrow": "B2B2B RETENTION", "title": "Churn reduction mode.",
        "blocks": [
            {"t": "p", "text": "Once the agent runs, show the client how to resell access to THEIR customers. That changes churn psychology."},
            {"t": "li", "text": "They become less likely to cancel because it becomes revenue infrastructure."},
            {"t": "li", "text": "They become a case study."},
            {"t": "li", "text": "They introduce you to peers in the same vertical."},
            {"t": "callout", "text": STRONG_BLOCKS["b2b2b_callout"]},
        ]
    },
    {
        "n": 10, "eyebrow": "RISK CONTROL", "title": "Reduce risk before reducing price.",
        "blocks": [
            {"t": "li", "text": "Fixed scope: one task per agent, one outcome."},
            {"t": "li", "text": "Fixed channel: one Slack or Telegram thread."},
            {"t": "li", "text": "Fixed deadline: live by day two after handoff."},
            {"t": "li", "text": "Fixed metric: what “done” looks like in 30 days."},
            {"t": "p", "text": "If it misses the agreed target by day 30, partial refund."},
        ]
    },
    {
        "n": 11, "eyebrow": "ASSUME CLOSE", "title": "Close from the first touch.",
        "blocks": [
            {"t": "quote", "text": STRONG_BLOCKS["quote_close"]},
            {"t": "p", "text": "“If I could [exact outcome] in 48 hours at £5,000/month, which side of this are you on?”"},
            {"t": "callout", "text": "Next action is a fixed call, not a vague follow-up."},
        ]
    },
    {
        "n": 12, "eyebrow": "CONTACT", "title": "One next step.",
        "blocks": [
            {"t": "p", "text": "Primary booking: beacons.ai/humanarchitect"},
            {"t": "p", "text": "Offer site: alkalinearchitect.github.io/ai-employee/"},
            {"t": "quote", "text": "One agent. One workflow. One outcome."},
        ]
    },
    {
        "n": 13, "eyebrow": "CONTACT", "title": "The ask.",
        "blocks": [
            {"t": "p", "text": "This is not a product demo. This is an invitation to a conversation about whether one defined body of work in your business could be owned by an AI employee — managed, monitored, and improved by us."},
            {"t": "callout", "text": "Next action: one 20-minute call. Not a pitch. A diagnosis."},
            {"t": "p", "text": "Book at beacons.ai/humanarchitect or reply to this deck with your worst task. I will reply with a 90-second scoping note."},
        ]
    },
]
