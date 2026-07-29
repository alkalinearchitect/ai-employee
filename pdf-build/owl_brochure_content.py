SITE="https://alkalinearchitect.github.io/ai-employee/"
BOOK="https://beacons.ai/humanarchitect"
SUB="https://substack.com/@humanarchitect"

COVER={
 "eyebrow":"HUMAN ARCHITECT  ·  OWL",
 "title":"THE FULFILLMENT LAYER",
 "sub":"How to close £5,000/month AI-employee clients, ship in 48 hours, and run fulfillment without writing code.",
 "tag":"Sell an outcome, not a tool. Charge rent on the loop.",
 "foot":"Internal strategy brochure · VERIFIED from live sources",
}
PAGES=[]
PAGES.append({"n":2,"eyebrow":"THE BUSINESS MODEL","title":"A headcount replacement, not a dashboard",
 "blocks":[
  ("p","A managed AI employee is a deployed AI worker that handles one defined job for a client for a flat monthly fee. The client pays to receive an outcome, not to own software they have to figure out. That distinction is the whole business."),
  ("callout","\"Most operators have AI. Almost none have an agent that ships. The tool sits idle while you do the delivery by hand — and margin bleeds out every single week.\""),
  ("p","Owl charges **£5,000 per client, per month**. That includes unlimited usage, unlimited updates, and full management by us. Delivery target: live in their Slack within 48 hours."),
  ("callout","Refund rule: if the agent misses the agreed target by day 30, the client gets a partial refund. We only win if they get value."),
 ]})
PAGES.append({"n":3,"eyebrow":"WHAT THE CLIENT GETS","title":"Built. Onboarded. Fulfilled.",
 "blocks":[
  ("li","<b>A custom AI employee.</b> Built for the exact work the client needs, not a toy template."),
  ("li","<b>It lives in Slack.</b> Your team talks to it where work already happens. No new app to learn."),
  ("li","<b>Hands-off fulfillment.</b> Customer support, daily tasks, follow-ups — handled."),
  ("li","<b>Health visibility.</b> Telegram alerts so the owner sees it working without babysitting."),
 ]})
PAGES.append({"n":4,"eyebrow":"THE ACQUISITION PLAYBOOK","title":"How to close $5k/mo clients",
 "blocks":[
  ("li","<b>1 · Lead with a £999 audit,</b> not the £5k retainer. Cold prospects say no to £5k. The audit pays you to learn their business AND shows the exact pain to solve."),
  ("li","<b>2 · Pick ONE specialised agent</b> from the audit — the one with the most obvious ROI. One sharp agent beats ten half-built ones."),
  ("li","<b>3 · Price £5,000/mo, all-in.</b> Unlimited usage, unlimited updates, fully managed."),
  ("li","<b>4 · Ship by day two.</b> Same-day or next-day delivery changes the entire sales dynamic."),
  ("callout","The old model (charge £4k upfront, retain £350/mo) is dead. The new model is monthly recurring, delivered fast, with a value-back guarantee."),
 ]})
PAGES.append({"n":5,"eyebrow":"THE MATH","title":"Why the margin is ~90%",
 "blocks":[
  ("p","10 clients × £5,000 = <b>£50,000/month recurring.</b>"),
  ("p","Overhead per client is roughly workspace costs plus modest compute. One person runs the whole operation with sub-agents executing deep work under an orchestrator."),
  ("callout","Key insight: almost no client needs an army of agents — they need one or two specialised ones. That is why \"unlimited\" is safe to promise."),
  ("quote","Build once. Fulfill forever. Charge rent on the loop."),
 ]})
PAGES.append({"n":6,"eyebrow":"THE ARCHITECTURE","title":"Orchestrator + Swarm",
 "blocks":[
  ("p","One orchestrator agent handles the client relationship. Specialised sub-agents do the work: outbound, sales follow-up, content, support. Split exists for one reason: <b>minimise blast radius.</b>"),
  ("p","If one sub-agent breaks, the rest keep running. If one client task explodes, the others stay steady. Isolation is not optional."),
  ("callout","The agent is leverage, not a sales pitch. Say: \"I have a build system. You get the agent by Friday.\""),
  ("p","Delivery loop: <b>Build → Onboard → Fulfill → Pay.</b> Repeats every month, hands-off."),
 ]})
PAGES.append({"n":7,"eyebrow":"KNOWLEDGE FIRST","title":"Lead with the knowledge layer",
 "blocks":[
  ("p","Before any agent becomes useful, it needs a governed knowledge base. Use a simple schema: function-based folders, metadata on every fact, protected tier for credentials."),
  ("li","Organised by function: Company / Customers / Offers / Sales / Ops / Finance."),
  ("li","Every fact carries provenance, owner, sensitivity, and review date."),
  ("li","Distillation pipeline: raw inputs → wiki → outputs. Maintenance is part of the product."),
  ("callout","A governed knowledge base is one of the few moats left in the AI age. Sell it as a service for £5k+."),
 ]})
PAGES.append({"n":8,"eyebrow":"THE STACK","title":"What we use and why",
 "blocks":[
  ("p","Self-hosted takes more setup but pays back in margin and control. The agent does not need the fanciest model — it needs the right tool attached to the right workflow."),
  ("callout","Rule: every component must justify its cost in margin or control. If a paid tool costs more than the value it extracts, replace it or remove it."),
  ("table",[
    ["Part","Purpose","Note"],
    ["Orchestrator","Manage clients and delegate tasks","One central Hermes agent"],
    ["Slack","Primary comms channel","Client never leaves their workspace"],
    ["Telegram","Owner visibility + alerts","Lightweight, low upkeep"],
    ["Knowledge base","Client context + business rules","Markdown, versioned"],
    ["Health checks","Uptime + silent alerts","Cron + Telegram fallback"],
  ]),
 ]})
PAGES.append({"n":9,"eyebrow":"THE CHECKLIST","title":"Owl launch checklist",
 "blocks":[
  ("li","<b>Target real businesses.</b> SMBs doing £1M–£2M+ revenue pay faster and ask fewer questions."),
  ("li","<b>Foot in the door:</b> start with a £999 audit, not a £5k sell."),
  ("li","<b>Discovery questions:</b> What task takes 2+ hours every day? What breaks when it slips? What would 24/7 coverage unlock?"),
  ("li","<b>Ship fast:</b> same-day or next-day delivery changes the sales dynamic."),
  ("li","<b>Retention:</b> help the client resell the agent to THEIR customers — B2B2B never churns."),
  ("li","<b>Keep overhead tiny</b> and self-hosted. Margin compounds when you do."),
  ("li","<b>Teach publicly</b> on Substack/X to pull inbound leads."),
 ]})
PAGES.append({"n":10,"eyebrow":"NEXT STEPS","title":"What to do this week",
 "blocks":[
  ("li","Publish one short post explaining the Fulfillment Layer in plain language."),
  ("li","Run 5 discovery calls using the script in section 3."),
  ("li","Close the first £999 audit within 7 days."),
  ("li","Build the first live agent and ship by day two."),
  ("li","Collect results, record a case study, publish again."),
  ("callout","Repeat until the model is proven. Then scale with sub-agents, not more of you."),
  ("li",SITE),
  ("li",BOOK),
  ("quote","First movers with a real fulfillment layer own the category."),
 ]})
