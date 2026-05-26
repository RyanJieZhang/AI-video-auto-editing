from __future__ import annotations

import argparse
import json
from pathlib import Path

import imageio.v3 as iio


ROOT = Path(__file__).resolve().parents[1]


def parse_review(path: Path) -> tuple[float | None, str]:
    if not path.exists():
        return None, "missing quality review"
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "Average score:" in line:
            raw = line.split("Average score:", 1)[1].split("/", 1)[0].strip()
            try:
                return float(raw), "ok"
            except ValueError:
                return None, "average score is not parseable"
    return None, "average score not found"


def inspect_video(path: Path) -> dict:
    meta = iio.immeta(path)
    width, height = meta.get("size", (0, 0))
    return {
        "path": str(path),
        "exists": path.exists(),
        "width": width,
        "height": height,
        "duration": float(meta.get("duration", 0)),
        "fps": float(meta.get("fps", 0)),
        "audio_codec": meta.get("audio_codec"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Check whether an export is ready to publish.")
    parser.add_argument("video", type=Path)
    parser.add_argument("--review", type=Path, default=ROOT / "exports" / "quality-review.md")
    parser.add_argument("--min-score", type=float, default=8.0)
    parser.add_argument("--vertical", action="store_true", help="Require 9:16-ish vertical output.")
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    video = args.video.resolve()
    checks: list[dict] = []
    passed = True

    if not video.exists():
        checks.append({"name": "video exists", "passed": False, "detail": str(video)})
        passed = False
        report = {"passed": passed, "checks": checks}
    else:
        info = inspect_video(video)
        checks.append({"name": "video exists", "passed": True, "detail": str(video)})
        checks.append({"name": "duration > 3s", "passed": info["duration"] > 3, "detail": f'{info["duration"]:.2f}s'})
        checks.append({"name": "fps >= 23", "passed": info["fps"] >= 23, "detail": f'{info["fps"]:.2f} fps'})
        checks.append({"name": "audio present", "passed": bool(info["audio_codec"]), "detail": info["audio_codec"] or "none"})
        if args.vertical:
            ratio = info["width"] / max(1, info["height"])
            checks.append({"name": "vertical aspect", "passed": 0.50 <= ratio <= 0.60, "detail": f'{info["width"]}x{info["height"]}'})
        average, review_detail = parse_review(args.review.resolve())
        checks.append({"name": "quality review exists", "passed": average is not None, "detail": review_detail})
        if average is not None:
            checks.append({"name": f"average score >= {args.min_score}", "passed": average >= args.min_score, "detail": f"{average:.1f}/10"})
        passed = all(check["passed"] for check in checks)
        report = {"passed": passed, "video": info, "checks": checks}

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for check in checks:
        marker = "PASS" if check["passed"] else "FAIL"
        print(f"[{marker}] {check['name']}: {check['detail']}")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
