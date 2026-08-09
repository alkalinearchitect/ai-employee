import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
base = '/root/ai-employee/revenue-os/out_v3'
files = {
    'owl-pricing-scope.pdf': 'Owl — Pricing & Scope (black/violet, Inter, 3:4)',
    'owl-objection-close.pdf': 'Owl — Objection & Close Playbook (black/violet, Inter, 3:4)',
    'owl-onboarding-guide.pdf': 'Owl — Client Onboarding Guide (black/violet, Inter, 3:4)',
    'owl-awareness.pdf': 'Owl — The Non-Human Employee (awareness, black/violet, Inter, 3:4)',
    'how-it-works.pdf': 'Owl — How It Works (black/violet, Inter, 3:4)',
    'white-label.pdf': 'Owl — White-Label Partner Brief (black/violet, Inter, 3:4)',
}
for fn, cap in files.items():
    path = os.path.join(base, fn)
    with open(path, 'rb') as fp:
        r = requests.post(
            f'https://api.telegram.org/bot{tok}/sendDocument',
            data={'chat_id': chat, 'caption': cap},
            files={'document': (fn, fp)},
            timeout=90,
        )
    print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:120])
