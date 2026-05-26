---
name: footage-analyzer
description: "Analyzes raw footage before editing. Use when Codex receives existing video files and needs to extract frames, detect shots, identify usable moments, locate text or logos, score visual quality, flag bad footage, and create a shot list before script, timeline, or edit decisions."
---

# Footage Analyzer

Use this skill whenever the user provides raw video. A high-quality edit starts by understanding the footage, not by cutting immediately.

## Responsibilities

- Inspect video metadata: duration, resolution, FPS, codec, audio.
- Extract representative frames or contact sheets.
- Detect scene changes or meaningful shot ranges.
- Identify subjects, text, logos, weak shots, motion blur, low-quality frames, and standout moments.
- Score each shot for usefulness.
- Produce a shot list that later layers can edit from.

## Workflow

1. Read all user-provided video paths.
2. Generate contact sheets or key frames into a temporary QA folder.
3. Segment footage into shots or practical time ranges.
4. Score shots using: subject clarity, composition, motion, lighting, brand fit, edit value, and risk.
5. Mark text overlays or areas that need cleanup.
6. Write `plan/shot-list.md` and `plan/footage-notes.md`.

## Output

`plan/shot-list.md`:

```md
| Shot | Time Range | Description | Quality | Use | Risks | Notes |
| --- | --- | --- | ---: | --- | --- | --- |
```

`plan/footage-notes.md`:

```md
# Footage Notes

## Metadata

## Best Moments

## Weak or Unusable Moments

## Text / Logo / Cleanup Needs

## Editing Opportunities
```

## Do Not

- Do not make final edit decisions.
- Do not hide bad footage quality; mark it clearly.
- Do not overwrite original footage.
- Do not assume every clip must be used.
