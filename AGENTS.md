# Video Creation Workflow

This workspace uses an 8-layer video creation workflow. Follow this route for any video task unless the user explicitly asks to skip or override a layer.

## Default Route

1. Workflow Router / Index: `video-workflow-router`
2. Creative & Planning: use the project workflow brief template
3. Voiceover Editor: `voiceover-editor`
4. Asset Factory: `asset-gathering`
5. Asset Usage & Alignment: `asset-usage-planner`
6. Motion / HyperFrames: `motion-fragments`
7. Audio Direction: `audio-director`
8. Remotion Assembly: `remotion-assembler` plus `remotion-best-practices`
9. QA / Gotchas / Packaging / Export: `remotion-gotchas-index` and `platform-packaging`
10. Prompt Iteration / Workflow Optimization: `video-prompt-lab`

Use `workflow/video-creation-system.md` as the operating manual.

## Routing Rules

- Start every new video request by identifying the current layer, desired output, available inputs, and missing blockers.
- Do not let one prompt do every job. Move layer by layer and produce a concrete artifact at each layer.
- Keep planning, script, assets, timeline, motion, Remotion implementation, and export notes as separate artifacts.
- When writing or editing Remotion code, use the installed `remotion-best-practices` skill.
- When gathering video, image, music, or SFX assets, use `asset-gathering` and record provenance in `plan/asset-list.md`.
- When deciding how obtained assets are stitched into the edit, use `asset-usage-planner` and write `plan/timeline.md`.
- When planning music, SFX, ducking, or voice priority, use `audio-director`.
- When implementing Remotion `Composition`, `Scene`, `Sequence`, captions, audio, and `editPlan`, use `remotion-assembler`.
- When preview/render issues appear, use `remotion-gotchas-index` before broad refactors.
- When preparing titles, thumbnails, timestamps, export settings, and publishing notes, use `platform-packaging`.
- When refining prompts, comparing production attempts, or updating the workflow/skills after a test run, use `video-prompt-lab`.
- Prefer existing project conventions once a Remotion project exists.
- Ask the user only for decisions that materially affect creative direction, factual accuracy, rights, or publishing.

## Expected Artifacts

- `plan/creative-brief.md`
- `plan/script.md`
- `plan/asset-list.md`
- `plan/timeline.md`
- `plan/motion-plan.md`
- `src/` Remotion implementation files, once the project is scaffolded
- `exports/` rendered outputs and packaging notes
- `prompts/` reusable prompts for full runs, layer reruns, and retrospectives
- `workflow/prompt-iteration-log.md`

## Done Definition

A video task is complete only when the relevant layer output is written down, checked, and ready for the next layer. For full production tasks, completion means the Remotion preview or render has been verified, packaging notes are available, and the prompt iteration log records what should be reused or changed next time.
