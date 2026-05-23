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

## Assets

```text
Use asset-gathering to create or update plan/asset-list.md from the current script and brief. Identify what must be found, generated, downloaded, transcoded, or verified. Save assets into assets/ only when acquisition is allowed. Do not decide final timeline placement.
```

## Asset Usage

```text
Use asset-usage-planner to map the current assets to script beats. Produce plan/timeline.md with scenes, timing, asset IDs, visual roles, on-screen text, and gaps. Do not download new assets.
```

## Motion

```text
Use motion-fragments to create plan/motion-plan.md from the timeline. Design hook frames, data cards, transitions, kinetic captions, and any demo focus moments. Keep each fragment implementable in Remotion.
```

## Audio

```text
Use audio-director to create plan/audio-plan.md. Specify BGM mood, music candidate needs, SFX timing, ducking, voice priority, fades, and loop points. Route missing music/SFX to asset-gathering.
```

## Remotion

```text
Use remotion-assembler and remotion-best-practices to implement the current plan in Remotion. Use Composition, Scene, Sequence, editPlan, CaptionLayer, and AudioLayer. Do not invent missing asset paths; report gaps.
```

## QA

```text
Use remotion-gotchas-index to inspect the current Remotion project for preview/render/timing/asset/caption/audio risks. Patch narrowly, then verify.
```

## Packaging

```text
Use platform-packaging to prepare exports/packaging.md with title options, description, timestamps, thumbnail or cover plan, hashtags/tags, export settings, and QA notes. Do not rewrite the video.
```
