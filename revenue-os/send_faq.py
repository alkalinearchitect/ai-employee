import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
path = '/root/ai-employee/revenue-os/out/owl-customer-faq.pdf'
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': 'Owl Customer FAQ - 15pp (gold/ivory, NHI-led)'},
        files={'document': ('owl-customer-faq.pdf', fp)},
        timeout=90,
    )
print('SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
