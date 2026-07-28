# MP4 Web Streaming / Scrub-Readiness Audit

**Date:** 2026-07-28
**Source:** `/root/ai-employee/assets/vid/` (copied from `/root/wordhumanitai/assets/vid/`)
**Tooling:** ffprobe/ffmpeg (ffmpeg 6.x, libx264)
**Verdict rule (per task):** FAIL if no faststart (moov before mdat) OR average GOP > 2 s.

## Per-file results

| file | codec | dims | dur (s) | kbps | faststart | #keyframes | avg GOP (s) | max GOP (s) | verdict |
|------|-------|------|---------|------|-----------|-----------|-------------|-------------|---------|
| hero.mp4 | h264 | 1920x1080 | 8.04 | 9157 | YES | 3 | 2.68 | 3.46 | **FAIL** (GOP>2s) |
| ads1.mp4 | h264 | 1920x1080 | 10.04 | 9282 | YES | 3 | 3.35 | 4.38 | **FAIL** (GOP>2s) |
| ads2.mp4 | h264 | 1920x1080 | 10.04 | 9495 | YES | 7 | 1.43 | 2.04 | BORDER (avg OK, max 2.04s) |
| ads3.mp4 | h264 | 1920x1080 | 10.04 | 9544 | YES | 3 | 3.35 | 4.25 | **FAIL** (GOP>2s) |
| conn_hero_ads1.mp4 | h264 | 1920x1080 | 1.92 | 2426 | YES | 1 | 1.92 | 1.92 | OK (single-keyframe 2s transition) |
| conn_ads1_ads2.mp4 | h264 | 1920x1080 | 1.92 | 2551 | YES | 1 | 1.92 | 1.92 | OK (single-keyframe 2s transition) |
| conn_ads2_ads3.mp4 | h264 | 1920x1080 | 1.92 | 3560 | YES | 1 | 1.92 | 1.92 | OK (single-keyframe 2s transition) |
| m/hero.mp4 | h264 | 720x1280 | 8.04 | 3027 | YES | 3 | 2.68 | 3.46 | **FAIL** (GOP>2s) |
| m/ads1.mp4 | h264 | 720x1280 | 10.04 | 4517 | YES | 3 | 3.35 | 4.38 | **FAIL** (GOP>2s) |
| m/ads2.mp4 | h264 | 720x1280 | 10.04 | 5314 | YES | 7 | 1.43 | 2.04 | BORDER (avg OK, max 2.04s) |
| m/ads3.mp4 | h264 | 720x1280 | 10.04 | 5242 | YES | 3 | 3.35 | 4.25 | **FAIL** (GOP>2s) |

**Summary:** 11 files. All h264 (web-compatible) and all have correct faststart (moov before mdat). 6 files FAIL on GOP > 2 s; 3 conn_* clips are short 1.92 s transitions (single keyframe — fine, they aren't scrubbed). `ads2.mp4` / `m/ads2.mp4` pass the avg rule but their max keyframe gap is 2.04 s — tighten if strict ≤1 s scrubbing is required.

## Root cause
All FAIL files were encoded with a very large keyframe interval (ffmpeg default gop ~250, or CRF scene-cut driven). Hero/ads are 8–10 s loops with only 3 keyframes → player can only seek to ~3–4 fixed points → poor scrubbing. The working CIC site exhibits the same defect (these are byte-identical copies of the source).

## Re-encode fix (tested — DONE TO /tmp ONLY, NOT applied to assets)

Real test on hero.mp4:
- Original: 9.21 MB, 3 keyframes (avg GOP 2.68 s).
- `-g 24 -crf 23`: **6.29 MB**, 10 keyframes → avg GOP **0.80 s**. (~32% SMALLER, because source was over-bitrated at ~9 Mbps; CRF 23 lands at ~6 Mbps.)
- `-g 30 -crf 23`: 6.14 MB, GOP 0.80–1.0 s.

Re-encoding **reduces** total size (est. 48 MB of bad files → ~31 MB), so no GitHub Pages risk. Current repo total 68.8 MB ≪ 1 GB Pages/repo soft limit.

### Command (run per file; video-only, no audio track present)
```bash
# Strict <=1s GOP at 24/25 fps (recommended):
ffmpeg -i IN.mp4 -c:v libx264 -pix_fmt yuv420p -movflags +faststart -g 24 -crf 23 OUT.mp4

# Or task-example -g 30 (GOP <=1.25s at 24fps, <=1.0s at 30fps):
ffmpeg -i IN.mp4 -c:v libx264 -pix_fmt yuv420p -movflags +faststart -g 30 -crf 23 OUT.mp4
```
No `-c:a` needed (files have no audio stream). Replace IN/OUT per file.

### Files to re-encode
- `hero.mp4`, `ads1.mp4`, `ads3.mp4`
- `m/hero.mp4`, `m/ads1.mp4`, `m/ads3.mp4`
- (optional) `ads2.mp4`, `m/ads2.mp4` if strict ≤1 s max-GOP scrubbing is required.
- conn_* left as-is (intentional single-keyframe 2 s transitions).

## Verification to run after re-encoding
```bash
for f in hero ads1 ads3 m/hero m/ads1 m/ads3; do
  ffprobe -v trace "$f.mp4" 2>&1 | grep -oE "type:'(moov|mdat)'" | head -2   # expect moov mdat
  ffprobe -v error -select_streams v:0 -skip_frame nokey -show_entries frame=pts_time -of csv=p=0 "$f.mp4" | wc -l  # expect >= duration (GOP<=1s)
done
```
