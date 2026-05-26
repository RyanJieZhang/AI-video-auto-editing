# Video Creation Workflow

This workspace uses a quality-first video creation workflow. Follow this route for any video task unless the user explicitly asks to skip or override a layer.

## Default Route

1. Workflow Router / Index: `video-workflow-router`
2. Creative Direction: `creative-director`
3. Creative & Planning: use the project workflow brief template
4. Footage Analysis, when raw video exists: `footage-analyzer`
5. Voiceover Editor: `voiceover-editor`
6. Asset Factory: `asset-gathering`
7. Edit Direction: `edit-director`
8. Asset Usage & Alignment: `asset-usage-planner`
9. Motion / HyperFrames: `motion-fragments`
10. Look Design: `look-designer`
11. Audio Direction: `audio-director`
12. Remotion Assembly: `remotion-assembler` plus `remotion-best-practices`
13. Technical QA / Gotchas: `remotion-gotchas-index`
14. Quality Review: `quality-critic`
15. Packaging / Export: `platform-packaging`
16. Prompt Iteration / Workflow Optimization: `video-prompt-lab`

Use `workflow/video-creation-system.md` as the operating manual.

## Routing Rules

- Start every new video request by identifying the current layer, desired output, available inputs, and missing blockers.
- Do not let one prompt do every job. Move layer by layer and produce a concrete artifact at each layer.
- Keep planning, script, assets, timeline, motion, Remotion implementation, and export notes as separate artifacts.
- Before scripting or editing, use `creative-director` to define the style, hook, reference direction, and quality bar.
- When the user provides raw footage, use `footage-analyzer` before deciding what to cut.
- Before final timeline assembly, use `edit-director` to choose pacing, shot order, retention beats, and what to remove.
- Before implementation polish, use `look-designer` to define color, typography, captions, titles, and visual consistency.
- When writing or editing Remotion code, use the installed `remotion-best-practices` skill.
- When gathering video, image, music, or SFX assets, use `asset-gathering` and record provenance in `plan/asset-list.md`.
- When deciding how obtained assets are stitched into the edit, use `asset-usage-planner` and write `plan/timeline.md`.
- When planning music, SFX, ducking, or voice priority, use `audio-director`.
- When implementing Remotion `Composition`, `Scene`, `Sequence`, captions, audio, and `editPlan`, use `remotion-assembler`.
- When preview/render issues appear, use `remotion-gotchas-index` before broad refactors.
- After any meaningful draft render, use `quality-critic`; if average score is below 8/10, route fixes back to the responsible layer instead of calling it final.
- When preparing titles, thumbnails, timestamps, export settings, and publishing notes, use `platform-packaging`.
- When refining prompts, comparing production attempts, or updating the workflow/skills after a test run, use `video-prompt-lab`.
- Prefer existing project conventions once a Remotion project exists.
- Ask the user only for decisions that materially affect creative direction, factual accuracy, rights, or publishing.

## Expected Artifacts

- `plan/creative-brief.md`
- `plan/creative-direction.md`
- `plan/shot-list.md` and `plan/footage-notes.md` when raw footage exists
- `plan/script.md`
- `plan/asset-list.md`
- `plan/edit-decision-list.md`
- `plan/timeline.md`
- `plan/motion-plan.md`
- `plan/lookbook.md` and `plan/title-style.md`
- `src/` Remotion implementation files, once the project is scaffolded
- `exports/` rendered outputs and packaging notes
- `exports/quality-review.md`
- `prompts/` reusable prompts for full runs, layer reruns, and retrospectives
- `workflow/prompt-iteration-log.md`

## Done Definition

A video task is complete only when the relevant layer output is written down, checked, and ready for the next layer. For full production tasks, completion means the Remotion preview or render has been verified, the quality review scores at least 8/10 average or clearly marks the draft as demo-only, packaging notes are available, and the prompt iteration log records what should be reused or changed next time.
