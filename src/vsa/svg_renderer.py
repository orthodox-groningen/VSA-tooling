from xml.sax.saxutils import escape

from .ast import TextNode, ScopeNode, PitchMarkerNode
from .svg_glyphs import SVGGlyphRenderer
from .scope_layout import build_scope_layout, estimate_text_width
from .svg_layout_measure import measure_document_width


class SVGRenderer:
    def __init__(self):
        self.height = 190
        self.font_family = "Segoe UI"
        self.glyphs = SVGGlyphRenderer(unit=12)

    def render_document(self, document):
        width = measure_document_width(document)

        x = 40.0
        baseline_y = 110.0

        parts = []

        parts.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width:.0f}" height="{self.height}" '
            f'viewBox="0 0 {width:.0f} {self.height}">'
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

        return x + estimate_text_width(text, 20)

    def _render_scope(self, parts, node, x, baseline_y):
        layout = build_scope_layout(node)

        running_x = x

        for column in layout.columns:
            parts.extend(
                self.glyphs.render_height_modifier(
                    [column.ehm],
                    running_x,
                    baseline_y - 38,
                    column.width,
                )
            )

            parts.extend(
                self.glyphs.render_length_modifier(
                    [column.elm],
                    running_x,
                    baseline_y + 18,
                    column.width,
                )
            )

            running_x += column.width

        parts.append(
            f'<text x="{x:.2f}" y="{baseline_y:.2f}" '
            f'font-family="{self.font_family}" font-size="20">'
            f'{escape(layout.text)}</text>'
        )

        return x + layout.width + 4

    def _render_pitch_marker(self, parts, node, x, baseline_y):
        width = max(34.0, max(len(node.height_modifier), 1) * 28.0)

        if node.height_modifier:
            column_width = width / len(node.height_modifier)

            for index, ehm in enumerate(node.height_modifier):
                parts.extend(
                    self.glyphs.render_height_modifier(
                        [ehm],
                        x + index * column_width,
                        baseline_y - 38,
                        column_width,
                    )
                )

        parts.append(
            f'<line x1="{x:.2f}" y1="{baseline_y - 8:.2f}" '
            f'x2="{x + width:.2f}" y2="{baseline_y - 8:.2f}" '
            f'stroke="black" stroke-width="2"/>'
        )

        return x + width + 8
