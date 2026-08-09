import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
base = '/root/ai-employee/revenue-os/out'
fn = 'why-nhi-manifesto.pdf'
path = os.path.join(base, fn)
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': "NOHUMA — 'Why Non-Human Intelligence' manifesto (WHY-first, Sinek Golden Circle). Rebuilt to match the site: near-black #08080B, gunmetal, violet #8b5cf6, Inter. 8 pages."},
        files={'document': (fn, fp)},
        timeout=120,
    )
print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
