# 8-Layer Video Creation System

This workflow turns a video request into a staged production process. The goal is clear ownership per layer: planning, voice, assets, alignment, motion, Remotion build, and export should not collapse into one vague prompt.

## 1. Workflow Router / Index

Skill: `video-workflow-router`

Purpose: decide where the request belongs and which skill or tool should be called.

Inputs:
- User request
- Existing project files
- Any references, brand notes, audience notes, assets, or target platform

Actions:
- Identify the active layer.
- List missing inputs.
- Decide whether to continue, ask a focused question, or produce the next artifact.
- Route Remotion implementation work through `remotion-best-practices`.

Output:
- Short layer diagnosis and next action.

## 2. Creative & Planning

Purpose: clarify topic, audience, hook, chapters, visual direction, and production constraints.

Actions:
- Define objective, audience, format, platform, duration, tone, and core message.
- Draft the hook and chapter structure.
- Decide the visual language: documentary, tutorial, data card, product demo, meme, cinematic, editorial, or hybrid.
- Record assumptions and facts that need verification.

Output:
- `plan/creative-brief.md`

## 3. Voiceover Editor

Skill: `voiceover-editor`

Purpose: turn the idea into spoken narration that fits timing and pacing.

Actions:
- Rewrite text for speech, not reading.
- Split narration into spoken beats.
- Mark pauses, emphasis, and transitions.
- Estimate duration per beat.
- Keep each beat tied to a visual need.

Output:
- `plan/script.md`

## 4. Asset Factory

Skill: `asset-gathering`

Purpose: collect, generate, download, transcode, and validate assets.

Actions:
- Build an asset list from the script and visual direction.
- Separate required, optional, and fallback assets.
- Track source, rights/licensing status, dimensions, format, and processing notes.
- Generate or edit bitmap assets when needed.
- Convert media to Remotion-friendly formats when needed.

Output:
- `plan/asset-list.md`
- Asset files in `assets/`

## 5. Asset Usage & Alignment

Skill: `asset-usage-planner`

Purpose: assign assets to narration and timeline slots so there is no duplication, gap, or misalignment.

Actions:
- Map every spoken beat to an asset, visual treatment, or text/card moment.
- Define timing, start frame, end frame, transitions, and on-screen text.
- Flag repeated assets and weak visual beats.
- Confirm that the timeline fits target duration.

Output:
- `plan/timeline.md`

## 6. Motion / HyperFrames

Skill: `motion-fragments`

Purpose: design advanced visual moments before coding.

Actions:
- Define hook frames, data cards, transitions, website demos, kinetic text, meme-style backgrounds, and cover/title frames.
- Specify motion intent: reveal, emphasis, contrast, momentum, pause, proof, or payoff.
- Keep animation purposeful and readable.

Output:
- `plan/motion-plan.md`

## Audio Direction

Skill: `audio-director`

Purpose: decide BGM, SFX, ducking, voice priority, loop points, and audio mix notes.

Actions:
- Select music mood, tempo, and licensing needs.
- Ask `asset-gathering` for missing music/SFX assets.
- Map SFX to motion events and transitions.
- Record voice priority and ducking notes.

Output:
- `plan/audio-plan.md`

## 7. Remotion Assembly

Skill: `remotion-assembler` plus `remotion-best-practices`

Purpose: implement the video in React/TypeScript with Remotion.

Actions:
- Use `remotion-best-practices`.
- Scaffold a Remotion project if none exists.
- Build compositions, timeline components, subtitles, audio, and asset imports.
- Keep timing constants and content data structured.
- Use Remotion Studio for preview.

Output:
- Remotion project files
- Working Studio preview

## 8. QA / Packaging / Export

Skills: `remotion-gotchas-index`, `platform-packaging`

Purpose: verify, render, package, and prepare publishing material.

Actions:
- Preview the full video.
- Check text fit, timing, audio sync, safe areas, asset quality, and spelling.
- Render the final video.
- Create title, description, cover/thumbnail notes, and publishing checklist.

Output:
- Final render in `exports/`
- Packaging notes

## Prompt Iteration / Workflow Optimization

Skill: `video-prompt-lab`

Purpose: improve the prompts, workflow, and skills after each test run.

Actions:
- Run full-production or layer-rerun prompts from `prompts/`.
- Compare expected artifacts against actual outputs.
- Record friction, failed assumptions, skill boundary drift, asset gaps, and Remotion structure issues.
- Update prompts, workflow docs, or the relevant skill.
- Mark the first successful full production as Baseline v1.

Output:
- `workflow/prompt-iteration-log.md`
- Updated prompts or skills when needed

## Core Principle

Planning -> Assets -> Alignment -> Motion -> Assembly -> Export.

Each layer should hand the next layer a concrete artifact. If an artifact is missing, create it before moving on.
