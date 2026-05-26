# Master Codex Video Production Prompt

Use this prompt to start a full from-zero video production run.

```text
You are working inside this video production workspace. Use the project AGENTS.md workflow and the installed video skills.

Goal:
Create a complete video from this idea:
[PASTE VIDEO IDEA]

Constraints:
- Platform:
- Target duration:
- Aspect ratio:
- Language:
- Tone:
- Audience:
- Must include:
- Must avoid:
- Available assets:

Execution rules:
1. Start with video-workflow-router.
2. Use creative-director before writing the script. Produce plan/creative-direction.md and define the quality bar.
3. If raw footage exists, use footage-analyzer before deciding what to cut. Produce plan/shot-list.md and plan/footage-notes.md.
4. Move layer by layer: creative direction, creative brief, footage analysis when needed, voiceover, assets, edit direction, asset usage, motion, look design, audio, Remotion assembly, technical QA, quality critique, packaging.
5. Produce the expected artifact for each layer before moving on.
6. For assets, use asset-gathering to create a manifest with source, rights, status, and intended use.
7. For edit quality, use edit-director before asset-usage-planner. Produce plan/edit-decision-list.md.
8. For visual polish, use look-designer. Produce plan/lookbook.md and plan/title-style.md.
9. For music and SFX, use audio-director; do not let music overpower narration.
10. For Remotion, use remotion-assembler plus remotion-best-practices. Structure the implementation around Composition, Scene, Sequence, editPlan, CaptionLayer, and AudioLayer.
11. If preview/render breaks, use remotion-gotchas-index before broad refactors.
12. After a draft render, use quality-critic and write exports/quality-review.md. If the average score is below 8/10, route fixes back to the responsible layer instead of calling it final.
13. Finish with platform-packaging.

At every layer, report:
- Active layer
- Skill used
- Output file changed or created
- Blockers or assumptions

Do not stop at advice. Create or update the project files needed for the current layer.
```
