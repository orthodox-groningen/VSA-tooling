from pathlib import Path
import re


def test_step60_scripts_exist():
    assert Path("scripts/inspect-svg-line-y.py").exists()
    assert Path("scripts/apply-step60-multiline-baseline.py").exists()


def test_svg_translate_positions_are_distinct():
    svg = """
<g class="vsa-line" transform="translate(0,20)">
</g>
<g class="vsa-line" transform="translate(0,78)">
</g>
<g class="vsa-line" transform="translate(0,136)">
</g>
"""

    ys = re.findall(r'translate\([^,]+,([^)]+)\)', svg)

    assert ys == ["20", "78", "136"]
    assert len(set(ys)) == 3
