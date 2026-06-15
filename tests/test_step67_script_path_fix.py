from pathlib import Path


def test_update_spacing_script_adds_src_to_syspath():
    text = Path("scripts/update-spacing-diagnostics-metadata.py").read_text(encoding="utf-8")

    assert "sys.path.insert" in text
    assert 'ROOT / "src"' in text
    assert "from vsa.text_metrics import" in text
