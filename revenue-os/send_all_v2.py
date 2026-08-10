import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
base = '/root/ai-employee/revenue-os/out'
files = [
    ('nohuma-brand-bible.pdf', 'NOHUMA Brand Bible v2 — the locked standard (palette, Perfect-Fourth type, WHY-first voice, match-the-site rule).'),
    ('owl-pricing.pdf', 'NOHUMA — Pricing & Scope (v2 brand).'),
    ('owl-objection.pdf', 'NOHUMA — Objection & Close (v2 brand).'),
    ('owl-onboarding.pdf', 'NOHUMA — Client Onboarding (v2 brand).'),
    ('owl-awareness.pdf', 'NOHUMA — The Non-Human Employee awareness (v2 brand).'),
    ('owl-howitworks.pdf', 'NOHUMA — How It Works / 8 parts (v2 brand).'),
    ('owl-whitelabel.pdf', 'NOHUMA — White-Label Partner (v2 brand).'),
    ('owl-customer-faq.pdf', 'NOHUMA — Client FAQ (v2 brand).'),
    ('why-nhi-manifesto.pdf', 'NOHUMA — Why Non-Human Intelligence manifesto (v2 brand).'),
    ('dewey-whitepaper.pdf', 'NOHUMA — The Dewey Method white paper (NOTE: still v1 pure-black; re-render pending).'),
]
for fn, cap in files:
    path = os.path.join(base, fn)
    if not os.path.exists(path):
        print("MISSING", fn); continue
    with open(path, 'rb') as fp:
        r = requests.post(
            f'https://api.telegram.org/bot{tok}/sendDocument',
            data={'chat_id': chat, 'caption': cap},
            files={'document': (fn, fp)},
            timeout=120,
        )
    print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:160])
