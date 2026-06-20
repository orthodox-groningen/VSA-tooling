from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_step127_architecture_policy_marks_old_final_pitch_errors_obsolete():
    text = read("docs/architecture/parser-stap-127-pitch-marker-policy-consolidation.md")

    assert "VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER" in text
    assert "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER" in text
    assert "obsolete" in text
    assert "geen expliciete eindtooncontrole" in text


def test_step127_docs_define_empty_marker_as_neutral_height():
    text = read("docs/spec/vsa-height-markers.md")

    assert "Een eindmarkering `[:]` is niet leeg" in text
    assert "equivalent aan `[-:]`" in text
    assert "[~:]" in text


def test_step127_user_docs_do_not_present_old_pitch_codes_as_current_examples():
    text = read("docs/user-guide.md")

    assert "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH" in text
    assert "VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER` en `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` zijn obsolete" in text
