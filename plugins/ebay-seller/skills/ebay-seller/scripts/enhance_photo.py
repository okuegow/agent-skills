"""Honest photo enhancement for eBay listings: orient, white-balance, autocontrast,
center on a square white canvas. Optional background removal via rembg if installed.
Never removes defects — only light, background, and framing are touched."""
from __future__ import annotations

import re as _re
from pathlib import Path

from PIL import Image, ImageOps, ImageStat

TARGET = 1600


def _white_balance(img: Image.Image) -> Image.Image:
    """Simple gray-world white balance on an RGB image."""
    mean = ImageStat.Stat(img).mean[:3]
    avg = sum(mean) / 3
    scales = [avg / m if m else 1.0 for m in mean]
    bands = [
        b.point(lambda v, s=s: min(255, int(v * s)))
        for b, s in zip(img.split()[:3], scales)
    ]
    return Image.merge("RGB", bands)


def _remove_background(img: Image.Image):
    """Return an RGBA image with background removed, or None if rembg is unavailable or fails at runtime."""
    try:
        from rembg import remove
        return remove(img)
    except Exception:
        return None  # rembg missing OR installed-but-broken -> keep original background


def _square_on_white(img: Image.Image, size: int = TARGET) -> Image.Image:
    """Center the image (RGB/RGBA) on a square white canvas of `size`; only shrinks, never upscales."""
    if img.mode == "RGBA":
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img)
    img = img.convert("RGB")
    # thumbnail() only shrinks — small sources stay small and get padded, never upscaled/blurred
    img.thumbnail((size, size), Image.LANCZOS)
    canvas = Image.new("RGB", (size, size), (255, 255, 255))
    canvas.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
    return canvas


def enhance(in_path, out_path, use_rembg: bool = True) -> dict:
    """Enhance a product photo and write JPEG. Returns {'output', 'applied'[]}."""
    applied = []
    img = ImageOps.exif_transpose(Image.open(in_path)).convert("RGB")
    applied.append("auto-orient")
    img = _white_balance(img)
    applied.append("white-balance")
    img = ImageOps.autocontrast(img, cutoff=1)
    applied.append("autocontrast")

    cut = _remove_background(img) if use_rembg else None
    if cut is not None:
        img = cut
        applied.append("background-removed")
    else:
        applied.append("background-kept")

    out = _square_on_white(img)
    applied.append(f"square-{TARGET}")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, "JPEG", quality=90)
    return {"output": str(out_path), "applied": applied}


def enhance_all(photos_dir, use_rembg: bool = True) -> list:
    """Enhance every original-N.jpg in photos_dir to enhanced-N.jpg.
    Returns a list of {'original', 'enhanced', 'applied'} in numeric order."""
    photos_dir = Path(photos_dir)
    originals = []
    for p in photos_dir.glob("original-*.jpg"):
        m = _re.search(r"original-(\d+)\.jpg$", p.name)
        if m:
            originals.append((int(m.group(1)), p))
    results = []
    for n, src in sorted(originals):
        out_name = f"enhanced-{n}.jpg"
        res = enhance(src, photos_dir / out_name, use_rembg=use_rembg)
        results.append({"original": src.name, "enhanced": out_name, "applied": res["applied"]})
    return results


if __name__ == "__main__":
    import sys

    print(enhance(sys.argv[1], sys.argv[2]))
