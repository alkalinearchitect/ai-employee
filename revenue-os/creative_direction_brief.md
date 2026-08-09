# Owl NHI — Creative-Direction Brief (analysis only, no build)

_Prepared for the rebuild team. Executable line-by-line. Constraints are LOCKED:_
- Canvas `#000000` full-bleed, `@page 9in 12in; margin:0`
- Text `#FFFFFF`/`#EDEDED`, ONE accent `#8b5cf6` (violet) only — no gold/green/gradient/second hue
- 3:4, large readable Inter (body ≥38pt)
- Inter embedded via `@font-face`

---

## 0. What the renderer actually does (read first)

From `build_v2.py`:
- **Every slide is `<div class="page cover">`.** The `.cover` override forces `justify-content:flex-start; padding-top:84px` on ALL pages — so covers and content pages are structurally identical. There is no cover/content rhythm. The skill's intent (covers flex-start, content centered) was abandoned; the "fix" for clipping flattened the whole deck into one template.
- **The watermark is dead.** Every slide contains `<div class="wm">NHI</div>` but `render()` strips it with `html.replace(...)` before printing. `.wm` CSS is unreachable. So the deck has **zero brand mark** — only text. The owl/NHI identity is entirely absent.
- **Layout = 3 floating text blocks.** kicker (violet 26pt) + headline (62pt) + body (38pt) + optional `.rule` + footer. No frame, no grid, no motif, no card system. Pure typographic hierarchy on a void.

That is the root of "weak / auto-generated": a text dump with no visual system.

---

## 1. Why text-on-black + violet kicker + one headline + body reads as WEAK

It is *typographic hierarchy floating on black* with no designed structure. Missing visual layers:

1. **Identity layer** — no owl/NHI mark, no monogram. Nothing says "this is a brand," so it reads like a generated text card.
2. **Frame layer** — no corner/registration system, no border ticks. The eye gets no "this is a composed page" signal.
3. **Grid/rhythm layer** — no baseline grid, no consistent vertical bands. Text floats with arbitrary top padding.
4. **Structure layer** — no cards, no index rail, no two-column or diagram. One block of copy per page = monotone.
5. **Motif layer** — no recurring geometric NHI symbol (the "1 brain + 4 specialists" idea has no visual).
6. **Negative-space discipline** — covers and content use the same density; the void is accidental, not composed.
7. **Editorial meta-system** — footer exists but isn't a deliberate rail; pages feel orphaned.

Net: repetition without variation + no mark + no frame = the "AI template" tell.

---

## 2. 7 concrete, constraint-safe repeatable devices

All use ONLY `#000`, `#EDEDED`/`#FFF`, and `#8b5cf6` (violet may be used at low opacity via `opacity`/`rgba` — still one hue, no gradient).

1. **Corner registration ticks** — thin violet hairlines (1–2pt) forming an L in each corner at a fixed 40pt inset. Print-registration feel = instantly "designed artifact." Apply to every page identically.
2. **Geometric owl/NHI monogram** — a refined mark built from circles + arcs only (e.g. two concentric arcs = an eye, or a minimal owl head from one circle + two triangle ears). Place top-right at fixed size (~64pt). White or violet, single color. This is the missing brand anchor.
3. **Negative-space hero (cover only)** — cover-title occupies the upper third; the lower two-thirds is deliberate void with the monogram + one violet rule. Contrast = the "stunning" beat.
4. **Index rail** — a fixed top or left "01 / 08" in violet tracking deck position; pairs with the monogram so every page is locatable.
5. **Hairline rule system + baseline grid** — replace the lone `.rule` with a consistent system: violet rule under kicker (100×6pt), thin `#2a2a2e` hairline above the footer meta-rail. Snap all type to a 12pt baseline rhythm.
6. **Numbered framework cards** — content pages use hairline-bordered cards (1pt `#8b5cf6` or `#2a2a2e`, NO fill) to present the "1 brain + 4 specialists" or step lists as a structured grid instead of one paragraph. Stroke-only = monochrome, no gradient.
7. **Recurring NHI node motif** — a small stroke-only diagram (1 central node + 4 satellites, or concentric radar arcs) used as a consistent emblem in a corner or as a faint background anchor at low opacity. This is the visual language for "Non-Human Intelligence."

---

## 3. Cover vs Content — templates (positions, not code)

**COVER** (airy, top-anchored, hero void):
- Top band (padding-top ~84pt): violet kicker (e.g. "Owl · Non-Human Intelligence") → giant cover-title (82pt, ≤13ch, upper third only).
- One short cover-sub (38pt) beneath.
- Single violet rule.
- THEN VOID — lower ~55% of page is empty black.
- Monogram top-right; corner ticks all four corners; NO page number (or tiny, bottom-right only).
- Rhythm role: the breath. One idea, maximum space.

**CONTENT** (denser, structured, centered or top-structured):
- Monogram top-right; index rail "0X / 0Y" top-left; corner ticks.
- kicker/num (violet) → headline (62pt) → hairline → body in a constrained column OR a 2-up card grid (device #6).
- Footer meta-rail: deck name (left) · section (center) · page number (right), separated by a thin hairline.
- Rhythm role: the argument. More density than cover, but still airy via the grid.

Differentiation = cover is 70% void / 30% type; content is 55% type / 45% void with structure. That contrast is the deck's pulse.

---

## 4. The "text overlay" error — cause + robust fix

**Single most likely cause:** `justify-content:center` on a `.page` whose total content height (kicker + headline + body + footer) **exceeds the printable area** (page height 864pt − top/bottom padding). A centered flexbox centers the overflow, pushing the top equally above the page edge; with `overflow:hidden` the kicker/headline top is **clipped at y<0** — the exact defect the skill warns about ("Do NOT center a tall cover… pushes the kicker to y<0 and clips").

**Robust fix (do all):**
- Default ALL pages to `justify-content:flex-start` with explicit `padding-top`. Reserve `center` ONLY for pages verified short.
- Wrap copy in a `.content` div with `max-height: calc(100% - footer)` and `overflow:hidden` scoped to that wrapper (not the page), so a too-long page fails visibly in review, never silently clips the top.
- Enforce a copy-length budget per page (kicker + headline + body must fit the printable height at the locked type scale).
- Pre-render guard: render → `fitz` measure → assert top text box y ≥ padding; fail the build if clipped. (The skill already verifies rect 648×864; add a top-clip assertion.)
- Never apply `.cover` (flex-start) to content and never apply centered to tall pages — pick one rule per page type and keep them distinct (this also restores the cover/content rhythm lost in build_v2.py).

---

## 5. Execution notes for rebuild

- Keep `build_v2.py`'s locked scale, embedded Inter, 9×12 margin:0, `overflow:hidden`, `@page` — those are correct.
- DELETE the dead `.wm` CSS; REPLACE the all-`cover` class with real `cover` vs `.page` distinction.
- Add the 7 devices as reusable CSS classes + one SVG monogram (inline, stroke-only violet/white).
- Do NOT introduce gold/green/gradient or a second hue — violet opacity only.
- Verify: fitz page count + rect 648×864 + top-clip assertion + vision-QA 2 pages in parent session.
