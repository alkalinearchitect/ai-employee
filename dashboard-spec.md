# Dewey/Owl Operational Dashboard — Spec

## 1) What T currently monitors (and how)

| Method | Source | Frequency |
|--------|--------|-----------|
| Telegram alerts | `~/.hermes/cron/output/*.log` piped by cron to chat `813848257` | event-driven / per gate fail |
| CLI agent list | `manage-client.sh list` (scans `client-agents/*/manifest.json` + `pgrep`) | ad‑hoc |
| CLI agent logs | `manage-client.sh logs <name>` tails `~/.hermes/profiles/<name>/logs/gateway.log` | ad‑hoc |
| CLI system health | `manage-client.sh health` (memory/disk/load + per-agent RSS) | ad‑hoc |
| systemd status | `systemctl --user status hermes-gateway` | ad‑hoc |
| Vault consistency | cron job `Vault Consistency Check` → Telegram if fails | daily 06:00 |
| Security watchdog | cron job (`Security Watchdog`) → Telegram if gate fails | every 240m |
| VPS health monitor | cron job (`VPS Health Monitor`) → Telegram if gate fails | 09:00 + 21:00 |

Live stack state (now):
- Gateway: active (running) but repeatedly **crashing at startup** because default model `poolside/laguna-s-2.1:free` via OpenRouter returns HTTP 401, and cron model `tencent/hy3:free` on Nous returns HTTP 404.
- Clients: **2 real manifests** (`test-dryrun`, `test-dryrun-agent`), both `status=created`. No live production clients visible yet.
- Handlers: Hermes CLI (subagent), stealth-browser MCP, no Orgo/Composio.
- Revenue track: hardcoded £5,000 in `dashboard.html` only — no per-client revenue ledger.

---

## 2) Gaps vs a real operational dashboard

| Need | Current | Gap |
|------|---------|-----|
| **Cron failure visibility** | Telegram ping per fail; some crons failing silently for days | No aggregated failure rate, no trend, no "who failed first/today/7d" |
| **Provider / model health** | Unknown until a 401/404 blows up a cron | No auth status card, no model-availability check, no latency probe |
| **Agent-alive vs manifest drift** | `manage-client.sh list` flags "running but no process" | No live age/last-ping metric, no diff by client |
| **Client SLA / outcomes** | None | No reply-latency, no outbound touch count, no comms-channel status |
| **Gateway API server state** | Gateway warning in logs | Dashboard must not depend on `api_server` if it's disabled; must read systemd directly |
| **Security posture** | Telegram on fail only; earlier false positives from stale port allowlist | Need classified port table with owner field instead of flat "unexpected" |
| **Revenue / ARR** | Static text in `dashboard.html` | No ARR tracker, no payment status, no renewal flags |
| **iMessage/Signal bridge** | Not wired yet | Dashboard should be comms-agnostic (Telegram + Slack + future iMessage) |

---

## 3) Exact widgets / data sources needed

### Widget A — "Cron Heartbeat" (top-left)
**One row per job.**
Data source: `~/.hermes/cron/jobs.json` + `~/.hermes/cron/executions.db` (SQLite `executions` table)
Columns: Job | Schedule | Last run | Last status | Fail 24h | Fail 7d | Next run

Derived columns:
- `fail_24h` = `COUNT(*) FROM executions WHERE job_id=? AND status='failed' AND claimed_at > now-24h`
- `fail_7d` = same, 7 days
- Color: green <= 0 fails, yellow 1–2, red 3+

### Widget B — "Provider & Model Health" (top-center)
**One card per provider.**
Data sources:
- Nous `https://inference-api.nousresearch.com/v1/models` (auth probe)
- OpenRouter `https://openrouter.ai/api/v1/models` (auth probe)
- Default-model smoke test: lightweight `POST /chat/completions` with `max_tokens: 1`
Columns: Provider | Auth | Models reachable | Default model | Latency | Last error

Must also highlight: `tencent/hy3:free` 404 on Nous; `poolside/laguna-2.1:free` 401 on OpenRouter (currently the real blockers).

### Widget C — "Agent Fleet" (top-right)
**One row per client agent.**
Data sources: `client-agents/*/manifest.json` + `pgrep -f hermes.*gateway.*<name>` + ps RSS
Columns: Agent | Client | Job | Channel | PID | RSS | Uptime | Manifest vs process drift

Drift flag = `status` field `running` but no PID → red.

### Widget D — "Comms / Client" (center table)
**One row per client bound to a channel.**
Data sources: `client-agents/*/manifest.json` (platform + thread metadata), Telegram inbound logs, Slack webhook status
Columns: Client | Channel | Last inbound | Last outbound | Status | Notes

"Last inbound" = newest event timestamp from telegram/Slack inbound logs. Without an event bus, derive from `gateway.log` grep for `<client_id>` or workspace routing tag.

### Widget E — "Security Snapshot" (left sidebar)
Pulled from last `security-watchdog.log` run.
Columns: Ports (classified by owner; unknown = red), Auth fails 24h, Suspicious procs, Cron fails 24h

Must classify: 22=ssh, 443=vps-gateway:443/tailscale, 3002=firecrawl, 8080=agent-os, 8799=webui, 8765=custom. "Unexpected" = red.

### Widget F — "Gateway State" (right sidebar)
Data source: `systemctl --user show hermes-gateway --property=ActiveState,SubState,ExecMainStartTimestamp,FragmentPath,NRestarts`
Columns: Status | Uptime | Restarts | API server enabled | Last error

