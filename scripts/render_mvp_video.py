from __future__ import annotations

import math
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "exports"
EXPORTS.mkdir(exist_ok=True)

WIDTH = 720
HEIGHT = 1280
FPS = 24
DURATION_SECONDS = 60
TOTAL_FRAMES = FPS * DURATION_SECONDS


SCENES = [
    {
        "start": 0,
        "end": 5,
        "title": "一个万能 prompt？",
        "subtitle": "先停一下",
        "caption": "如果你想让一个 prompt 自动剪完整条视频，我先劝你停一下。",
        "accent": "orange",
        "items": ["VIDEO PRODUCTION LINE"],
    },
    {
        "start": 5,
        "end": 10,
        "title": "视频创作不是一道题",
        "subtitle": "它是一条生产线",
        "caption": "因为视频创作不是一道题，它是一条生产线。",
        "accent": "blue",
        "items": ["规划", "脚本", "素材", "装配", "导出"],
    },
    {
        "start": 10,
        "end": 16,
        "title": "一个 prompt 同时做所有事",
        "subtitle": "很快就会互相打架",
        "caption": "一个 prompt 同时写脚本、找素材、配音乐、做动效、写代码，很快就会互相打架。",
        "accent": "orange",
        "items": ["脚本", "素材", "音乐", "动效", "代码"],
    },
    {
        "start": 16,
        "end": 22,
        "title": "最常见的翻车点",
        "subtitle": "问题不是一个，而是一串",
        "caption": "最常见的问题是：素材没来源，时间线错位，音乐盖住人声，代码还到处硬编码。",
        "accent": "orange",
        "items": ["素材没来源", "时间线错位", "音乐盖人声", "代码硬编码"],
    },
    {
        "start": 22,
        "end": 29,
        "title": "更稳的方法",
        "subtitle": "拆成职责清晰的 Agent",
        "caption": "更稳的方式，是把它拆成多个 Agent：规划、口播、素材、对齐、动效、音频、Remotion、QA 和发布。",
        "accent": "blue",
        "items": ["规划", "口播", "素材", "对齐", "动效", "音频", "Remotion", "QA", "发布", "复盘"],
    },
    {
        "start": 29,
        "end": 36,
        "title": "每层只交付一个文件",
        "subtitle": "下一层接着用",
        "caption": "每一层只做自己的事，并且交付一个文件给下一层。",
        "accent": "green",
        "items": ["creative-brief.md", "script.md", "asset-list.md", "timeline.md"],
    },
    {
        "start": 36,
        "end": 43,
        "title": "职责边界要清楚",
        "subtitle": "找素材，不等于剪时间线",
        "caption": "比如素材层只负责找和验证素材，不负责最终剪辑；时间线层只负责怎么拼，不负责下载。",
        "accent": "blue",
        "items": ["Asset Gathering", "Asset Usage Planner"],
    },
    {
        "start": 43,
        "end": 50,
        "title": "到 Remotion 才开始装配",
        "subtitle": "Composition / Scene / Sequence",
        "caption": "到 Remotion 阶段，Agent 才把脚本、素材、字幕、音频和动效装配成 Composition、Scene 和 Sequence。",
        "accent": "blue",
        "items": ["Composition", "Scene", "Sequence", "CaptionLayer", "AudioLayer"],
    },
    {
        "start": 50,
        "end": 56,
        "title": "最后不是结束",
        "subtitle": "QA 和 Prompt Lab 会复盘",
        "caption": "最后 QA 找问题，Prompt Lab 复盘，把这次经验变成下一次的流程。",
        "accent": "green",
        "items": ["QA", "Prompt Lab", "下一次更稳"],
    },
    {
        "start": 56,
        "end": 60,
        "title": "别追求万能 prompt",
        "subtitle": "追求一条能反复成功的视频生产线",
        "caption": "所以，别追求万能 prompt。追求一条能反复成功的视频生产线。",
        "accent": "orange",
        "items": ["AI-video-auto-editing"],
    },
]


COLORS = {
    "ink": (23, 32, 51),
    "muted": (91, 101, 120),
    "line": (217, 226, 242),
    "soft": (245, 248, 252),
    "white": (255, 255, 255),
    "blue": (21, 91, 213),
    "orange": (255, 106, 0),
    "green": (31, 138, 91),
    "dark": (23, 32, 51),
}


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


