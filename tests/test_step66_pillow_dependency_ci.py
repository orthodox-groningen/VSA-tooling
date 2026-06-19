from pathlib import Path


def test_rendering_requirements_include_pillow():
    text = Path("requirements-rendering.txt").read_text(encoding="utf-8")

    assert "Pillow" in text


def test_install_rendering_deps_script_exists():
    assert Path("scripts/install-rendering-deps.cmd").exists()




def test_docs_mention_pillow_and_dejavu_ci():
    text = Path("docs/rendering-fonts.md").read_text(encoding="utf-8")

    assert "Pillow" in text
    assert "fonts-dejavu-core" in text
    assert "DejaVu Sans" in text