Read API server state from `gateway.log` latest — currently refuses to start because `API_SERVER_KEY` is rejected. Dashboard must not crash in absence of `api_server`.

### Widget G — "ARR & Revenue" (top strip)
**Hard numbers.**
Data sources: `client-agents/*/manifest.json` count of `status=running`, not hardcoded £5,000.
Columns: Active clients | ARR (running × £60k) | This‑month billable | Outstanding renewals

No ledger exists yet; dashboard should surface **missing data** clearly rather than fake numbers.

### Widget H — "Alert Timeline" (bottom table)
All alerts rendered as a unified stream, not per-silo.
Sources: recent lines from `~/.hermes/cron/output/*.log`, `~/.hermes/logs/errors.log`, last_run errors from `jobs.json`
Columns: Time | Source | Severity | Message | Link

---

## 4) Priority build order

### P1 — Replace ad-hoc Telegram debugging (this week)
1. **Cron Heartbeat** (Widget A) + **Provider Health** (Widget B)
   - Why: T already receives per-fail Telegram pings. These two cards consolidate all those pings into one glance. Currently 5/13 jobs failing; T can't see the failure rate at a glance.
   - Implementation: static `cron.html` that reads `jobs.json` + executes the SQLite `executions.db` queries, hits Nous `GET /v1/models` and OpenRouter `GET /v1/models` (no-auth falls back to "unknown"), renders a table. Auto-refresh every 120s.
   - Source paths to actually use:
     - `/root/.hermes/cron/jobs.json` → `json.load()`
     - `/root/.hermes/cron/executions.db` → `sqlite3`
     - `/root/.hermes/cron/output/security-watchdog.log` → last run parse
     - `/root/.hermes/cron/output/health-monitor.log` → latest gate states
     - `/root/.hermes/logs/gateway.log` → API server / auth errors
   - Tech: pure client-side HTML + fetch against a tiny `/root/ai-employee/backend/state.py` that returns JSON. No new infra.

2. **Alert exhaust reducer**
   - A backend script (`/root/ai-employee/backend/cron-alert-suppressor.py`) that evaluates the verifier gates and **only pages Telegram if**:
     - a.) a new job fails for the first time, or
     - b.) an existing failure switches to healthy.
   - This turns the 5 current failing-until-healthy pings from screaming into a single-once alert, drastically reducing iMessage/Telegram noise.

### P2 — Replace `manage-client.sh list` (next week)
3. **Agent Fleet** (Widget C) + **Gateway State** (Widget F)
   - Why: stops T from SSH-ing in to run bash commands.
   - Data: `pgrep`-like logic via `ps aux` in backend; manifest json parse.
   - Surface: uptime, RSS, manifest drift.

### P3 — Client SLA & Comms (next week after P2)
4. **Comms / Client** (Widget D)
   - Parse `gateway.log` for inbound/outbound per client workspace ("platform routing key"). Derive last-inbound per client.
   - If no inbound found for > 6h → yellow; > 12h → red (matches current "agents healthy" definition in `dashboard.html`).

### P4 — Revenue & ARR (after T confirms client list)
5. **ARR & Revenue** (Widget G)
   - Source-of-truth: `client-agents/*/manifest.json` client name + billing status (extend manifest schema with `monthly_revenue_gbp` and `status=running`).
   - Compute: `SUM(monthly_revenue_gbp) where status=running`, this-month tick as fractional ARR.

### P5 — Hardening / breadcrumbs
6. **Security Snapshot** (Widget E) with owner-classified ports.
7. **Alert timeline persistence**: append every cron failure to `~/.hermes/cron/output/watchdog-state.json` so the backend can dedupe.

---

## Non-goals (Do NOT build)
- iMessage bridge (T either wires via Hermes plugin later or keeps Telegram).
- Add Orgo/Composio/paid observability (explicit out-of-scope per AGENTS.md).
- Rebuild the static marketing site at `/root/ai-employee/dashboard.html` — make it shell out to `/root/ai-employee/backend/state.py` first; only rebuild markup after backend exists.

---

## Backend sketch — exact endpoints to build at `/root/ai-employee/backend/state.py`

```python
# endpoints
GET /api/state              → exact JSON used by dashboard.html
GET /api/cron/jobs          → jobs.json + sqlite fail counts (24h, 7d)
GET /api/cron/failures      → {job_id, message, last_error, last_failed_at}
GET /api/providers          → {nous: {auth: bool, models_count, default_model, latency_ms, last_error}, openrouter: {...}}
GET /api/agents/fleet       → [{name, client, job, platform, pid, rss_mb, uptime, manifest_status, drift}]
GET /api/agents/alerts      → [{time, source, level, message, detail}]
GET /api/vps/security       → from last security-watchdog.log run
GET /api/vps/gateway        → systemctl --user show hermes-gateway
```

Live deployment:
- Backend: `/root/ai-employee/backend/state.py`
- Port: `33331` on `127.0.0.1`
- Frontend reads `/backend` when hosted, or `http://127.0.0.1:33331` when local
- Currently running PID is available via Hermes background process management under session `proc_12061bfa1d0f`

Read `/root/.hermes/cron/jobs.json` directly — it already contains everything you need except fail counts, which come from `/root/.hermes/cron/executions.db`.
