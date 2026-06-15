from pathlib import Path

from vsa.parser import Parser
from vsa.svg_line_layout import build_lines
from vsa.markdown_newline_policy import preserve_vsa_source_newlines


def test_preserve_vsa_source_newlines_normalizes_without_joining():
    source = "eerste\r\ntweede\rderde"

    assert preserve_vsa_source_newlines(source) == "eerste\ntweede\nderde"


def test_renderer_layout_respects_preserved_physical_lines():
    source = preserve_vsa_source_newlines(
        "[:] Uit {/de} {/ho}{/ge} zijt {\\Gij}\n"
        "Drie {/da}{/gen} {/zijt} Gij {\\in}\n"
        "Gij {/zijt} {/ons} {/le}ven [:]"
    )

    document = Parser(source).parse()
    lines = build_lines(document, max_width=2000)

    assert len(lines) == 3


def test_pipeline_sources_do_not_replace_newlines_with_spaces():
    offenders = []

    for path in Path("src/vsa").glob("*.py"):
        text = path.read_text(encoding="utf-8")
        if '.replace("\\n", " ")' in text or ".replace('\\n', ' ')" in text:
            offenders.append(str(path))

    assert offenders == []


def test_pipeline_sources_do_not_join_vsa_lines_with_space():
    offenders = []

    suspicious = [
        '" ".join(lines)',
        "' '.join(lines)",
        '" ".join(block_lines)',
        "' '.join(block_lines)",
        '" ".join(vsa_lines)',
        "' '.join(vsa_lines)",
        '" ".join(source_lines)',
        "' '.join(source_lines)",
    ]

    for path in Path("src/vsa").glob("*.py"):
        text = path.read_text(encoding="utf-8")
        if any(pattern in text for pattern in suspicious):
            offenders.append(str(path))

    assert offenders == []
