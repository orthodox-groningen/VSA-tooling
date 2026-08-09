"""Conformance: valid vsa-templates pass; invalid ones fail."""

from pathlib import Path

import pytest
import yaml

from vsa_template_validate import (
    EXAMPLES_INVALID,
    EXAMPLES_VALID,
    TemplateValidationError,
    load_template,
    validate_template,
)


def _yaml_files(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.yaml"))


def _known_ids() -> set[str]:
    ids: set[str] = set()
    for path in _yaml_files(EXAMPLES_VALID):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and isinstance(doc.get("id"), str):
            ids.add(doc["id"])
    return ids


KNOWN_IDS = _known_ids()


@pytest.mark.parametrize("path", _yaml_files(EXAMPLES_VALID), ids=lambda p: p.name)
def test_valid_templates_pass(path: Path) -> None:
    validate_template(load_template(path), known_ids=KNOWN_IDS)


@pytest.mark.parametrize("path", _yaml_files(EXAMPLES_INVALID), ids=lambda p: p.name)
def test_invalid_templates_fail(path: Path) -> None:
    with pytest.raises(TemplateValidationError):
        validate_template(load_template(path), known_ids=KNOWN_IDS)


def test_invalid_cycle_unknown_code() -> None:
    path = EXAMPLES_INVALID / "cycle-unknown-phrase.yaml"
    with pytest.raises(TemplateValidationError) as exc:
        validate_template(load_template(path), known_ids=KNOWN_IDS)
    assert exc.value.code == "TEMPLATE-CYCLE-REF"


def test_invalid_final_in_cycle_code() -> None:
    path = EXAMPLES_INVALID / "final-in-cycle.yaml"
    with pytest.raises(TemplateValidationError) as exc:
        validate_template(load_template(path), known_ids=KNOWN_IDS)
    assert exc.value.code == "TEMPLATE-FINAL-NOT-IN-CYCLE"


def test_invalid_missing_voice_code() -> None:
    path = EXAMPLES_INVALID / "missing-voice-pitch.yaml"
    with pytest.raises(TemplateValidationError) as exc:
        validate_template(load_template(path), known_ids=KNOWN_IDS)
    assert exc.value.code == "TEMPLATE-PITCHES"


def test_invalid_sequence_unknown_code() -> None:
    path = EXAMPLES_INVALID / "sequence-unknown-phrase.yaml"
    with pytest.raises(TemplateValidationError) as exc:
        validate_template(load_template(path), known_ids=KNOWN_IDS)
    assert exc.value.code == "TEMPLATE-SEQUENCE-REF"


def test_invalid_same_as_missing_code() -> None:
    path = EXAMPLES_INVALID / "same-as-missing-target.yaml"
    with pytest.raises(TemplateValidationError) as exc:
        validate_template(load_template(path), known_ids=KNOWN_IDS)
    assert exc.value.code == "TEMPLATE-SAME-AS-REF"


def test_tropaar_toon_5_aliases_stichier() -> None:
    doc = load_template(EXAMPLES_VALID / "tropaar-toon-5.yaml")
    assert doc["same_as"] == "stichier-toon-5"
    validate_template(doc, known_ids=KNOWN_IDS)
