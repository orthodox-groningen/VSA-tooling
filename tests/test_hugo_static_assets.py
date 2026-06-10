from pathlib import Path


def test_preview_script_writes_svgs_to_hugo_static_dir():
    text = Path("scripts/build-preview.cmd").read_text(encoding="utf-8")

    assert "examples\\hugo-demo\\static\\vsa" in text
    assert "generated\\preview\\static\\vsa" not in text


def test_serve_script_writes_svgs_to_hugo_static_dir():
    text = Path("scripts/serve-hugo.cmd").read_text(encoding="utf-8")

    assert "examples\\hugo-demo\\static\\vsa" in text
    assert "generated\\hugo\\static\\vsa" not in text


def test_production_script_writes_svgs_to_hugo_static_dir():
    text = Path("scripts/build-production.cmd").read_text(encoding="utf-8")

    assert "examples\\hugo-demo\\static\\vsa" in text
    assert "generated\\production\\static\\vsa" not in text
