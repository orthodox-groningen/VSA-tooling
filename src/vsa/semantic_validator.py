from dataclasses import dataclass, field

from .diagnostics import DiagnosticCollection
from .height_markers import (
    height_marker_refs,
    _pitch_of_ehm_list,
    _marker_for_pitch,
)

DOC_BASE = "docs/user-guide-config-severity.md"


def _format_pitch(pitch: float) -> str:
    """Geeft een leesbare representatie van een pitchwaarde: '2' i.p.v. '2.0'."""
    return str(int(pitch)) if pitch == int(pitch) else str(pitch)


@dataclass
class SemanticValidationResult:
    items: list

    @property
    def diagnostics(self):
        return self.items

    @property
    def ok(self):
        return not self.has_fatal_errors()

    def has_errors(self):
        return len(self.items) > 0

    def has_fatal_errors(self):
        return any(item.severity == "error" for item in self.items)

    def has_warnings(self):
        return any(item.severity == "warning" for item in self.items)


@dataclass
class SemanticValidationOptions:
    severity_overrides: dict[str, str] = field(default_factory=dict)


class SemanticValidator:
    def __init__(
        self,
        document,
        options: SemanticValidationOptions | None = None,
        source_text: str = "",
    ):
        self.document = document
        self.height_markers = height_marker_refs(document)
        self.options = options or SemanticValidationOptions()
        self.source_text = source_text

    def _line_column(self, offset: int | None) -> tuple[int, int]:
        """Zet een character-offset om naar (regel, kolom), of (1, 1) als onbekend."""
        if not self.source_text or offset is None:
            return 1, 1
        pos = max(0, min(offset, len(self.source_text)))
        before = self.source_text[:pos]
        line = before.count("\n") + 1
        last_nl = before.rfind("\n")
        col = (pos + 1) if last_nl == -1 else (pos - last_nl)
        return line, col

    def validate(self):
        diagnostics = DiagnosticCollection()

        self._validate_modifier_counts(diagnostics)
        self._validate_height_marker_sequence(diagnostics)

        return SemanticValidationResult(diagnostics.items)

    def _height_markers(self):
        return self.height_markers

    def _severity(self, code: str) -> str:
        return self.options.severity_overrides.get(code, "error")

    def _validate_modifier_counts(self, diagnostics):
        code = "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"

        for node in getattr(self.document, "nodes", []):
            if type(node).__name__ != "ScopeNode":
                continue

            height = len([
                value for value in getattr(node, "height_modifier", [])
                if value != "&"
            ])
            length = len([
                value for value in getattr(node, "length_modifier", [])
                if value != "&"
            ])

            if height > 0 and length > 0 and height != length:
                diagnostics.add(
                    code=code,
                    message_nl=(
                        "Hoogte- en lengte-modifier bevatten niet hetzelfde "
                        "aantal muzikale posities."
                    ),
                    line=1,
                    column=1,
                    severity=self._severity(code),
                    category="semantic",
                    hint_nl=(
                        "Controleer of hoogte- en lengtemodifiers evenveel "
                        "muzikale posities bevatten."
                    ),
                    doc_url=DOC_BASE,
                )

    def _validate_height_marker_sequence(self, diagnostics: DiagnosticCollection) -> None:
        """Controleert of elke lokale hoogte-markering overeenkomt met de berekende hoogte.

        De eerste markering geeft de beginhoogte. Elke volgende markering
        (rol 'local_height') wordt vergeleken met de cumulatieve hoogte op
        basis van alle EHMs van de tussenliggende zangelementen.
        Bij een mismatch wordt de berekende hoogte aangehouden voor verdere
        validatie, zodat alle fouten in één keer zichtbaar zijn.
        """
        markers = self._height_markers()
        if len(markers) < 2:
            return

        code = "VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH"
        nodes = self.document.nodes
        current_pitch: float = _pitch_of_ehm_list(markers[0].ehm)
        prev_index: int = markers[0].index

        for ref in markers[1:]:
            for node in nodes[prev_index + 1 : ref.index]:
                if type(node).__name__ == "ScopeNode":
                    ehm = getattr(node, "height_modifier", [])
                    current_pitch += _pitch_of_ehm_list(ehm)

            declared: float = _pitch_of_ehm_list(ref.ehm)
            if declared != current_pitch:
                correct = _marker_for_pitch(current_pitch)
                line, col = self._line_column(ref.node.start)
                pitch_str = _format_pitch(current_pitch)
                declared_str = _format_pitch(declared)
                diagnostics.add(
                    code=code,
                    message_nl=(
                        f"Hoogte-markering declareert hoogte {declared_str}, "
                        f"maar de berekende hoogte op deze positie is {pitch_str}."
                    ),
                    line=line,
                    column=col,
                    severity=self._severity(code),
                    category="semantic",
                    hint_nl=f"Wijzig de markering naar `{correct}`.",
                    doc_url=DOC_BASE,
                )

            prev_index = ref.index
