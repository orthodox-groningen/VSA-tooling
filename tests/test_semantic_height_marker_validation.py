"""Tests voor semantische validatie van hoogte-markeringen.

Elke lokale markering ([X:] na de eerste) wordt gecontroleerd tegen de
cumulatieve hoogte berekend uit alle tussenliggende EHMs.
"""

import pytest

from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator, SemanticValidationOptions
from vsa.height_markers import _pitch_of_ehm, _pitch_of_ehm_list, _marker_for_pitch


# ---------------------------------------------------------------------------
# Hulpfunctie
# ---------------------------------------------------------------------------

def _validate(source: str):
    document = Parser(source).parse()
    return SemanticValidator(document, source_text=source).validate()


# ---------------------------------------------------------------------------
# Pitch-rekenkundige helpers
# ---------------------------------------------------------------------------

class TestPitchHelpers:
    def test_empty_ehm_is_zero(self):
        assert _pitch_of_ehm("") == 0.0

    def test_neutral_is_zero(self):
        assert _pitch_of_ehm("-") == 0.0
        assert _pitch_of_ehm("~") == 0.0

    def test_single_rise(self):
        assert _pitch_of_ehm("/") == 1.0

    def test_double_rise(self):
        assert _pitch_of_ehm("//") == 2.0

    def test_single_fall(self):
        assert _pitch_of_ehm("\\") == -1.0

    def test_double_fall(self):
        assert _pitch_of_ehm("\\\\") == -2.0

    def test_sharp_prefix_adds_half(self):
        assert _pitch_of_ehm("+/") == 1.5
        assert _pitch_of_ehm("#/") == 1.5
        assert _pitch_of_ehm("♯/") == 1.5

    def test_flat_prefix_subtracts_half(self):
        assert _pitch_of_ehm("b\\") == -1.5
        assert _pitch_of_ehm("♭\\") == -1.5

    def test_sharp_on_neutral_is_half(self):
        assert _pitch_of_ehm("+-") == 0.5
        assert _pitch_of_ehm("#-") == 0.5

    def test_flat_on_neutral_is_minus_half(self):
        assert _pitch_of_ehm("b-") == -0.5

    def test_sharp_on_fall_is_minus_half(self):
        assert _pitch_of_ehm("+\\") == -0.5
        assert _pitch_of_ehm("#\\") == -0.5

    def test_flat_on_rise_is_plus_half(self):
        assert _pitch_of_ehm("b/") == 0.5

    def test_double_plus_sharp(self):
        assert _pitch_of_ehm("+//") == 2.5

    def test_list_sums(self):
        assert _pitch_of_ehm_list(["/", "\\"]) == 0.0
        assert _pitch_of_ehm_list(["//", "/"]) == 3.0
        # b\ = -0.5 + (-1) = -1.5; #\ = +0.5 + (-1) = -0.5; sum = -2.0
        assert _pitch_of_ehm_list(["b\\", "#\\"]) == -2.0

    def test_empty_list_is_zero(self):
        assert _pitch_of_ehm_list([]) == 0.0


class TestMarkerForPitch:
    def test_zero(self):
        assert _marker_for_pitch(0.0) == "[:]"

    def test_positive_integer(self):
        assert _marker_for_pitch(1.0) == "[/:]"
        assert _marker_for_pitch(3.0) == "[///:]"

    def test_negative_integer(self):
        assert _marker_for_pitch(-1.0) == "[\\:]"
        assert _marker_for_pitch(-2.0) == "[\\\\:]"

    def test_positive_half(self):
        assert _marker_for_pitch(0.5) == "[+-:]"
        assert _marker_for_pitch(1.5) == "[+/:]"
        assert _marker_for_pitch(2.5) == "[+//:]"

    def test_negative_half(self):
        assert _marker_for_pitch(-0.5) == "[b-:]"
        assert _marker_for_pitch(-1.5) == "[b\\:]"
        assert _marker_for_pitch(-2.5) == "[b\\\\:]"


# ---------------------------------------------------------------------------
# Validatieregels
# ---------------------------------------------------------------------------

