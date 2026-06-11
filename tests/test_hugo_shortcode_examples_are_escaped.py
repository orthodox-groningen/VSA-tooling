from pathlib import Path
import re


def test_markdown_demo_escapes_shortcode_example():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/markdown.md"
    ).read_text(encoding="utf-8")

    assert "{{</* vsa" in text
    assert "*/>}}" in text


def test_markdown_demo_has_no_unescaped_vsa_shortcode_in_code_example():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/markdown.md"
    ).read_text(encoding="utf-8")

    unescaped = re.findall(r"\{\{<\s+vsa\b", text)

    assert unescaped == []


def test_demo_pages_do_not_contain_unescaped_vsa_shortcode_examples():
    for path in Path("examples/hugo-demo/content-source").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        unescaped = re.findall(r"\{\{<\s+vsa\b", text)

        assert unescaped == [], f"{path}: {unescaped}"
