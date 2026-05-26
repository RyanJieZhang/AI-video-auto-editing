# Quality Upgrade Plan

This document records the change from a workflow that can produce videos to a workflow that can improve videos.

## Why The First Demo Felt Weak

The first system could route tasks and generate artifacts, but it lacked the roles that normally create production value:

- A director to set taste and style.
- A footage analyst to understand what raw material is actually good.
- An edit director to choose rhythm, cuts, removals, and retention beats.
- A look designer to unify color, captions, titles, and visual finish.
- A quality critic to score the draft and force another pass.

Without these layers, the workflow can become organized but still visually average.

## New Quality Layers

| Layer | Skill | Purpose | Main Artifact |
| --- | --- | --- | --- |
| Creative Direction | `creative-director` | Define style, hook, reference direction, and quality bar | `plan/creative-direction.md` |
| Footage Analysis | `footage-analyzer` | Inspect raw footage, score shots, mark cleanup needs | `plan/shot-list.md`, `plan/footage-notes.md` |
| Edit Direction | `edit-director` | Decide opening shot, pacing, cut logic, removals | `plan/edit-decision-list.md` |
| Look Design | `look-designer` | Define color, typography, captions, title cards, polish | `plan/lookbook.md`, `plan/title-style.md` |
| Quality Critique | `quality-critic` | Score the draft and route fixes back to owners | `exports/quality-review.md` |

## New Route

```text
User Need
-> Workflow Router
-> Creative Director
-> Creative Brief
-> Footage Analyzer, if raw footage exists
-> Voiceover Editor
-> Asset Gathering
-> Edit Director
-> Asset Usage Planner
-> Motion Fragments
-> Look Designer
-> Audio Director
-> Remotion / FFmpeg Assembly
-> Technical QA
-> Quality Critic
-> Packaging
-> Prompt Lab Retrospective
```

## Quality Gate

A full video is not considered final unless:

- Technical QA passes.
- `exports/quality-review.md` exists.
- Average quality score is at least 8/10, or the video is explicitly marked as demo-only.
- The top fixes are routed to responsible layers.

## Next Practical Test

Use a real footage-based task, then force these outputs before editing:

- `plan/creative-direction.md`
- `plan/shot-list.md`
- `plan/edit-decision-list.md`
- `plan/lookbook.md`
- `exports/quality-review.md`

## New Tooling

- `scripts/analyze_footage.py`: extracts frames, creates a contact sheet, detects rough shot ranges, writes `plan/shot-list.md` and `plan/footage-notes.md`.
- `scripts/create_export_version.py`: archives renders and review files into versioned folders such as `exports/v001`.
- `platform-profiles/`: platform-specific guidance for Bilibili, Xiaohongshu, Douyin, and YouTube Shorts.
