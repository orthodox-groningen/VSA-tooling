from .ast import Document, TextNode, ScopeNode, PitchMarkerNode, HeightMarkerNode
from .errors import VSASyntaxError


BRACKET_DIRECTIVE_END = ":]"

BASE_EHM_VALUES = [
    "/////",
    "////",
    "///",
    "//",
    "/",
    "\\\\\\\\\\",
    "\\\\\\\\",
    "\\\\\\",
    "\\\\",
    "\\",
    "-",
    "~",
]

# Canonical form: '+' and '♯' are aliases for '#'; '♭' is alias for 'b'.
HALFTOON_PREFIXES = ["#", "♯", "+", "b", "♭"]

HALFTOON_CANONICAL: dict[str, str] = {
    "#": "#",
    "♯": "#",
    "+": "#",
    "b": "b",
    "♭": "b",
}

EHM_VALUES = sorted(
    BASE_EHM_VALUES + [p + b for p in HALFTOON_PREFIXES for b in BASE_EHM_VALUES],
    key=len,
    reverse=True,
)

ELM_VALUES = [
    "__",
    "..",
    "_.",
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
        end_token = self.text.find(BRACKET_DIRECTIVE_END, self.pos + 1)

        if end_token == -1:
            raise VSASyntaxError("Toonhoogte-markering mist bracket-directive eindtoken ':]'", start)

        raw_modifier = self.text[self.pos + 1:end_token]
        height_modifier = self._parse_pitch_marker_modifier(raw_modifier, start)

        self.pos = end_token + len(BRACKET_DIRECTIVE_END)

        return HeightMarkerNode(
            height_modifier=height_modifier,
            start=start,
            end=self.pos,
        )

    def _parse_pitch_marker_modifier(self, raw_modifier: str, start: int) -> list[str]:
        if raw_modifier == "":
            return []

        if raw_modifier not in EHM_VALUES:
            raise VSASyntaxError(f"Ongeldige modifier: {raw_modifier}", start)

        return [raw_modifier]

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

        height_modifier, element, length_modifier = self._split_scope_content(content, start)

        self.pos = end + 1

        return ScopeNode(
            height_modifier=height_modifier,
            text=element,
            length_modifier=length_modifier,
        )

    def _split_scope_content(self, content: str, start: int):
        prefix_candidates = self._prefix_candidates(content, EHM_VALUES)
        suffix_candidates = self._suffix_candidates(content, ELM_VALUES)

        best = None

        for prefix_len, height_modifier in prefix_candidates:
            for suffix_start, length_modifier in suffix_candidates:
                if prefix_len > suffix_start:
                    continue

                element = content[prefix_len:suffix_start]

                if element == "":
                    continue

                if any(ch in MODIFIER_CHARS for ch in element):
                    continue

                score = prefix_len + (len(content) - suffix_start)

                if best is None or score > best[0]:
                    best = (score, height_modifier, element, length_modifier)

        if best is None:
            if any(ch in MODIFIER_CHARS for ch in content):
                raise VSASyntaxError("Modifierteken binnen zangelement", start)

            return [], content, []

        _, height_modifier, element, length_modifier = best

        return height_modifier, element, length_modifier

    def _prefix_candidates(self, content: str, allowed_values: list[str]):
        candidates = [(0, [])]

        def walk(index, parts):
            matched_any = False

            for value in allowed_values:
                if content.startswith(value, index):
                    next_index = index + len(value)
                    new_parts = parts + [value]
                    candidates.append((next_index, new_parts))
                    matched_any = True

                    if content.startswith("&", next_index):
                        walk(next_index + 1, new_parts)

            return matched_any

        walk(0, [])

        return candidates

    def _suffix_candidates(self, content: str, allowed_values: list[str]):
        candidates = [(len(content), [])]

        for index in range(len(content)):
            raw = content[index:]

            try:
                parts = self._split_modifier(raw, allowed_values)
            except VSASyntaxError:
                continue

            candidates.append((index, parts))

        return candidates

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
