import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
path = '/root/ai-employee/revenue-os/out/construction-bible.pdf'
fn = 'construction-bible.pdf'
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': "NOHUMA — The Construction Bible. 23pp black/white full-bleed. WHAT the Dewey/NOHUMA system is (grounded in DEWEY_INTEL.md + knowledge base), the 8 parts, 1+4 architecture, 48h delivery, the real tool stack, the construction verdict, 7 real-company segments w/ POI + use cases + income, cross-cutting use cases, money model, 30-day playbook, copy-paste openers, FAQ (capabilities + objections), and a verified-vs-to-confirm page. No hallucinated stats or contacts."},
        files={'document': (fn, fp)},
        timeout=120,
    )
print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
