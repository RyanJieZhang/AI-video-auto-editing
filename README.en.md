# AI-video-auto-editing

[中文](README.zh-CN.md) | [English](README.en.md)

A Codex Skills + Remotion workflow project for AI-assisted video creation and automated editing.

This repository is not built around a single all-powerful prompt. Instead, it turns video creation into a reusable, debuggable, and continuously improvable production system: creative planning, voiceover writing, asset gathering, asset alignment, motion design, audio direction, Remotion assembly, QA, export, and publishing.

## Project Purpose

This project is designed to help build a from-zero-to-one video creation workflow:

- Start from a video idea, raw footage, or production brief.
- Let Codex break the task into clear production layers.
- Produce a concrete artifact at each layer.
- Hand each artifact to the next layer.
- Implement, preview, render, and package the video with Remotion.
- Review each production attempt and improve the prompts and skills for the next run.

Core principle:

```text
Planning -> Script -> Assets -> Alignment -> Motion -> Audio -> Remotion Assembly -> QA/Export -> Retrospective
```

## 8-Layer Video Creation System

The project uses layered collaboration instead of asking one prompt to do everything.

| Layer | Module | Responsibility | Skill |
| --- | --- | --- | --- |
| 1 | Workflow Router / Index | Decide the current stage and which skill to use | `video-workflow-router` |
| 2 | Creative & Planning | Define topic, audience, hook, chapters, and visual direction | Project workflow template |
| 3 | Voiceover Editor | Rewrite narration, split spoken beats, plan A-roll/B-roll | `voiceover-editor` |
| 4 | Asset Factory | Search, generate, download, transcode, and validate assets | `asset-gathering` |
| 5 | Asset Usage & Alignment | De-duplicate assets, assign timeline slots, align to meaning | `asset-usage-planner` |
| 6 | Motion / HyperFrames | Plan hook frames, transitions, data cards, and advanced motion | `motion-fragments` |
| 7 | Audio Direction | Plan BGM, SFX, ducking, and voice priority | `audio-director` |
| 8 | Remotion Assembly / QA / Export | Build Composition, Scene, Sequence, captions, and exports | `remotion-assembler`, `remotion-gotchas-index`, `platform-packaging` |

Additional optimization skill:

| Module | Responsibility | Skill |
| --- | --- | --- |
| Prompt Lab | Test prompts, review failures, and improve workflow/skills | `video-prompt-lab` |

## Repository Structure

```text
.
├── AGENTS.md
├── README.md
├── README.zh-CN.md
├── README.en.md
├── assets/
├── exports/
├── plan/
├── prompts/
│   ├── layer-rerun-prompts.md
│   ├── master-codex-video-production.md
│   └── retrospective-prompt.md
├── skills/
│   ├── asset-gathering/
│   ├── asset-usage-planner/
│   ├── audio-director/
│   ├── motion-fragments/
│   ├── platform-packaging/
│   ├── remotion-assembler/
│   ├── remotion-gotchas-index/
│   ├── video-prompt-lab/
│   ├── video-workflow-router/
│   └── voiceover-editor/
└── workflow/
    ├── layer-output-templates.md
    ├── prompt-iteration-log.md
    └── video-creation-system.md
```

### Key Directories

- `AGENTS.md`: Project-level Codex execution rules and routing logic.
- `workflow/`: Full video creation system, layer output templates, and prompt iteration log.
- `prompts/`: Reusable prompts for full production runs, layer reruns, and retrospectives.
- `skills/`: Custom Codex Skills created for this video workflow.
- `plan/`: Creative brief, script, asset list, timeline, motion plan, audio plan, and other intermediate artifacts.
- `assets/`: Video clips, images, music, sound effects, screenshots, and generated assets.
- `exports/`: Final renders, thumbnails, publishing copy, and QA notes.

## Custom Skills

This repository includes 10 custom Codex Skills.

### `video-workflow-router`

