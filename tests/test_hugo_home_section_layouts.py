from pathlib import Path


def test_hugo_home_layout_exists():
    assert Path("examples/hugo-demo/layouts/_default/home.html").exists()


def test_hugo_section_list_layout_exists():
    assert Path("examples/hugo-demo/layouts/_default/list.html").exists()


def test_hugo_home_layout_defines_main_block():
    text = Path("examples/hugo-demo/layouts/_default/home.html").read_text(encoding="utf-8")

    assert '{{ define "main" }}' in text
    assert "{{ .Content }}" in text


def test_hugo_list_layout_defines_main_block():
    text = Path("examples/hugo-demo/layouts/_default/list.html").read_text(encoding="utf-8")

    assert '{{ define "main" }}' in text
    assert "{{ .Content }}" in text
