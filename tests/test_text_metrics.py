from vsa.text_metrics import estimate_scope_text_width, estimate_text_width


def test_narrow_text_is_narrower_than_wide_text():
    assert estimate_text_width("iiii", 20) < estimate_text_width("mmmm", 20)


def test_space_width_is_preserved():
    assert estimate_text_width(" ", 20) > 0


def test_scope_text_width_has_small_safety_margin():
    assert estimate_scope_text_width("de", 20) > estimate_text_width("de", 20)


def test_eeu_is_wider_than_old_too_compact_guess_for_three_letters():
    assert estimate_text_width("eeu", 20) >= 30
