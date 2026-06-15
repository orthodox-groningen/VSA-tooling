from pathlib import Path


def test_inspect_hugo_svg_usage_script_exists():
    assert Path("scripts/inspect-hugo-svg-usage.py").exists()


def test_inspect_script_mentions_vsa_line_count():
    text = Path("scripts/inspect-hugo-svg-usage.py").read_text(encoding="utf-8")
    assert "vsa-line count" in text
    assert "HTML verwijzingen naar SVG" in text
    assert "CSS hints" in text


def test_hugo_public_svg_files_have_vsa_line_when_built():
    public_vsa = Path("examples/hugo-demo/public/vsa")
    if not public_vsa.exists():
        return

    svg_files = list(public_vsa.glob("*.svg"))
    if not svg_files:
        return

    assert any(
        'class="vsa-line"' in path.read_text(encoding="utf-8", errors="ignore")
        for path in svg_files
    )
