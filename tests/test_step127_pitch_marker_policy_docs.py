from pathlib import Path

from docs_contracts import read_docs, assert_terms


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_step127_architecture_policy_marks_old_final_pitch_errors_obsolete():
    text = read("docs/history/parser-steps/parser-stap-127-pitch-marker-policy-consolidation.md")

    assert_terms(
        text,
        (
            "VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER",
            "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER",
            "obsolete",
            "geen expliciete eindtooncontrole",
        ),
    )


def test_step127_docs_define_empty_marker_as_neutral_height():
    text = read_docs("rendering_spec", "validation_spec")

    assert_terms(
        text,
        ("Een eindmarkering `[:]`", "neutrale hoogte", "equivalent aan `[-:]`", "[~:]"),
    )


def test_step127_user_docs_do_not_present_old_pitch_codes_as_current_examples():
    text = read_docs("validation_spec", "diagnostics_reference")

    assert "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH" in text
    assert "VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER" in text
    assert "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER" in text
    assert "obsolete" in text.lower()
