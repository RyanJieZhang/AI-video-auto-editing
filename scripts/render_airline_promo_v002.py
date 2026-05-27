from __future__ import annotations

import argparse
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import imageio.v2 as imageio
import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "exports" / "张府皇家航空宣传片2_已修改.mp4"
DEFAULT_OUTPUT = ROOT / "exports" / "zhangfu-airline-v002-vertical.mp4"

WIDTH = 720
HEIGHT = 1280
FPS = 24


@dataclass(frozen=True)
class Beat:
    start: float
    end: float
    title: str
    caption: str
    tag: str


BEATS = [
    Beat(0.0, 1.5, "降落長沙", "张府皇家航空，把城市入口拍成第一记忆点。", "OPENING"),
    Beat(1.5, 3.1, "从登机到客舱", "先给环境，再给服务，观众更容易进入故事。", "SERVICE"),
    Beat(3.1, 5.7, "机身与客舱质感", "保留高识别度镜头，让品牌看起来更完整。", "PROOF"),
    Beat(5.7, 8.3, "机场标识修正", "用竖屏包装弱化修补区域，把注意力拉回品牌。", "POLISH"),
    Beat(8.3, 10.0, "下一版可继续打磨", "从技术 demo 进入可发布短片，需要每版都有评分。", "QA"),
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


FONT_TITLE = font(58, True)
FONT_CAPTION = font(28, True)
FONT_SMALL = font(18, True)
FONT_TAG = font(20, True)


def beat_for_second(second: float) -> Beat:
    for beat in BEATS:
        if beat.start <= second < beat.end:
            return beat
    return BEATS[-1]


def ease_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def cover_resize(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize((int(image.width * scale), int(image.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def fit_resize(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    max_w, max_h = max_size
    scale = min(max_w / image.width, max_h / image.height)
    return image.resize((int(image.width * scale), int(image.height * scale)), Image.Resampling.LANCZOS)


def grade(image: Image.Image) -> Image.Image:
    image = ImageEnhance.Color(image).enhance(1.12)
    image = ImageEnhance.Contrast(image).enhance(1.10)
    image = ImageEnhance.Sharpness(image).enhance(1.08)
    return image


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font_obj: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        test = current + char
        if draw.textbbox((0, 0), test, font=font_obj)[2] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font_obj: ImageFont.FreeTypeFont, fill, max_width: int) -> int:
    x, y = xy
    for line in wrap_text(draw, text, font_obj, max_width):
        draw.text((x, y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font_obj)
        y += bbox[3] - bbox[1] + 10
    return y


def overlay_panel(base: Image.Image, box: tuple[int, int, int, int], fill: tuple[int, int, int, int], radius: int = 28) -> None:
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle(box, radius=radius, fill=fill)
    base.alpha_composite(layer)


def compose_frame(frame: Image.Image, second: float) -> Image.Image:
    beat = beat_for_second(second)
    frame = grade(frame.convert("RGB"))

    bg = cover_resize(frame, (WIDTH, HEIGHT)).filter(ImageFilter.GaussianBlur(20))
    bg = ImageEnhance.Brightness(bg).enhance(0.62).convert("RGBA")

    canvas = bg
    draw = ImageDraw.Draw(canvas)

    local_t = ease_out((second - beat.start) / max(0.1, beat.end - beat.start))
    fg = fit_resize(frame, (656, 420)).convert("RGBA")
    fg_y = int(372 - (1 - local_t) * 18)
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    x = (WIDTH - fg.width) // 2
    shadow_draw.rounded_rectangle((x - 8, fg_y - 8, x + fg.width + 8, fg_y + fg.height + 8), 28, fill=(0, 0, 0, 90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(fg, (x, fg_y))

    overlay_panel(canvas, (42, 52, WIDTH - 42, 308), (9, 24, 45, 208), 30)
    draw = ImageDraw.Draw(canvas)
    draw.text((70, 78), beat.tag, font=FONT_TAG, fill=(121, 192, 255))
    draw_wrapped(draw, (70, 120), beat.title, FONT_TITLE, (255, 255, 255), WIDTH - 140)
    draw.line((70, 284, WIDTH - 70, 284), fill=(255, 255, 255, 72), width=2)

    overlay_panel(canvas, (42, 842, WIDTH - 42, 1074), (255, 255, 255, 230), 28)
    draw = ImageDraw.Draw(canvas)
    draw_wrapped(draw, (72, 882), beat.caption, FONT_CAPTION, (13, 31, 56), WIDTH - 144)
    draw.text((72, 1018), "张府皇家航空  |  v002 竖屏预览", font=FONT_SMALL, fill=(72, 91, 120))

    progress = min(1.0, max(0.0, second / BEATS[-1].end))
    draw.rounded_rectangle((42, HEIGHT - 74, WIDTH - 42, HEIGHT - 62), radius=8, fill=(255, 255, 255, 86))
    draw.rounded_rectangle((42, HEIGHT - 74, int(42 + (WIDTH - 84) * progress), HEIGHT - 62), radius=8, fill=(37, 126, 255, 230))
    return canvas.convert("RGB")


def mux_audio(video_no_audio: Path, source: Path, output: Path) -> None:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    command = [
        ffmpeg,
        "-y",
        "-i",
        str(video_no_audio),
        "-i",
        str(source),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0?",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        str(output),
    ]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def render(source: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    reader = imageio.get_reader(source)
    meta = reader.get_meta_data()
    source_fps = float(meta.get("fps", FPS))
    duration = float(meta.get("duration", 10.0))
    total_frames = int(duration * FPS)

    with tempfile.TemporaryDirectory(dir=output.parent) as tmpdir:
        temp_video = Path(tmpdir) / "v002_no_audio.mp4"
        writer = imageio.get_writer(temp_video, fps=FPS, codec="libx264", quality=8, macro_block_size=1)
        try:
            for out_index in range(total_frames):
                second = out_index / FPS
                source_index = min(int(second * source_fps), int(duration * source_fps) - 1)
                frame = Image.fromarray(reader.get_data(source_index))
                writer.append_data(np.asarray(compose_frame(frame, second)))
        finally:
            writer.close()
            reader.close()
        try:
            mux_audio(temp_video, source, output)
        except subprocess.CalledProcessError:
            output.write_bytes(temp_video.read_bytes())


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a polished vertical v002 airline promo from the edited source video.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    render(args.source.resolve(), args.output.resolve())
    print(f"Wrote {args.output.resolve()}")


if __name__ == "__main__":
    main()
