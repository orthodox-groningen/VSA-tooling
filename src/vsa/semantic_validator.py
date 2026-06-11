from dataclasses import dataclass

from .diagnostics import Diagnostic, DiagnosticCollection


@dataclass
class SemanticValidationResult:
    items: list[Diagnostic]

    @property
    def diagnostics(self):
        return self.items

    @property
    def ok(self):
        return not self.has_fatal_errors()

    def has_errors(self):
        """Backward-compatible: any semantic diagnostic counts as an issue."""
        return len(self.items) > 0

    def has_fatal_errors(self):
        return any(item.severity == "error" for item in self.items)

    def has_warnings(self):
        return any(item.severity == "warning" for item in self.items)


class SemanticValidator:
    def __init__(self, document):
        self.document = document

    def validate(self):
        diagnostics = DiagnosticCollection()

        self._validate_modifier_counts(diagnostics)
        self._validate_pitch_marker_ending(diagnostics)

        return SemanticValidationResult(diagnostics.items)

    def _validate_modifier_counts(self, diagnostics):
        for node in getattr(self.document, "nodes", []):
            if not _is_scope_node(node):
                continue

            height_count = _musical_position_count(
                getattr(node, "height_modifier", [])
            )
            length_count = _musical_position_count(
                getattr(node, "length_modifier", [])
            )

            if (
                height_count > 0
                and length_count > 0
                and height_count != length_count
            ):
                diagnostics.add(
                    code="VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH",
                    message_nl=(
                        "Hoogte- en lengte-modifier bevatten niet hetzelfde "
                        "aantal muzikale posities."
                    ),
                    line=1,
                    column=1,
                    severity="error",
                )

    def _validate_pitch_marker_ending(self, diagnostics):
        nodes = getattr(self.document, "nodes", [])

        if len(nodes) < 3:
            return

        meaningful_nodes = [
            node for node in nodes
            if not _is_empty_text_node(node)
        ]

        if len(meaningful_nodes) < 3:
            return

        first = meaningful_nodes[0]
        last = meaningful_nodes[-1]

        if not _is_pitch_marker_node(first):
            return

        if not _contains_sung_material(meaningful_nodes):
            return

        if not _is_pitch_marker_node(last):
            diagnostics.add(
                code="VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER",
                message_nl=(
                    "Een VSA-frase die met een pitch-marker begint, moet "
                    "ook met een afsluitende pitch-marker eindigen."
                ),
                line=1,
                column=1,
                severity="error",
            )
            return

        if len(getattr(last, "height_modifier", [])) == 0:
            diagnostics.add(
                code="VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER",
                message_nl=(
                    "Een afsluitende pitch-marker na gezongen tekst mag niet leeg zijn. "
                    "Gebruik bijvoorbeeld [\\\\:] als afsluitende beweging."
                ),
                line=1,
                column=1,
                severity="error",
            )


def _musical_position_count(values):
    return len([value for value in values if value != "&"])


def _is_scope_node(node):
    return type(node).__name__ == "ScopeNode"


def _is_pitch_marker_node(node):
    return type(node).__name__ == "PitchMarkerNode"


def _is_empty_text_node(node):
    return (
        type(node).__name__ == "TextNode"
        and getattr(node, "text", "").strip() == ""
    )


def _contains_sung_material(nodes):
    return any(_is_scope_node(node) for node in nodes)
