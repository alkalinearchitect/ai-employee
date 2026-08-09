#!/usr/bin/env python3
"""Owl leads tracker — simple JSON pipeline.
Usage:
  owl_leads.py add <name> <company> <channel> <pain...>
  owl_leads.py list
  owl_leads.py show <id>
  owl_leads.py update <id> <field> <value...>
Fields: name, company, channel, pain, score (int), status
Status flow: new -> contacted -> replied -> call -> closed_won | closed_lost
"""
import json, sys, os, datetime
PATH = os.path.expanduser("/root/ai-employee/revenue-os/leads.json")

def load():
    if os.path.exists(PATH):
        try:
            return json.load(open(PATH))
        except Exception:
            return []
    return []

def save(d):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    json.dump(d, open(PATH, "w"), indent=2)

def nid(d):
    return max([x.get("id", 0) for x in d], default=0) + 1

CMD = sys.argv[1] if len(sys.argv) > 1 else "list"

if CMD == "add":
    d = load()
    name = sys.argv[2] if len(sys.argv) > 2 else "?"
    company = sys.argv[3] if len(sys.argv) > 3 else "?"
    channel = sys.argv[4] if len(sys.argv) > 4 else "?"
    pain = " ".join(sys.argv[5:]) if len(sys.argv) > 5 else ""
    rec = {"id": nid(d), "name": name, "company": company, "channel": channel,
           "pain": pain, "score": 0, "status": "new",
           "created": datetime.date.today().isoformat()}
    d.append(rec)
    save(d)
    print(f"Added lead #{rec['id']}: {name} @ {company} ({channel})")
elif CMD == "list":
    d = load()
    if not d:
        print("No leads yet. Add one: owl_leads.py add <name> <company> <channel> <pain>")
        sys.exit()
    for x in d:
        print(f"#{x['id']}  {x['name']} @ {x['company']}  [{x['channel']}]  score={x['score']}  status={x['status']}")
        if x.get("pain"):
            print(f"      pain: {x['pain']}")
elif CMD == "show":
    lid = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    for x in load():
        if x["id"] == lid:
            print(json.dumps(x, indent=2))
            break
    else:
        print("not found")
elif CMD == "update":
    lid = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    field = sys.argv[3] if len(sys.argv) > 3 else ""
    val = " ".join(sys.argv[4:])
    if field == "score":
        try:
            val = int(val)
        except Exception:
            pass
    d = load()
    for x in d:
        if x["id"] == lid:
            x[field] = val
            save(d)
            print(f"#{lid} {field} -> {val}")
            break
    else:
        print("not found")
else:
    print(__doc__)
