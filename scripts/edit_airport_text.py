from __future__ import annotations

import subprocess
from pathlib import Path

import imageio.v2 as imageio
import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat


INPUT = Path(r"E:\桌面\张府皇家航空宣传片2.mp4")
OUTPUT = Path(r"E:\桌面\张府皇家航空宣传片2_已修改.mp4")
TEMP_VIDEO = Path(r"E:\自学\projects\AI视频自动剪辑\exports\airport_text_edit_no_audio.mp4")


def font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path(r"C:\Windows\Fonts\msyhbd.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
        Path(r"C:\Windows\Fonts\msyh.ttc"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


FONT_RUNWAY = font(48)
FONT_JETBRIDGE_TOP = font(46)
RED = (145, 28, 50)


def blur_patch(image: Image.Image, box: tuple[int, int, int, int], radius: int = 8) -> None:
    x1, y1, x2, y2 = box
    crop = image.crop((x1, y1, x2, y2)).filter(ImageFilter.GaussianBlur(radius))
    image.paste(crop, (x1, y1))


def sample_patch(
    image: Image.Image,
    box: tuple[int, int, int, int],
    source_box: tuple[int, int, int, int],
    radius: int = 4,
) -> None:
    x1, y1, x2, y2 = box
    crop = image.crop(source_box).resize((x2 - x1, y2 - y1)).filter(ImageFilter.GaussianBlur(radius))
    image.paste(crop, (x1, y1))


def average_patch(image: Image.Image, box: tuple[int, int, int, int], source_box: tuple[int, int, int, int]) -> None:
    stat = ImageStat.Stat(image.crop(source_box))
    color = tuple(int(v) for v in stat.mean[:3])
    ImageDraw.Draw(image).rectangle(box, fill=color)


def draw_masked_text(
    image: Image.Image,
    xy: tuple[int, int],
    text: str,
    font_obj: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
) -> None:
    # Avoid drawing replacement text over the dark blue aircraft tail.
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text(xy, text, font=font_obj, fill=(*fill, 255))
    base = image.convert("RGBA")
    base_pixels = base.load()
    layer_pixels = layer.load()
    for y in range(max(0, xy[1] - 4), min(image.height, xy[1] + font_obj.size + 22)):
        for x in range(max(0, xy[0] - 4), min(image.width, xy[0] + font_obj.size * len(text) + 32)):
            r, g, b, _ = base_pixels[x, y]
            if layer_pixels[x, y][3] and not (b > r + 25 and b > g + 10 and r < 120):
                base_pixels[x, y] = layer_pixels[x, y]
    image.paste(base.convert("RGB"))


def edit_runway_terminal(image: Image.Image) -> None:
    # Scene around 8s: remove the synthetic rooftop Chinese text and write "長沙"
    # back at terminal-roof scale.
    sample_patch(image, (60, 100, 525, 205), (60, 45, 525, 150), radius=8)
    draw_masked_text(image, (270, 118), "長沙", FONT_RUNWAY, RED)


def edit_jetbridge(image: Image.Image) -> None:
    # Scene around 9s: remove the yellow branding text printed on the side of the jet bridge.
    blur_patch(image, (420, 335, 600, 385), radius=18)


def main() -> None:
    reader = imageio.get_reader(INPUT)
    meta = reader.get_meta_data()
    fps = float(meta["fps"])

    writer = imageio.get_writer(
        TEMP_VIDEO,
        fps=fps,
        codec="libx264",
        quality=9,
        macro_block_size=16,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart"],
    )

    count = 0
    try:
        for frame in reader:
            t = count / fps
            image = Image.fromarray(frame).convert("RGB")

            if 7.75 <= t < 8.85:
                edit_runway_terminal(image)
            if t >= 8.85:
                edit_jetbridge(image)

            writer.append_data(np.asarray(image))
            count += 1
    finally:
        writer.close()
        reader.close()

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    command = [
        ffmpeg,
        "-y",
        "-i",
        str(TEMP_VIDEO),
        "-i",
        str(INPUT),
        "-map",
        "0:v:0",
        "-map",
        "1:a?",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        str(OUTPUT),
    ]
    subprocess.run(command, check=True)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