class TestHeightMarkerValidation:
    def test_no_markers_no_error(self):
        result = _validate("{aap}")
        assert result.ok
        assert not any(
            d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
            for d in result.diagnostics
        )

    def test_single_marker_no_error(self):
        result = _validate("[//:] {/aap}{/noot}")
        assert result.ok

    def test_consistent_rising_sequence(self):
        # start=2, +1+1=4, markering=4 → OK
        result = _validate("[//:] {/aap}{/noot} [////:]")
        assert result.ok

    def test_mismatch_rising(self):
        # start=2, +1+1=4, maar markering declareert 0
        result = _validate("[//:] {/noot}{/mies} [:]")
        codes = [d.code for d in result.diagnostics]
        assert "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH" in codes

    def test_mismatch_hint_contains_correct_marker(self):
        result = _validate("[//:] {/noot}{/mies} [:]")
        mismatch = next(
            d for d in result.diagnostics
            if d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        )
        assert "[////:]" in mismatch.hint_nl

    def test_mismatch_message_contains_computed_delta(self):
        result = _validate("[//:] {/noot}{/mies} [:]")
        mismatch = next(
            d for d in result.diagnostics
            if d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        )
        assert mismatch.message_nl == "computed = marker + 4"

    def test_consistent_falling_sequence(self):
        # start=-1, -1-1=-3, markering=-3 → OK
        result = _validate("[\\:] {\\aap}{\\noot} [\\\\\\:]")
        assert result.ok

    def test_mismatch_falling(self):
        # start=-1, -1-1=-3, maar markering declareert 0
        result = _validate("[\\:] {\\aap}{\\noot} [:]")
        codes = [d.code for d in result.diagnostics]
        assert "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH" in codes

    def test_mixed_rise_and_fall_consistent(self):
        # start=-1, +1=0, markering=0 → OK (niet fout!)
        result = _validate("[\\:] {/aap} [:]")
        assert result.ok

    def test_neutral_scope_contributes_zero(self):
        # start=1, {tekst}=0, markering=1 → OK
        result = _validate("[//:] {aap} [//:]")
        assert result.ok

    def test_multiple_mismatches_all_reported(self):
        # Twee onafhankelijke foute lokale markeringen → beide fouten zichtbaar
        result = _validate("[//:] {/aap} [//:] {/noot} [//:]")
        mismatches = [
            d for d in result.diagnostics
            if d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        ]
        assert len(mismatches) == 2

    def test_cascade_mismatches_after_wrong_marker_are_suppressed(self):
        # Eén foute markering; latere [:] zijn alleen fout door die cascade
        result = _validate("[//:] {/aap}{/noot} [:] [:]")
        mismatches = [
            d for d in result.diagnostics
            if d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        ]
        assert len(mismatches) == 1

    def test_halftone_consistent(self):
        # [:] {+\aap.}{#\noot_}{b\mies} [b\\:]
        # 0 + (-0.5) + (-0.5) + (-1.5) = -2.5; [b\\:] = -0.5 + -2 = -2.5 → OK
        result = _validate("[:]  {+\\aap.}{#\\noot_}{b\\mies} [b\\\\:]")
        assert result.ok

    def test_halftone_mismatch(self):
        # [:] {+\aap} [:]  →  0 + (-0.5) = -0.5, maar markering zegt 0
        result = _validate("[:] {+\\aap} [:]")
        codes = [d.code for d in result.diagnostics]
        assert "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH" in codes

    def test_halftone_mismatch_hint(self):
        result = _validate("[:] {+\\aap} [:]")
        mismatch = next(
            d for d in result.diagnostics
            if d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        )
        assert "[b-:]" in mismatch.hint_nl

    def test_line_column_points_to_wrong_marker(self):
        # Marker staat op regel 2, kolom 5
        source = "[//:]\n    [:] {/aap}"
        result = _validate(source)
        # Er is geen mismatch hier want start=2, {:}=0 met EHM na markering
        # Juiste test: fout op regel 1 kolom 7 (het foute [:] op eerste regel)
        source2 = "[//:] {/aap} [:]"
        result2 = _validate(source2)
        mismatch = next(
            d for d in result2.diagnostics
            if d.code == "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        )
        # Markering staat aan het eind, dus kolom > 1
        assert mismatch.column > 1

    def test_severity_overridable_to_warning(self):
        opts = SemanticValidationOptions(
            severity_overrides={"VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH": "warning"}
        )
        document = Parser("[//:] {/noot} [:]").parse()
        result = SemanticValidator(
            document, opts, source_text="[//:] {/noot} [:]"
        ).validate()
        assert result.ok  # geen fatal error
        assert result.has_warnings()
