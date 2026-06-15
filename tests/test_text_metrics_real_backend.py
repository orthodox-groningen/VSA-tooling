from vsa.text_metrics import (
    estimate_scope_text_width,
    estimate_text_width,
    get_font_metrics,
    using_real_font_metrics,
)


def test_font_metrics_backend_is_reported():
    metrics = get_font_metrics(20, "Segoe UI")

    assert metrics.backend in {"pillow", "fallback"}
    assert metrics.ascent > 0
    assert metrics.descent >= 0


def test_text_width_is_positive():
    assert estimate_text_width("eeu", 20) > 0


def test_wide_text_is_wider_than_narrow_text():
    assert estimate_text_width("mmmm", 20) > estimate_text_width("iiii", 20)


def test_scope_text_width_keeps_safety_margin():
    assert estimate_scope_text_width("baard", 20) > estimate_text_width("baard", 20)


def test_real_font_metrics_detection_returns_boolean():
    assert isinstance(using_real_font_metrics(20, "Segoe UI"), bool)
