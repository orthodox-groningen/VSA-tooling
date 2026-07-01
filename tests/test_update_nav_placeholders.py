import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _nav_module():
    path = ROOT / "scripts" / "update-nav-placeholders.py"
    spec = importlib.util.spec_from_file_location("update_nav_placeholders", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_page_nav_href_is_lowercase_for_hugo_permalink():
    nav = _nav_module()
    path = Path("USTAV-liturgie-met-diaken.md")
    assert nav.page_nav_href(path) == "ustav-liturgie-met-diaken/"


def test_pages_here_skips_draft_and_vsa_nav_exclude(tmp_path: Path):
    nav = _nav_module()
    section = tmp_path / "zondag"
    section.mkdir()
    (section / "_index.md").write_text(
        "---\ntitle: Zondag\n---\n\n<!-- VSA-NAV:PAGES-HERE -->\n",
        encoding="utf-8",
    )
    (section / "toon-1.md").write_text(
        "---\ntitle: Toon 1\ndraft: true\nvsa_nav_exclude: true\n---\n",
        encoding="utf-8",
    )
    (section / "published.md").write_text(
        "---\ntitle: Published\n---\n",
        encoding="utf-8",
    )

    items = nav.child_page_items_here(section)
    assert any("published/" in item for item in items)
    assert not any("toon-1/" in item for item in items)


def test_praktijk_index_nav_uses_lowercase_ustav_href(tmp_path: Path):
    nav = _nav_module()
    root = tmp_path / "content"
    praktijk = root / "praktijk"
    praktijk.mkdir(parents=True)
    (praktijk / "_index.md").write_text(
        "---\ntitle: Praktijk\n---\n\n<!-- VSA-NAV:PAGES-HERE -->\n",
        encoding="utf-8",
    )
    (praktijk / "USTAV-liturgie-met-diaken.md").write_text(
        '---\ntitle: "USTAV-liturgie-met-diaken"\n---\n',
        encoding="utf-8",
    )

    updated = nav.update_file_text(
        (praktijk / "_index.md").read_text(encoding="utf-8"),
        praktijk / "_index.md",
        root,
    )
    assert "ustav-liturgie-met-diaken/" in updated
    assert "USTAV-liturgie-met-diaken/" not in updated
