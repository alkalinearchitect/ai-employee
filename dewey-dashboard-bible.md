# Dewey Dashboard & Demo Bible — Plain English, Full Steps

Owner: Human Architect / Owl
Audience: T (final judge), operators, and anyone building the managed-AI-employee product.
Updated: 2026-08-10
Source tier: VERIFIED (what exists on this VPS) + BUILT THIS SESSION (PDF export) + GAP (what's missing).

---

## 0. THE ONE-LINE ANSWER

**Dewey (Nick's agent) has NO client dashboard.** The client talks to the agent inside
their own Slack / Telegram / iMessage. The operator (Nick) watches fleet health through
a paid tool called Latitude. The chat thread IS the interface.

**We have something better — but it's half-built.** On this VPS we have:
- a real working **site-audit demo** (the Auditor),
- a **dashboard shell** (frontend only, no live data yet),
- and (added this session) a **PDF export** on the audit so the demo becomes a deliverable.

The honest status: the demo works, the dashboard is a shell, the PDF is now real.

---

## 1. WHAT DEWEY / NICK'S STACK ACTUALLY DOES

Per the Dewey knowledge base (verified from Nick's posts + Corey Ganim thread):

| Piece | What it is | Who sees it |
|---|---|---|
| The agent | A Hermes agent built per client, lives 24/7 | Client, in their Slack/Telegram |
| Onboarding | Discovery call recorded in Granola → agent built → dropped into client's Slack | Nick + client |
| Support | iMessage group chat with client for ongoing support | Nick + client |
| Fleet view | Latitude (paid observability) shows all agents' health | Nick only |
| Client dashboard | **None.** The chat thread is the UI | — |

**The gap this creates (T's Aug 10 thesis):** a chat bubble hides capability. Users feel
"magic" for ~30 seconds, then stall ("what else can it do?") and churn in a week.
**Fix:** ship a REAL app behind the agent — a control panel showing every feature/workflow
so users build intuition. The agent is the operating layer UNDER the conversation.

We already named ours: **Owl Operations Dashboard** (`/root/ai-employee/dashboard.html`).

---

## 2. WHAT WE HAVE ON THIS VPS (verified file paths)

### A. The Auditor (REAL, WORKING) — our demo tool
Location: `/root/ai-employee/auditor/`
- `auditor.py` — scrapes a company website, finds "manual work tells", guesses industry.
- `assessor.py` — turns raw signals into plain English: their bottleneck + how an AI employee helps.
- `app.py` — Flask web app (port 5005). Paste a URL → see the audit on screen.
- `pdf_audit.py` — **ADDED THIS SESSION.** Builds a black/white PDF from the audit result.
- PDF route `/audit-pdf` — **ADDED THIS SESSION.** Download button on the result page.

What it does, step by step:
1. You paste a company URL (e.g. a dentist, solicitor, estate agent).
2. It fetches their LIVE site and reads real signals: tech stack, number of pages,
   emails, and vocabulary that shows manual work ("enquiry", "appointment", "review").
3. It matches those words to "manual tells" = work a human does by hand an agent can own.
4. It labels the industry (Dentists, Solicitors, Estate Agents, etc.) if it's one that
   hasn't adopted AI yet — flagged "under-served by AI".
5. The assessor writes the bottleneck + "how we help" in plain words.
6. **Honesty rule baked in:** scraped facts are labelled real; the bottleneck wording is
   labelled "our assessment, not a claim about the company." No invented numbers.

Tested live this session: `https://www.mydentist.co.uk/` →
industry=Dentists, 55 pages, 7 manual tells, "under-served by AI" = TRUE. PDF built,
valid, zero violet.

### B. The Dashboard (SHELL ONLY — not live)
Location: `/root/ai-employee/dashboard.html`
- Shows: Revenue (£5k/client/mo), Active clients, Agents healthy, Alerts.
- Client table + alerts table.
- **Problem:** it fetches `/api/state`, `/api/agents/fleet`, `/api/agents/alerts` —
  **no backend serves those endpoints.** So today it shows "0 clients / No agents."
- It's a blueprint. To make it real we need a tiny backend that reads real cron/agent
  state and returns JSON. (See Section 5, Gap 1.)
- Note: it uses violet `#7A5CFF` in the CSS. That's off the NOHUMA PDF brief (no violet),
  though acceptable on a screen. For a black/white PDF deliverable we keep violet OUT.

---

## 3. HOW THE DEMO IS RUN (for a prospect, live)

Plain steps — anyone can do this:

1. On the VPS, start the auditor: `cd /root/ai-employee/auditor && python3 app.py`
2. It serves on `http://localhost:5005` (or expose via Tailscale/Cloudflare for remote).
3. Open it. Paste the prospect's website URL. Hit "Run audit".
4. Show them, on screen: their industry, the manual tasks a person does by hand,
   and exactly how an Owl worker would own each one.
5. Hit "Download PDF audit" → a black/white one-pager lands. Hand it over / send to Telegram.
6. The close: "We'd build you that worker. Live in 48 hours. £5k/month. If it hasn't
   paid for itself by day 30, first month's on us."

Why this demo lands: it's not a pitch deck — it's THEIR site, read live, with THEIR
bottleneck named. No fake stats. The PDF is the leave-behind.

---

## 4. HOW THE CLIENT USES IT (the real product, post-sale)

Per the verified Dewey method, the client experience is:

1. **Discovery call** (20 min) — we map the one workflow that drains them.
2. **We build the worker** — it goes INTO their existing Slack or Telegram. No new app to learn.
3. **Crawl-walk-run onboarding** — "set it up in Slack, talk to it in Slack for a bit."
   Don't oneshot. Treat it like onboarding a new human employee ("your intern on day three").
4. **They watch it work** — it drafts replies, chases invoices, books slots, writes the
   weekly report. They approve, it sends.
5. **The operating layer (OUR edge over Nick):** instead of only a chat thread, we give
   them the Owl dashboard — a real app showing every task, approve/reject, hours saved.
   This is what stops the 1-week churn.

Difference from Nick's stack (by design):
- Nick uses paid services (Orgo, Composio, AgentMail, AgentPhone, Latitude).
- We run self-hosted on this VPS, free stack, Beacons for payments.
- We add a client-facing dashboard. Nick doesn't.

---

## 5. THE GAPS (honest — what's NOT done)

1. **Dashboard has no backend.** `dashboard.html` calls APIs that don't exist.
   Fix: write a small Flask/JSON backend that reads real cron health + agent sessions
   and serves `/api/state`, `/api/agents/fleet`, `/api/agents/alerts`. ~1 file.
2. **No live client yet.** 0 paying clients. The auditor + PDF are the top of funnel;
   the close is human (T on the call).
3. **Auditor runs locally only.** To demo remotely, expose port 5005 via Tailscale
   funnel or Cloudflare tunnel. Not done.
4. **Dashboard violet.** If we ever PDF the dashboard, strip `#7A5CFF` to steel/white.
5. **No auth on auditor.** Anyone with the URL can run audits. Fine for demo, lock down
   before any public exposure.

---

## 6. QUICK REFERENCE — THE FULL STEP CHAIN (audit → PDF → client)

```
Prospect URL
   ↓  auditor.py fetches LIVE site
Real signals (stack, pages, tells, industry)
   ↓  assessor.py reasons
Bottleneck + "how we help" (labelled assessment)
   ↓  app.py renders
On-screen audit + Download PDF button
   ↓  pdf_audit.py (reportlab, black/white, no violet)
nohuma-audit-<domain>.pdf  ← the deliverable
   ↓  send to Telegram 813848257 OR hand to prospect
Close: £5k/mo, live in 48h, day-30 refund
   ↓  post-sale
Worker in client's Slack/Telegram + Owl dashboard (operating layer)
```

---

## 7. FILE INDEX

| File | Status | Purpose |
|---|---|---|
| `/root/ai-employee/auditor/auditor.py` | VERIFIED working | scrape + detect manual tells |
| `/root/ai-employee/auditor/assessor.py` | VERIFIED working | signals → plain-English story |
| `/root/ai-employee/auditor/app.py` | VERIFIED working | web demo + PDF route |
| `/root/ai-employee/auditor/pdf_audit.py` | BUILT this session | black/white PDF builder |
| `/root/ai-employee/dashboard.html` | SHELL (no backend) | Owl ops dashboard frontend |
| `/root/ai-employee/dewey-knowledge-base.md` | VERIFIED | source of Dewey/Nick facts |

END OF BIBLE