FONT_H1 = font(54, True)
FONT_H1_SMALL = font(46, True)
FONT_H2 = font(30, True)
FONT_BODY = font(25, True)
FONT_SMALL = font(18, True)
FONT_MONO = font(22, True)


def ease_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1 - pow(1 - t, 3)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


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


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font_obj: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    max_width: int,
    line_gap: int = 8,
) -> int:
    x, y = xy
    for line in wrap_text(draw, text, font_obj, max_width):
        draw.text((x, y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font_obj)
        y += bbox[3] - bbox[1] + line_gap
    return y


def rounded(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def current_scene(second: float):
    for scene in SCENES:
        if scene["start"] <= second < scene["end"]:
            return scene
    return SCENES[-1]


def draw_background(draw: ImageDraw.ImageDraw, scene: dict):
    accent = COLORS[scene["accent"]]
    base = (247, 251, 255)
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        warm = (255, 247, 239) if scene["accent"] == "orange" else (238, 244, 255)
        color = tuple(int(lerp(base[i], warm[i], ratio * 0.55)) for i in range(3))
        draw.line([(0, y), (WIDTH, y)], fill=color)
    draw.ellipse((WIDTH - 210, -170, WIDTH + 180, 220), fill=(*accent, 34))
    draw.ellipse((-150, HEIGHT - 420, 150, HEIGHT - 120), fill=(21, 91, 213, 18))


def draw_header(draw: ImageDraw.ImageDraw, scene: dict, local_frame: int):
    accent = COLORS[scene["accent"]]
    t = ease_out(local_frame / 18)
    y_offset = int(lerp(34, 0, t))
    draw.text((52, 62 + y_offset), f"{SCENES.index(scene) + 1:02d} / {len(SCENES):02d}", font=FONT_SMALL, fill=accent)
    h1 = FONT_H1_SMALL if len(scene["title"]) > 12 else FONT_H1
    draw_text_block(draw, (52, 122 + y_offset), scene["title"], h1, COLORS["ink"], WIDTH - 104, 10)
    draw_text_block(draw, (52, 265 + y_offset), scene["subtitle"], FONT_H2, COLORS["muted"], WIDTH - 104, 6)


def draw_caption(draw: ImageDraw.ImageDraw, scene: dict):
    box = (52, HEIGHT - 190, WIDTH - 52, HEIGHT - 62)
    rounded(draw, box, 22, (23, 32, 51), None)
    draw_text_block(draw, (78, HEIGHT - 164), scene["caption"], FONT_BODY, COLORS["white"], WIDTH - 156, 6)


def draw_progress(draw: ImageDraw.ImageDraw, frame: int):
    x1, y1, x2, y2 = 52, 34, WIDTH - 52, 44
    rounded(draw, (x1, y1, x2, y2), 8, COLORS["line"])
    progress = frame / max(1, TOTAL_FRAMES - 1)
    rounded(draw, (x1, y1, int(lerp(x1, x2, progress)), y2), 8, COLORS["blue"])


def draw_visual(draw: ImageDraw.ImageDraw, scene: dict, local_frame: int):
    accent = COLORS[scene["accent"]]
    kind = SCENES.index(scene)
    items = scene["items"]

    if kind in (0, 1, 9):
        box = (52, 650, WIDTH - 52, 860)
        rounded(draw, box, 24, COLORS["white"], COLORS["line"], 3)
        label = items[0]
        text_font = FONT_H2 if len(label) < 20 else FONT_MONO
        bbox = draw.textbbox((0, 0), label, font=text_font)
        draw.text(((WIDTH - (bbox[2] - bbox[0])) // 2, 730), label, font=text_font, fill=accent)
        return

    if kind == 2:
        for i, item in enumerate(items):
            t = ease_out((local_frame - i * 5) / 16)
            y = int(lerp(780, 580 + i * 54, t))
            x = 82 + i * 22
            rounded(draw, (x, y, x + 500, y + 58), 16, COLORS["white"], accent, 3)
            draw.text((x + 28, y + 12), item, font=FONT_MONO, fill=COLORS["ink"])
        return

    if kind == 3:
        positions = [(52, 560), (370, 560), (52, 720), (370, 720)]
        for i, item in enumerate(items):
            t = ease_out((local_frame - i * 7) / 12)
            x, y = positions[i]
            pad = int(lerp(20, 0, t))
            rounded(draw, (x, y + pad, x + 298, y + 126 + pad), 18, COLORS["white"], COLORS["line"], 3)
            draw_text_block(draw, (x + 24, y + 38 + pad), item, FONT_MONO, accent if i == 0 else COLORS["ink"], 250, 4)
        return

    if kind == 4:
        for i, item in enumerate(items):
            t = ease_out((local_frame - i * 3) / 10)
            x = int(lerp(100, 52, t))
            y = 500 + i * 50
            rounded(draw, (x, y, WIDTH - 52, y + 40), 12, COLORS["white"], COLORS["line"], 2)
            draw.text((x + 18, y + 7), f"{i + 1}. {item}", font=FONT_SMALL, fill=COLORS["ink"])
        return

    if kind == 5:
        for i, item in enumerate(items):
            y = 560 + i * 82
            rounded(draw, (64, y, WIDTH - 64, y + 56), 14, COLORS["white"], COLORS["line"], 2)
            draw.rectangle((64, y, 78, y + 56), fill=accent)
            draw.text((94, y + 13), item, font=FONT_MONO, fill=COLORS["ink"])
        return

    if kind == 6:
        labels = [("Asset Gathering", "找 / 生成 / 验证 / 来源"), ("Asset Usage", "分配 / 对齐 / 去重 / 时间线")]
        for i, (title, body) in enumerate(labels):
            x = 52 + i * 320
            rounded(draw, (x, 610, x + 296, 820), 22, COLORS["white"], accent if i == 0 else COLORS["line"], 3)
            draw_text_block(draw, (x + 22, 645), title, FONT_SMALL, accent if i == 0 else COLORS["ink"], 250, 4)
            draw_text_block(draw, (x + 22, 715), body, FONT_SMALL, COLORS["muted"], 250, 4)
        return

    if kind == 7:
        for i, item in enumerate(items):
            x = 80 + i * 28
            y = 540 + i * 66
            rounded(draw, (x, y, WIDTH - 80 - i * 28, y + 54), 12, accent if i == 0 else COLORS["white"], COLORS["line"], 2)
            fill = COLORS["white"] if i == 0 else COLORS["ink"]
            draw.text((x + 24, y + 12), item, font=FONT_MONO, fill=fill)
        return

    if kind == 8:
        labels = [("QA", 80, 570), ("Prompt Lab", 250, 720), ("下一次更稳", 430, 570)]
        for item, x, y in labels:
            rounded(draw, (x, y, x + 220, y + 96), 20, accent if item == "Prompt Lab" else COLORS["white"], COLORS["line"], 3)
            fill = COLORS["white"] if item == "Prompt Lab" else COLORS["ink"]
            draw_text_block(draw, (x + 24, y + 30), item, FONT_SMALL, fill, 180, 4)


def render_frame(frame: int) -> np.ndarray:
    second = frame / FPS
    scene = current_scene(second)
    local_frame = frame - int(scene["start"] * FPS)
    image = Image.new("RGB", (WIDTH, HEIGHT), (247, 251, 255))
    draw = ImageDraw.Draw(image, "RGBA")

    draw_background(draw, scene)
    draw_progress(draw, frame)
    draw_header(draw, scene, local_frame)
    draw_visual(draw, scene, local_frame)
    draw_caption(draw, scene)
    return np.asarray(image)


def main() -> None:
    output = EXPORTS / "why-not-one-prompt-demo.mp4"
    writer = imageio.get_writer(
        output,
        fps=FPS,
        codec="libx264",
        quality=8,
        macro_block_size=16,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart"],
    )
    try:
        for frame in range(TOTAL_FRAMES):
            writer.append_data(render_frame(frame))
            if frame % FPS == 0:
                print(f"rendered {frame // FPS:02d}s / {DURATION_SECONDS}s")
    finally:
        writer.close()

    print(f"wrote {output}")


if __name__ == "__main__":
    main()
