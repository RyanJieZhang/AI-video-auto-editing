---
name: video-workflow-router
description: "Routes multi-step video production requests across specialized video skills. Use at the start of any video creation, editing, Remotion, asset, voiceover, audio, motion, packaging, or export task to decide which skill handles the current layer and what artifact should be produced next."
---

# Video Workflow Router

Use this skill before doing video work. Decide the active layer, call the right downstream skill, and keep each layer from taking over another layer's job.

## Route Map

1. Style, hook, reference direction, quality bar: use `creative-director`.
2. Raw footage inspection, shot scoring, text/logo cleanup needs: use `footage-analyzer`.
3. Concept, audience, structure, production constraints: use planning in the project workflow.
4. Voiceover, spoken beats, narration timing, A-roll/B-roll intent: use `voiceover-editor`.
5. Search, generate, download, transcode, verify, and manifest assets: use `asset-gathering`.
6. Opening shot, cut rhythm, removals, retention beats: use `edit-director`.
7. Assign assets to beats, remove duplicates, build an edit plan: use `asset-usage-planner`.
8. Hook frames, advanced transitions, data cards, demos, kinetic moments: use `motion-fragments`.
9. Color, typography, captions, title cards, and visual polish: use `look-designer`.
10. BGM, music search, sound effects, ducking, audio priority: use `audio-director`.
11. Remotion Composition, Scene, Sequence, CaptionLayer, editPlan implementation: use `remotion-assembler` and `remotion-best-practices`.
12. Debugging Remotion failures or risky patterns: use `remotion-gotchas-index`.
13. Scoring draft quality and routing fixes: use `quality-critic`.
14. Titles, thumbnails, timestamps, descriptions, platform exports: use `platform-packaging`.

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
- Do not call a draft final before `quality-critic` scores it.
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
