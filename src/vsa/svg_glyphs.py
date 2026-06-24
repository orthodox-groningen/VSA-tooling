from xml.sax.saxutils import escape

from .parser import HALFTOON_CANONICAL

# Visual symbols for halftoon prefixes.
# '#' (canonical kruis) → '+' matches Liturgikon convention.
# 'b' (canonical mol)   → '♭' uses the standard flat symbol.
# Override via SVGGlyphRenderer(prefix_symbols={...}) for alternative styles.
DEFAULT_PREFIX_SYMBOLS: dict[str, str] = {
    "#": "+",
    "b": "♭",
}

# Single-character prefix chars (all aliases), used to detect prefix tokens.
_HALFTOON_PREFIX_CHARS: frozenset[str] = frozenset(HALFTOON_CANONICAL)


def _split_ehm_token(value: str) -> tuple[str | None, str]:
    """Split an EHM token into (canonical_prefix, base).

    Returns (None, value) when no halftoon prefix is present.
    """
    if len(value) >= 2 and value[0] in _HALFTOON_PREFIX_CHARS:
        return HALFTOON_CANONICAL[value[0]], value[1:]
    return None, value


class SVGGlyphRenderer:
    def __init__(
        self,
        unit: float = 8.0,
        upper_width_factor: float = 0.48,
        lower_width_factor: float = 0.55,
        upper_stroke_width_factor: float = 0.075,
        lower_stroke_width_factor: float = 0.075,
        upper_color: str = "black",
        lower_color: str = "red",
        prefix_symbols: dict[str, str] | None = None,
    ):
        self.unit = unit
        self.upper_width_factor = upper_width_factor
        self.lower_width_factor = lower_width_factor
        self.upper_stroke_width = max(1.0, unit * upper_stroke_width_factor)
        self.lower_stroke_width = max(1.0, unit * lower_stroke_width_factor)
        self.upper_color = upper_color
        self.lower_color = lower_color
        self.prefix_symbols = prefix_symbols if prefix_symbols is not None else DEFAULT_PREFIX_SYMBOLS

    def render_height_modifier(self, values, x, y, width):
        parts = []

        if not values:
            return parts

        count = len(values)
        col_width = width / count

        for index, value in enumerate(values):
            cx = x + (index * col_width) + (col_width / 2)
            parts.extend(self._render_ehm(value, cx, y, col_width))

        return parts

    def render_length_modifier(self, values, x, y, width):
        parts = []

        if not values:
            return parts

        count = len(values)
        col_width = width / count

        for index, value in enumerate(values):
            cx = x + (index * col_width) + (col_width / 2)
            parts.extend(self._render_elm(value, cx, y, col_width))

        return parts

    def _render_ehm(self, value, cx, y, col_width):
        if value in ("", "~"):
            return []

        prefix, base = _split_ehm_token(value)
        parts = self._render_base_ehm(base, cx, y, col_width)

        if prefix is not None and parts:
            symbol = self.prefix_symbols.get(prefix, prefix)
            # Position the prefix just to the left of the glyph's left edge.
            glyph_width = self._glyph_width(col_width, self.upper_width_factor, cap_factor=1.35)
            x_prefix = cx - glyph_width / 2 - 1.0
            # For stacked slashes, center the prefix vertically on the full stack.
            stack_count = (
                len(base)
                if base and len(set(base)) == 1 and set(base) <= {"/", "\\"}
                else 1
            )
            stack_gap = max(3.0, self.unit * 0.46)
            stack_center_y = y - (stack_count - 1) * stack_gap / 2
            parts = [self._text(symbol, x_prefix, stack_center_y + 4, anchor="end")] + parts

        return parts

    def _render_base_ehm(self, base, cx, y, col_width):
        """Render a base EHM (without any halftoon prefix)."""
        if base in ("", "~"):
            return []

        width = self._glyph_width(col_width, self.upper_width_factor, cap_factor=1.35)
        half_width = width / 2
        half_height = half_width * 0.45

        if base == "-":
            return [
                self._line(
                    cx - half_width,
                    y,
                    cx + half_width,
                    y,
                    color=self.upper_color,
                    stroke_width=self.upper_stroke_width,
                    css_class="vsa-glyph vsa-upper-glyph vsa-glyph-flat",
                )
            ]

        if set(base) == {"/"}:
            return self._stacked_slashes(
                cx,
                y,
                len(base),
                up=True,
                half_width=half_width,
                half_height=half_height,
            )

        if set(base) == {"\\"}:
            return self._stacked_slashes(
                cx,
                y,
                len(base),
                up=False,
                half_width=half_width,
                half_height=half_height,
            )

        return []

    def _render_elm(self, value, cx, y, col_width):
        if value in ["", "~", "-"]:
            return []

        width = self._glyph_width(col_width, self.lower_width_factor, cap_factor=1.45)
        half_width = width / 2

        if value == "_.":
            gap = self.unit * 0.35
            return [
                self._line(
                    cx - half_width,
                    y,
                    cx + half_width,
                    y,
                    color=self.lower_color,
                    stroke_width=self.lower_stroke_width,
                    css_class="vsa-glyph vsa-lower-glyph vsa-glyph-length",
                ),
                self._line(
                    cx - half_width,
                    y + gap,
                    cx,
                    y + gap,
                    color=self.lower_color,
                    stroke_width=self.lower_stroke_width,
                    css_class="vsa-glyph vsa-lower-glyph vsa-glyph-length",
                ),
            ]

        if set(value) == {"_"}:
            parts = []
            for index in range(len(value)):
                yy = y + index * (self.unit * 0.35)
                parts.append(
                    self._line(
                        cx - half_width,
                        yy,
                        cx + half_width,
                        yy,
                        color=self.lower_color,
                        stroke_width=self.lower_stroke_width,
                        css_class="vsa-glyph vsa-lower-glyph vsa-glyph-length",
                    )
                )
            return parts

        if set(value) == {"."}:
            r = max(1.5, self.unit * 0.20)
            dot_spacing = self.unit * 0.5           # center-to-center for ".."
            parts = []
            for index in range(len(value)):
                yy = y + index * dot_spacing
                parts.append(
                    f'<circle class="vsa-glyph vsa-lower-glyph vsa-glyph-dot" '
                    f'cx="{cx:.2f}" cy="{yy:.2f}" r="{r:.2f}" '
                    f'fill="{self.lower_color}" stroke="none"/>'
                )
            return parts

        return []

    def _glyph_width(self, col_width, factor, cap_factor):
        # Uniforme accentlengte: liever ongeveer één dikke letter breed dan
        # woordbreed. Bij heel smalle tekst blijft de glyph binnen de tekst.
        desired = col_width * factor
        cap = self.unit * cap_factor
        return max(1.0, min(col_width, desired, cap))

    def _stacked_slashes(self, cx, y, count, up, half_width, half_height):
        parts = []

        stack_gap = max(3.0, self.unit * 0.46)

        for index in range(count):
            yy = y - index * stack_gap

            if up:
                parts.append(
                    self._line(
                        cx - half_width,
                        yy + half_height,
                        cx + half_width,
                        yy - half_height,
                        color=self.upper_color,
                        stroke_width=self.upper_stroke_width,
                        css_class="vsa-glyph vsa-upper-glyph vsa-glyph-rise",
                    )
                )
            else:
                parts.append(
                    self._line(
                        cx - half_width,
                        yy - half_height,
                        cx + half_width,
                        yy + half_height,
                        color=self.upper_color,
                        stroke_width=self.upper_stroke_width,
                        css_class="vsa-glyph vsa-upper-glyph vsa-glyph-fall",
                    )
                )

        return parts

    def _line(self, x1, y1, x2, y2, color, stroke_width, css_class):
        return (
            f'<line class="{css_class}" '
            f'x1="{x1:.2f}" y1="{y1:.2f}" '
            f'x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{escape(color)}" stroke-width="{stroke_width:.2f}" '
            f'stroke-linecap="round"/>'
        )

    def _text(self, value, x, y, anchor="start"):
        anchor_attr = f' text-anchor="{anchor}"' if anchor != "start" else ""
        return (
            f'<text class="vsa-glyph-text" x="{x:.2f}" y="{y:.2f}" '
            f'xml:space="preserve"{anchor_attr} '
            f'font-family="Consolas" font-size="{self.unit * 2.0:.2f}">'
            f'{escape(value)}</text>'
        )
