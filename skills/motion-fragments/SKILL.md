---
name: motion-fragments
description: "Designs advanced video motion moments before implementation. Use for HyperFrames, hook visuals, data cards, transitions, kinetic text, website demo moments, meme backgrounds, thumbnail/title frames, and scene-level motion plans. Do not use to own the main timeline or download assets."
---

# Motion Fragments

Design motion ideas as reusable fragments that can be implemented later in Remotion.

## Responsibilities

- Create hook frames and high-retention opening moments.
- Design data cards, comparison cards, callouts, demo focus states, kinetic text, and transition concepts.
- Specify animation intent, timing, easing, hierarchy, and readability.
- Hand implementation notes to `remotion-assembler`.

## Workflow

1. Read `plan/timeline.md` and the visual direction.
2. Identify moments that need motion beyond a simple cut.
3. Design each fragment with purpose: reveal, emphasis, proof, contrast, momentum, pause, or payoff.
4. Keep each fragment implementable as a Remotion component.
5. Write `plan/motion-plan.md`.

## Output

```md
| Fragment | Scene/Beat | Purpose | Visual Design | Motion | Inputs | Remotion Notes |
| --- | --- | --- | --- | --- | --- | --- |
```

## Remotion Handoff

Name fragments in component-friendly form, such as:

- `HookColdOpen`
- `MetricCardReveal`
- `WebsiteZoomCallout`
- `CaptionImpactBeat`
- `MemeBackgroundLoop`

## Do Not

- Do not take over the main edit timeline.
- Do not download assets.
- Do not bury important text under flashy motion.
- Do not create motion that cannot be described in timing, state, and visual hierarchy.
