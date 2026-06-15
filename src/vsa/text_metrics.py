from __future__ import annotations


NARROW_CHARS = set("ijlI.,;:!|'`´’‘")
WIDE_CHARS = set("mwMW@#%&")
SPACE_CHARS = set(" \t")
DIGIT_CHARS = set("0123456789")


def estimate_text_width(text: str, font_size: float, preserve_whitespace: bool = True) -> float:
    """Estimate rendered SVG text width.

    This is intentionally still lightweight and deterministic.

    It is better than a raw character-count multiplier because it distinguishes:
    - narrow glyphs: i, l, punctuation
    - wide glyphs: m, w, M, W
    - normal glyphs
    - spaces

    Later this can be replaced by real font metrics.
    """

    if text == "":
        return 0.0

    visible = text if preserve_whitespace else text.strip()

    if visible == "":
        return 0.0

    units = 0.0

    for char in visible:
        units += _char_width_units(char)

    return round(max(0.0, units * font_size), 2)


def estimate_scope_text_width(text: str, font_size: float) -> float:
    if text == "":
        return round(max(4.0, font_size * 0.25), 2)

    # Kleine veiligheidsmarge voor sung text omdat SVG niet exact gemeten wordt.
    return round(max(4.0, estimate_text_width(text, font_size) + font_size * 0.08), 2)


def _char_width_units(char: str) -> float:
    if char in SPACE_CHARS:
        return 0.36

    if char in NARROW_CHARS:
        return 0.28

    if char in WIDE_CHARS:
        return 0.78

    if char in DIGIT_CHARS:
        return 0.55

    if char.isupper():
        return 0.62

    if char in "-_/\\()[]{}":
        return 0.42

    return 0.52
