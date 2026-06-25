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
    text = COMMENT_ONLY_LINE_RE.sub("", text)
    return HTML_COMMENT_RE.sub("", text)
