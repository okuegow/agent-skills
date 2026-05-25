from pathlib import Path
from scripts import state


def test_save_then_load_roundtrip(tmp_path):
    item = tmp_path / "item1"
    data = {"phase": "neu", "artikel": {"bezeichnung": "Nikon AF-S 50mm"}}
    state.save_state(item, data)
    assert state.load_state(item) == data


def test_save_is_atomic_no_tmp_left(tmp_path):
    item = tmp_path / "item2"
    state.save_state(item, {"phase": "neu"})
    leftovers = list(item.glob("*.tmp"))
    assert leftovers == []
    assert (item / "state.json").exists()


def test_already_ran_today_true_when_dates_match():
    assert state.already_ran_today({"letzter_lauf": "2026-05-25"}, "2026-05-25") is True


def test_already_ran_today_false_when_missing_or_different():
    assert state.already_ran_today({}, "2026-05-25") is False
    assert state.already_ran_today({"letzter_lauf": "2026-05-24"}, "2026-05-25") is False


def test_mark_ran_sets_date():
    s = state.mark_ran({"phase": "live"}, "2026-05-25")
    assert s["letzter_lauf"] == "2026-05-25"


def test_slugify_normalizes():
    assert state.slugify("Nikon AF-S 50mm f/1.8") == "nikon-af-s-50mm-f-1-8"
    assert state.slugify("  Leder Sessel!  ") == "leder-sessel"


def test_new_item_dir_creates_named_folder(tmp_path):
    d = state.new_item_dir(tmp_path, "2026-05-25", "Leder Sessel")
    assert d.name == "2026-05-25-leder-sessel"
    assert d.is_dir()


def test_find_similar_items_matches_close_name(tmp_path):
    items = tmp_path / "items"
    d = state.new_item_dir(items, "2026-05-20", "Nikon AF-S 50mm")
    state.save_state(d, {"artikel": {"bezeichnung": "Nikon AF-S 50mm"}})
    hits = state.find_similar_items(items, "Nikon AF-S 50 mm")
    assert d.name in hits


def test_find_similar_items_ignores_unrelated(tmp_path):
    items = tmp_path / "items"
    d = state.new_item_dir(items, "2026-05-20", "Leder Sessel")
    state.save_state(d, {"artikel": {"bezeichnung": "Leder Sessel"}})
    assert state.find_similar_items(items, "Nikon Objektiv") == []


def test_find_similar_items_empty_when_no_root(tmp_path):
    assert state.find_similar_items(tmp_path / "nope", "irgendwas") == []


def test_slugify_transliterates_umlauts():
    assert state.slugify("Größe Längsträger") == "groesse-laengstraeger"


def test_mark_ran_does_not_mutate_input():
    original = {"phase": "live"}
    state.mark_ran(original, "2026-05-25")
    assert "letzter_lauf" not in original
