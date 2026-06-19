from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update-nav-placeholders.py"
BUILD = ROOT / "scripts" / "build-hugo.cmd"


def load_module():
    spec = spec_from_file_location("update_nav_placeholders", SCRIPT)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_marker_only_update_preserves_frontmatter_headings_and_free_markdown(tmp_path):
    mod = load_module()
    root = tmp_path / "content"
    month = root / "praktijk" / "feesteigen" / "12-dec"
    month.mkdir(parents=True)

    page = month / "_index.md"
    page.write_text(
        """---
title: "December"
---

# Mijn eigen kop

| [Home](../../../) | [Omhoog](../) |

Eigen tekst vóór marker.

<!-- VSA-NAV:PAGES -->
<!-- VSA-NAV-GENERATED:PAGES-START -->
oud
<!-- VSA-NAV-GENERATED:PAGES-END -->

Eigen tekst na marker.
""",
        encoding="utf-8",
    )

    child = month / "12-06-nicolaas-van-myra.md"
    child.write_text('---\ntitle: "H. Nicolaas van Myra (6 December)"\n---\n', encoding="utf-8")

    updated = mod.update_file_text(page.read_text(encoding="utf-8"), page, root)

    assert 'title: "December"' in updated
    assert "# Mijn eigen kop" in updated
    assert "| [Home](../../../) | [Omhoog](../) |" in updated
    assert "Eigen tekst vóór marker." in updated
    assert "Eigen tekst na marker." in updated
    assert "oud" not in updated
    assert "- [H. Nicolaas van Myra (6 December)](12-06-nicolaas-van-myra/)" in updated


def test_marker_without_generated_block_gets_only_matching_block_inserted(tmp_path):
    mod = load_module()
    root = tmp_path / "content"
    directory = root / "voorbeeld"
    directory.mkdir(parents=True)
    page = directory / "_index.md"
    page.write_text("Voor\n<!-- VSA-NAV:CHILDREN -->\nNa\n", encoding="utf-8")

    updated = mod.update_file_text(page.read_text(encoding="utf-8"), page, root)

    assert "Voor\n<!-- VSA-NAV:CHILDREN -->\n<!-- VSA-NAV-GENERATED:CHILDREN-START -->" in updated
    assert "<!-- VSA-NAV-GENERATED:CHILDREN-END -->\nNa" in updated


def test_build_hugo_runs_nav_update_only_on_generated_content():
    text = BUILD.read_text(encoding="utf-8").replace("\r\n", "\n")

    assert 'scripts\\update-nav-placeholders.py generated\\hugo\\content' in text
    assert 'scripts\\update-spacing-diagnostics-metadata.py generated\\hugo\\content\\voorbeelden\\rendering\\spacing-diagnostiek.md' in text
    assert 'update-nav-placeholders.py examples\\hugo-demo\\content-source' not in text
