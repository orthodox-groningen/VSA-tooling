from dataclasses import dataclass


@dataclass
class Diagnostic:
    code: str
    message_nl: str
    line: int
    column: int
    severity: str = "error"
    category: str = "general"
    hint_nl: str = ""
    doc_url: str = ""


class DiagnosticCollection:
    def __init__(self):
        self.items = []

    def add(
        self,
        code,
        message_nl,
        line,
        column,
        severity="error",
        category="general",
        hint_nl="",
        doc_url="",
    ):
        self.items.append(
            Diagnostic(
                code=code,
                message_nl=message_nl,
                line=line,
                column=column,
                severity=severity,
                category=category,
                hint_nl=hint_nl,
                doc_url=doc_url,
            )
        )

    def has_errors(self):
        """Backward-compatible: any diagnostic counts as an issue."""
        return len(self.items) > 0

    def has_fatal_errors(self):
        return any(item.severity == "error" for item in self.items)

    def has_warnings(self):
        return any(item.severity == "warning" for item in self.items)
