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
2. Move layer by layer: creative brief, voiceover, assets, asset usage, motion, audio, Remotion assembly, QA, packaging.
3. Produce the expected artifact for each layer before moving on.
4. For assets, use asset-gathering to create a manifest with source, rights, status, and intended use.
5. For music and SFX, use audio-director; do not let music overpower narration.
6. For Remotion, use remotion-assembler plus remotion-best-practices. Structure the implementation around Composition, Scene, Sequence, editPlan, CaptionLayer, and AudioLayer.
7. If preview/render breaks, use remotion-gotchas-index before broad refactors.
8. Finish with platform-packaging.

At every layer, report:
- Active layer
- Skill used
- Output file changed or created
- Blockers or assumptions

Do not stop at advice. Create or update the project files needed for the current layer.
```
