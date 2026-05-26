from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class FrameSample:
    time: float
    image: Image.Image
    brightness: float
    contrast: float
    sharpness: float
    diff: float


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


FONT_LABEL = font(22, True)
FONT_SMALL = font(16, True)


def to_gray(frame: np.ndarray) -> np.ndarray:
    rgb = frame.astype(np.float32)
    return 0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]


def sharpness_score(gray: np.ndarray) -> float:
    gx = np.diff(gray, axis=1)
    gy = np.diff(gray, axis=0)
    return float((gx.var() + gy.var()) / 2)


def frame_stats(frame: np.ndarray, previous_gray: np.ndarray | None) -> tuple[float, float, float, float, np.ndarray]:
    gray = to_gray(frame)
    brightness = float(gray.mean())
    contrast = float(gray.std())
    sharpness = sharpness_score(gray)
    diff = 0.0 if previous_gray is None else float(np.mean(np.abs(gray - previous_gray)))
    return brightness, contrast, sharpness, diff, gray


def quality_label(brightness: float, contrast: float, sharpness: float) -> tuple[int, str]:
    score = 10
    notes: list[str] = []
    if brightness < 45:
        score -= 2
        notes.append("too dark")
    elif brightness > 220:
        score -= 2
        notes.append("too bright")
    if contrast < 28:
        score -= 2
        notes.append("low contrast")
    if sharpness < 120:
        score -= 2
        notes.append("soft/blurred")
    elif sharpness < 260:
        score -= 1
        notes.append("slightly soft")
    score = max(1, min(10, score))
    return score, ", ".join(notes) if notes else "usable"


def detect_shots(samples: list[FrameSample], threshold: float) -> list[tuple[float, float, list[FrameSample]]]:
    shots: list[tuple[float, float, list[FrameSample]]] = []
    current: list[FrameSample] = []
    start = samples[0].time if samples else 0.0
    for sample in samples:
        if current and sample.diff > threshold:
            shots.append((start, current[-1].time, current))
            current = []
            start = sample.time
        current.append(sample)
    if current:
        shots.append((start, current[-1].time, current))
    return shots


def make_contact_sheet(samples: list[FrameSample], output: Path, columns: int = 4) -> None:
    thumb_w, thumb_h = 320, 180
    rows = math.ceil(len(samples) / columns)
    sheet = Image.new("RGB", (thumb_w * columns, thumb_h * rows), "white")
    draw = ImageDraw.Draw(sheet)
    for index, sample in enumerate(samples):
        x = (index % columns) * thumb_w
        y = (index // columns) * thumb_h
        thumb = sample.image.resize((thumb_w, thumb_h))
        sheet.paste(thumb, (x, y))
        draw.rectangle((x, y, x + 92, y + 28), fill=(0, 0, 0))
        draw.text((x + 8, y + 4), f"{sample.time:05.2f}s", font=FONT_SMALL, fill=(255, 255, 255))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92)


