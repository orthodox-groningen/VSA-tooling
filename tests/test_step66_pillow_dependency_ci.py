from pathlib import Path

from docs_contracts import PARSER_STEPS, read_doc, read, assert_terms


def test_rendering_requirements_include_pillow():
    text = Path("requirements-rendering.txt").read_text(encoding="utf-8")

    assert "Pillow" in text


def test_install_rendering_deps_script_exists():
    assert Path("scripts/install-rendering-deps.cmd").exists()




def test_docs_mention_pillow_and_dejavu_ci():
    text = read_doc("rendering_fonts_guide") + read(
        PARSER_STEPS / "parser-stap-66-pillow-dependency-ci.md"
    )

    assert_terms(text, ("Pillow", "fonts-dejavu-core", "DejaVu Sans"))
