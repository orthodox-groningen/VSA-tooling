from pathlib import Path


def test_docs_glossary_template_contains_markdown_table_header():
    text = Path("docs/terminologie/_index.template").read_text(encoding="utf-8")

    assert "| Term | Definitie |" in text
    assert "|------|-----------|" in text
    assert '{% hrg="vsa-tools" %}' in text


def test_docs_glossary_alias_converter_uses_alias_text():
    text = Path("docs/tev2-config.yaml").read_text(encoding="utf-8")

    assert "{{#if glossaryAlias}}" in text
    assert "[{{glossaryAlias}}]({{term}}.md)" in text
    assert "[{{glossaryAbbr}}]({{term}}.md)" in text
    assert "terms/{{term}}.md" not in text


def test_hugo_glossary_alias_converter_uses_alias_text():
    text = Path("examples/hugo-demo/tev2-config.yaml").read_text(
        encoding="utf-8"
    )

    assert "{{#if glossaryAlias}}" in text
    assert "[{{glossaryAlias}}](terminologie/{{term}}/)" in text
    assert "[{{glossaryAbbr}}](terminologie/{{term}}/)" in text
    assert "terms/{{term}}.md" not in text


def test_generated_docs_glossary_has_alias_rows_and_valid_relative_links():
    text = Path("docs/terminologie/_index.md").read_text(encoding="utf-8")

    assert "| Term | Definitie |" in text
    assert "| [VSA-inline-include](include-vsa.md) | Alias voor [@include-vsa](include-vsa.md). |" in text
    assert "| [AST](ast.md) | Afkorting van [Abstract Syntax Tree](ast.md). |" in text
    assert "terms/" not in text
    assert "[](" not in text
