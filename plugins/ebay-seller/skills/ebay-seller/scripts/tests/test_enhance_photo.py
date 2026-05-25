from pathlib import Path
from PIL import Image
from scripts import enhance_photo


def _make_photo(path, size=(800, 600), color=(120, 90, 60)):
    Image.new("RGB", size, color).save(path, "JPEG")


def test_enhance_outputs_square_target_jpeg(tmp_path):
    src = tmp_path / "in.jpg"
    out = tmp_path / "enhanced.jpg"
    _make_photo(src)
    res = enhance_photo.enhance(src, out, use_rembg=False)
    assert out.exists()
    assert res["output"] == str(out)
    w, h = Image.open(out).size
    assert w == h == enhance_photo.TARGET


def test_enhance_without_rembg_keeps_background(tmp_path):
    src = tmp_path / "in.jpg"
    out = tmp_path / "enhanced.jpg"
    _make_photo(src)
    res = enhance_photo.enhance(src, out, use_rembg=False)
    assert "background-kept" in res["applied"]
    assert "white-balance" in res["applied"]


def test_enhance_all_processes_every_photo(tmp_path):
    photos = tmp_path / "photos"
    photos.mkdir()
    for i in (1, 2, 3):
        Image.new("RGB", (640, 480), (100 + i * 10, 90, 70)).save(
            photos / f"original-{i}.jpg", "JPEG"
        )
    results = enhance_photo.enhance_all(photos, use_rembg=False)
    assert [r["enhanced"] for r in results] == [
        "enhanced-1.jpg",
        "enhanced-2.jpg",
        "enhanced-3.jpg",
    ]
    for i in (1, 2, 3):
        out = photos / f"enhanced-{i}.jpg"
        assert out.exists() and Image.open(out).size == (enhance_photo.TARGET, enhance_photo.TARGET)


def test_enhance_all_empty_when_no_originals(tmp_path):
    photos = tmp_path / "photos"
    photos.mkdir()
    assert enhance_photo.enhance_all(photos, use_rembg=False) == []
