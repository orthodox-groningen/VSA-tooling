from pathlib import Path


def test_rendering_requirements_include_pillow():
    text = Path("requirements-rendering.txt").read_text(encoding="utf-8")

    assert "Pillow" in text


def test_install_rendering_deps_script_exists():
    assert Path("scripts/install-rendering-deps.cmd").exists()


def test_apply_step66_script_mentions_github_fonts():
    text = Path("scripts/apply-step66-pillow-dependency-ci.py").read_text(encoding="utf-8")

    assert "fonts-dejavu-core" in text
    assert "requirements-rendering.txt" in text


def test_docs_mention_pillow_and_dejavu_ci():
    text = Path("docs/rendering-fonts.md").read_text(encoding="utf-8")

    assert "Pillow" in text
    assert "fonts-dejavu-core" in text
    assert "DejaVu Sans" in text
