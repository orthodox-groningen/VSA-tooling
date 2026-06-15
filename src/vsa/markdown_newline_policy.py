from __future__ import annotations

import re


def preserve_vsa_source_newlines(source: str) -> str:
    """Preserve physical VSA source lines for parsing/rendering.

    Normalize CRLF/CR to LF, but never join lines with spaces.

    Markdown hardbreak whitespace at the end of a VSA source line
    is not musical content. Strip it before preserving the newline.
    """

    source = source.replace("\r\n", "\n").replace("\r", "\n")
    source = re.sub(r"[ \t]+\n", "\n", source)
    return source
