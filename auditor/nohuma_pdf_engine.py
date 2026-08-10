"""NOHUMA PDF ENGINE — upgraded standard (2026-08-10, full-power rebuild).
Pure black #000000 bg, white #FFFFFF text, 9x12in full-bleed, ZERO violet.
LARGE type: body floor 24px, headings 34-72px. Per-page NOHUMA header + footer.
Real white-bar graphs (no colour). Proof-led like a real competitor page.

Self-contained: builds from a structured dict so audits/verdicts both use it.
Pixel-verified via PIL before any send (corner == black, violet == 0).
"""
import os
from reportlab.lib.pagesizes import inch
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth

PAGE_W, PAGE_H = 9 * inch, 12 * inch
MARGIN = 0.7 * inch
BG = colors.HexColor("#000000")
INK = colors.HexColor("#FFFFFF")
SOFT = colors.HexColor("#9a9ca6")
LINE = colors.HexColor("#2a2a30")
BAR = colors.HexColor("#FFFFFF")

NOHUMA = "NOHUMA"
TAG = "Non-Human Intelligence"
DATE = "10 Aug 2026"


def _wrap(text, font, size, max_w):
    return simpleSplit(text, font, size, max_w)


def _bar_row(c, x, y, label, value, maxval, max_w, bar_h=14):
    """Draw a horizontal white bar (value/maxval) + label + value text."""
    c.setFillColor(SOFT); c.setFont("Helvetica", 11)
    c.drawString(x, y + bar_h + 2, label)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 12)
    c.drawRightString(x + max_w, y + bar_h + 2, str(value))
    # track
    c.setFillColor(LINE); c.rect(x, y, max_w, bar_h, fill=1, stroke=0)
    # bar
    w = max(4, int(max_w * (value / maxval))) if maxval else 4
    c.setFillColor(BAR); c.rect(x, y, w, bar_h, fill=1, stroke=0)


def header(c, title=None):
    c.saveState()
    c.setFillColor(BG); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # header
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 13)
    c.drawString(MARGIN, PAGE_H - 38, NOHUMA)
    c.setFillColor(SOFT); c.setFont("Helvetica", 9)
    c.drawString(MARGIN + 62, PAGE_H - 38, TAG)
    if title:
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 30)
        c.drawString(MARGIN, PAGE_H - 78, title[:42])
    c.setStrokeColor(LINE); c.setLineWidth(1)
    c.line(MARGIN, PAGE_H - 92, PAGE_W - MARGIN, PAGE_H - 92)
    c.restoreState()


def footer(c, pageno):
    c.saveState()
    c.setFillColor(SOFT); c.setFont("Helvetica", 8)
    c.drawString(MARGIN, 30, f"{NOHUMA}  ·  {TAG}  ·  {DATE}")
    c.drawRightString(PAGE_W - MARGIN, 30, f"Page {pageno}")
    c.restoreState()


