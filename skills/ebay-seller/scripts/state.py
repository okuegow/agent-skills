"""State helpers for the eBay seller skill: atomic persistence, idempotency, dedupe."""
from __future__ import annotations

import json
import os
import re
import tempfile
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

STATE_FILE = "state.json"

_UMLAUT_MAP = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
                             "Ä": "ae", "Ö": "oe", "Ü": "ue"})


def load_state(item_dir) -> dict:
    with open(Path(item_dir) / STATE_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_state(item_dir, state: dict) -> None:
    """Atomically write state.json (temp file + os.replace) so a crash mid-write never corrupts it."""
    item_dir = Path(item_dir)
    item_dir.mkdir(parents=True, exist_ok=True)
    target = item_dir / STATE_FILE
    fd, tmp = tempfile.mkstemp(dir=item_dir, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def already_ran_today(state: dict, today_iso: str) -> bool:
    return state.get("letzter_lauf") == today_iso


def mark_ran(state: dict, today_iso: str) -> dict:
    return {**state, "letzter_lauf": today_iso}


def slugify(text: str) -> str:
    text = text.lower().strip().translate(_UMLAUT_MAP)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def new_item_dir(items_root, date_iso: str, bezeichnung: str) -> Path:
    slug = slugify(bezeichnung) or "unbekannt"
    d = Path(items_root) / f"{date_iso}-{slug}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def find_similar_items(items_root, bezeichnung: str, threshold: float = 0.6) -> list:
    """Return existing item dir names whose stored bezeichnung is similar (dedupe check)."""
    items_root = Path(items_root)
    if not items_root.exists():
        return []
    target = slugify(bezeichnung)
    hits = []
    for d in sorted(p for p in items_root.iterdir() if p.is_dir()):
        try:
            existing = load_state(d).get("artikel", {}).get("bezeichnung", "")
        except (FileNotFoundError, json.JSONDecodeError):
            continue
        if SequenceMatcher(None, target, slugify(existing)).ratio() >= threshold:
            hits.append(d.name)
    return hits
