---
name: remotion-gotchas-index
description: "Debugs and prevents common Remotion video implementation problems. Use when Remotion preview, render, timing, assets, audio, captions, frame math, staticFile paths, bundling, or composition registration behaves incorrectly. Keep fixes narrow and avoid large redesigns."
---

# Remotion Gotchas Index

Use this skill when something in Remotion is broken, suspicious, or likely to break during render.

## Check First

- Composition is registered and selected correctly.
- Duration, FPS, width, and height match the target.
- Frame math uses `useCurrentFrame()` relative to local Sequence timing when needed.
- Asset paths use `staticFile()` or imports consistently.
- Browser-only APIs are not called during render in unsafe ways.
- Audio files load, start at the expected frame, and do not clip.
- Captions fit safe areas and do not overlap key visuals.
- Fonts are loaded before render if custom typography is used.

## Debug Route

1. Reproduce the issue in Studio or render logs.
2. Locate the smallest failing Composition, Scene, or Sequence.
3. Inspect timing and asset paths before changing design.
4. Patch narrowly.
5. Re-run preview or render command.

## Common Fixes

- Blank preview: check composition ID, exported component, root registration, and runtime errors.
- Missing asset: check `public/` path, `staticFile()`, filename casing, and spaces.
- Captions drift: compare seconds, frames, FPS, and Sequence offsets.
- Audio out of sync: check `startFrom`, `endAt`, Sequence `from`, and FPS conversions.
- Layout jumps: give boards, media, cards, and caption containers stable dimensions.

## Do Not

- Do not redesign the video while debugging.
- Do not replace the main timeline unless it is the proven cause.
- Do not make broad refactors for a one-line asset path or timing bug.
- Do not ignore render verification after a fix.
