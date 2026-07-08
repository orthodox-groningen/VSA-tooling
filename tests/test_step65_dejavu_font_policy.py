from pathlib import Path

from vsa.config import SVGRenderingConfig
from vsa.text_metrics import DEFAULT_FONT_FAMILY, get_font_metrics


def test_default_render_font_is_dejavu_sans():
    assert SVGRenderingConfig().font_family == "DejaVu Sans"
    assert DEFAULT_FONT_FAMILY == "DejaVu Sans"


def test_project_font_location_is_documented():
    assert Path("assets/fonts/README.md").exists()
    assert Path("docs/guides/rendering-fonts.md").exists()
    assert Path("licenses/DejaVu-Fonts.txt").exists()


def test_font_metrics_reports_font_path_field():
    metrics = get_font_metrics(20, "DejaVu Sans")

    assert hasattr(metrics, "font_path")
    assert metrics.backend in {"pillow", "fallback"}


def test_debug_font_metrics_script_exists():
    assert Path("scripts/debug-font-metrics.py").exists()