Decides which layer the current task belongs to and which skill should handle the next step.

Use it when:

- Starting a new video task.
- You are not sure whether to edit the script, assets, timeline, or Remotion code.
- A multi-round edit needs to be reoriented.

### `voiceover-editor`

Turns an idea or draft into spoken video narration.

Responsible for:

- Rewriting for natural speech.
- Splitting spoken beats.
- Estimating beat duration.
- Marking A-roll / B-roll needs.
- Marking visual support required for each beat.

Not responsible for:

- Downloading assets.
- Final editing decisions.
- Remotion implementation.

### `asset-gathering`

Owns asset acquisition and the asset manifest.

Responsible for:

- Searching assets.
- Generating assets.
- Downloading assets.
- Transcoding assets.
- Verifying usability.
- Recording source, rights, purpose, and status.

Typical outputs:

```text
plan/asset-list.md
assets/
```

### `asset-usage-planner`

Decides how gathered assets should be stitched into the video.

Responsible for:

- Mapping assets to script beats.
- Planning A-roll / B-roll.
- Avoiding repeated or redundant assets.
- Building a scene-level timeline.
- Detecting missing assets.

Typical output:

```text
plan/timeline.md
```

### `motion-fragments`

Plans advanced motion and high-impact visual moments.

Responsible for:

- Hook frames.
- Data cards.
- Kinetic captions.
- Transitions.
- Website demo focus moments.
- Meme-style backgrounds.
- Thumbnail or title frames.

Typical output:

```text
plan/motion-plan.md
```

### `audio-director`

Plans music and sound design.

Responsible for:

- BGM style.
- Music energy and rhythm.
- Ducking.
- Voice priority.
- SFX timing.
- Loop points.
- Fade-in and fade-out.

Typical output:

```text
plan/audio-plan.md
```

### `remotion-assembler`

Turns all planning artifacts into Remotion code.

Core structure:

- `Composition`
- `Scene`
- `Sequence`
- `editPlan`
- `CaptionLayer`
- `AudioLayer`

Use it together with the Remotion best practices skill.

### `remotion-gotchas-index`

Debugs common Remotion problems.

Use it for:

- Blank previews.
- Broken asset paths.
- Caption drift.
- Audio desync.
- Render errors.
- Frame math mistakes.
- `staticFile()` path issues.

Principle: make narrow fixes, not broad redesigns.

### `platform-packaging`

Prepares the finished video for publishing.

Responsible for:

- Titles.
- Descriptions.
- Timestamps.
- Hashtags.
- Thumbnail / cover notes.
- Export settings.
- QA notes.

Typical output:

```text
exports/packaging.md
```

### `video-prompt-lab`

Continuously improves the whole system.

Responsible for:

- Testing the master prompt.
- Recording failure modes.
- Improving the workflow.
- Revising skills.
- Turning the first successful full production into Baseline v1.

Typical output:

```text
workflow/prompt-iteration-log.md
```

## Starting a Video Project

The recommended workflow is to start with a clear production request, not only raw media.

Use this template:

```text
I want to create a video:

Topic:
Platform:
Target duration:
Aspect ratio:
Language:
Style:
Audience:
Existing assets:
Must keep:
Must remove:
Desired effect:
Reference videos/links:
```

If you already have raw footage, images, music, or text, place them in `assets/` and describe how they should be used.

## Recommended Workflow

### 1. Use the Master Prompt

Open:

```text
prompts/master-codex-video-production.md
```

Copy the prompt, fill in the specific video request, and send it to Codex.

Expected sequence:

1. Use `video-workflow-router`.
2. Create `plan/creative-brief.md`.
3. Use `voiceover-editor`.
4. Create `plan/script.md`.
5. Use `asset-gathering`.
6. Create `plan/asset-list.md`.
7. Use `asset-usage-planner`.
8. Create `plan/timeline.md`.
9. Use `motion-fragments`.
10. Create `plan/motion-plan.md`.
11. Use `audio-director`.
12. Create `plan/audio-plan.md`.
13. Use `remotion-assembler`.
14. Implement the Remotion project.
15. Use `remotion-gotchas-index` for QA.
16. Use `platform-packaging`.
17. Produce exports and publishing materials.

