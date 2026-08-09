import fitz, sys
OUT="/root/ai-employee/revenue-os/out_build"
fail=0
for n in ("owl-pricing-scope","owl-objection-close"):
    d=fitz.open(f"{OUT}/{n}.pdf")
    print("==",n,"pages",d.page_count)
    for p in d:
        r=p.rect
        ok_size = abs(r.width-648)<1 and abs(r.height-864)<1
        fonts=[f[3] for f in p.get_fonts()]
        inter=all("Inter" in f for f in fonts) and fonts
        pix=p.get_pixmap(clip=fitz.Rect(0,0,4,4))
        px=pix.pixel(1,1)
        clipped=[]
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines",[]):
                for s in l["spans"]:
                    x0,y0,x1,y1=s["bbox"]
                    if x0<-1 or y0<-1 or x1>r.width+1 or y1>r.height+1:
                        clipped.append(s["text"][:30])
        st = ok_size and inter and px==(0,0,0) and not clipped
        if not st: fail=1
        print(f" p{p.number+1} size={r.width:.0f}x{r.height:.0f} fonts={set(fonts)} bg={px} clipped={clipped} {'OK' if st else 'FAIL'}")
print("RESULT", "PASS" if not fail else "FAIL")
