"""Test-hulp: paden + re-export van de product-validator."""

from pathlib import Path

from vsa.template_validate import (  # noqa: F401
    ANCHORS,
    TemplateValidationError,
    collect_template_ids,
    load_template,
    validate_template,
)

SPEC_ROOT = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "specification-vsa-templates"
)
LIBRARY = SPEC_ROOT / "library"
EXAMPLES_VALID = LIBRARY  # */template.yaml
EXAMPLES_INVALID = SPEC_ROOT / "examples" / "invalid"