### 2. Rerun One Layer

If one layer is weak, do not restart everything.

Open:

```text
prompts/layer-rerun-prompts.md
```

Choose the prompt for the specific layer.

Example for rewriting voiceover:

```text
Use voiceover-editor to rewrite plan/script.md for stronger spoken pacing.
Preserve the core message, split beats clearly, estimate timing, and mark visual needs.
Do not download assets or edit Remotion code.
```

Example for re-planning asset usage:

```text
Use asset-usage-planner to map the current assets to script beats.
Produce plan/timeline.md with scenes, timing, asset IDs, visual roles, on-screen text, and gaps.
Do not download new assets.
```

### 3. Run a Retrospective

After each full production attempt or failed run, use:

```text
prompts/retrospective-prompt.md
```

Ask Codex to update:

```text
workflow/prompt-iteration-log.md
```

Focus on:

- Which skill was selected incorrectly.
- Which layer produced vague or unusable output.
- Whether asset sources were clear.
- Whether music and SFX were tracked.
- Whether the Remotion structure was clean.
- Which prompt sentence should change.
- Which skill rule should be updated.

## Installing / Copying Skills

The `skills/` directory in this repository is a project copy. To make Codex load these skills locally, copy them into the Codex skills directory.

Windows PowerShell example:

```powershell
$repoSkills = "E:\OneDrive - The University of Sydney (Students)\文档\AI视频自动剪辑\skills"
$codexSkills = "$env:USERPROFILE\.codex\skills"
Copy-Item "$repoSkills\*" $codexSkills -Recurse -Force
```

Restart Codex after copying.

## GitHub CLI

This project is hosted at:

```text
https://github.com/RyanJieZhang/AI-video-auto-editing
```

Install GitHub CLI on Windows:

```powershell
winget install --id GitHub.cli
```

Login:

```powershell
gh auth login
```

Check status:

```powershell
gh auth status
```

Common Git commands:

```powershell
git status
git add .
git commit -m "Update workflow"
git push
```

## Remotion Workflow

This repository currently stores workflow documents, prompts, and skills. Once actual video production begins, a Remotion project can be generated inside this repository.

Recommended structure:

```text
src/
├── Root.tsx
├── compositions/
├── scenes/
├── components/
├── data/
│   └── editPlan.ts
└── layers/
    ├── CaptionLayer.tsx
    └── AudioLayer.tsx
```

Remotion implementation principles:

- `Composition` defines the entry, dimensions, FPS, and total duration.
- `Scene` represents a semantic section.
- `Sequence` places content in time.
- `editPlan` structures the script, assets, and timeline.
- `CaptionLayer` renders subtitles.
- `AudioLayer` manages BGM, SFX, and voice strategy.

## Current Status

- [x] Created the 8-layer video creation workflow.
- [x] Created 10 custom Codex Skills.
- [x] Created the master production prompt.
- [x] Created layer rerun prompts.
- [x] Created the retrospective prompt.
- [x] Created the prompt iteration log.
- [x] Uploaded the project to GitHub.
- [ ] Complete the first full video production run.
- [ ] Mark Baseline v1.
- [ ] Continue improving skills based on real production results.

## Suggested Next Steps

1. Choose a concrete video topic.
2. Use `prompts/master-codex-video-production.md` to start the first full production.
3. Reach a Remotion preview or render.
4. Use `prompts/retrospective-prompt.md` to review the run.
5. Update prompts, workflow, or skills.
6. After the first successful run, mark that version as Baseline v1.

## License

No license has been specified yet. Before public reuse, consider adding MIT, Apache-2.0, or a private-use notice.
