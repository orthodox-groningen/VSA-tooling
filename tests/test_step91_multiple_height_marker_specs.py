from pathlib import Path


SPEC = Path("docs/architecture/parser-stap-91-multiple-height-marker-specs.md")
TODO = Path("docs/todo.md")


def test_step91_spec_exists():
    assert SPEC.exists()


def test_step91_spec_defines_marker_shape_without_ampersand():
    text = SPEC.read_text(encoding="utf-8")

    assert "[<EHM>:]" in text
    assert "`&` is geen onderdeel van een hoogte-markering." in text
    assert "[/&:]" in text


def test_step91_spec_has_no_invalid_ampersand_example_as_valid_example():
    text = SPEC.read_text(encoding="utf-8")
    valid_section = (
        text
        .split("Voorbeelden van geldige hoogte-markeringen:", 1)[1]
        .split("Voorbeelden van ongeldige hoogte-markeringen:", 1)[0]
    )

    assert "[/&:]" not in valid_section
    assert "[&:]" not in valid_section


def test_step91_spec_allows_invalid_ampersand_example_as_invalid_example():
    text = SPEC.read_text(encoding="utf-8")
    invalid_section = text.split("Voorbeelden van ongeldige hoogte-markeringen:", 1)[1]

    assert "[/&:]" in invalid_section
    assert "[&:]" in invalid_section


def test_step91_spec_allows_multiple_height_markers():
    text = SPEC.read_text(encoding="utf-8")

    assert "meerdere hoogte-markeringen" in text
    assert "Elke hoogte-markering geeft een (toon)hoogte aan" in text
    assert "Elke volgende hoogte-markering" in text


def test_step91_spec_allows_text_around_markers():
    text = SPEC.read_text(encoding="utf-8")

    assert "tekst vóór de eerste hoogte-markering" in text
    assert "tekst na de laatste hoogte-markering" in text
    assert "tussen hoogte-markeringen mag tekst staan" in text


def test_step91_spec_says_svg_treats_markers_equally():
    text = SPEC.read_text(encoding="utf-8")

    assert "De SVG-renderer behandelt alle hoogte-markeringen gelijk." in text
    assert "geen aparte visuele status" in text


def test_step91_todo_is_consolidated_in_main_todo():
    assert TODO.exists()
    text = TODO.read_text(encoding="utf-8")

    assert "Meerdere hoogte-markeringen" in text
    assert "parseracceptatie" in text
    assert "AST-representatie" in text
    assert "validatorregels" in text
    assert "SVG-rendering" in text
