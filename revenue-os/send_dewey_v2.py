import os, requests
tok=None
for line in open('/root/.hermes/.env'):
    line=line.strip()
    if line.startswith('TELEGRAM_BOT_TOKEN='):
        tok=line.split('=',1)[1]; break
chat=813848257
base='/root/ai-employee/revenue-os/out'
fn='dewey-whitepaper.pdf'
path=os.path.join(base,fn)
with open(path,'rb') as fp:
    r=requests.post(f'https://api.telegram.org/bot{tok}/sendDocument',
        data={'chat_id':chat,'caption':'NOHUMA — The Dewey Method white paper (NOW v2 brand: gunmetal/violet/Inter, matching the site). Re-rendered to replace the old pure-black version.'},
        files={'document':(fn,fp)},timeout=120)
print(fn,'SENT OK' if r.json().get('ok') else 'FAIL: '+r.text[:160])
