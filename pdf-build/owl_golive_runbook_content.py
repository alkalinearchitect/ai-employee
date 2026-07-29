SITE="https://alkalinearchitect.github.io/ai-employee/"
BOOK="https://beacons.ai/humanarchitect"
SUB="https://substack.com/@humanarchitect"

COVER={
 "eyebrow":"HUMAN ARCHITECT  ·  OWL",
 "title":"CLIENT GO-LIVE RUNBOOK",
 "sub":"Pre-launch checklist, smoke tests, isolation checks, latency benchmarks, and sign-off criteria. Built from operational audit, 2026-07-29.",
 "tag":"If it isn't tested, it isn't live.",
 "foot":"Internal operations · VERIFIED",
}
PAGES=[]

PAGES.append({"n":2,"eyebrow":"PRIME DIRECTIVE","title":"No go-live without passing this",
 "blocks":[
  ("p","This runbook is the quality gate between 'built' and 'live.' No client sees a live agent unless every check below passes.例外: none."),
  ("callout","Operator rule: you do not ship what you have not witnessed. If you did not see it pass, it failed."),
  ("quote","Fast is fine, but verified is final."),
 ]})

PAGES.append({"n":3,"eyebrow":"SCOPE","title":"What this covers",
 "blocks":[
  ("li","<b>Identity:</b> agent name, Slack/Telegram channel, avatar/bio, owner-visible alias."),
  ("li","<b>Knowledge:</b> context.md loaded, facts reviewed by T, protected tier sealed."),
  ("li","<b>Tools:</b> only scoped skills/tools are enabled; no debug/admin tools exposed."),
  ("li","<b>Comms:</b> client-facing channel distinct from T oversight channel."),
  ("li","<b>Health:</b> cron/ping test, Telegram alert confirmed, restart benchmark noted."),
  ("li","<b>Backup:</b> profile + token + config archived before go-live."),
 ]})

PAGES.append({"n":4,"eyebrow":"PRE-FLIGHT","title":"Before you build",
 "blocks":[
  ("step_title","1 · Confirm intake"),
  ("step","Client signed agreement + intake form returned. Discovery call notes filed under clients/<name>/."),
  ("step_title","2 · Confirm isolation"),
  ("step","New profile created. No shared tokens with other clients. Run: token-isolation-check.sh <profile>."),
  ("step_title","3 · Confirm knowledge base"),
  ("step","clients/<name>/context.md is complete and reviewed: Business / Facts / Standing instructions / Failure points."),
  ("step_title","4 · Confirm billing"),
  ("step","Invoice sent, payment confirmed, client chat/channel provisioned."),
  ("callout","Do not build for a client who has not paid. No exceptions."),
 ]})

PAGES.append({"n":5,"eyebrow":"SMOKE TEST","title":"Functional checks",
 "blocks":[
  ("step_title","5 · Agent boots"),
  ("step","Start the agent. Verify process uptime >60s, no crash loops, memory within quota."),
  ("step_title","6 · Channel handshake"),
  ("step","Send 'ping' from client channel. Agent replies within latency threshold. If no reply in 90s, fail."),
  ("step_title","7 · Tone + scope"),
  ("step","Send a scoped-task prompt from the client brief. Agent replies using client brand voice, does not invent capabilities."),
  ("step_title","8 · Fallback behaviour"),
  ("step","Send an out-of-scope question. Agent declines cleanly and offers the correct path. No hallucinated promises."),
  ("step_title","9 · Tool boundary"),
  ("step","Verify only scoped tools respond. Admin/debug endpoints are not reachable from the client channel."),
  ("step_title","10 · Health alert"),
  ("step","Trigger a test alert. T receives Telegram confirmation within threshold. Fix before proceeding if missing."),
 ]})

