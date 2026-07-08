from docs_contracts import PARSER_STEPS, read, read_docs, assert_terms


HISTORICAL_CONTRACT = PARSER_STEPS / "parser-stap-92-height-marker-parser-contract.md"


def test_step92_historical_parser_contract_preserves_examples():
    text = read(HISTORICAL_CONTRACT)

    assert_terms(
        text,
        (
            "samengestelde eindtoken",
            "[<EHM>:]",
            "[//:] {\\Heer}, [\\:] ontferm {/U}.",
            "[/&\\:] fout",
            "[_:] fout",
            "[//\\:] fout",
        ),
    )


def test_current_syntax_spec_defines_height_marker_as_single_bracket_token():
    text = read_docs("syntax_spec", "architecture_parser")

    assert_terms(
        text,
        (
            "toonhoogte-markering ::=",
            "[ EHM ]",
            '":]" ;',
            "lexer / bracket-scanner",
            "Bracket-dispatch",
        ),
    )


def test_current_rendering_spec_keeps_pitch_markers_in_document_order():
    text = read_docs("rendering_spec", "architecture_rendering")

    assert_terms(
        text,
        (
            "height_markers = alle HeightMarkerNode nodes in bronvolgorde",
            "De renderer behandelt elke hoogte-markering hetzelfde",
            "gewone positionele semantische nodes",
        ),
    )
