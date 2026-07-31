# Dewey Knowledge Base — Front-Facing Owl Telegram Assistant

Owner: Tyson Architect / HumanitAI
Source tier: VERIFIED / UNVERIFIED labeled
Updated: 2026-07-30

---

## 1. Identity

**Nick Vasilescu**
- Handles: @nickvasiles (X), @nickvasilescu (GitHub/Instagram)
- LinkedIn: linkedin.com/in/nick-vasilescu-426445392
- Location: San Francisco Bay Area
- Role: Cofounder of Orgo; founder of Agent Empire
- Verified followers X: 14,293 (as of 2026-07-29)

**Dewey**
- Nick's Hermes agent; acts as principal operator for his managed-AI-employee business
- Dewey builds, deploys, and supports client AI employees
- Runs on Hermes Agent + Orgo cloud computers
- Communicates with Nick via iMessage; handles onboarding and support autonomously
- Nick describes Dewey as: "forward deployed engineer", "chief of staff", "co-founder"

VERIFIED: Nick's public posts + Corey Ganim thread + repo nicks-stack confirm Dewey exists and operates as described.

---

## 2. Business Model

**Offer:** Managed AI employee
- Always-on Hermes agent built and supported for the client
- Includes computer/VM, email, phone/IM, tools, payment rail, knowledge base, observability

**Price:** $5,000/month per client
- Community note: often practiced as unlimited agents for ~$5K/month, typically 3-5 agents per client
- Payment: client pays T via Beacons; agent operational spend via T's payment rail

**Delivery promise:** Same-day or within 48 hours after payment/wire

**Target client:** Real businesses doing $1M–$2M+ annual revenue
- NOT startups; SMBs pay more and ask fewer questions

**Role split:**
- Human (Tyson): discovery calls, relationship, close deal, answer agent questions
- Agent (Dewey/OWL): build client agent, onboard into platform, ongoing support, deploy VMs

VERIFIED: Closed design agency client on 2026-07-21 confirmed in Nick's post.

---

## 3. The 8 Parts of Every AI Employee

1. Computer — this VPS or Orgo cloud VM
2. Email — domain alias per client
3. Phone/IM — Telegram/Slack/iMessage
4. Comms — client's Slack or Telegram thread
5. Tools — Hermes skills + terminal/file/web
6. Payment — client pays via Beacons; agent spends via operator card
7. Knowledge — client context file: one fact, one home
8. Observability — cron health → Telegram alert

VERIFIED: Corey Ganim thread explicitly lists: email, phone, card.

---

## 4. Stack: 80/20 Reference

**Harness:** Hermes Agent or OpenClaw

**Models:** gpt-5.5 default via Nous; gpt-5.6-sol; Grok 4.5 for low-reasoning speed

**Cloud computer:** Orgo VM — 8GB RAM / 4 CPU minimum per docs.orgo.ai

**Messaging:** Telegram, Slack, iMessage, SMS via AgentPhone webhook bridge

**Knowledge base:** Obsidian HermesVault

**Memory:** Honcho

**Integrations:** Composio +1000 apps

**Observability:** Latitude

**Agent services:** AgentMail, AgentCard, AgentPhone

**Notetaker:** Granola for discovery call recording

**macOS workspace:** OS1 app optional

Package agent card/email/phone: ~$20/month

VERIFIED: Listed in nicks-stack README + Corey Ganim thread.

---

## 5. Core Workflow: 48-Hour Delivery

1. Discovery call recorded in Granola
2. Client dumps docs/context into Slack or Telegram
3. Discovery transcript automatically turned into skills
4. Templated stack cloned for each client via Orgo
5. Agent built and onboarded autonomously by Dewey/OWL
6. Client wires money; agent live same day/48h

**Postal rule:** The valuable skill is asking the right questions and knowing which tool to point the agent at.

---

## 5.5 Verified METHODS (from Nick's own YouTube transcripts + X posts, 2026-07-31)