PAGES.append({"n":6,"eyebrow":"ISOLATION + LATENCY","title":"Hard gates",
 "blocks":[
  ("step_title","11 · Token isolation check"),
  ("step","Run token-isolation-check.sh clients/<name>. Confirmed: no token overlap with other profiles."),
  ("step_title","12 · Memory/disk quota"),
  ("step","Record baseline memory and disk. Set max-memory guard. Alert if breached by >20%."),
  ("step_title","13 · Latency benchmark"),
  ("step","Measure round-trip for 5 consecutive client prompts. Median must be under threshold. If any exceeds 2x median, investigate before go-live."),
  ("step_title","14 · Backup created"),
  ("step","tar archive of profile + token + config + context.md. Stored in backup store with date and client name."),
 ]})

PAGES.append({"n":7,"eyebrow":"HANDOFF","title":"Client-facing go-live",
 "blocks":[
  ("step_title","15 · Owner intro message"),
  ("step","Send the branded intro message in the client channel: agent name, one-line purpose, one example prompt."),
  ("step_title","16 · First win"),
  ("step","Within 24 hours, the agent must complete one visible, useful task in the client channel."),
  ("step_title","17 · Health channel"),
  ("step","Confirm T oversight Telegram thread is receiving alerts. Confirm client knows who to contact."),
  ("step_title","18 · Sign-off"),
  ("step","Record go-live timestamp, baseline metrics, and client confirmation in clients/<name>/log.md."),
 ]})

PAGES.append({"n":8,"eyebrow":"FAIL CRITERIA","title":"When to halt",
 "blocks":[
  ("table",[
    ["Check","Fail condition","Action"],
    ["Boot","Crash loop or OOM within 5 minutes","Fix before go-live; escalate to T."],
    ["Channel handshake","No reply within 90s on 'ping'","Check gateway/auth; do not ship."],
    ["Tone + scope","Hallucinated capability or wrong voice","Re-load context.md; re-test."],
    ["Fallback","Agent tries to answer out-of-scope","Add deny list; re-test."],
    ["Tool boundary","Admin endpoint reachable from client","Remove exposure; verify isolation."],
    ["Health alert","No Telegram alert within threshold","Fix cron/chat ID; do not ship."],
    ["Token isolation","Shared token found","Regenerate; rebuild; re-test."],
    ["Latency","Median exceeds threshold or any >2x median","Profile/trace before go-live."],
    ["Backup","Archive missing or corrupt","Create backup; proceed only after verified."],
  ]),
 ]})

PAGES.append({"n":9,"eyebrow":"ROLLBACK","title":"If go-live breaks",
 "blocks":[
  ("p","If the agent fails after client notification, execute rollback in this order:"),
  ("li","<b>1 · Stop:</b> halt agent process immediately."),
  ("li","<b>2 · Restore:</b> revert to last known-good backup."),
  ("li","<b>3 · Verify:</b> rerun smoke test on restored snapshot."),
  ("li","<b>4 · Communicate:</b> tell the client the status and next ETA within 1 hour."),
  ("li","<b>5 · Post-mortem:</b> log root cause, fix, and prevention to clients/<name>/log.md."),
  ("callout","Never claim live again until the full smoke test passes after rollback."),
 ]})

PAGES.append({"n":10,"eyebrow":"CHECKLIST","title":"One-page sign-off",
 "blocks":[
  ("li","Intake complete and payment confirmed."),
  ("li","Profile created with isolated token."),
  ("li","context.md reviewed by T."),
  ("li","Agent boots and stays up >60s."),
  ("li","Client channel 'ping' replies within 90s."),
  ("li","Scoped prompt returns correct tone and scope."),
  ("li","Out-of-scope prompt declines cleanly."),
  ("li","Admin tools not reachable from client channel."),
  ("li","Telegram health alert confirmed."),
  ("li","Token isolation check passed."),
  ("li","Memory/disk baseline recorded."),
  ("li","Latency benchmark within threshold."),
  ("li","Backup archive created and verified."),
  ("li","Owner intro message sent."),
  ("li","First win scheduled within 24h."),
  ("li","Sign-off recorded in log.md."),
 ]})
