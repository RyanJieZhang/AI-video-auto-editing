from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "exports"


def next_version(exports_dir: Path) -> str:
    existing = []
    for path in exports_dir.glob("v[0-9][0-9][0-9]"):
        if path.is_dir():
            try:
                existing.append(int(path.name[1:]))
            except ValueError:
                pass
    return f"v{(max(existing) + 1 if existing else 1):03d}"


def copy_if_exists(source: Path, dest_dir: Path) -> str | None:
    if not source.exists():
        return None
    dest = dest_dir / source.name
    shutil.copy2(source, dest)
    return dest.name


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive a rendered video and related notes into exports/vNNN.")
    parser.add_argument("video", type=Path)
    parser.add_argument("--name", default=None, help="Version folder name such as v002. Defaults to next available.")
    parser.add_argument("--notes", type=Path, nargs="*", default=[])
    parser.add_argument("--quality-review", type=Path, default=EXPORTS / "quality-review.md")
    parser.add_argument("--packaging", type=Path, default=EXPORTS / "packaging.md")
    args = parser.parse_args()

    EXPORTS.mkdir(exist_ok=True)
    version = args.name or next_version(EXPORTS)
    version_dir = EXPORTS / version
    version_dir.mkdir(parents=True, exist_ok=True)

    copied: list[str] = []
    video_name = copy_if_exists(args.video.resolve(), version_dir)
    if video_name:
        copied.append(video_name)
    for path in [args.quality_review, args.packaging, *args.notes]:
        copied_name = copy_if_exists(path.resolve(), version_dir)
        if copied_name:
            copied.append(copied_name)

    manifest = [
        "# Export Version",
        "",
        f"- Version: `{version}`",
        f"- Created: {datetime.now().isoformat(timespec='seconds')}",
        f"- Source video: `{args.video}`",
        "",
        "## Files",
        "",
    ]
    manifest.extend([f"- `{name}`" for name in copied] or ["- No files copied"])
    manifest.extend(
        [
            "",
            "## Review Checklist",
            "",
            "- [ ] Watch full video end to end",
            "- [ ] Compare against creative direction",
            "- [ ] Check captions and safe areas",
            "- [ ] Check audio clarity and loudness",
            "- [ ] Run or update quality review",
            "- [ ] Decide: final, revise, or demo-only",
        ]
    )
    (version_dir / "manifest.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"Wrote {version_dir}")


if __name__ == "__main__":
    main()
