---
name: asset-gathering
description: "Finds, generates, downloads, validates, transcodes, and manifests video production assets. Use when Codex needs to automatically obtain video clips, images, screenshots, generated visuals, icons, data media, music candidates, or sound effects for a video. Do not use for final timeline assembly or aesthetic editing."
---

# Asset Gathering

Build the asset pool. This skill owns acquisition and validation, not final editing taste.

## Sources

Use the best legal and practical source for each need:

- User-provided files first.
- Public web sources only when browsing is allowed and attribution/licensing is tracked.
- Generated bitmap images via image generation when a custom visual is needed.
- Screenshots or screen recordings for website/app demos when the project needs real interface proof.
- Stock/music/SFX sources only when licensing is acceptable for the target platform.

## Acquisition Workflow

1. Read `plan/script.md` and `plan/creative-brief.md` if present.
2. Create a required/optional/fallback asset list.
3. For each asset, define search query or generation prompt, intended beat, format, minimum quality, and rights status.
4. Download or generate assets into `assets/` using stable, descriptive filenames.
5. Transcode only when needed for Remotion compatibility.
6. Verify each file opens, has sufficient resolution/duration, and matches the intended beat.
7. Write or update `plan/asset-list.md`.

## Manifest Schema

```md
| ID | Beat | Filename | Type | Source | Rights | Status | Use Case | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Use IDs like `IMG001`, `VID001`, `SFX001`, `BGM001`, `DATA001`.

## Music And SFX

Collect music and sound effects as candidates only. Final audio priority, ducking, loop points, and mix notes belong to `audio-director`.

## Do Not

- Do not decide final timeline placement.
- Do not beautify the final edit.
- Do not use unclear copyrighted material without recording risk.
- Do not silently invent sources; record provenance or mark as generated.
