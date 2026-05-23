---
name: video-workflow-router
description: "Routes multi-step video production requests across specialized video skills. Use at the start of any video creation, editing, Remotion, asset, voiceover, audio, motion, packaging, or export task to decide which skill handles the current layer and what artifact should be produced next."
---

# Video Workflow Router

Use this skill before doing video work. Decide the active layer, call the right downstream skill, and keep each layer from taking over another layer's job.

## Route Map

1. Concept, audience, hook, structure, visual direction: use planning in the project workflow.
2. Voiceover, spoken beats, narration timing, A-roll/B-roll intent: use `voiceover-editor`.
3. Search, generate, download, transcode, verify, and manifest assets: use `asset-gathering`.
4. Assign assets to beats, remove duplicates, build an edit plan: use `asset-usage-planner`.
5. Hook frames, advanced transitions, data cards, demos, kinetic moments: use `motion-fragments`.
6. BGM, music search, sound effects, ducking, audio priority: use `audio-director`.
7. Remotion Composition, Scene, Sequence, CaptionLayer, editPlan implementation: use `remotion-assembler` and `remotion-best-practices`.
8. Debugging Remotion failures or risky patterns: use `remotion-gotchas-index`.
9. Titles, thumbnails, timestamps, descriptions, platform exports: use `platform-packaging`.

## Routing Protocol

For every request, state:

- Active layer
- Inputs found
- Missing blockers
- Skill to use next
- Artifact to produce

Proceed when the missing blockers are not essential. Ask only when the choice affects creative direction, factual accuracy, rights, or publishing.

## Boundaries

- Do not download or generate assets directly; route to `asset-gathering`.
- Do not write Remotion components directly; route to `remotion-assembler`.
- Do not patch random timeline issues from packaging; route back to the responsible layer.
- Do not combine planning, asset acquisition, implementation, and export in one undifferentiated answer.

## Handoff Format

```md
Layer:
Using skill:
Inputs:
Missing:
Next artifact:
Decision:
```
