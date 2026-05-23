---
name: asset-usage-planner
description: "Plans how gathered assets are used in the video timeline. Use to assign assets to spoken beats, de-duplicate clips/images, map A-roll/B-roll, create edit plans, align assets with narration timing, and decide scene-level asset usage. Do not use for downloading assets."
---

# Asset Usage Planner

Convert assets and narration into an edit plan that Remotion can implement.

## Responsibilities

- Map every spoken beat to assets or a deliberate no-asset visual treatment.
- Remove duplicate or redundant assets.
- Ensure each asset has a reason to appear.
- Allocate start/end times and scene ownership.
- Identify gaps that require `asset-gathering`.

## Workflow

1. Read `plan/script.md` and `plan/asset-list.md`.
2. Group beats into scenes.
3. Assign A-roll, B-roll, cards, screenshots, demos, text moments, and transitions.
4. Decide whether each asset is background, primary visual, overlay, cutaway, or proof.
5. Build `plan/timeline.md`.
6. Flag weak beats, missing assets, repeated visuals, or timing overload.

## Timeline Output

```md
| Scene | Beat | Start | End | Asset IDs | Visual Role | On-Screen Text | Notes |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
```

## Scene Rules

- One scene should express one clear idea or shift.
- Do not force an asset into a beat if text or motion is stronger.
- Prefer fewer stronger assets over constant unrelated B-roll.
- Keep short-form pacing readable: avoid stacking narration, captions, animated text, and busy footage at once.

## Do Not

- Do not download assets.
- Do not implement React components.
- Do not make music ducking decisions.
- Do not solve missing material by pretending the asset exists; send the gap back to `asset-gathering`.
