from xml.sax.saxutils import escape

from .ast import TextNode, ScopeNode, PitchMarkerNode


class SVGRenderer:
    def __init__(self):
        self.width = 1200
        self.height = 160
        self.font_family = "Segoe UI"
        self.mono_family = "Consolas"

    def render_document(self, document):
        x = 40
        baseline_y = 85

        parts = []

        parts.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{self.width}" height="{self.height}">'
        )

        parts.append('<rect width="100%" height="100%" fill="white"/>')

        for node in document.nodes:
            if isinstance(node, TextNode):
                x = self._render_text(parts, node.text, x, baseline_y)

            elif isinstance(node, ScopeNode):
                x = self._render_scope(parts, node, x, baseline_y)

            elif isinstance(node, PitchMarkerNode):
                x = self._render_pitch_marker(parts, node, x, baseline_y)

        parts.append("</svg>")

        return "\n".join(parts)

    def render(self, positions):
        """
        Backwards compatible fallback voor oudere tests.
        Rendert alleen musical positions, zonder gewone TextNodes.
        """
        from .ast import Document, ScopeNode

        nodes = [
            ScopeNode(
                height_modifier=[position.ehm],
                text=position.text,
                length_modifier=[position.elm],
            )
            for position in positions
        ]

        return self.render_document(Document(nodes=nodes))

    def _render_text(self, parts, text, x, baseline_y):
        if text == "":
            return x

        safe = escape(text)

        parts.append(
            f'<text x="{x}" y="{baseline_y}" '
            f'font-family="{self.font_family}" font-size="20">'
            f'{safe}</text>'
        )

        return x + self._estimate_text_width(text, 20)

    def _render_scope(self, parts, node, x, baseline_y):
        text_width = self._estimate_text_width(node.text, 20)
        modifier_count = max(len(node.height_modifier), len(node.length_modifier), 1)
        scope_width = max(text_width, modifier_count * 24)

        center_x = x + scope_width / 2

        if node.height_modifier:
            glyph = "&".join(node.height_modifier)
            parts.append(
                f'<text x="{center_x}" y="{baseline_y - 28}" '
                f'text-anchor="middle" '
                f'font-family="{self.mono_family}" font-size="16">'
                f'{escape(glyph)}</text>'
            )

        parts.append(
            f'<text x="{x}" y="{baseline_y}" '
            f'font-family="{self.font_family}" font-size="20">'
            f'{escape(node.text)}</text>'
        )

        if node.length_modifier:
            glyph = "&".join(node.length_modifier)
            parts.append(
                f'<text x="{center_x}" y="{baseline_y + 26}" '
                f'text-anchor="middle" '
                f'font-family="{self.mono_family}" font-size="16">'
                f'{escape(glyph)}</text>'
            )

        return x + scope_width + 4

    def _render_pitch_marker(self, parts, node, x, baseline_y):
        width = 30

        if node.height_modifier:
            glyph = "&".join(node.height_modifier)
            parts.append(
                f'<text x="{x + width / 2}" y="{baseline_y - 28}" '
                f'text-anchor="middle" '
                f'font-family="{self.mono_family}" font-size="16">'
                f'{escape(glyph)}</text>'
            )

        parts.append(
            f'<line x1="{x}" y1="{baseline_y - 8}" '
            f'x2="{x + width}" y2="{baseline_y - 8}" '
            f'stroke="black" stroke-width="2"/>'
        )

        return x + width + 8

    def _estimate_text_width(self, text, font_size):
        # Eenvoudige schatting; later vervangen door echte layout.
        return max(8, len(text) * font_size * 0.55)
