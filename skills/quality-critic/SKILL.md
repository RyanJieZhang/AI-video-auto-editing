---
name: quality-critic
description: "Reviews finished or draft videos for quality, not just technical correctness. Use after preview or render to score hook strength, clarity, pacing, visual polish, audio, captions, platform fit, originality, and production value, then route fixes back to the responsible skill."
---

# Quality Critic

Use this skill after a draft render, preview, or meaningful production milestone. This is the quality gate that decides whether the video is publishable or needs another pass.

## Responsibilities

- Score the video against a clear rubric.
- Identify the weakest layer causing quality problems.
- Separate taste issues from technical bugs.
- Route fixes back to the correct owner.
- Decide whether the video is publishable, demo-only, or needs rework.

## Rubric

Score each item from 1 to 10:

- Hook strength
- Message clarity
- Footage selection
- Edit rhythm
- Visual polish
- Caption readability
- Audio quality
- Motion design
- Platform fit
- Memorability

## Workflow

1. Inspect the latest render, preview frame, packaging notes, and timeline.
2. Score the rubric.
3. List the top 3 quality blockers.
4. Route each blocker to the responsible skill.
5. Write `exports/quality-review.md`.
6. If average score is below 8, do not mark the video as final.

## Output

```md
# Quality Review

## Verdict

## Scores

| Dimension | Score | Notes | Owner |
| --- | ---: | --- | --- |

## Top Fixes

## Publishability

## Next Pass
```

## Do Not

- Do not only check for broken files.
- Do not say "looks good" without scores.
- Do not fix everything directly; route changes to the owning layer.
- Do not approve a video with weak hook, unreadable text, or poor audio.
