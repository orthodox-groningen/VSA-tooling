from dataclasses import dataclass


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
    text_width = estimate_scope_text_width(text, text_font_size)

    if count <= 1:
        grid_width = text_width
    else:
        # Multi-EHM/ELM scopes hebben ruimte nodig voor afzonderlijke glyphs.
        # Daarom krijgt zo'n scope minstens count * minimum_column_width,
        # plus een kleine rechterbuffer zodat de filler-line zichtbaar kan zijn.
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
        width=grid_width,
        columns=columns,
        text_width=text_width,
        filler_width=filler_width,
    )


def estimate_scope_text_width(text: str, font_size: float):
    if text == "":
        return max(4.0, font_size * 0.25)

    return round(max(4.0, len(text) * font_size * 0.55), 2)


def estimate_text_width(text: str, font_size: float, preserve_whitespace: bool = True):
    if text == "":
        return 0.0

    visible = text if preserve_whitespace else text.strip()

    if visible == "":
        return 0.0

    return round(len(visible) * font_size * 0.55, 2)
