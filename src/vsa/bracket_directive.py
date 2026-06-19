from __future__ import annotations

from typing import NamedTuple


BRACKET_DIRECTIVE_END = ":]"

# Valid EHM values for pitch/height-marker directives.
# The empty string represents the neutral marker `[:]`.
VALID_EHM_VALUES = {
    "",
    "/////",
    "////",
    "///",
    "//",
    "+/",
    "/",
    "-\\",
    "\\\\\\\\\\",
    "\\\\\\\\",
    "\\\\\\",
    "\\\\",
    "\\",
    "-",
    "~",
    "/\\",
}


class BracketDirective(NamedTuple):
    start: int
    end: int
    body: str

    @property
    def source(self) -> str:
        return "[" + self.body + BRACKET_DIRECTIVE_END


def find_bracket_directives(text: str) -> list[BracketDirective]:
    directives: list[BracketDirective] = []
    index = 0

    while index < len(text):
        start = text.find("[", index)
        if start < 0:
            break

        end_token = text.find(BRACKET_DIRECTIVE_END, start + 1)
        if end_token < 0:
            index = start + 1
            continue

        body = text[start + 1:end_token]
        end = end_token + len(BRACKET_DIRECTIVE_END)
        directives.append(BracketDirective(start=start, end=end, body=body))
        index = end

    return directives


def is_pitch_marker_directive(directive: BracketDirective) -> bool:
    return is_valid_ehm(directive.body)


def is_valid_ehm(value: str) -> bool:
    return value in VALID_EHM_VALUES


def pitch_marker_bodies(text: str) -> list[str]:
    return [
        directive.body
        for directive in find_bracket_directives(text)
        if is_pitch_marker_directive(directive)
    ]
