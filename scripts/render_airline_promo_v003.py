from __future__ import annotations

import argparse
import math
import subprocess
import tempfile
import wave
from dataclasses import dataclass
from pathlib import Path

import imageio.v2 as imageio
import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "exports" / "张府皇家航空宣传片2_已修改.mp4"
DEFAULT_OUTPUT = ROOT / "exports" / "zhangfu-airline-v003-cinematic.mp4"
DEFAULT_COVER = ROOT / "exports" / "cover-v003.png"
DEFAULT_BGM = ROOT / "assets" / "audio" / "v003_bgm.wav"

WIDTH = 720
HEIGHT = 1280
FPS = 24


@dataclass(frozen=True)
class Beat:
    start: float
    end: float
    title: str
    caption: str


BEATS = [
    Beat(0.0, 1.8, "降落長沙", "张府皇家航空抵达长沙机场"),
    Beat(1.8, 3.6, "城市入口", "先看到城市，再记住品牌"),
    Beat(3.6, 6.4, "云端礼遇", "用机身、客舱和机场建立质感"),
    Beat(6.4, 8.6, "抵达一刻", "红色航站楼标识只保留長沙"),
    Beat(8.6, 10.0, "启程不凡", "张府皇家航空 | 长沙机场"),
]


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


FONT_HERO = font(60, True)
FONT_CAPTION = font(30, True)
FONT_SMALL = font(20, True)
FONT_META = font(17, True)


def current_beat(second: float) -> Beat:
    for beat in BEATS:
        if beat.start <= second < beat.end:
            return beat
    return BEATS[-1]


def ease_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def cover_resize(image: Image.Image, size: tuple[int, int], x_bias: float = 0.5) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize((int(image.width * scale), int(image.height * scale)), Image.Resampling.LANCZOS)
    left = int((resized.width - target_w) * x_bias)
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def fit_resize(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    scale = min(max_size[0] / image.width, max_size[1] / image.height)
    return image.resize((int(image.width * scale), int(image.height * scale)), Image.Resampling.LANCZOS)


def grade(image: Image.Image) -> Image.Image:
    image = ImageEnhance.Color(image).enhance(1.16)
    image = ImageEnhance.Contrast(image).enhance(1.14)
    image = ImageEnhance.Sharpness(image).enhance(1.08)
    return image


def add_vignette(image: Image.Image) -> Image.Image:
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    pixels = overlay.load()
    cx, cy = WIDTH / 2, HEIGHT / 2
    max_dist = math.sqrt(cx * cx + cy * cy)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2) / max_dist
            alpha = int(max(0, dist - 0.38) * 180)
            pixels[x, y] = (0, 8, 18, alpha)
    base = image.convert("RGBA")
    base.alpha_composite(overlay)
    return base


def draw_gradient(draw: ImageDraw.ImageDraw) -> None:
    for y in range(0, 430):
        alpha = int(170 * (1 - y / 430))
        draw.rectangle((0, y, WIDTH, y + 1), fill=(0, 12, 28, alpha))
    for y in range(770, HEIGHT):
        alpha = int(190 * ((y - 770) / (HEIGHT - 770)))
        draw.rectangle((0, y, WIDTH, y + 1), fill=(0, 10, 24, alpha))


