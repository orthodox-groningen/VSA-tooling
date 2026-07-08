from pathlib import Path


PAGES = [
    "examples/hugo-demo/content-source/_index.md",
    "examples/hugo-demo/content-source/voorbeelden/_index.md",
    "examples/hugo-demo/content-source/voorbeelden/basis.md",
    "examples/hugo-demo/content-source/voorbeelden/multiline.md",
    "examples/hugo-demo/content-source/voorbeelden/fouten.md",
    "examples/hugo-demo/content-source/voorbeelden/markdown.md",
    "examples/hugo-demo/content-source/voorbeelden/cli.md",
    "examples/hugo-demo/content-source/voorbeelden/rendering.md",
]


def test_demo_pages_exist():
    for page in PAGES:
        assert Path(page).exists()


def test_base_template_contains_navigation():
    text = Path(
        "examples/hugo-demo/layouts/_default/baseof.html"
    ).read_text(encoding="utf-8")

    assert "Voorbeelden" in text
    assert 'voorbeelden/" | relURL' in text
    assert 'voorbeelden/basis/' not in text
    assert 'voorbeelden/cli/' not in text
    assert "relURL" in text


def test_examples_index_contains_section_navigation():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/_index.md"
    ).read_text(encoding="utf-8")

    assert '"CLI        | cli/"' in text
    assert '"Rendering  | rendering/"' in text
    assert "VSA-NAV:PAGES-HERE" not in text


def test_examples_pages_use_local_navigation():
    pages = [
        "examples/hugo-demo/content-source/voorbeelden/basis.md",
        "examples/hugo-demo/content-source/voorbeelden/multiline.md",
        "examples/hugo-demo/content-source/voorbeelden/fouten.md",
        "examples/hugo-demo/content-source/voorbeelden/markdown.md",
    ]

    for page in pages:
        text = Path(page).read_text(encoding="utf-8")
        assert "{{< navbuttons" in text
        assert '"Voorbeelden | ../"' in text


def test_cli_demo_contains_validate_example():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/cli.md"
    ).read_text(encoding="utf-8")

    assert "vsa validate" in text
    assert "OK" in text


def test_markdown_demo_contains_build_markdown():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/markdown.md"
    ).read_text(encoding="utf-8")

    assert "vsa build-markdown" in text
    assert "generated\\content" in text