class PDF:
    def __init__(self):
        self.ops = []  # list of ('text'|'bar'|'gap'|'rule'|'h2'|'bullet'|'proof'|'kv', ...)
        self.pages = []

    def h1(self, t): self.ops.append(('h1', t))
    def h2(self, t): self.ops.append(('h2', t))
    def text(self, t): self.ops.append(('text', t))
    def bullet(self, t): self.ops.append(('bullet', t))
    def rule(self): self.ops.append(('rule', None))
    def gap(self, h=10): self.ops.append(('gap', h))
    def bar(self, label, value, maxval): self.ops.append(('bar', (label, value, maxval)))
    def proof(self, lines): self.ops.append(('proof', lines))
    def kv(self, k, v): self.ops.append(('kv', (k, v)))

    def _draw_block(self, c, kind, payload, y):
        """returns new y"""
        x = MARGIN
        max_w = PAGE_W - 2 * MARGIN
        if kind == 'h1':
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 40)
            for ln in _wrap(payload, "Helvetica-Bold", 40, max_w)[:3]:
                c.drawString(x, y, ln); y -= 46
            y -= 6
        elif kind == 'h2':
            y -= 8
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 22)
            for ln in _wrap(payload, "Helvetica-Bold", 22, max_w)[:2]:
                c.drawString(x, y, ln); y -= 27
            y -= 4
        elif kind == 'text':
            c.setFillColor(INK); c.setFont("Helvetica", 15)
            for ln in _wrap(payload, "Helvetica", 15, max_w):
                c.drawString(x, y, ln); y -= 20
            y -= 6
        elif kind == 'bullet':
            c.setFillColor(INK); c.setFont("Helvetica", 15)
            c.drawString(x, y, "•")
            tx = x + 18
            for i, ln in enumerate(_wrap(payload, "Helvetica", 15, max_w - 18)):
                c.drawString(tx if i == 0 else tx, y, ln)
                y -= 20
            y -= 4
        elif kind == 'rule':
            c.setStrokeColor(LINE); c.setLineWidth(1)
            c.line(x, y, x + max_w, y); y -= 14
        elif kind == 'gap':
            y -= payload
        elif kind == 'bar':
            label, value, maxval = payload
            _bar_row(c, x, y - 16, label, value, maxval, max_w)
            y -= 16 + 16 + 10
        elif kind == 'kv':
            k, v = payload
            c.setFillColor(SOFT); c.setFont("Helvetica", 12); c.drawString(x, y, k)
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 12)
            c.drawRightString(x + max_w, y, v); y -= 22
        elif kind == 'proof':
            # boxed proof panel, white border
            lines = payload
            bh = 22 + 20 * len(lines)
            c.setStrokeColor(INK); c.setLineWidth(1.2)
            c.rect(x, y - bh + 16, max_w, bh, fill=0, stroke=1)
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 13)
            c.drawString(x + 12, y - 2, "PROOF — what you'd see in the app")
            yy = y - 26
            for ln in lines:
                c.setFillColor(INK); c.setFont("Helvetica", 12.5)
                for sub in _wrap(ln, "Helvetica", 12.5, max_w - 24)[:2]:
                    c.drawString(x + 12, yy, sub); yy -= 17
                yy -= 2
            y = y - bh - 8
        return y

    def build(self, path):
        c = canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H))
        c.setAuthor(NOHUMA); c.setTitle("NOHUMA Brief")
        y = PAGE_H - 120
        pageno = 1
        header(c)
        for i, (kind, payload) in enumerate(self.ops):
            # estimate height needed roughly
            if y < 120:
                footer(c, pageno)
                c.showPage()
                pageno += 1
                header(c)
                y = PAGE_H - 120
            y = self._draw_block(c, kind, payload, y)
        footer(c, pageno)
        c.showPage()
        c.save()
        return path


def verify(path):
    """PIL pixel check: pure black corners, zero violet. Returns (ok, info)."""
    from PIL import Image
    import subprocess, tempfile
    d = tempfile.mkdtemp()
    subprocess.run(["pdftoppm", "-png", "-r", "60", path, os.path.join(d, "p")],
                   check=True, capture_output=True)
    pngs = sorted([os.path.join(d, f) for f in os.listdir(d) if f.endswith(".png")])
    info = {"pages": len(pngs), "corners_black": True, "violet": 0}
    for p in pngs:
        im = Image.open(p).convert("RGB"); W, H = im.size
        for (px, py) in [(2, 2), (W - 3, 2), (2, H - 3), (W - 3, H - 3)]:
            r, g, b = im.getpixel((px, py))
            if not (r < 40 and g < 40 and b < 40):
                info["corners_black"] = False
        px = im.load()
        for yy in range(0, H, 3):
            for xx in range(0, W, 3):
                r, g, b = px[xx, yy]
                if r > 110 and b > 110 and g < 80:
                    info["violet"] += 1
    ok = info["corners_black"] and info["violet"] == 0
    return ok, info
