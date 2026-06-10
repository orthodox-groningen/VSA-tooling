from dataclasses import dataclass
from typing import Optional


@dataclass
class Diagnostic:
    code: str
    message_nl: str
    line: int
    column: int
    severity: str = "error"


class DiagnosticCollection:
    def __init__(self):
        self.items = []

    def add(
        self,
        code: str,
        message_nl: str,
        line: int,
        column: int,
        severity: str = "error",
    ):
        self.items.append(
            Diagnostic(
                code=code,
                message_nl=message_nl,
                line=line,
                column=column,
                severity=severity,
            )
        )

    def has_errors(self):
        return any(x.severity == "error" for x in self.items)
