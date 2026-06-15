from dataclasses import dataclass

from .text_metrics import (
    estimate_scope_text_width as _estimate_scope_text_width,
    estimate_text_width as _estimate_text_width,
)


MIN_GLYPH_CELL_WIDTH = 14.0


@dataclass
class ScopeColumn:
    ehm: str
    elm: str
    width: float


@dataclass
class ScopeLayout:
    text: str
    width: float
    columns: list[ScopeColumn]
    text_width: float = 0.0
    filler_width: float = 0.0


def build_scope_layout(
    node,
    minimum_column_width: float = MIN_GLYPH_CELL_WIDTH,
    text_font_size: float = 20.0,
    font_family: str = "Segoe UI",
):
    hm = node.height_modifier or []
    lm = node.length_modifier or []

    if not hm and not lm:
        hm = ["~"]
        lm = ["~"]
    elif hm and not lm:
        lm = ["~"] * len(hm)
    elif lm and not hm:
        hm = ["~"] * len(lm)

    count = max(len(hm), len(lm), 1)

    if len(hm) == 1 and count > 1:
        hm = hm * count

    if len(lm) == 1 and count > 1:
        lm = lm * count

    text = node.text
    text_width = estimate_scope_text_width(text, text_font_size, font_family=font_family)

    if count <= 1:
        grid_width = text_width
    else:
        grid_width = max(
            text_width + minimum_column_width,
            count * minimum_column_width,
        )

    column_width = grid_width / count
    filler_width = max(0.0, grid_width - text_width)

    columns = [
        ScopeColumn(
            ehm=hm[index],
            elm=lm[index],
            width=column_width,
        )
        for index in range(count)
    ]

    return ScopeLayout(
        text=text,
        width=round(grid_width, 2),
        columns=columns,
        text_width=round(text_width, 2),
        filler_width=round(filler_width, 2),
    )


def estimate_scope_text_width(text: str, font_size: float, font_family: str = "Segoe UI"):
    return _estimate_scope_text_width(text, font_size, font_family=font_family)


def estimate_text_width(
    text: str,
    font_size: float,
    preserve_whitespace: bool = True,
    font_family: str = "Segoe UI",
):
    return _estimate_text_width(
        text,
        font_size,
        preserve_whitespace=preserve_whitespace,
        font_family=font_family,
    )
