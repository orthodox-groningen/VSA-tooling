from pathlib import Path


def test_step78_model_is_retired_by_step79():
    assert Path("docs/hugo-navigation-placeholders.md").exists()
    assert Path("scripts/update-nav-placeholders.py").exists()


def test_step78_whole_index_nav_model_is_not_documented_as_current():
    doc = Path("docs/hugo-navigation-placeholders.md").read_text(encoding="utf-8")

    assert "VSA-NAV:HOME" in doc
    assert "VSA-INDEX-NAV-START" in doc
    assert "Verouderd model" in doc
