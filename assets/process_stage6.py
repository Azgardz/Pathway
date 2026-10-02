from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ASSETS = Path(__file__).resolve().parent
GEN = Path(r"C:\Users\HYPE\.codex\generated_images\01a0f56f-b997-77c3-a613-04d1941712ac")
SOURCES = {
    "D1-daun-jati.png": GEN / "exec-9d92c2c1-0fdd-4568-ab9a-749fe6ab5982.png",
    "D2-pucuk-merah.png": GEN / "exec-cf739e5c-189f-427b-be13-ba0ce60d0fd0.png",
    "D3-ranting-pinus.png": GEN / "exec-4bd7f16b-3b99-4a2c-8c9c-d05f37f822cc.png",
    "D4-edelweis.png": GEN / "exec-fba4d4de-769b-4181-b19c-2111440bb95c.png",
    "D5-daun-kering-kecil.png": GEN / "exec-019cb858-a084-4fa9-8d01-e24463f44821.png",
    "B1-daun-samping-kiri.png": GEN / "exec-ef0bc879-8a84-4969-87fe-8ae7e00e7aeb.png",
    "B2-daun-samping-kanan.png": GEN / "exec-9e481308-7e4b-4236-941e-03bb635cf0ed.png",
    "J1-jurnal-sampul.png": GEN / "exec-d388a2af-b7bf-4f0d-9135-1ac69258d435.png",
    "J2-jurnal-sampul-dalam.png": GEN / "exec-386baa19-c38c-4a61-93f9-2740f14567e0.png",
    "J3-jurnal-halaman.png": GEN / "exec-349ca100-11d9-461f-b18b-78482b5be580.png",
    "J4-pensil.png": GEN / "exec-ca617047-3e54-43f8-be5e-61d0998cf938.png",
    "J5-edelweis-kering.png": GEN / "exec-92fcee38-6a67-468a-af15-0ce85cd03443.png",
    "G1-bingkai-foto.png": GEN / "exec-01786c7b-fef2-4306-8dda-2820d5fb2e32.png",
    "G2-bingkai-kayu.png": GEN / "exec-f97ad2ed-e98e-496c-b801-8b7d596cd9cf.png",
    "X1-kertas.png": GEN / "exec-300204c6-6eb5-4600-85b0-aaf9a21f9d94.png",
}


def resize_rgba(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    rgba = image.convert("RGBA")
    r, g, b, a = rgba.split()
    ar = a.resize(size, Image.Resampling.LANCZOS)
    aa = np.asarray(ar, dtype=np.float32)
    channels = []
    for channel in (r, g, b):
        premul = ImageChops.multiply(channel, a).resize(size, Image.Resampling.LANCZOS)
        values = np.asarray(premul, dtype=np.float32)
        restored = np.where(aa > 0, np.minimum(255, values * 255 / np.maximum(aa, 1)), 0)
        channels.append(Image.fromarray(restored.astype(np.uint8), "L"))
    return Image.merge("RGBA", (*channels, ar))


def clean_alpha(image: Image.Image) -> tuple[Image.Image, int, int]:
    data = np.array(image.convert("RGBA"), dtype=np.uint8)
    a = data[:, :, 3]
    edge = np.asarray(Image.fromarray(((a < 40) * 255).astype(np.uint8), "L").filter(ImageFilter.MaxFilter(7))) > 0
    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    fringe_color = (
        ((r > 235) & (g < 85) & (b < 90))
        | ((b > 210) & (r < 90) & (g < 125))
        | ((g > 230) & (r < 105) & (b < 105))
        | ((r > 235) & (g > 230) & (b < 55))
        | ((r > 215) & (b > 190) & (g < 75))
    )
    fringe = edge & fringe_color
    removed = int(np.count_nonzero(fringe & (a > 0)))
    data[fringe | (a < 8)] = (0, 0, 0, 0)
    a = data[:, :, 3]
    rounded = int(np.count_nonzero((a >= 245) & (a < 255)))
    a[a >= 245] = 255
    data[:, :, 3] = a
    return Image.fromarray(data, "RGBA"), removed, rounded


def crop_visible(image: Image.Image, threshold: int = 12) -> Image.Image:
    a = np.asarray(image.getchannel("A"))
    ys, xs = np.where(a > threshold)
    return image.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1))


