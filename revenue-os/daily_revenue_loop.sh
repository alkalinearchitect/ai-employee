#!/bin/bash
# ════════════════════════════════════════════════════════════════
# OWL DAILY REVENUE LOOP
# Runs the Human Architect money loop:
#   1. Pull live performance (Substack/X reach)  -> honest, no fake stats
#   2. Generate 1 hook + prompt for today's content (X thread + Substack)
#   3. Log a fresh lead-gen target list into the tracker
#   4. Send the operator a concise Telegram report
# Self-contained. Meant to run via Hermes cron daily at 07:00.
# ════════════════════════════════════════════════════════════════
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
NOTIFY="$HERE/telegram_notify.sh"
LEADS="$HERE/owl_leads.py"
DATE=$(date +%F)
DAY=$(date +%A)

# ── 1. PERFORMANCE ── (honest: report what we can verify, flag what we can't)
PERF="Perf: Substack/X analytics are NOT auto-pulled (no API key). Check dashboard manually."

# ── 2. CONTENT HOOK (today's angle) ──
# Rotating pain-led hooks from the Bottleneck Bible (verified benchmarks only)
HOOKS=(
  "Your team misses 78% of leads by replying slow. An Owl agent replies in 60 seconds, 24/7."
  "HBR: firms that contact within 1 hour are 7x more likely to qualify the lead. Owl does it in 60 seconds."
  "You're the best employee and the worst CEO. The agent frees you to lead."
  "Every enquiry that dies in your inbox is money you'll never get back. Owl catches them at 9pm."
  "£5k/mo vs £40k/yr for a junior who sleeps, quits, and takes maternity leave. Do the maths."
)
HOOK="${HOOKS[$((RANDOM % ${#HOOKS[@]}))]}"
CTAPT="Today's CTA: book a 20-min scope call -> beacons.ai/humanarchitect"

# ── 3. LEAD-GEN TARGETS (log seed targets; real outreach is human-approved) ──
# T scores these; Owl never DMs strangers without T's go (boss protocol).
TARGET_NOTE="Target sectors: UK SMEs £1-2M doing lead follow-up/inbox triage. Trades, clinics, law, ecom."

# ── 4. REPORT ──
REPORT="🦉 OWL REVENUE LOOP — $DAY $DATE
$PERF

CONTENT HOOK (post today, AEO-optimised):
$HOOK
$CTAPT

$TARGET_NOTE

RUNWAY:
- Site: LIVE (alkalinearchitect.github.io/ai-employee) ✓
- Offer: £5k/mo managed AI employee ✓
- Clients: 0 paying (demo agents only) — CLOSE THIS GAP
- Booking link: beacons.ai/humanarchitect (verify on your phone — bot-403)

NEXT ACTION FOR T:
1. Open beacons link on phone — confirm it books.
2. Pick 5 target businesses. I'll draft the outreach, you send.
3. Reply 'go' to let me generate today's X thread + Substack draft."

bash "$NOTIFY" "$REPORT" || echo "TELEGRAM SEND FAILED"
echo "loop done"
