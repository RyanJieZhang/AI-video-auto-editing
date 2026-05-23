# Retrospective Prompt

Use this after a full or partial production run.

```text
Use video-prompt-lab to review the last video production run.

Inputs:
- Current project files
- Any failed commands or preview/render issues
- The final or latest output

Review:
1. Which layer worked best?
2. Which layer produced vague, missing, or unusable output?
3. Did any skill do work outside its responsibility?
4. Were asset sources, music/SFX, rights, and file paths tracked well?
5. Did the Remotion implementation correctly separate Composition, Scene, Sequence, editPlan, CaptionLayer, and AudioLayer?
6. What exact prompt sentence should be changed?
7. What exact workflow or skill rule should be changed?

Update:
- workflow/prompt-iteration-log.md
- prompts/master-codex-video-production.md if the main prompt needs tightening
- the relevant skill only if the failure belongs in reusable behavior
```
