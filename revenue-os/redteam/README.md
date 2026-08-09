# OWL VISUAL SYSTEM — Red Team handoff

Artifacts in `/root/ai-employee/revenue-os/redteam/`:
- `owl_css.css` — paste-ready CSS (all classes, grid layout, @font-face, @page)
- `owl_monogram.svg` — owl monogram + NHI node motif (inline SVG snippets)
- `owl_design_system.html` — standalone live demo: 4 page templates, all 7 devices
- `README.md` — this file

## Locked constraints
Black #000 full-bleed, 9in x 12in, margin 0. Text #FFFFFF / #EDEDED / #9a9aa2 / #6a6a72 (neutrals) + ONE accent violet **#8b5cf6**. Hairline neutral **#2a2a2e**. Inter only, embedded from `file:///root/fonts/`. No gold, green, gradient, second hue, or watermark glyph.

## The 7 devices (class names)
| # | Device | Markup |
|---|---|---|
| 1 | Corner registration ticks | `.tick.tl/.tr/.bl/.br` (4 empty divs, 40pt inset) |
| 2 | Owl monogram | `<div class="monogram">…svg…</div>` — top-right, 64pt |
| 3 | Negative-space hero | `.page.cover` + `.void` spacer after cover block |
| 4 | Index rail | `<div class="railidx">02 / 06</div>` — content pages only |
| 5 | Hairline rules | `.rule` (100x6pt violet under kicker) + `.hairline` + `.footrow` top border |
| 6 | Numbered framework cards | `.cards.two/.three/.one` > `.card` > `.n` `.t` `.d`; `.card.on` = violet border |
| 7 | NHI node motif | `.node-emblem` (corner, 86pt) or `.node-bg` (faint 10% anchor, cover only) |

## Templates
- **A — COVER**: ticks + monogram + kicker + `.cover-title` (82pt) + `.rule` + `.cover-sub` + `.void` + footrow (deck name left, page right). No index rail. Optional `.node-bg`.
- **B — CONTENT/body**: ticks + monogram + railidx + kicker + rule + `.headline` (62pt) + `.hairline` + `.body` blocks + `.void` + optional `.stat` + footrow (deck / section / page).
- **C — CONTENT/cards**: same head, then `.cards two` with 2 or 4 `.card`. Add `.node-emblem` bottom-right.
- **D — CLOSE**: template B with booking line, single `.body` pair.

## Deck → template mapping (6 decks)
Every deck: p1 = A (cover), last page = D (close/booking). Middle pages:
1. **Offer deck** — B (flat £5,000/mo, everything included), B (48h live or first month refunded), B (day-30 >£5k saved or refund), C (8-part stack as 4 cards x2 pages or `.cards.two`).
2. **How it works** — C (1 brain + 4 specialists), B (isolated VPS, scoped, portable), C (8-part stack).
3. **Industries** — C `.cards.two` (trades / clinics / law / ecom), B per-industry outcome.
4. **Proof** — B with `.stat` (HBR 7x / 78%), B (booking beacons.ai/humanarchitect).
5. **White-label / partner** — B (white-label, single tier, cancel anytime), C (steps).
6. **One-pager** — A + one B + D.

## Copy-length budget (hard — prevents `.main` overflow)
Usable `.main` height ≈ 10.1in after padding + footrow.
- kicker: **≤ 34 chars**, one line.
- cover-title: **≤ 16 chars** (1 line) or ≤ 26 chars (2 lines max).
- cover-sub: **≤ 90 chars** (3 lines max at 38pt).
- headline: **≤ 60 chars** (max 3 lines at 62pt).
- body paragraph: **≤ 120 chars**; **max 3 `.body` blocks** per page (2 if a `.stat` or cards are present).
- card `.t` ≤ 22 chars, `.d` ≤ 60 chars; **max 4 cards** per page with a headline, 6 without.
- foot ≤ 46 chars (ellipsis guard exists but don't rely on it).
- One idea per page. If it doesn't fit, split the page — never shrink type.

## Audit gate (Blue Team must pass all)
1. Render to PDF via headless Chrome `--no-pdf-header-footer`; page count == section count, no blank trailing page.
2. Rasterise every page to PNG and eyeball: **zero** overlap, zero clipped text, zero content crossing the footer hairline.
3. Colour scan: only `#8b5cf6` (+ its rgba/opacity) as non-neutral. Grep the HTML/CSS for `gold|#c9a|linear-gradient|#0f0|green` → must be empty.
4. Font check: `pdffonts` shows Inter embedded (all three weights used are subset-embedded); no fallback sans.
5. Type floor: no computed font-size below 20pt; body ≥ 38pt.
6. Every page has 4 ticks + monogram; every content page has an index rail matching its real position (`0X / 0Y`).
7. Banned words absent: synergy, leverage, revolutionize, seamless, empower, paradigm, robust, solutions, cutting-edge.
8. Facts: only the verified list (flat £5,000/mo; 48h or first month refunded; day-30 >£5k or refund; isolated VPS scoped portable; 1 brain + 4 specialists; 8-part stack; white-label single tier; cancel anytime; trades/clinics/law/ecom; HBR 7x/78%; booking beacons.ai/humanarchitect; Operated by Human Architect). No invented numbers.
