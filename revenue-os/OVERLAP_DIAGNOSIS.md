# Owl PDF — Text-Overlap Root-Cause Diagnosis + Exact CSS Fix

**Scope:** print-layout diagnosis of `build_v2.py` (6 Owl decks, 40 pages). No PDF built.
**Deliverable:** `layout_fix.css` (paste-ready) + the HTML wrapper change below.

---

## 1. Root cause (confirmed by math + real-font measurement)

### Critical correction to the assumed mechanism
The brief assumed content pages use `justify-content:center` and overflow *symmetrically*.
That is **NOT** what this code does. Every one of the 40 pages is written as
`<div class="page cover">`, and `.cover { justify-content:flex-start; padding-top:84px; }`
overrides `.page`'s `justify-content:center`. So **all pages are top-aligned** (`flex-start`).
The symmetric-overflow scenario is a latent trap only — it would appear if a rebuild ever
removes the `.cover` class from content pages.

### The real mechanism
- `.page` is `position:relative; height:12in; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-start; padding:92px 95px` (cover overrides top→84px).
- The body column (kicker/num + headline + body) is in **normal flow, top-aligned, with NO height constraint**.
- `.foot` and `.pnum` are `position:absolute; bottom:30px`. They are anchored to the page bottom and live *outside* the flow.
- `overflow:hidden` on `.page` **masks** the failure: a tall column is silently clipped at the page edge instead of being fixed.

So when a page's body column is taller than the space between the top padding and the
absolute footer band, its lower lines render *on top of* the footer, and `overflow:hidden`
hides the worst cases by cutting text off.

### The math (1in = 72pt; 1px(CSS) = 0.75pt)
- Page: 9in × 12in = 648pt × 864pt.
- Content width = 648 − 2×95px(=71.25pt) = **505.5pt**.
- Footer band: `bottom:30px` = 22.5pt from page bottom; footer text ~20pt tall → footer occupies
  y ≈ **821.5–841.5pt** from top.
- Body starts at `padding-top:84px` = 63pt. To clear the footer it must end by ~821.5pt →
  **max safe body height ≈ 758pt (≈1011 CSS-px)**.
- If body height > **795pt (covers, no footer)** or **801pt (footed pages, full page)** it is
  **clipped** by `overflow:hidden`.

### Measured heights (PIL + real Inter TTFs, greedy word-wrap at 505.5pt)
- **OVERLAP (body invades absolute footer):** PRICING p03 (≈793pt), PRICING p05 (≈764pt).
  Both exceed the 758pt safe limit → last body line(s) sit under "Operated by Human Architect".
- **CLIP (overflow:hidden cuts text):** PRICING cover p1 (≈869pt), ONBOARDING p03 (≈875pt).
  These exceed full page height → bottom lines silently removed.
- **Near-threshold (recheck after rebuild):** HOWITWORKS p05 (≈752pt), ONBOARDING p04 (≈757pt) —
  within a hair of the limit; real kerning may push them over.

---

## 2. Every overlap / defect risk in the current CSS

1. **Footer vs body (VERTICAL)** — *primary defect.* Absolute `.foot` at `bottom:30px` collides
   with a top-aligned body column that is taller than the safe band. Confirmed on p03, p05.
2. **pnum vs body (VERTICAL)** — `.pnum` is also absolute at `bottom:30px`; any body line that
   reaches the bottom-right corner overlaps the page number. Same trigger as #1.
3. **footer vs pnum (HORIZONTAL)** — both absolute at `bottom:30px`, left:80px / right:80px. In the
   current copy the footers are short enough not to reach the pnum, BUT a longer footer (e.g. the
   one on ONBOARDING p08: "Flat £5,000/month · Cancel anytime · Human Architect") would — there is
   no rule preventing it. Latent risk.
4. **`overflow:hidden` masks real overflow** — it clips a too-tall column instead of preventing the
   overlap, so defects are invisible in source and only show as missing/cut text in the PDF.
5. **Cover pages themselves clip** — covers have no footer, but a too-tall cover (PRICING p1) is
   still cut by `overflow:hidden`. Confirmed.
6. **Latent symmetric-overflow trap** — if `.cover` is ever removed from content pages,
   `justify-content:center` resumes and overflow becomes top **and** bottom → worse overlap.
7. **Watermark** — `.wm` is stripped before render (build_v2.py line 231), so no watermark overlap.

---

## 3. Robust layout model that CANNOT overlap (the fix)

Move `.foot`/`.pnum` out of absolute positioning and into a **reserved CSS-grid footer row**.
The body lives in its own grid track; the footer track is always below it, so body text
**physically cannot reach the footer** no matter how tall the body is.

Paste `layout_fix.css` over the `<style>` block in `build_v2.py`. The only required HTML change:

**Content page — wrap body in `.main`, put foot+pnum in `.footrow`:**
```html
<!-- BEFORE -->
<div class="page cover"><div class="wm">NHI</div>
<div class="kicker">Pricing</div><div class="headline">…</div>
<div class="body">…</div>
<div class="foot">Operated by Human Architect</div><div class="pnum">02</div></div>

<!-- AFTER -->
<div class="page cover"><div class="wm">NHI</div>
<div class="main">
  <div class="kicker">Pricing</div><div class="headline">…</div>
  <div class="body">…</div>
</div>
<div class="footrow"><div class="foot">Operated by Human Architect</div><div class="pnum">02</div></div></div>
```

**Cover page (no footer):** just wrap the body in `.main`; omit `.footrow` (its grid row
auto-collapses to 0, so the cover keeps its current look).

### Why this is overlap-proof
- Grid rows `1fr auto`: the footer row is sized to its content and pinned to the bottom; the body
  cell (`1fr`) can never extend past its own track into the footer.
- `.main { min-height:0; overflow:hidden }`: if a body is still too tall, it clips **inside its own
  cell** — ugly, but it can NEVER bleed onto the footer. This converts an invisible `overflow:hidden`
  page-clip into a localized, diagnosable clip.
- `.foot` gets `max-width: calc(100% - 56px); text-overflow:ellipsis` and `.footrow` uses
  `justify-content:space-between`, so footer text can never collide with the pnum even if it grows.
- `.page` keeps `overflow:hidden` only as a final safety net.

---

## 4. `overflow:hidden` — mask or fix?

Currently it **masks** the bug (clips tall columns, hides cut text). The grid fix makes overlap
structurally impossible, so `overflow:hidden` becomes a harmless safety net rather than the thing
standing between you and a broken layout. **But you must still size content to fit** on the pages
that currently clip (PRICING p1 cover, ONBOARDING p03): either shorten the copy or drop `body` to
34–36pt on those pages. The grid guarantees no *overlap*; it does not auto-shrink text.

---

## 5. Action list for the rebuild team
1. Replace the `<style>` CSS with `layout_fix.css` (or apply the diff by hand).
2. Wrap each content page's kicker/num+headline+body in `<div class="main">…</div>` and move
   `.foot`+`.pnum` into a trailing `<div class="footrow">…</div>`.
3. Wrap each cover page's content in `<div class="main">…</div>` (no footrow).
4. Re-check/shorten the two clipping pages (PRICING p1, ONBOARDING p03) so nothing is cut.
5. Optional: remove `justify-content:center` from `.page` (dead, overridden by `.cover`) to kill the
   latent symmetric-overflow trap.
