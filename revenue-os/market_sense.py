#!/usr/bin/env python3
"""NOHUMA autonomous market-sense loop.
Runs weekly. Scans real signals on the managed-AI-employee market and writes a
dated brief to market_briefs/. No send, no spend, read-only research.
Honesty rule: cite sources, never invent stats.
"""
import os, json, datetime
from hermes_tools import web_search, write_file

OUT = "/root/ai-employee/revenue-os/market_briefs"
os.makedirs(OUT, exist_ok=True)
today = datetime.date.today().isoformat()

queries = [
    "managed AI employee market size 2026",
    "AI agent adoption SME UK 2026 statistics",
    "AI employee agency competitors pricing 2026",
    "non-human intelligence workforce trend 2026",
]

brief = {"date": today, "signals": []}
for q in queries:
    try:
        res = web_search(q, limit=3)
        for r in res.get("data", {}).get("web", []):
            brief["signals"].append({
                "query": q,
                "title": r.get("title"),
                "url": r.get("url"),
                "snippet": r.get("description", "")[:280],
            })
    except Exception as e:
        brief["signals"].append({"query": q, "error": str(e)[:120]})

path = f"{OUT}/brief_{today}.json"
write_file(path, json.dumps(brief, indent=2))
print(f"Wrote {path} with {len(brief['signals'])} signals")
