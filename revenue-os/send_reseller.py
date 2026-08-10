import os, requests
tok=None
for line in open('/root/.hermes/.env'):
    line=line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok=line.split('=',1)[1]; break
chat=813848257
base='/root/ai-employee/revenue-os'
items=[
 ('out/nohuma-reseller-programme.pdf','NOHUMA — Reseller Programme (FULL PDF, v2 brand, 9pp). Model, 30% margin, tiers, onboarding, white-label, guarantee. The closable path to wealthy brands via channel leverage.'),
 ('reseller-targets.md','NOHUMA — Reseller outreach targets: real UK MSPs, AI agencies, franchise consultancies (Cloudtango, Elevate AI, Agent Maestro, ZackBot, Familia, etc). Working list, verify before send.'),
]
for fn,cap in items:
    path=os.path.join(base,fn)
    if not os.path.exists(path): print("MISSING",fn); continue
    with open(path,'rb') as fp:
        r=requests.post(f'https://api.telegram.org/bot{tok}/sendDocument',
            data={'chat_id':chat,'caption':cap}, files={'document':(os.path.basename(fn),fp)}, timeout=120)
    print(os.path.basename(fn),'SENT OK' if r.json().get('ok') else 'FAIL: '+r.text[:160])