**A. The 8 components of a useful AI employee (from "build an AI employee" masterclass, video fAhwYrjmQRk):**
1. Computer (Orgo VM / VPS)
2. Email (domain alias)
3. Phone number (AgentPhone / iMessage)
4. Comms channel (Telegram / Slack — "meet the customer where they are")
5. Tools & connectors (Composio +1000 apps, MCPs)
6. Card (AgentCard — so the agent can spend autonomously)
7. Knowledge base (Obsidian vault — "one fact, one home")
8. Observability (Latitude — fleet-wide signal monitoring)

**B. Architecture: 1 orchestrator + N sub-agents (VERIFIED from transcript):**
- Build ONE strong general-purpose main agent = orchestrator.
- It hands off to specialized sub-agents: outbound lead gen, sales follow-up, content/assets, support, etc.
- WHY: isolation minimizes blast radius — "if you can create sub agents, you minimize the blast radius of things that can go wrong."
- T's /root/dewey/AGENTS.md already mirrors this (orchestrator + 4 sub-agents).

**C. Business build/fulfill method (from managed-agent workshop w/ Jordan, video kdvm_kRZk8A):**
- Charge $5K/month, EVERYTHING included (usage, agents, tokens). No separate line items.
- Crawl-walk-run onboarding: "set it up with Slack. Talk to it in Slack for a little bit." Don't oneshot.
- Onboarding a client agent ≈ onboarding a new human employee ("your intern on day three").
- Most common client interface: Telegram + Slack.
- Orgo computer has Slack pre-installed; agent can self-configure Slack/Telegram via computer-use.

**D. OCA offer framework (from xTxb922RCP0 — OpenClaw Agency pitch):**
- OLD model: high-ticket one-off, 30–45 days custom code, weak retainer. SCRAPPED.
- NEW offer: charge retainer UP FRONT, deliver ONE full automation in <7 days, money-back guarantee if not fulfilled in 7 days.
- "You give them an entire automation under 7 days — you just infiltrated their business with the agent."
- Then expand to fleet / B2B2B resell.

