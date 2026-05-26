# Prompt Iteration Log

Use this log to turn production attempts into a stable workflow.

## Baseline

- Status: not yet proven by a complete successful production
- Goal: complete one full video from idea to Remotion preview/render and packaging
- Promotion rule: after the first successful run, mark its prompts, workflow files, and skill versions as Baseline v1

## Iteration Template

```md
## Iteration N

Date:
Prompt used:
Video idea:
Target platform/duration:

What worked:

What failed or felt slow:

Skill routing issues:

Asset/music/SFX issues:

Remotion Composition/Scene/Sequence issues:

Prompt change:

Workflow or skill change:

Next test:
```

## Iteration 1

Date: 2026-05-25

Prompt used:

制作一个 60 秒竖屏视频，讲清楚“为什么不要用一个万能 prompt 自动剪视频”，风格清晰、节奏快、适合发到 B 站或小红书。

Video idea:

Explain why one universal prompt is not enough for automated video editing, and present the project’s layered Agent workflow as the solution.

Target platform/duration:

B 站 / 小红书, vertical, 60 seconds.

What worked:

- The 8-layer workflow produced clear planning artifacts before implementation.
- A no-external-assets MVP was feasible using generated graphic cards.
- The Python fallback renderer successfully produced a 60-second vertical MP4.
- The output is suitable as a first demonstrable demo.

What failed or felt slow:

- The local shell did not have npm available, so Remotion Studio/render could not be verified yet.
- The MVP has no real voiceover, BGM, or SFX.
- Visual style is clear but still closer to an explainer prototype than a polished social post.

Skill routing issues:

- Routing worked: planning -> script -> asset manifest -> timeline -> motion -> audio -> Remotion assembly -> QA -> packaging.
- Future improvement: add an explicit fallback route for “render a proof video without npm/Remotion runtime.”

Asset/music/SFX issues:

- External assets were intentionally avoided for rights safety.
- BGM and SFX are listed as missing planned assets.

Remotion Composition/Scene/Sequence issues:

- Remotion source files were created around `Composition`, `Scene`, `Sequence`, `editPlan`, and caption/progress layers.
- Runtime verification is pending dependency installation.

Prompt change:

Add this instruction to future MVP prompts: “If Remotion dependencies are unavailable, create a local fallback render while still writing Remotion source.”

Workflow or skill change:

Consider updating `remotion-assembler` with a fallback-render note for environments without npm.

Next test:

Install Node/npm or Remotion dependencies, run Remotion Studio, and render the same composition at 1080x1920 with audio.
