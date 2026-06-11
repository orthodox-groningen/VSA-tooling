from dataclasses import dataclass, field
import re

from .parser import Parser


START_MARKER = "::: vsa-notatie"
END_MARKER = ":::"


DEFAULT_METADATA = {
    "do": "F4",
    "mode": "major",
    "tempo": "100",
    "validate-ending": "true",
    "duration-model": "default",
}


@dataclass
class MarkdownBlock:
    start_line: int
    end_line: int
    metadata: dict[str, str] = field(default_factory=dict)
    body: str = ""

    def effective_metadata(self):
        result = dict(DEFAULT_METADATA)
        result.update(self.metadata)
        return result

    def parse_body(self):
        return Parser(self.body).parse()


def parse_markdown_blocks(markdown: str):
    lines = markdown.splitlines()
    blocks = []

    index = 0
    in_code_fence = False
    fence_marker = ""

    while index < len(lines):
        stripped = lines[index].strip()

        fence = _opening_or_closing_fence(stripped)

        if fence:
            if not in_code_fence:
                in_code_fence = True
                fence_marker = fence
            elif _closes_fence(stripped, fence_marker):
                in_code_fence = False
                fence_marker = ""

            index += 1
            continue

        if in_code_fence or stripped != START_MARKER:
            index += 1
            continue

        start_line = index + 1
        index += 1

        metadata = {}
        body_lines = []

        while index < len(lines):
            stripped_inner = lines[index].strip()

            if stripped_inner == END_MARKER:
                break

            parsed_metadata = _parse_metadata_line(stripped_inner)

            if parsed_metadata is not None:
                key, value = parsed_metadata
                metadata[key] = value
            else:
                body_lines.append(lines[index])

            index += 1

        if index >= len(lines):
            end_line = len(lines)
        else:
            end_line = index + 1

        blocks.append(
            MarkdownBlock(
                start_line=start_line,
                end_line=end_line,
                metadata=metadata,
                body="\n".join(body_lines).strip(),
            )
        )

        index += 1

    return blocks


def _parse_metadata_line(line: str):
    if line == "":
        return None

    hash_match = re.fullmatch(r"#\s*([^:]+)\s*:\s*(.*)", line)

    if hash_match:
        return hash_match.group(1).strip(), hash_match.group(2).strip().strip('"')

    assignment_match = re.fullmatch(r"([A-Za-z0-9_-]+)\s*=\s*\"(.*)\"", line)

    if assignment_match:
        return assignment_match.group(1).strip(), assignment_match.group(2).strip()

    return None


def _opening_or_closing_fence(stripped: str):
    if stripped.startswith("```"):
        return "```"

    if stripped.startswith("~~~"):
        return "~~~"

    return ""


def _closes_fence(stripped: str, fence_marker: str):
    return stripped.startswith(fence_marker)
