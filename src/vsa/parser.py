from .ast import Document, TextNode, ScopeNode, PitchMarkerNode
from .errors import VSASyntaxError


EHM_VALUES = [
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
]

ELM_VALUES = [
    "__",
    "..",
    "_",
    ".",
    "-",
    "~",
]

MODIFIER_CHARS = set("&~+-\\/_.")


class Parser:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def parse(self) -> Document:
        nodes = []

        while self.pos < len(self.text):
            if self._starts_with("{"):
                nodes.append(self._parse_scope())
            elif self._starts_with("["):
                nodes.append(self._parse_pitch_marker())
            elif self._starts_with("}"):
                raise VSASyntaxError("Losse sluitaccolade", self.pos)
            else:
                nodes.append(self._parse_text())

        return Document(nodes=nodes)

    def _parse_text(self) -> TextNode:
        start = self.pos

        while self.pos < len(self.text):
            if self.text[self.pos] in "{[":
                break
            if self.text[self.pos] == "}":
                raise VSASyntaxError("Losse sluitaccolade", self.pos)
            self.pos += 1

        return TextNode(self.text[start:self.pos])

    def _parse_pitch_marker(self) -> PitchMarkerNode:
        start = self.pos

        end = self.text.find("]", self.pos)

        if end == -1:
            raise VSASyntaxError("Toonhoogte-markering zonder afsluitende ']'", start)

        content = self.text[self.pos + 1:end]

        if not content.endswith(":"):
            raise VSASyntaxError("Toonhoogte-markering mist ':'", start)

        raw_modifier = content[:-1]
        height_modifier = self._split_modifier(raw_modifier, EHM_VALUES) if raw_modifier else []

        self.pos = end + 1

        return PitchMarkerNode(height_modifier=height_modifier)

    def _parse_scope(self) -> ScopeNode:
        start = self.pos

        end = self.text.find("}", self.pos)

        if end == -1:
            raise VSASyntaxError("Scope zonder afsluitende accolade", start)

        content = self.text[self.pos + 1:end]

        if content == "":
            raise VSASyntaxError("Scope zonder zangelement", start)

        if any(ch.isspace() for ch in content):
            raise VSASyntaxError("Whitespace binnen scope", start)

        height_modifier, rest = self._consume_prefix_modifier(content, EHM_VALUES)
        length_modifier, element = self._consume_suffix_modifier(rest, ELM_VALUES)

        if element == "":
            raise VSASyntaxError("Scope zonder zangelement", start)

        if any(ch in MODIFIER_CHARS for ch in element):
            raise VSASyntaxError("Modifierteken binnen zangelement", start)

        self.pos = end + 1

        return ScopeNode(
            height_modifier=height_modifier,
            text=element,
            length_modifier=length_modifier,
        )

    def _consume_prefix_modifier(self, content: str, allowed_values: list[str]) -> tuple[list[str], str]:
        parts = []
        remaining = content

        while remaining:
            matched = None

            for value in allowed_values:
                if remaining.startswith(value):
                    matched = value
                    break

            if matched is None:
                break

            parts.append(matched)
            remaining = remaining[len(matched):]

            if remaining.startswith("&"):
                remaining = remaining[1:]
                continue

            break

        return parts, remaining

    def _consume_suffix_modifier(self, content: str, allowed_values: list[str]) -> tuple[list[str], str]:
        best = None

        for index in range(len(content) + 1):
            candidate_text = content[:index]
            candidate_modifier = content[index:]

            if candidate_modifier == "":
                continue

            try:
                parts = self._split_modifier(candidate_modifier, allowed_values)
            except VSASyntaxError:
                continue

            best = (parts, candidate_text)

        if best is None:
            return [], content

        return best

    def _split_modifier(self, modifier: str, allowed_values: list[str]) -> list[str]:
        if modifier == "":
            return []

        parts = modifier.split("&")

        if any(part == "" for part in parts):
            raise VSASyntaxError("Leeg modifierdeel", self.pos)

        for part in parts:
            if part not in allowed_values:
                raise VSASyntaxError(f"Ongeldige modifier: {part}", self.pos)

        return parts

    def _starts_with(self, value: str) -> bool:
        return self.text.startswith(value, self.pos)
