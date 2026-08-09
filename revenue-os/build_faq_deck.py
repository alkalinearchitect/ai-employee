#!/usr/bin/env python3
"""Owl Customer FAQ deck v2 — true v10 gold/ivory, large type, editorial chrome.
15pp, 1080x1350, NHI-led. Content fields: TITLE/ANSWER/BOLD/DETAIL.
"""
import os, re, subprocess, sys
from PIL import Image
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350

def parse(text):
    blocks, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^PAGE\s+(\d+)\s*$", line.strip())
        if m:
            cur = int(m.group(1)); blocks[cur] = {}; continue
        if cur is None:
            continue
        for k in ("TITLE", "ANSWER", "BOLD", "DETAIL"):
            if line.strip().startswith(k + ":"):
                blocks[cur][k] = line.strip()[len(k) + 1:].strip(); break
    return blocks

def e(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def cover(b):
    return f"""
    <div class="slide cover">
      <div class="eyebrow">OWL · NON-HUMAN INTELLIGENCE</div>
      <h1 class="ct">{e(b.get('TITLE','Owl'))}</h1>
      <div class="gold-rule"></div>
      <h2 class="csub">{e(b.get('ANSWER','THE CUSTOMER FAQ'))}</h2>
      <p class="cbold">{e(b.get('BOLD',''))}</p>
      <p class="cdetail">{e(b.get('DETAIL',''))}</p>
      <div class="foot-line">Managed AI Employee · £5,000 / month · beacons.ai/humanarchitect</div>
    </div>"""

def contents(b):
    items = [x.strip() for x in b.get("DETAIL", "").split("·") if x.strip()]
    lis = "".join(f"<li>{e(it)}</li>" for it in items)
    return f"""
    <div class="slide">
      <div class="eyebrow">CONTENTS</div>
      <h2 class="q">{e(b.get('TITLE',''))}</h2>
      <p class="a lead-a">{e(b.get('ANSWER',''))}</p>
      <ol class="toc">{lis}</ol>
    </div>"""

def faq(b):
    return f"""
    <div class="slide">
      <div class="eyebrow">CUSTOMER FAQ</div>
      <h2 class="q">{e(b.get('TITLE',''))}</h2>
      <p class="a">{e(b.get('ANSWER',''))}</p>
      <div class="bold-box">{e(b.get('BOLD',''))}</div>
      <p class="detail">{e(b.get('DETAIL',''))}</p>
    </div>"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0A0A0A;color:#F5F1E8;font-family:'Inter',system-ui,-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
.slide{width:1080px;height:1350px;overflow:hidden;padding:96px 96px 120px;display:flex;flex-direction:column;justify-content:center;position:relative;border-bottom:1px solid rgba(245,241,232,0.05)}
.eyebrow{font-family:'Inter',sans-serif;font-size:24px;letter-spacing:.26em;text-transform:uppercase;color:#b5b0a0;font-weight:600;margin-bottom:34px}
.gold-rule{width:96px;height:4px;background:#C9A961;margin:40px 0;border-radius:2px}
.ct{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:150px;line-height:.96;letter-spacing:-.03em;color:#F5F1E8}
.csub{font-family:Georgia,serif;font-weight:700;font-size:58px;line-height:1.05;color:#F5F1E8;margin-top:8px;letter-spacing:-.01em}
.cbold{font-size:38px;line-height:1.35;color:#C9A961;font-weight:600;margin-top:42px;max-width:20ch}
.cdetail{font-size:32px;line-height:1.5;color:#F5F1E8;max-width:22ch;margin-top:24px}
.foot-line{position:absolute;bottom:84px;left:96px;right:96px;font-size:24px;color:#b5b0a0;letter-spacing:.02em;border-top:1px solid rgba(245,241,232,0.12);padding-top:24px}
.q{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:62px;line-height:1.05;letter-spacing:-.015em;color:#F5F1E8;margin-bottom:40px;max-width:18ch}
.a{font-size:38px;line-height:1.5;color:#F5F1E8;font-weight:400;max-width:26ch;margin-bottom:36px}
.lead-a{font-size:34px;color:#F5F1E8;margin-bottom:30px;max-width:28ch}
.bold-box{margin:0 0 34px;padding:30px 34px;border-left:5px solid #C9A961;background:rgba(201,169,97,0.09);border-radius:4px;font-size:36px;line-height:1.4;color:#F5F1E8;font-weight:600;max-width:25ch}
.detail{font-size:30px;line-height:1.55;color:#b5b0a0;font-weight:400;max-width:28ch}
.toc{list-style:none;counter-reset:t;margin-top:6px}
.toc li{counter-increment:t;font-size:29px;line-height:1.4;color:#F5F1E8;padding:13px 0 13px 58px;position:relative;border-bottom:1px solid rgba(245,241,232,0.08)}
.toc li::before{content:counter(t,decimal-leading-zero);position:absolute;left:0;top:13px;color:#C9A961;font-family:Georgia,serif;font-weight:700;font-size:27px}
.page-num{position:absolute;bottom:84px;right:96px;font-size:22px;color:#6a6864;letter-spacing:.12em}
.nhi-foot{position:absolute;bottom:84px;left:96px;font-size:22px;color:#6a6864;letter-spacing:.08em}
"""

def build_html(blocks, n=15):
    parts = []
    for i in range(1, n + 1):
        b = blocks.get(i, {})
        if i == 1:
            parts.append(cover(b))
        elif i == 2:
            parts.append(contents(b))
        else:
            parts.append(faq(b))
        # footer chrome on pages 2..n only (cover has its own foot-line)
        if i >= 2:
            parts[-1] = parts[-1].replace("</div>", f'<div class="nhi-foot">OWL · NON-HUMAN INTELLIGENCE</div><div class="page-num">{i:02d} / {n:02d}</div></div>', 1)
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(parts)}</body></html>"

def render(html_path, pdf_path, n):
    Image.MAX_IMAGE_PIXELS = 400_000_000
    full = os.path.join(OUT, "_full.png")
    win_h = n * H + 20
    cmd = ["chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--window-size={W},{win_h}", f"--screenshot={full}", f"file://{html_path}"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    if r.returncode != 0:
        raise SystemExit("chromium failed: " + r.stderr[-400:])
    im = Image.open(full)
    imgs = [im.crop((0, i * H, W, i * H + H)) for i in range(n)]
    imgs[0].save(pdf_path, "PDF", resolution=72.0, save_all=True, append_images=imgs[1:])
    doc = fitz.open(pdf_path)
    bad = [i + 1 for i in range(len(doc)) if (round(doc[i].mediabox.width), round(doc[i].mediabox.height)) != (W, H)]
    size = os.path.getsize(pdf_path)
    if bad or size < 50_000:
        raise SystemExit(f"VERIFY FAIL bad={bad} size={size}")
    return len(doc), size

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "faq_copy.txt")
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    blocks = parse(open(src).read())
    html = build_html(blocks, n)
    hp = os.path.join(OUT, "faq_deck.html")
    open(hp, "w").write(html)
    pdf = os.path.join(OUT, "owl-customer-faq.pdf")
    cnt, sz = render(hp, pdf, n)
    print(f"OK {cnt} pages, {sz} bytes -> {pdf}")
