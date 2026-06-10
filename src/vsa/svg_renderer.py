from xml.sax.saxutils import escape

from .ast import TextNode, ScopeNode, PitchMarkerNode
from .svg_glyphs import SVGGlyphRenderer


class SVGRenderer:
    def __init__(self):
        self.width = 1200
        self.height = 180
        self.font_family = "Segoe UI"
        self.glyphs = SVGGlyphRenderer(unit=12)

    def render_document(self, document):
        x = 40
        baseline_y = 105

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

        parts.append(
            f'<text x="{x:.2f}" y="{baseline_y:.2f}" '
            f'font-family="{self.font_family}" font-size="20">'
            f'{escape(text)}</text>'
        )

        return x + self._estimate_text_width(text, 20)

    def _render_scope(self, parts, node, x, baseline_y):
        text_width = self._estimate_text_width(node.text, 20)
        modifier_count = max(len(node.height_modifier), len(node.length_modifier), 1)
        scope_width = max(text_width, modifier_count * 28)

        parts.extend(
            self.glyphs.render_height_modifier(
                node.height_modifier,
                x,
                baseline_y - 34,
                scope_width,
            )
        )

        parts.append(
            f'<text x="{x:.2f}" y="{baseline_y:.2f}" '
            f'font-family="{self.font_family}" font-size="20">'
            f'{escape(node.text)}</text>'
        )

        parts.extend(
            self.glyphs.render_length_modifier(
                node.length_modifier,
                x,
                baseline_y + 18,
                scope_width,
            )
        )

        return x + scope_width + 4

    def _render_pitch_marker(self, parts, node, x, baseline_y):
        width = 34

        parts.extend(
            self.glyphs.render_height_modifier(
                node.height_modifier,
                x,
                baseline_y - 34,
                width,
            )
        )

        parts.append(
            f'<line x1="{x:.2f}" y1="{baseline_y - 8:.2f}" '
            f'x2="{x + width:.2f}" y2="{baseline_y - 8:.2f}" '
            f'stroke="black" stroke-width="2"/>'
        )

        return x + width + 8

    def _estimate_text_width(self, text, font_size):
        return max(8, len(text) * font_size * 0.55)
