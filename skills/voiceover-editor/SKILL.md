---
name: voiceover-editor
description: "Creates and edits video narration for spoken delivery. Use for voiceover transcription, rewriting text into natural speech, aligning narration to visual beats, splitting spoken beats, estimating duration, and planning A-roll/B-roll strategy. Do not use for downloading assets or final visual editing."
---

# Voiceover Editor

Turn an idea or draft into narration that can be timed, voiced, and edited.

## Responsibilities

- Rewrite text for speech instead of reading.
- Split narration into short spoken beats.
- Estimate duration per beat using normal speaking pace.
- Mark pauses, emphasis, and moments needing visual support.
- Decide A-roll versus B-roll intent for each beat.

## Workflow

1. Identify the audience, platform, target duration, and tone.
2. Draft or refine the hook first.
3. Break the script into beats of one idea each.
4. Assign each beat a visual need: face, screen, photo, data card, motion graphic, demo, meme, or text-only.
5. Flag facts, quotes, numbers, and claims that need verification.

## Output

Write `plan/script.md`:

```md
# Voiceover Script

| Beat | Time | Voiceover | Spoken Direction | Visual Need | A/B Roll |
| --- | --- | --- | --- | --- | --- |
```

## Do Not

- Do not download, generate, or license assets.
- Do not make final timeline decisions beyond narration-level timing.
- Do not replace the user's voice with TTS unless explicitly asked.
- Do not polish visuals; hand visual needs to `asset-gathering` and `asset-usage-planner`.
