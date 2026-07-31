# Technical Proposal — Arsenal FC AI Employee
**To:** Head of Software & Analytics, Arsenal Football Club  
**Executive Sponsor:** Nick Vasilescu / Dewey Autonomous Operator  
**Stack:** Python (PyData) + SQL + TypeScript  
**Environment:** Club-existing data vendor feeds → internal PostgreSQL + dbt → dashboard → Slack

---

## 1. Integration Assumptions

We build on top of the data layer Arsenal already licenses and normalizes internally. We do not resell data or build another subscription dashboard. We build **orchestration software** that sits inside your estate.

| Input | Expected form | Where it sits today (public signal) |
|---|---|---|
| Opta / StatsBomb event stream | JSON / parquet exports | Standard in top-flight analytics |
| Player tracking (optical / GPS) | Second Spectrum / Catapult CSV/JSON | Listed in Research Engineer job scope at Sobha Realty Training Centre |
| Video timestamps | Match-phase XML / proprietary tool exports | Standard video analysis workflow |
| Internal context | Injury, minutes, selection spreadsheets | Club ops |

If Arsenal does not currently ship these into a single warehouse, the AI employee’s first deliverable is the **normalization layer** — because model accuracy depends on feature consistency.

---

## 2. Full-Stack Application Spec

### 2.1 Repo Layout

```
arsenal-ai/
├── pipelines/               # Airflow / Prefect orchestration
│   ├── dbt_project/         # dbt models with tests
│   ├── extract_raw.py       # vendor-specific ingestors
│   └── transform_core.py    # feature engineering
├── models/                 # PyData packages
│   ├── xg/
│   ├── pass_network/
│   ├── setpiece/
│   └── availability/
├── api/                    # FastAPI service (internal)
│   ├── routers/
│   └── schemas/
├── web/                    # TypeScript/React plugin
│   ├── public/
│   ├── components/
│   └── app.tsx
├── ops/                    # Docker, env, cron
└── knowledge/              # Club context, opponent IDs, feature flags
```

### 2.2 Core Application Server

```python
# api/app.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pipelines.transform_core import feature_store
from models.xg import xg_model
from models.pass_network import spatial_network

app = FastAPI(title="Arsenal AI Employee — Internal API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://intra.arsenal.internal"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/api/v1/xg/match/{match_id}")
def match_xg(match_id: str, user=Depends(auth_club_internal)):
    chain = feature_store.build_xg_chain(match_id)
    return {
        "match_id": match_id,
        "xg_for": xg_model.team(chain, team="Arsenal"),
        "xg_against": xg_model.team(chain, team="opponent"),
        "micro_events": chain.to_dict("records"),
    }

@app.get("/api/v1/network/match/{match_id}")
def passing_network(match_id: str, user=Depends(auth_club_internal)):
    coords = feature_store.pass_coords(match_id)
    return spatial_network.build(coords, method="force_directed")

@app.get("/api/v1/setpiece/corners")
def corner_optimizer(opponent_id: str, user=Depends(auth_club_internal)):
    zones = feature_store.opponent_corner_zones(opponent_id)
    return {
        "weak_zones": zones.top_conceding(n=3),
        "arsenal_strength": zones.arsenal_scoring(),
        "delivery_suggestion": zones.optimal_cross_zone(),
    }
```

Deployment: single Docker container behind club VPN. Auth via club SSO or basic bearer token until SSO is integrated.

---

## 3. Data Pipeline Architecture

### 3.1 Extract

- **Opta/StatsBomb:** scheduled parquet pull nightly during season; on-demand during match week.
- **Tracking:** optical-tracking JSON normalized to second-spectrum frame schema; GPS merged to event index via last-kick timestamp anchor.
- **Context:** internal CSV/Google Sheets exports synced via `rclone` or SFTP into `extract_raw/` with freshness check.

### 3.2 Transform (dbt + Python)

```
raw_intel
  └─ stg_matches               (clean dates, competition labels)
  └─ stg_events                (type, outcome, assist_id, under_pressure)
  └─ stg_tracking_frames       (player_id, frame, x/y, speed)
  └─ stg_player_minutes        (player, date, mins_played, injury_flag)

int_features
  └─ fct_xg_chain              (sequence_id, shot_x, shot_y, preceding_passes)
  └─ fct_pass_network_edges    (from_player, to_player, count, avg_x, avg_y)
  └─ fct_zone_defense          (zone_id, opponent, defensive_actions)
  └─ fct_availability_risk     (player_id, weekly_score, minutes_threshold)

mart_arsenal_opponent
  └─ xg_differential_last_5
  └─ corner_zone_conceded_vs_arsenal_scoring
```

Tests enforced on every run:
- `dbt test` on PK uniqueness, referential integrity, null rates.
- Feature validity: `x`/`y` coordinates within pitch boundaries (0.0–105.0 / 0.0–68.0).

### 3.3 Orchestration

Prefect (or Airflow) DAG:
```
nightly_refresh
  ├── extract_raw
  ├── dbt_run
  ├── build_features
  ├── refresh_dashboard_db
  └── post_slack_alert_if_anomaly
```

Match-day hot-refresh trigger: GitHub Actions webhook pushed by score watcher after full-time.