def centered_asset(source: Path, canvas_size: tuple[int, int], max_size: tuple[int, int]) -> Image.Image:
    image, _, _ = clean_alpha(Image.open(source))
    cropped = crop_visible(image)
    scale = min(max_size[0] / cropped.width, max_size[1] / cropped.height)
    scaled = resize_rgba(cropped, (round(cropped.width * scale), round(cropped.height * scale)))
    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    canvas.alpha_composite(scaled, ((canvas_size[0] - scaled.width) // 2, (canvas_size[1] - scaled.height) // 2))
    return clean_alpha(canvas)[0]


def chroma_key(source: Path, target: tuple[int, int]) -> Image.Image:
    rgb = np.array(Image.open(source).convert("RGB"), dtype=np.float32)
    dist = np.sqrt(rgb[:, :, 0] ** 2 + (255 - rgb[:, :, 1]) ** 2 + rgb[:, :, 2] ** 2)
    alpha = np.clip((dist - 24) / 70 * 255, 0, 255).astype(np.uint8)
    rgba = np.dstack((rgb.astype(np.uint8), alpha))
    # Remove green spill only from semitransparent boundary pixels.
    semi = (alpha > 0) & (alpha < 250)
    max_rb = np.maximum(rgba[:, :, 0], rgba[:, :, 2])
    rgba[:, :, 1][semi] = np.minimum(rgba[:, :, 1][semi], max_rb[semi])
    image = Image.fromarray(rgba, "RGBA")
    image = resize_rgba(image, target)
    return clean_alpha(image)[0]


def exact_registered_journal(source: Path) -> Image.Image:
    image, _, _ = clean_alpha(Image.open(source))
    cropped = crop_visible(image)
    # Identical 1000x1400 outer registration for J1, J2, and J3.
    book = resize_rgba(cropped, (1000, 1400))
    canvas = Image.new("RGBA", (1200, 1600), (0, 0, 0, 0))
    canvas.alpha_composite(book, (100, 100))
    return clean_alpha(canvas)[0]


def fill_green_window(image: Image.Image) -> Image.Image:
    data = np.array(image.convert("RGBA"), dtype=np.uint8)
    r, g, b, a = [data[:, :, i] for i in range(4)]
    green = (g > 115) & (g > r * 1.18) & (g > b * 1.18)
    for y in range(data.shape[0]):
        xs = np.where(green[y])[0]
        if xs.size >= 18:
            left, right = int(xs.min()), int(xs.max())
            data[y, left : right + 1] = (0, 255, 0, 255)
    return Image.fromarray(data, "RGBA")


def gallery_frame(source: Path) -> Image.Image:
    image, _, _ = clean_alpha(Image.open(source))
    image = fill_green_window(image)
    cropped = crop_visible(image)
    scale = min(1100 / cropped.width, 1300 / cropped.height)
    frame = resize_rgba(cropped, (round(cropped.width * scale), round(cropped.height * scale)))
    frame = fill_green_window(frame)
    canvas = Image.new("RGBA", (1200, 1400), (0, 0, 0, 0))
    canvas.alpha_composite(frame, ((1200 - frame.width) // 2, (1400 - frame.height) // 2))
    return clean_alpha(canvas)[0]


outputs = {}
specs = {
    "D1-daun-jati.png": (900, 900),
    "D2-pucuk-merah.png": (850, 850),
    "D3-ranting-pinus.png": (900, 900),
    "D4-edelweis.png": (900, 900),
    "D5-daun-kering-kecil.png": (560, 560),
    "J5-edelweis-kering.png": (820, 820),
}
for name, max_size in specs.items():
    outputs[name] = centered_asset(SOURCES[name], (1024, 1024), max_size)

outputs["J4-pensil.png"] = centered_asset(SOURCES["J4-pensil.png"], (1024, 512), (900, 350))
outputs["B1-daun-samping-kiri.png"] = chroma_key(SOURCES["B1-daun-samping-kiri.png"], (1024, 1536))
outputs["B2-daun-samping-kanan.png"] = chroma_key(SOURCES["B2-daun-samping-kanan.png"], (1024, 1536))
for name in ("J1-jurnal-sampul.png", "J2-jurnal-sampul-dalam.png", "J3-jurnal-halaman.png"):
    outputs[name] = exact_registered_journal(SOURCES[name])
outputs["G1-bingkai-foto.png"] = gallery_frame(SOURCES["G1-bingkai-foto.png"])
outputs["G2-bingkai-kayu.png"] = gallery_frame(SOURCES["G2-bingkai-kayu.png"])

# Seamless X1 through a mirrored 2x2 tile; alpha stays fully opaque.
paper = Image.open(SOURCES["X1-kertas.png"]).convert("RGB").resize((512, 512), Image.Resampling.LANCZOS)
x1 = Image.new("RGB", (1024, 1024))
x1.paste(paper, (0, 0))
x1.paste(paper.transpose(Image.Transpose.FLIP_LEFT_RIGHT), (512, 0))
x1.paste(paper.transpose(Image.Transpose.FLIP_TOP_BOTTOM), (0, 512))
x1.paste(paper.transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.FLIP_TOP_BOTTOM), (512, 512))
outputs["X1-kertas.png"] = x1.convert("RGBA")

for name, image in outputs.items():
    image.save(ASSETS / name, optimize=True)
    alpha = np.asarray(image.getchannel("A"))
    print(f"{name}|{image.width}x{image.height}|alpha={alpha.min()}-{alpha.max()}|transparent={np.count_nonzero(alpha == 0)}")


def checker(size: tuple[int, int], cell: int = 22) -> Image.Image:
    out = Image.new("RGB", size, (226, 226, 233))
    d = ImageDraw.Draw(out)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                d.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(190, 190, 200))
    return out.convert("RGBA")


sheet = Image.new("RGB", (2400, 2750), (24, 23, 41))
sd = ImageDraw.Draw(sheet)
title = ImageFont.truetype("arial.ttf", 42)
label = ImageFont.truetype("arial.ttf", 21)
small = ImageFont.truetype("arial.ttf", 19)
sd.text((48, 28), "PATHWAY BASECAMP — TAHAP 6", font=title, fill="white")
sd.text((50, 84), "Daun • jurnal • bingkai galeri • tekstur kertas", font=small, fill=(205, 205, 222))
order = [
    "D1-daun-jati.png", "D2-pucuk-merah.png", "D3-ranting-pinus.png", "D4-edelweis.png",
    "D5-daun-kering-kecil.png", "B1-daun-samping-kiri.png", "B2-daun-samping-kanan.png", "J1-jurnal-sampul.png",
    "J2-jurnal-sampul-dalam.png", "J3-jurnal-halaman.png", "J4-pensil.png", "J5-edelweis-kering.png",
    "G1-bingkai-foto.png", "G2-bingkai-kayu.png", "X1-kertas.png",
]
tile_w, tile_h = 550, 580
for idx, name in enumerate(order):
    col, row = idx % 4, idx // 4
    x, y = 48 + col * 585, 135 + row * 650
    sd.text((x, y), name, font=label, fill="white")
    tile = checker((tile_w, tile_h))
    thumb = outputs[name].copy()
    thumb.thumbnail((500, 525), Image.Resampling.LANCZOS)
    tile.alpha_composite(thumb, ((tile_w - thumb.width) // 2, (tile_h - thumb.height) // 2))
    sheet.paste(tile.convert("RGB"), (x, y + 35))
sheet.save(ASSETS / "contact-sheet-tahap-6.png", optimize=True)
