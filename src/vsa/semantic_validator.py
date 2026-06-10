from .diagnostics import DiagnosticCollection
from .ast import ScopeNode


class SemanticValidator:
    def __init__(self, document):
        self.document = document
        self.diagnostics = DiagnosticCollection()

    def validate(self):
        for node in self.document.nodes:
            if not isinstance(node, ScopeNode):
                continue

            hm = node.height_modifier
            lm = node.length_modifier

            hm_count = len(hm)
            lm_count = len(lm)

            if hm_count > 0 and lm_count > 0 and hm_count != lm_count:
                self.diagnostics.add(
                    code="VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH",
                    message_nl="Hoogte- en lengte-modifier bevatten niet hetzelfde aantal muzikale posities.",
                    line=1,
                    column=1,
                )

        return self.diagnostics