---

## 4. ML Models for Football Analysis

All models are **calibrated, reproducible, and explainable** — required for coaching buy-in.

### 4.1 Expected Goals Model (xG)

- **Inputs:** shot `x`, `y`, `under_pressure`, `body_part`, `play_pattern`, `deflected`, `first_time`.
- **Estimator:** Gradient-boosted trees (`XGBClassifier`) with isotonic calibration.
- **Validation:** rolling 5-fold time-split cross-validation; calibration curve logged weekly in MLflow.
- **Output:** shot probability + chain probability per match; delta vs. mean xG for rolling window.

Why it matters: Arsenal’s attacking patterns are consistent enough to evaluate whether expected value is tracking actual results. A drift signal over 5 matches flags tactical or finishing issues before they show in scorelines.

### 4.2 Passing Network Analysis

- **Spatial input:** event-level `location` + `pass` recipient coordinates, filtered to open-play successful passes.
- **Method:** force-directed graph with node sizing by betweenness centrality; linker thickness by pass count; color by location cluster (left channel, half-space, central corridor).
- **Outputs:** 
  - Per-match PNG (auto-posted to Slack after each game)
  - Rolling 5-match average network with stdev bands showing network fragmentation or over-reliance on a single hub.

> Public signal: Passing network drift is used by Premier League clubs to detect tactical regression. Arsenal’s build-up under pressure patterns make this a high-signal duty for the First Team analysis remit described in the Research Engineer role.

### 4.3 Player Tracking / GPS Load Analysis

- **Input:** Last `n` matches of optical-tracking frames (resampled to 1 Hz) plus GPS sprint counts.
- **Features:**
  - High-intensity distance per 90
  - Top speed / accelerations / decelerations profile
  - Minutes since last >90-minute performance
- **Output:** weekly `availability_risk` score (0.0–1.0) for selection meetings.

> Note: this model uses public domain feature engineering (accelerations/decelerations are standard in Catapult/Second Spectrum workflows). It does not re-identify or predict injury; it flags sustained load spikes and congested fixture stretches.

### 4.4 Set-Piece Optimization

- **Input:** corner/ free-kick delivery zones + defensive assignment locations from tracking / event data; outcome (shot, clearance, goal).
- **Method:** kernel density estimation over opponent defensive zone; compare with Arsenal scoring-density from identical delivery types.
- **Output:**
  - Top-3 delivery zones by Arsenal scoring probability.
  - Defensive weak spots where Arsenal concede from opponent corners.
  - One-page PDF auto-generated before each match with exact zones + player markers.

---

## 5. Visualization Dashboards

### 5.1 Internal Web Dashboard (React + Plotly + Deck.gl)

Route structure:

```
/overview              → squad xG delta, upcoming fixtures, availability risk
/opponent/{id}         → opponent xG profile, passing network, weak zones
/setpieces/{match_id}  → corner/free-kick PDF preview, zone maps
/players/{id}/load     → GPS load chart, minutes trend, injury risk
```

Auth: club IP whitelist + bearer token until SSO is wired. Served on internal host (e.g., `dash.internal.arsenal.com`).

### 5.2 Slack Bot Notifications

```python
# ops/alerts.py
if xg_differential[-5:] < -1.2:
    slack_alerts.post(f"⚠️ xG regression: Arsenal {sum(xg_differential[-5:])} over last 5 matches")

if AvailabilityRisk.any(above=0.85):
    slack_alerts.selection_meeting("⚠️ 3 players above 85% load — review rotation")
```

Workflow: Slack app with scoped bot token to `#analysis-first-team`, `#scouting`, `#medical`.

---

## 6. Automation Workflows

| Workflow | Trigger | Action |
|---|---|---|
| Match report post | Full-time whistle event detected | Build passing network, xG summary, opponent context; post PDF + web link to Slack |
| Weekly availability | Monday 07:00 | Recount load; alert selection meeting if any player ≥85% |
| Opponent scout | 72 hours before next match | Pull opponent last-3-match xG, zone defense, set-piece tendencies; post 2-pager |
| Monthly model audit | 1st of month | MLflow calibration report + feature-drift summary → Head of Software & Analytics |

---

## 7. Operational Model

- **Hardware:** Club-preferred cloud or on-prem Linux host; minimum 4 CPU / 16 GB RAM.
- **Data governance:** All training occurs on machine-readable event/tracking data already in circulation in elite football. No fan PII, no player biometric re-identification beyond load metrics.
- **Support:** Weekly optimization cycle; new modules shipped as feature flags; observability via club-mandated logging.

---

## 8. Why This Fits Arsenal Specifically

The Head of Software & Analytics at Arsenal — publicly identified as **Chris Dove** on LinkedIn — leads a "globally distributed interdisciplinary team of data scientists, research engineers, data engineers, insights analysts, software engineers and video analysts." The club is publicly hiring a **Research Engineer** to "plan, implement, and deploy end-to-end internal products supporting the Men's First Team" at the Sobha Realty Training Centre.

The duty set above maps 1-to-1 to that team structure and the open role’s stated remit. We are not pitching a generic analytics dashboard; we are pitching a software service that **builds** the products that role is designed to ship — faster and cheaper than a single FTE hire.
