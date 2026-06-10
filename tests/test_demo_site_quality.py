from pathlib import Path

from vsa.validation_runner import validate_path


def test_hugo_single_template_does_not_add_duplicate_title():
    text = Path("examples/hugo-demo/layouts/_default/single.html").read_text(encoding="utf-8")

    assert "<h1>{{ .Title }}</h1>" not in text
    assert "{{ .Content }}" in text


def test_hugo_list_template_does_not_add_duplicate_title():
    text = Path("examples/hugo-demo/layouts/_default/list.html").read_text(encoding="utf-8")

    assert "<h1>{{ .Title }}</h1>" not in text
    assert "{{ .Content }}" in text


def test_multiline_demo_uses_correct_closing_pitch_marker():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/multiline.md"
    ).read_text(encoding="utf-8")

    assert r"[\\:]" in text
    assert "Zijn werken. [:]" not in text


def test_minimal_multiline_demo_uses_correct_closing_pitch_marker():
    text = Path("examples/minimal/100_multiline_demo.vsa").read_text(encoding="utf-8")

    assert r"[\\:]" in text
    assert "Zijn werken. [:]" not in text


def test_hugo_demo_content_validates():
    result = validate_path("examples/hugo-demo/content-source")

    assert result.ok, [message.message_nl for message in result.messages]
