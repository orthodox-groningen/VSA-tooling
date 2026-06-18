from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "hide-legacy-hugo-routes.py"


def load_module():
    spec = spec_from_file_location("hide_legacy_hugo_routes", SCRIPT)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_script_exists():
    assert SCRIPT.exists()


def test_legacy_source_detection():
    mod = load_module()
    content = mod.CONTENT

    assert mod.is_legacy_source(content / "zondag" / "toon-1.md")
    assert mod.is_legacy_source(content / "voorbeelden" / "praktijk" / "weekdagen" / "woensdag.md")
    assert mod.is_legacy_source(content / "praktijk" / "tropaar-toon-1.md")
    assert mod.is_legacy_source(content / "praktijk" / "kondak-toon-8.md")
    assert mod.is_legacy_source(content / "praktijk" / "zondag-toon-4.md")

    assert not mod.is_legacy_source(content / "praktijk" / "zondagen" / "tropaar-toon-1.md")
    assert not mod.is_legacy_source(content / "praktijk" / "weekdagen" / "woensdag.md")
    assert not mod.is_legacy_source(content / "voorbeelden" / "markdown.md")


def test_ensure_frontmatter_bool_adds_frontmatter():
    mod = load_module()

    text = "# Titel\n\nTekst\n"
    result = mod.ensure_frontmatter_bool(text, "draft", True)

    assert result.startswith("---\ndraft: true\n---")


def test_ensure_frontmatter_bool_updates_existing_key():
    mod = load_module()

    text = "---\ntitle: X\ndraft: false\n---\n\n# X\n"
    result = mod.ensure_frontmatter_bool(text, "draft", True)

    assert "draft: true" in result
    assert "draft: false" not in result


def test_ensure_frontmatter_bool_inserts_in_existing_frontmatter():
    mod = load_module()

    text = "---\ntitle: X\n---\n\n# X\n"
    result = mod.ensure_frontmatter_bool(text, "vsa_nav_exclude", True)

    assert "title: X" in result
    assert "vsa_nav_exclude: true" in result
