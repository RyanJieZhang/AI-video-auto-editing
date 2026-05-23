---
name: remotion-assembler
description: "Assembles video plans into Remotion React/TypeScript implementations. Use for Composition, Scene, Sequence, timeline data, editPlan, CaptionLayer, asset imports, audio tracks, Remotion Studio preview, and render-ready structure. Always pair with remotion-best-practices for Remotion code."
---

# Remotion Assembler

Turn the plan into Remotion code. Use `remotion-best-practices` with this skill.

## Inputs

- `plan/script.md`
- `plan/asset-list.md`
- `plan/timeline.md`
- `plan/motion-plan.md`
- `plan/audio-plan.md` if present
- Files in `assets/`

## Architecture

Use this hierarchy unless the existing project already has a stronger convention:

- `Composition`: top-level video entry, dimensions, FPS, duration, props.
- `Scenes`: semantic sections of the video, usually one idea per scene.
- `Sequences`: time placement for scenes, overlays, captions, assets, and audio.
- `CaptionLayer`: subtitles or kinetic captions generated from script beats.
- `editPlan`: structured data that maps scenes, beats, asset IDs, timings, and text.

## Workflow

1. Confirm a Remotion project exists; scaffold only if the folder is empty or the user asks.
2. Load Remotion best practices.
3. Convert `plan/timeline.md` into structured `editPlan` data.
4. Build scene components around content and timing, not one-off hardcoded frames.
5. Use `<Sequence>` for temporal placement.
6. Use asset imports or `staticFile()` consistently.
7. Add captions, audio, and SFX from the plan.
8. Start Studio preview when appropriate and verify that the composition is nonblank.

## Composition Pattern

```tsx
export const MainComposition = () => {
  return (
    <>
      {editPlan.scenes.map((scene) => (
        <Sequence key={scene.id} from={scene.from} durationInFrames={scene.duration}>
          <SceneRenderer scene={scene} />
        </Sequence>
      ))}
      <CaptionLayer beats={editPlan.beats} />
      <AudioLayer audio={editPlan.audio} />
    </>
  );
};
```

## Do Not

- Do not invent missing asset paths; send gaps to `asset-gathering`.
- Do not ignore the timeline and hardcode arbitrary timings.
- Do not bury all logic in one giant component.
- Do not skip preview verification for meaningful visual changes.