def compose_frame(frame: Image.Image, second: float) -> Image.Image:
    beat = current_beat(second)
    frame = grade(frame.convert("RGB"))
    progress = second / BEATS[-1].end

    bg = cover_resize(frame, (WIDTH, HEIGHT), x_bias=0.56).filter(ImageFilter.GaussianBlur(15))
    bg = ImageEnhance.Brightness(bg).enhance(0.72)
    canvas = add_vignette(bg)
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw_gradient(draw)

    inset = fit_resize(frame, (704, 396)).convert("RGBA")
    x = (WIDTH - inset.width) // 2
    y = 410 + int(math.sin(progress * math.pi) * 18)
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((x - 8, y - 8, x + inset.width + 8, y + inset.height + 8), 18, fill=(0, 0, 0, 120))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(12)))
    canvas.alpha_composite(inset, (x, y))

    local = ease_out((second - beat.start) / max(0.1, beat.end - beat.start))
    title_y = int(112 - (1 - local) * 20)
    draw.text((44, title_y), beat.title, font=FONT_HERO, fill=(255, 255, 255, 245))
    draw.text((48, title_y + 86), "ZHANGFU ROYAL AIRLINES", font=FONT_META, fill=(139, 199, 255, 230))

    caption_y = 900
    draw.rounded_rectangle((42, caption_y, WIDTH - 42, caption_y + 130), radius=22, fill=(255, 255, 255, 224))
    draw.text((70, caption_y + 32), beat.caption, font=FONT_CAPTION, fill=(11, 30, 56, 255))
    draw.text((70, caption_y + 88), "v003 cinematic vertical preview", font=FONT_SMALL, fill=(68, 83, 108, 230))

    draw.rounded_rectangle((42, HEIGHT - 74, WIDTH - 42, HEIGHT - 64), 6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((42, HEIGHT - 74, int(42 + (WIDTH - 84) * progress), HEIGHT - 64), 6, fill=(182, 32, 55, 230))
    return canvas.convert("RGB")


def generate_bgm(path: Path, duration: float, sample_rate: int = 48000) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    envelope = np.minimum(1, t / 1.2) * np.minimum(1, (duration - t) / 1.5)
    pad = (
        0.35 * np.sin(2 * np.pi * 110 * t)
        + 0.22 * np.sin(2 * np.pi * 165 * t)
        + 0.16 * np.sin(2 * np.pi * 220 * t)
    )
    pulse = 0.08 * np.sin(2 * np.pi * 2.2 * t) * np.sin(2 * np.pi * 55 * t)
    chime = np.zeros_like(t)
    for hit in (0.25, 6.4, 8.75):
        idx = t >= hit
        dt = t[idx] - hit
        chime[idx] += 0.18 * np.sin(2 * np.pi * 880 * dt) * np.exp(-dt * 7)
    audio = (pad + pulse + chime) * envelope * 0.28
    pcm = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(pcm.tobytes())


def mux_audio(video_no_audio: Path, source: Path, bgm: Path, output: Path) -> None:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    command = [
        ffmpeg,
        "-y",
        "-i",
        str(video_no_audio),
        "-i",
        str(source),
        "-i",
        str(bgm),
        "-filter_complex",
        "[1:a]volume=0.62[a0];[2:a]volume=0.22[a1];[a0][a1]amix=inputs=2:duration=shortest:dropout_transition=0[a]",
        "-map",
        "0:v:0",
        "-map",
        "[a]",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        str(output),
    ]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def render(source: Path, output: Path, cover: Path, bgm: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    reader = imageio.get_reader(source)
    meta = reader.get_meta_data()
    source_fps = float(meta.get("fps", FPS))
    duration = float(meta.get("duration", 10.0))
    total_frames = int(duration * FPS)
    generate_bgm(bgm, duration)

    with tempfile.TemporaryDirectory(dir=output.parent) as tmpdir:
        temp_video = Path(tmpdir) / "v003_no_audio.mp4"
        writer = imageio.get_writer(temp_video, fps=FPS, codec="libx264", quality=8, macro_block_size=1)
        try:
            for out_index in range(total_frames):
                second = out_index / FPS
                source_index = min(int(second * source_fps), int(duration * source_fps) - 1)
                frame = Image.fromarray(reader.get_data(source_index))
                composed = compose_frame(frame, second)
                if out_index == 8:
                    cover.parent.mkdir(parents=True, exist_ok=True)
                    composed.save(cover)
                writer.append_data(np.asarray(composed))
        finally:
            writer.close()
            reader.close()
        mux_audio(temp_video, source, bgm, output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render cinematic v003 vertical airline promo with simple BGM.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--cover", type=Path, default=DEFAULT_COVER)
    parser.add_argument("--bgm", type=Path, default=DEFAULT_BGM)
    args = parser.parse_args()
    render(args.source.resolve(), args.output.resolve(), args.cover.resolve(), args.bgm.resolve())
    print(f"Wrote {args.output.resolve()}")
    print(f"Wrote {args.cover.resolve()}")
    print(f"Wrote {args.bgm.resolve()}")


if __name__ == "__main__":
    main()