**E. X posting patterns (VERIFIED — how Nick markets):**
- Lead with a RESULT + a contrarian hook: "My Hermes agent builds AI employees for me. Just closed another $5K/mo customer. I'm not even building any of it."
- Show the human's tiny role: "All I do is ask the questions, record in Granola, Dewey takes over."
- Punch down on skepticism: Corey Ganim reply "bUt wHy wOuLd SoMeOnE pAy $5k/mo WhEn ClAuDe Is $20" → rebut with value (no maternity leave, no complaints, half cost of a domestic employee).
- Shoutout ecosystem (#orgo #orca_build) — network effects.
- Post cadence: multiple posts/day, same-day as wins.

**F. Discovery → delivery (consolidated, VERIFIED):**
1. Discovery call (Nick uses Granola notetaker to record).
2. Hand brief to Dewey → Dewey builds the client's Hermes agent + onboards to Slack.
3. 48h to live. Weekly improvements included.

## 6. Verified Signals

- Closed $5K/month client on 2026-07-21 (design agency, Slack onboarded)
- Multiple client agents onboarded via Dewey, including "Titan"
- 200+ Orgo computers under fleet management
- Agent uses iMessage group chat with clients for ongoing support
- Dewey signed up for Higgsfield and paid using agent card autonomously
- Testing multiple Hermes agents inside Buzz workspace as of 2026-07-28
- Giving agents their own iMessage phone numbers for loop notifications (2026-07-29)

VERIFIED: From Nick's X posts and Corey Ganim thread.

---

## 7. GitHub / Tooling

**nicks-stack**
- URL: https://github.com/nickvasilescu/nicks-stack
- Stars: 104, Forks: 30
- Ready-to-run Hermes agent template for Orgo
- Components: Hermes v0.18, gpt-5.5 default, Telegram QR onboarding, 13 MCPs, 1Password secrets, Dewey SOUL.md + 21 genericized skills

**hermes-desktop-os1**
- URL: https://github.com/nickvasilescu/hermes-desktop-os1
- Stars: 513, Forks: 89
- Native macOS workspace for Hermes on Orgo cloud computers

---

## 8. Quotes

- "the people who get the most out of hermes are using it as a chief of staff, AI employee, or a co-founder"
- "agents building agents is here"
- "nobody pays $5K/month for an agent that doesn't make them money"
- "build the client an agent, then help them resell it to THEIR customers. B2B2B never churns"
- "speed to value wins. the same day a client wires money, ship them something. agent live by day two"
- "sell to real businesses, not startups. SMBs doing $1M to $2M minimum pay more and ask fewer questions"
- "accepting that i, the human, am the bottleneck. time to let the agents do what they promised society"

---

## 9. T's Dewey Clone Mapping

**What T already has:**
- `AGENTS.md` at /root/dewey/AGENTS.md with orchestrator + 4 sub-agents
- client-agents scripts: create-client-agent.sh, deploy-client.sh, manage-client.sh
- dewey-clone-agent manifest.json
- Telegram gateway live: chat 813848257
- Revenue separated: Dewey income = T's personal Ltd, NOT HumanitAI CIC

**Difference from Nick's stack:**
- T does NOT use Orgo/Composio/AgentMail/AgentPhone/Latitude per current rules
- T runs self-hosted on own VPS; Nick uses Orgo cloud computers
- T uses Beacons for payments; Nick uses agent card directly
- T uses free-stack-only by default; Nick uses paid agent services (~$20/month)

---

## 10. Support Scripts Reference

**New client setup (T's version):**
1. `mkdir -p clients/<name>` + context.md + delegation.md
2. Wire comms: Slack webhook or Telegram thread
3. Add health-check cron → Telegram alert chat 813848257
4. Dry-run one task; verify no external paid service

**Manifest location:** /root/client-agents/dewey-clone-agent/manifest.json
**Operating manual:** /root/dewey/AGENTS.md
**Replica setup guide:** /root/client-agents/DEWEY-REPLICA-SETUP.md

---

## 11. Front-Facing Answers for Owl Telegram

**Q: What is Dewey?**
A: Dewey is a managed AI employee — an always-on agent that handles tasks, customer support, onboarding, and operations for small businesses. It's built on Hermes Agent and operates 24/7 through Telegram, Slack, or iMessage.

**Q: How much does it cost?**
A: $5,000/month per client, typically covering 3-5 agents. Clients are real businesses doing $1M–$2M+ in annual revenue.

**Q: How fast can it be live?**
A: Same-day or within 48 hours after payment. Discovery call → agent build → platform onboarding → live.

**Q: What can the AI employee actually do?**
A: 24/7 customer support, lead follow-up, task execution, ops automation, email/phone management, cloud computer booking, fleet management, and autonomous client onboarding.

**Q: Do I get my own agent or share one?**
A: Every client gets isolated agents with separate profiles, tokens, folders, sessions, and threads. One break doesn't take down the whole system.

**Q: What stack do you use?**
A: Hermes Agent + cloud VM + Telegram/Slack + Obsidian knowledge base + Honcho memory. No bloat, no unnecessary SaaS.

**Q: Is this for startups or real businesses?**
A: Real businesses. SMBs doing $1M–$2M+ annual revenue. They pay more and ask fewer questions.

**Q: Who is behind this?**
A: Tyson Architect / HumanitAI. Dewey is our managed AI-employee service. Revenue goes through T's personal business, not the CIC.

---

## 12. Open Gaps / UNVERIFIED

- Exact Hermes profile configs used in production for client agents (T's factory uses generic SOUL.md template, not Nick's 21 genericized skills)
- Exact prompts for turning discovery transcript → skills (Nick mentions Granola→skills but no public prompt)
- Agent Mail / Agent Phone exact provisioning steps (Nick uses paid services; T uses free stack — gap by design)
- Whether current VPS factory matches Orgo template — NO, T uses simplified self-hosted model (hosting already here)
- XQUIK_API_KEY not set on VPS → programmatic X scraping blocked; direct web_extract of X posts works
- TRANSCRIPT_API_KEY not held → YouTube transcripts pulled via prior session scrape (7 transcripts in /root/dewey/nick_vids/)

---

END OF KNOWLEDGE BASE
