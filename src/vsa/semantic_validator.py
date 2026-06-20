from dataclasses import dataclass, field

from .diagnostics import DiagnosticCollection
from .height_markers import height_marker_refs

DOC_BASE = "docs/user-guide-config-severity.md"


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
    def __init__(self, document, options: SemanticValidationOptions | None = None):
        self.document = document
        self.height_markers = height_marker_refs(document)
        self.options = options or SemanticValidationOptions()

    def validate(self):
        diagnostics = DiagnosticCollection()

        self._validate_modifier_counts(diagnostics)

        return SemanticValidationResult(diagnostics.items)

    def _height_markers(self):
        return self.height_markers

    def _severity(self, code: str):
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
