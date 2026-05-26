# Quality Gate

Use this gate after every rendered draft.

## Required Checks

1. The export opens and has a duration above 3 seconds.
2. The export has audio unless the project explicitly asks for silent motion graphics.
3. The aspect ratio matches the target platform profile.
4. `exports/quality-review.md` includes an average score.
5. Average quality score is at least 8/10 before calling the video final.

## Command

```powershell
python scripts/quality_gate.py exports/zhangfu-airline-v002-vertical.mp4 --vertical --min-score 8
```

## Decision

- `PASS`: Archive with `scripts/create_export_version.py` and mark as release candidate.
- `FAIL`: Route the failed dimension back to the owning skill and create another version.

## Why This Exists

Good video production needs a stop rule. Without a gate, every draft feels subjective and the agent can keep polishing the wrong layer.
