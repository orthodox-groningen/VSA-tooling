from xml.sax.saxutils import escape


class SVGGlyphRenderer:
    def __init__(self, unit: int = 10):
        self.unit = unit
        self.stroke_width = max(1, unit / 8)

    def render_height_modifier(self, values, x, y, width):
        parts = []

        if not values:
            return parts

        count = len(values)
        col_width = width / count

        for index, value in enumerate(values):
            cx = x + (index * col_width) + (col_width / 2)
            parts.extend(self._render_ehm(value, cx, y))

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

    def _render_ehm(self, value, cx, y):
        if value == "~":
            return []

        if value == "-":
            return [
                self._line(cx - self.unit / 2, y, cx + self.unit / 2, y)
            ]

        if value == "+/":
            return [
                self._text("+", cx - self.unit, y + 4),
                self._line(cx - self.unit / 2, y + self.unit / 2, cx + self.unit / 2, y - self.unit / 2),
            ]

        if value == "-\\":
            return [
                self._line(cx - self.unit, y, cx - self.unit / 4, y),
                self._line(cx - self.unit / 2, y - self.unit / 2, cx + self.unit / 2, y + self.unit / 2),
            ]

        if set(value) == {"/"}:
            return self._stacked_slashes(cx, y, len(value), up=True)

        if set(value) == {"\\"}:
            return self._stacked_slashes(cx, y, len(value), up=False)

        return []

    def _render_elm(self, value, cx, y, col_width):
        if value in ["~", "-"]:
            return []

        if set(value) == {"_"}:
            parts = []
            for index in range(len(value)):
                yy = y + index * (self.unit / 2)
                parts.append(
                    self._line(cx - col_width * 0.35, yy, cx + col_width * 0.35, yy)
                )
            return parts

        if set(value) == {"."}:
            parts = []
            for index in range(len(value)):
                yy = y + index * (self.unit / 2)
                parts.append(
                    f'<circle cx="{cx:.2f}" cy="{yy:.2f}" r="{self.unit / 8:.2f}" fill="black"/>'
                )
            return parts

        return []

    def _stacked_slashes(self, cx, y, count, up):
        parts = []

        for index in range(count):
            yy = y - index * self.unit

            if up:
                parts.append(
                    self._line(cx - self.unit / 2, yy + self.unit / 2, cx + self.unit / 2, yy - self.unit / 2)
                )
            else:
                parts.append(
                    self._line(cx - self.unit / 2, yy - self.unit / 2, cx + self.unit / 2, yy + self.unit / 2)
                )

        return parts

    def _line(self, x1, y1, x2, y2):
        return (
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" '
            f'x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="black" stroke-width="{self.stroke_width:.2f}" '
            f'stroke-linecap="round"/>'
        )

    def _text(self, value, x, y):
        return (
            f'<text x="{x:.2f}" y="{y:.2f}" '
            f'font-family="Consolas" font-size="{self.unit * 1.2:.2f}">'
            f'{escape(value)}</text>'
        )
