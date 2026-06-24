from .vsa_comments import strip_vsa_html_comments
from .diagnostics import DiagnosticCollection


class SyntaxValidator:
    def __init__(self, text: str):
        # HTML comments inside VSA notation are ignored for validation.
        self.text = strip_vsa_html_comments(text)
        self.diagnostics = DiagnosticCollection()

    def validate(self):
        stack = []

        line = 1
        column = 1

        for ch in self.text:
            if ch == "{":
                stack.append((line, column))

            elif ch == "}":
                if not stack:
                    self.diagnostics.add(
                        code="VSA-SYNTAX-UNEXPECTED-CLOSE-BRACE",
                        message_nl="Losse sluitaccolade.",
                        line=line,
                        column=column,
                    )
                else:
                    stack.pop()

            if ch == "\n":
                line += 1
                column = 1
            else:
                column += 1

        for line, column in stack:
            self.diagnostics.add(
                code="VSA-SYNTAX-UNCLOSED-SCOPE",
                message_nl="Scope zonder afsluitende accolade.",
                line=line,
                column=column,
            )

        return self.diagnostics
