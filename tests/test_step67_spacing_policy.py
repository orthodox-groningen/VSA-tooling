from pathlib import Path

from vsa.spacing_policy import filler_line_geometry, whitespace_width
from vsa.text_metrics import estimate_text_width


def test_whitespace_has_minimum_visual_width():
    assert whitespace_width(" ", 20) >= 10.0


def test_whitespace_is_wider_than_raw_metric_when_needed():
    assert whitespace_width(" ", 20) >= estimate_text_width(" ", 20)


def test_filler_line_is_shorter_than_reserved_width():
    start, end = filler_line_geometry(10, 90, 80, 20)

    assert end - start < 80
    assert end - start <= 36


def test_spacing_diagnostics_metadata_script_exists():
    assert Path("scripts/update-spacing-diagnostics-metadata.py").exists()
