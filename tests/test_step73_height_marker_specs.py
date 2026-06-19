from pathlib import Path

def test_height_marker_spec_exists():
    assert Path("docs/spec/vsa-height-markers.md").exists()

def test_height_marker_spec_allows_multiple_markers():
    text = Path("docs/spec/vsa-height-markers.md").read_text(encoding="utf-8")
    assert "mogen meerdere hoogte-markeringen voorkomen" in text
    assert "vóór de eerste hoogte-markering" in text
    assert "na de laatste hoogte-markering" in text

def test_height_marker_spec_says_first_marker_is_start_height():
    text = Path("docs/spec/vsa-height-markers.md").read_text(encoding="utf-8")
    assert "eerste hoogte-markering" in text
    assert "beginhoogte" in text

def test_height_marker_architecture_prefers_nodes():
    text = Path("docs/architecture/height-marker-model.md").read_text(encoding="utf-8")
    assert "positionele nodes" in text
    assert "Geen quick-and-dirty" in text
