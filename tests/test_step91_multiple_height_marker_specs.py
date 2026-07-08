from docs_contracts import PARSER_STEPS, read, read_doc, assert_terms


HISTORICAL_STEP = PARSER_STEPS / "parser-stap-91-multiple-height-marker-specs.md"


def test_step91_historical_addendum_preserves_decision_context():
    text = read(HISTORICAL_STEP)

    assert_terms(
        text,
        (
            "[<EHM>:]",
            "`&` is geen onderdeel van een hoogte-markering.",
            "meerdere hoogte-markeringen mogen in hetzelfde blok staan",
            "De SVG-renderer behandelt alle hoogte-markeringen gelijk",
        ),
    )


def test_multiple_height_marker_contract_is_in_current_specs():
    text = read_doc("syntax_spec") + read_doc("rendering_spec")

    assert_terms(
        text,
        (
            "[<EHM>:]",
            '":]" ;',
            "mogen meerdere hoogte-markeringen voorkomen",
            "eerste hoogte-markering = beginhoogte",
            "latere hoogte-markering = lokale hoogte op die positie",
        ),
    )


def test_multiple_height_marker_open_work_is_tracked_in_addenda():
    text = read_doc("todo_addendum")

    assert_terms(
        text,
        (
            "Meerdere hoogte-markeringen",
            "parseracceptatie",
            "AST-representatie",
            "validatorregels",
            "SVG-rendering",
        ),
    )
