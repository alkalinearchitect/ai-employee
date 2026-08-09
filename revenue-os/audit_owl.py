#!/usr/bin/env python3
"""Self-audit Owl PDFs with fitz:
(a) page rect == 648x864
(b) get_fonts() shows Inter not Liberation
(c) no span clipped within page
(d) full-bleed black
Returns 0 if all pass, 1 if any fail (with reasons)."""
import fitz, sys, os

OUT = "/root/ai-employee/revenue-os/out_build"
TOL = 1.5  # px tolerance for clip check

def audit(path):
    doc = fitz.open(path)
    fails = []
    # (a) rect
    for i, pg in enumerate(doc):
        r = pg.rect
        if abs(r.width - 648) > 0.5 or abs(r.height - 864) > 0.5:
            fails.append(f"(a) page {i} rect {r.width:.1f}x{r.height:.1f} != 648x864")
    # (b) fonts Inter not Liberation
    fonts_seen = set()
    for pg in doc:
        for f in pg.get_fonts(full=True):
            # f = (xref, ext, type, basefont, name, encoding, ...)
            base = f[3] or ""
            fonts_seen.add(base)
            if "Liberation" in base or "DejaVu" in base or base.startswith("Helv") or "Arial" in base:
                fails.append(f"(b) fallback font present: {base}")
    inter_ok = any("Inter" in b for b in fonts_seen)
    if not inter_ok:
        fails.append(f"(b) Inter NOT embedded; fonts seen: {sorted(fonts_seen)}")
    # (c) no span clipped within page (text bbox inside page rect)
    for i, pg in enumerate(doc):
        pr = pg.rect
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    bb = s["bbox"]
                    if bb[0] < -TOL or bb[1] < -TOL or bb[2] > pr.width + TOL or bb[3] > pr.height + TOL:
                        fails.append(f"(c) page {i} span clipped: {s['text'][:30]!r} bbox={tuple(round(x,1) for x in bb)}")
    # (d) full-bleed black: sample corner + center pixels must be ~black
    for i, pg in enumerate(doc):
        pix = pg.get_pixmap(dpi=24)
        samples = [(0,0),(pix.width-1,0),(0,pix.height-1),(pix.width-1,pix.height-1)]
        for (x,y) in samples:
            r,g,b = pix.pixel(x,y)
            if r > 12 or g > 12 or b > 12:
                fails.append(f"(d) page {i} corner not black: rgb=({r},{g},{b})")
    doc.close()
    return fails

if __name__ == "__main__":
    paths = sys.argv[1:] or [os.path.join(OUT, f) for f in os.listdir(OUT) if f.endswith(".pdf")]
    ok = True
    for p in paths:
        if not p.endswith(".pdf"): continue
        f = audit(p)
        if f:
            ok = False
            print(f"FAIL {p}")
            for x in f: print("   -", x)
        else:
            print(f"PASS {p}")
    sys.exit(0 if ok else 1)
