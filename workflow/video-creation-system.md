# Quality-First Video Creation System

This workflow turns a video request into a staged production process. The goal is not only to make a video run, but to make it improve. Planning, direction, footage analysis, edit judgment, visual design, audio, Remotion build, QA, quality critique, and packaging should not collapse into one vague prompt.

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

Skills: `creative-director` plus the project workflow brief template

Purpose: clarify topic, audience, hook, chapters, visual direction, reference style, and production constraints.

Actions:
- Use `creative-director` to set style, hook, reference direction, visual rules, pacing rules, and quality bar.
- Define objective, audience, format, platform, duration, tone, and core message.
- Draft the hook and chapter structure.
- Decide the visual language: documentary, tutorial, data card, product demo, meme, cinematic, editorial, or hybrid.
- Record assumptions and facts that need verification.

Output:
- `plan/creative-direction.md`
- `plan/creative-brief.md`

## Footage Analysis

Skill: `footage-analyzer`

Purpose: understand raw video before making edit decisions.

Use this layer when the user provides existing footage.

Actions:
- Inspect metadata, duration, FPS, resolution, audio, and codec.
- Extract key frames or contact sheets.
- Segment footage into shots or practical time ranges.
- Score shots for clarity, composition, motion, lighting, brand fit, and edit value.
- Identify text/logos/cleanup needs.
- Mark best moments and weak moments.

Output:
- `plan/shot-list.md`
- `plan/footage-notes.md`

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

Skills: `edit-director`, then `asset-usage-planner`

Purpose: assign assets to narration and timeline slots so there is no duplication, gap, or misalignment.

Actions:
- Use `edit-director` to choose opening shot, shot order, cut rhythm, retention beats, and removal decisions.
- Map every spoken beat to an asset, visual treatment, or text/card moment.
- Define timing, start frame, end frame, transitions, and on-screen text.
- Flag repeated assets and weak visual beats.
- Confirm that the timeline fits target duration.

Output:
- `plan/edit-decision-list.md`
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

## Look Design

Skill: `look-designer`

Purpose: improve perceived production quality through color, typography, captions, layout, titles, and visual consistency.

Actions:
- Define palette, contrast, type scale, caption style, card system, and safe areas.
- Specify title card, lower-third, callout, and end-card rules.
- Define color correction and grading notes.
- Identify scenes that need visual polish.

Output:
- `plan/lookbook.md`
- `plan/title-style.md`

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

## 8. QA / Quality / Packaging / Export

Skills: `remotion-gotchas-index`, `quality-critic`, `platform-packaging`

Purpose: verify, score, improve, render, package, and prepare publishing material.

Actions:
- Preview the full video.
- Check text fit, timing, audio sync, safe areas, asset quality, and spelling.
- Use `quality-critic` to score hook, clarity, footage, rhythm, visual polish, captions, audio, motion, platform fit, and memorability.
- If average quality is below 8/10, route fixes back to the responsible layer.
- Render the final video.
- Create title, description, cover/thumbnail notes, and publishing checklist.

Output:
- Final render in `exports/`
- `exports/quality-review.md`
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

Direction -> Footage Understanding -> Script -> Assets -> Edit Judgment -> Look/Sound -> Assembly -> Quality Review -> Export.

Each layer should hand the next layer a concrete artifact. If an artifact is missing, create it before moving on.
