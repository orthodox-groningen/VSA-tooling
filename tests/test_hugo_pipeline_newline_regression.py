from pathlib import Path
import subprocess
import sys


def test_step58_apply_script_exists():
    assert Path("scripts/apply-step58-real-pipeline-newlines.py").exists()


def test_tone8_like_source_has_three_render_lines_at_layout_level():
    from vsa.parser import Parser
    from vsa.svg_line_layout import build_lines

    source = (
        "[:] Uit {/de} {/ho}{/ge} zijt {\\Gij} neergedaald\n"
        "Drie {/da}{/gen} {/zijt} Gij {\\in} het graf\n"
        "Gij {/zijt} {/ons} {/le}ven [:]"
    )

    lines = build_lines(Parser(source).parse(), max_width=3000)

    assert len(lines) == 3
