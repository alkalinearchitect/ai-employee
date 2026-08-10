import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
path = '/root/ai-employee/revenue-os/out/construction-swarm-deck.pdf'
fn = 'construction-swarm-deck.pdf'
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': "NOHUMA — UK Construction Target OS (SWARM-ANALysed). 13pp black/white full-bleed. 3-agent parallel research consolidated: 7 real segments enriched with 20+ sourced companies (NG Bailey, T Clarke, Murphy £1.4bn, Wates £2.4bn, OCS £841m, Equans, Riverside, Southern Housing, Mears + more) + POIs/roles + bottleneck→NHUMA maps + prioritisation matrix + 6-objection library + provenance page. Verified POIs: Bailey, Whitby, Towse, Crosnier, Marshall. Every gap flagged, nothing invented."},
        files={'document': (fn, fp)},
        timeout=120,
    )
print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
