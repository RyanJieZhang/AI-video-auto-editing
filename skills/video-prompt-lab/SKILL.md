---
name: video-prompt-lab
description: "Runs iterative prompt experiments for the video creation workflow. Use when Codex needs to test prompts, compare outputs, refine the 8-layer video workflow, update video skills, capture failure modes, or turn a successful from-zero-to-one production into a reusable fixed process."
---

# Video Prompt Lab

Use this skill to improve the workflow itself. The goal is not one perfect prompt; the goal is a repeatable loop that turns trial runs into stronger prompts, sharper skill boundaries, and a stable production system.

## Loop

1. Choose a test prompt from `prompts/`.
2. Run the prompt against the current project state.
3. Capture the outputs, mistakes, friction, missing artifacts, and unclear skill routing.
4. Update workflow docs, prompts, or the relevant skill.
5. Run the smallest useful test again.
6. Promote the prompt only after it produces a complete artifact with fewer interventions.

## What To Measure

- Did the router pick the right skill and layer?
- Did each layer create the expected file?
- Did any skill do work outside its responsibility?
- Were missing assets, rights, music, SFX, captions, or Remotion timing handled explicitly?
- Did the Remotion structure use Composition, Scene, Sequence, editPlan, and CaptionLayer cleanly?
- Did QA catch real preview/render/package issues?

## Artifacts

Use these files:

- `prompts/master-codex-video-production.md`: main from-zero prompt.
- `prompts/layer-rerun-prompts.md`: targeted prompts for one layer at a time.
- `prompts/retrospective-prompt.md`: after-action review prompt.
- `workflow/prompt-iteration-log.md`: running record of prompt versions, tests, and changes.

## Revision Rules

- Improve one bottleneck at a time.
- Prefer tightening one skill's responsibility over making the router smarter about everything.
- Add examples only when the failure is repeated or predictable.
- Move detailed reusable guidance into a skill; keep project workflow docs as the operating map.
- Mark the first successful full production as the baseline process before optimizing for speed.

## Done Definition

A prompt iteration is done when the test result, observed failure/success, and resulting change are recorded in `workflow/prompt-iteration-log.md`.
