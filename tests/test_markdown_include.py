import pytest
from pathlib import Path

from vsa.markdown_include import resolve_includes, IncludeError


def test_passthrough_when_no_includes(tmp_path):
    source = tmp_path / "doc.md"
    source.write_text("# Titel\n\nGewone tekst.\n", encoding="utf-8")

    result = resolve_includes("# Titel\n\nGewone tekst.\n", source)

    assert result == "# Titel\n\nGewone tekst.\n"


def test_include_markdown(tmp_path):
    included = tmp_path / "fragment.md"
    included.write_text("Ingevoegde tekst.\n", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = "Voor.\n:::include fragment.md:::\nNa.\n"

    result = resolve_includes(text, source)

    assert "Ingevoegde tekst." in result
    assert ":::include" not in result
    assert "Voor." in result
    assert "Na." in result


def test_include_vsa(tmp_path):
    vsa_file = tmp_path / "melodie.vsa"
    vsa_file.write_text("[:] {/Hei_} is de Heer. [//:]", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = ":::include melodie.vsa:::\n"

    result = resolve_includes(text, source)

    assert "::: vsa-notatie" in result
    assert ":::" in result
    assert "{/Hei_}" in result
    assert ":::include" not in result


def test_include_svg(tmp_path):
    svg_file = tmp_path / "afbeelding.svg"
    svg_file.write_text("<svg></svg>", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = ":::include afbeelding.svg:::\n"

    result = resolve_includes(text, source)

    assert '<img src="afbeelding.svg" class="vsa-notation" />' in result
    assert ":::include" not in result


def test_recursive_include(tmp_path):
    inner = tmp_path / "inner.md"
    inner.write_text("Binnenste tekst.\n", encoding="utf-8")

    outer = tmp_path / "outer.md"
    outer.write_text(":::include inner.md:::\n", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = ":::include outer.md:::\n"

    result = resolve_includes(text, source)

    assert "Binnenste tekst." in result
    assert ":::include" not in result


def test_include_resolves_relative_to_including_file(tmp_path):
    sub = tmp_path / "hoofdstuk"
    sub.mkdir()

    melodie = sub / "melodie.md"
    melodie.write_text("Melodietekst.\n", encoding="utf-8")

    chapter = sub / "hoofdstuk.md"
    chapter.write_text(":::include melodie.md:::\n", encoding="utf-8")

    source = tmp_path / "boek.md"
    text = ":::include hoofdstuk/hoofdstuk.md:::\n"

    result = resolve_includes(text, source)

    assert "Melodietekst." in result


def test_multiple_includes_of_same_file(tmp_path):
    fragment = tmp_path / "fragment.md"
    fragment.write_text("Herhaalbaar.\n", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = ":::include fragment.md:::\n:::include fragment.md:::\n"

    result = resolve_includes(text, source)

    assert result.count("Herhaalbaar.") == 2


def test_cycle_detection(tmp_path):
    a = tmp_path / "a.md"
    b = tmp_path / "b.md"
    a.write_text(":::include b.md:::\n", encoding="utf-8")
    b.write_text(":::include a.md:::\n", encoding="utf-8")

    with pytest.raises(IncludeError, match="Kringverwijzing"):
        resolve_includes(":::include a.md:::\n", tmp_path / "doc.md")


def test_file_not_found(tmp_path):
    source = tmp_path / "doc.md"
    text = ":::include ontbreekt.md:::\n"

    with pytest.raises(IncludeError, match="Bestand niet gevonden"):
        resolve_includes(text, source)


def test_unknown_extension(tmp_path):
    unknown = tmp_path / "data.csv"
    unknown.write_text("a,b,c", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = ":::include data.csv:::\n"

    with pytest.raises(IncludeError, match="Onbekend bestandstype"):
        resolve_includes(text, source)


def test_include_inside_code_fence_is_ignored(tmp_path):
    fragment = tmp_path / "fragment.md"
    fragment.write_text("Mag niet verschijnen.\n", encoding="utf-8")

    source = tmp_path / "doc.md"
    text = "```\n:::include fragment.md:::\n```\n"

    result = resolve_includes(text, source)

    assert ":::include fragment.md:::" in result
    assert "Mag niet verschijnen." not in result
