---
name: audio-director
description: "Plans and directs video audio, including BGM selection, music acquisition strategy, sound effects, ducking, voice priority, beat hits, loop points, ambience, and audio mix notes. Use when a video needs music, SFX, narration balance, or audio timing. Do not use to generate TTS replacing the user unless explicitly requested."
---

# Audio Director

Make the audio plan support the edit instead of fighting the voice.

## Responsibilities

- Choose BGM mood, tempo, energy curve, and licensing requirements.
- Identify SFX needs by beat and motion event.
- Define voice priority, ducking, fade-in/fade-out, and loop points.
- Prepare implementation notes for Remotion audio tracks.

## Music Workflow

1. Read the brief, script, and timeline.
2. Define the music role: tension, pace, warmth, authority, humor, urgency, or atmosphere.
3. Search or request music candidates through `asset-gathering` when files are missing.
4. Pick one primary BGM and optional alternates.
5. Mark intro point, loop region, ducking amount, and ending treatment.

## SFX Workflow

1. Identify motion events that deserve sound.
2. Use SFX sparingly for impact, transitions, UI clicks, whooshes, notification beats, reveals, and comic emphasis.
3. Route missing SFX acquisition to `asset-gathering`.
4. Record exact beat/time and mix intent.

## Output

Write audio notes into `plan/timeline.md` or a dedicated `plan/audio-plan.md`:

```md
| Time | Audio | Asset ID | Mix | Purpose | Notes |
| --- | --- | --- | --- | --- | --- |
```

## Do Not

- Do not generate TTS to replace the user's voice unless asked.
- Do not let BGM overpower narration.
- Do not add SFX to every transition.
- Do not download final audio directly if acquisition/provenance should be tracked by `asset-gathering`.
