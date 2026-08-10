import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
path = '/root/ai-employee/revenue-os/out/construction-targets.pdf'
fn = 'construction-targets.pdf'
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': "NOHUMA — Who To Approach In UK Construction. 16 pages, black/white, full-bleed. 7 real-company target segments, sourced bottlenecks (CITB 206k by 2030, NLW £12.21, Mitie £4.51bn FY24, Balfour £10.0bn 2024, Awaab's Law Oct 2025), use cases + £5k/mo offer. Facts scrape-verified."},
        files={'document': (fn, fp)},
        timeout=120,
    )
print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
