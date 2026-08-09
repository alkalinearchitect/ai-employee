import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
base = '/root/ai-employee/revenue-os/out'
fn = 'dewey-whitepaper.pdf'
path = os.path.join(base, fn)
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': 'NOHUMA White Paper — The Dewey Method: Nick Vasilescu\'s exact managed-agent playbook and why it builds real wealth while most companies have not implemented AI (black/violet, Inter, 3:4).'},
        files={'document': (fn, fp)},
        timeout=120,
    )
print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