def write_markdown(
    video_path: Path,
    meta: dict,
    shots: list[tuple[float, float, list[FrameSample]]],
    output_dir: Path,
    plan_dir: Path,
) -> None:
    shot_lines = [
        "# Shot List",
        "",
        f"Source: `{video_path}`",
        "",
        "| Shot | Time Range | Description | Quality | Use | Risks | Notes |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    best: list[tuple[float, int, str]] = []
    weak: list[tuple[float, int, str]] = []
    for index, (start, end, samples) in enumerate(shots, start=1):
        avg_brightness = sum(s.brightness for s in samples) / len(samples)
        avg_contrast = sum(s.contrast for s in samples) / len(samples)
        avg_sharpness = sum(s.sharpness for s in samples) / len(samples)
        quality, risk = quality_label(avg_brightness, avg_contrast, avg_sharpness)
        use = "strong candidate" if quality >= 8 else "use briefly" if quality >= 6 else "avoid unless needed"
        description = "Potential shot segment detected from visual change analysis"
        shot_lines.append(
            f"| S{index:02d} | {start:.2f}-{end:.2f}s | {description} | {quality} | {use} | {risk} | brightness {avg_brightness:.0f}, contrast {avg_contrast:.0f}, sharpness {avg_sharpness:.0f} |"
        )
        target = best if quality >= 8 else weak if quality <= 5 else None
        if target is not None:
            target.append((start, quality, risk))

    notes = [
        "# Footage Notes",
        "",
        "## Metadata",
        "",
        f"- Source: `{video_path}`",
        f"- Duration: {meta.get('duration', 'unknown')}s",
        f"- FPS: {meta.get('fps', 'unknown')}",
        f"- Size: {meta.get('size', meta.get('source_size', 'unknown'))}",
        f"- Codec: {meta.get('codec', 'unknown')}",
        f"- Audio codec: {meta.get('audio_codec', 'none')}",
        "",
        "## Best Moments",
        "",
    ]
    notes.extend([f"- Around {start:.2f}s: quality {quality}/10 ({risk})" for start, quality, risk in best] or ["- No obvious high-scoring moments detected automatically."])
    notes.extend(["", "## Weak or Unusable Moments", ""])
    notes.extend([f"- Around {start:.2f}s: quality {quality}/10 ({risk})" for start, quality, risk in weak] or ["- No severe low-quality segment detected automatically."])
    notes.extend(
        [
            "",
            "## Text / Logo / Cleanup Needs",
            "",
            "- Automatic OCR is not enabled in this lightweight pass. Review the contact sheet manually for text, logos, and cleanup targets.",
            "",
            "## Editing Opportunities",
            "",
            "- Use high-scoring shots for opening, proof moments, and transitions.",
            "- Use lower-scoring shots only briefly or as background texture.",
            "- Run `edit-director` after this analysis to decide actual shot order and rhythm.",
            "",
            f"Contact sheet: `{output_dir / 'contact-sheet.jpg'}`",
        ]
    )

    plan_dir.mkdir(parents=True, exist_ok=True)
    (plan_dir / "shot-list.md").write_text("\n".join(shot_lines) + "\n", encoding="utf-8")
    (plan_dir / "footage-notes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")


def analyze(video_path: Path, output_dir: Path, plan_dir: Path, interval: float, threshold: float) -> None:
    reader = imageio.get_reader(video_path)
    meta = reader.get_meta_data()
    fps = float(meta["fps"])
    duration = float(meta.get("duration", 0))
    sample_times = [round(t, 3) for t in np.arange(0, max(duration, 0.01), interval)]
    if duration and (not sample_times or sample_times[-1] < duration - 0.1):
        sample_times.append(max(0.0, duration - 0.05))

    samples: list[FrameSample] = []
    previous_gray: np.ndarray | None = None
    frames_dir = output_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    for time in sample_times:
        frame = reader.get_data(min(int(time * fps), int(max(0, duration * fps - 1))))
        brightness, contrast, sharpness, diff, gray = frame_stats(frame, previous_gray)
        previous_gray = gray
        image = Image.fromarray(frame).convert("RGB")
        image.save(frames_dir / f"frame_{time:06.2f}s.jpg", quality=90)
        samples.append(FrameSample(time, image, brightness, contrast, sharpness, diff))
    reader.close()

    shots = detect_shots(samples, threshold)
    output_dir.mkdir(parents=True, exist_ok=True)
    make_contact_sheet(samples, output_dir / "contact-sheet.jpg")
    write_markdown(video_path, meta, shots, output_dir, plan_dir)

    json_data = {
        "source": str(video_path),
        "metadata": meta,
        "sample_interval": interval,
        "shot_threshold": threshold,
        "samples": [
            {
                "time": s.time,
                "brightness": s.brightness,
                "contrast": s.contrast,
                "sharpness": s.sharpness,
                "diff": s.diff,
            }
            for s in samples
        ],
        "shots": [
            {
                "start": start,
                "end": end,
                "sample_count": len(items),
            }
            for start, end, items in shots
        ],
    }
    (output_dir / "analysis.json").write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {plan_dir / 'shot-list.md'}")
    print(f"Wrote {plan_dir / 'footage-notes.md'}")
    print(f"Wrote {output_dir / 'contact-sheet.jpg'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze raw footage and produce shot-list artifacts.")
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--plan-dir", type=Path, default=ROOT / "plan")
    parser.add_argument("--interval", type=float, default=0.5)
    parser.add_argument("--threshold", type=float, default=34.0)
    args = parser.parse_args()

    video_path = args.video.resolve()
    output_dir = args.out or ROOT / "exports" / "analysis" / video_path.stem
    analyze(video_path, output_dir, args.plan_dir, args.interval, args.threshold)


if __name__ == "__main__":
    main()
