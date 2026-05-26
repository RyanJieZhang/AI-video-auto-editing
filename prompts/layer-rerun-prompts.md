# Layer Rerun Prompts

Use these when one layer needs another pass without disturbing the whole project.

## Router

```text
Use video-workflow-router to inspect the current project state. Tell me the active layer, missing artifacts, next skill, and next file to produce. Do not modify implementation code.
```

## Voiceover

```text
Use voiceover-editor to rewrite plan/script.md for stronger spoken pacing. Preserve the core message, split beats clearly, estimate timing, and mark visual needs. Do not download assets or edit Remotion code.
```

## Creative Direction

```text
Use creative-director to create or revise plan/creative-direction.md. Define the reference style, hook strategy, visual rules, pacing rules, avoid list, and quality bar. Do not download assets or implement code.
```

## Footage Analysis

```text
Use footage-analyzer to inspect the provided raw video files. Extract representative frames if needed, create plan/shot-list.md and plan/footage-notes.md, score each shot, and flag text/logo/cleanup needs. Do not make final edit decisions.
```

## Assets

```text
Use asset-gathering to create or update plan/asset-list.md from the current script and brief. Identify what must be found, generated, downloaded, transcoded, or verified. Save assets into assets/ only when acquisition is allowed. Do not decide final timeline placement.
```

## Asset Usage

```text
Use asset-usage-planner to map the current assets to script beats. Produce plan/timeline.md with scenes, timing, asset IDs, visual roles, on-screen text, and gaps. Do not download new assets.
```

## Edit Direction

```text
Use edit-director to create plan/edit-decision-list.md from the script, shot list, asset list, and creative direction. Choose opening shot, cut rhythm, shot order, retention beats, removals, and audio bridges. Do not download assets or implement code.
```

## Motion

```text
Use motion-fragments to create plan/motion-plan.md from the timeline. Design hook frames, data cards, transitions, kinetic captions, and any demo focus moments. Keep each fragment implementable in Remotion.
```

## Audio

```text
Use audio-director to create plan/audio-plan.md. Specify BGM mood, music candidate needs, SFX timing, ducking, voice priority, fades, and loop points. Route missing music/SFX to asset-gathering.
```

## Look Design

```text
Use look-designer to create plan/lookbook.md and plan/title-style.md. Define color, typography, caption system, title cards, lower thirds, safe areas, and visual polish rules. Do not change the story just for decoration.
```

## Remotion

```text
Use remotion-assembler and remotion-best-practices to implement the current plan in Remotion. Use Composition, Scene, Sequence, editPlan, CaptionLayer, and AudioLayer. Do not invent missing asset paths; report gaps.
```

## QA

```text
Use remotion-gotchas-index to inspect the current Remotion project for preview/render/timing/asset/caption/audio risks. Patch narrowly, then verify.
```

## Quality Critique

```text
Use quality-critic to review the latest draft render or preview. Score hook, clarity, footage, rhythm, visual polish, captions, audio, motion, platform fit, and memorability. Write exports/quality-review.md and route fixes back to the responsible layer if average score is below 8/10.
```

## Packaging

```text
Use platform-packaging to prepare exports/packaging.md with title options, description, timestamps, thumbnail or cover plan, hashtags/tags, export settings, and QA notes. Do not rewrite the video.
```
