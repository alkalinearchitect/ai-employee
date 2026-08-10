import os, requests
tok = None
for line in open('/root/.hermes/.env'):
    line = line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok = line.split('=', 1)[1]
        break
chat = 813848257
path = '/root/ai-employee/revenue-os/out/construction-income-dose.pdf'
fn = 'construction-income-dose.pdf'
with open(path, 'rb') as fp:
    r = requests.post(
        f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id': chat, 'caption': "NOHUMA — The Construction Income Dose. 16pp black/white full-bleed. Money model (clients x £5k/mo), 30-day playbook, 7 segments with REAL companies + POI + per-segment pitch + openers + objections. Confirmed POI names: Mark Bailey (Barratt Redrow), Jason Towse & Franck Crosnier (Mitie), Stephanie Marshall (T&T), Richard Whitby (L&Q). Income numbers are YOUR revenue at £5k/client; savings are illustrative until Day-30 timesheet proves them."},
        files={'document': (fn, fp)},
        timeout=120,
    )
print(fn, 'SENT OK' if r.json().get('ok') else 'FAIL: ' + r.text[:200])
