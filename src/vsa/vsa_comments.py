from __future__ import annotations

import re


HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
COMMENT_ONLY_LINE_RE = re.compile(
    r"^[ \t]*<!--.*?-->[ \t]*(?:\r\n|\n|\r|$)",
    re.MULTILINE | re.DOTALL,
)


def strip_vsa_html_comments(text: str) -> str:
    """Return VSA text with HTML comments removed.

    The source text itself is not modified by callers. This function is only
    used for parsing, validation and artifact generation.

    A comment is ignored completely: it is not text, whitespace, newline or
    rendering metadata.

    Comment-only lines are removed including their line ending, so they do not
    introduce blank rendered lines. Inline comments are removed in place.
    """
    stripped, _ = strip_vsa_html_comments_with_offset_map(text)
    return stripped


def strip_vsa_html_comments_with_offset_map(text: str) -> tuple[str, list[int]]:
    """Return stripped VSA text and a per-character source offset map.

    ``offset_map[i]`` is the index in the original ``text`` of stripped
    character ``i``. Use this to map parser/validator positions in stripped
    text back to the caller's source text for diagnostics.
    """
    offset_map: list[int] = []
    out: list[str] = []

    index = 0
    length = len(text)

    while index < length:
        line_start = index
        line_end = index
        while line_end < length and text[line_end] not in "\r\n":
            line_end += 1

        line_content = text[line_start:line_end]
        if line_end < length:
            if text[line_end : line_end + 2] == "\r\n":
                line_ending = "\r\n"
                next_index = line_end + 2
            else:
                line_ending = text[line_end]
                next_index = line_end + 1
        else:
            line_ending = ""
            next_index = line_end

        if COMMENT_ONLY_LINE_RE.match(line_content + line_ending):
            index = next_index
            continue

        content_index = 0
        while content_index < len(line_content):
            if line_content[content_index : content_index + 4] == "<!--":
                comment_end = line_content.find("-->", content_index)
                if comment_end >= 0:
                    content_index = comment_end + 3
                    continue

            character = line_content[content_index]
            out.append(character)
            offset_map.append(line_start + content_index)
            content_index += 1

        for offset_in_ending, character in enumerate(line_ending):
            out.append(character)
            offset_map.append(line_end + offset_in_ending)

        index = next_index

    return "".join(out), offset_map


def semantic_offset_to_source(offset_map: list[int], semantic_offset: int) -> int:
    """Map a character offset in stripped text to the original source offset."""
    if not offset_map:
        return max(0, semantic_offset)

    if semantic_offset < 0:
        return offset_map[0]

    if semantic_offset >= len(offset_map):
        return offset_map[-1] + 1

    return offset_map[semantic_offset]
