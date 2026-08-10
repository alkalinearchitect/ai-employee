import os, requests
tok=None
for line in open('/root/.hermes/.env'):
    line=line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok=line.split('=',1)[1]; break
chat=813848257
base='/root/ai-employee/revenue-os'
items=[
 ('out/nohuma-established-brands.pdf','NOHUMA — For Established Brands / Multi-Site (v2 brand). Positions NOHUMA for wealthy brands like CeX via reseller + white-label, NOT direct big-contract chase. 8pp.'),
 ('nohuma_channel_strategy.md','NOHUMA channel strategy — swarm analysis: reseller partnerships 8/10 (30-45d to cash) is the closable path; public-sector/enterprise-direct are traps for a 1-person studio.'),
 ('market_intel_review_big_ai_contracts.md','NOHUMA market-intel review — kills the "big AI contract, direct, solo" thesis; pursue only via framework/channel. Sources cited, no invented stats.'),
]
for fn,cap in items:
    path=os.path.join(base,fn)
    if not os.path.exists(path): print("MISSING",fn); continue
    with open(path,'rb') as fp:
        r=requests.post(f'https://api.telegram.org/bot{tok}/sendDocument',
            data={'chat_id':chat,'caption':cap}, files={'document':(os.path.basename(fn),fp)}, timeout=120)
    print(os.path.basename(fn),'SENT OK' if r.json().get('ok') else 'FAIL: '+r.text[:160])
