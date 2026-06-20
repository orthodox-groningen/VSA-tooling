"""Tests for halftoon-prefix EHM tokens (#, b and their aliases).

Design decisions verified here:
- '#' (kruis) and 'b' (mol) are the canonical prefix symbols.
- '+' and '♯' are aliases for '#'; '♭' is an alias for 'b'.
- A halftoon-prefix is only valid when immediately followed by a base-EHM
  (/, //, \, \\, -, ~, etc.) — never standalone.
- zangelement-char is unchanged: 'b', '#', '♭', '♯' may appear in
  zangelement text when not immediately followed by a base-EHM.
"""

import pytest

from vsa.parser import (
    BASE_EHM_VALUES,
    EHM_VALUES,
    HALFTOON_CANONICAL,
    HALFTOON_PREFIXES,
    Parser,
)
from vsa.svg_glyphs import DEFAULT_PREFIX_SYMBOLS, SVGGlyphRenderer, _split_ehm_token


# ---------------------------------------------------------------------------
# Parser constants
# ---------------------------------------------------------------------------


class TestEhmValuesStructure:
    def test_base_ehm_values_excludes_old_atomic_tokens(self):
        assert "+/" not in BASE_EHM_VALUES
        assert "-\\" not in BASE_EHM_VALUES

    def test_ehm_values_contains_all_canonical_prefix_base_combinations(self):
        for base in BASE_EHM_VALUES:
            for prefix in ["#", "b"]:
                assert prefix + base in EHM_VALUES, f"Missing: {prefix + base!r}"

    def test_ehm_values_contains_alias_combinations(self):
        for base in BASE_EHM_VALUES:
            for alias in ["+", "♯", "♭"]:
                assert alias + base in EHM_VALUES, f"Missing alias: {alias + base!r}"

    def test_ehm_values_sorted_longest_first(self):
        for i in range(len(EHM_VALUES) - 1):
            assert len(EHM_VALUES[i]) >= len(EHM_VALUES[i + 1])

    def test_halftoon_canonical_covers_all_prefixes(self):
        assert set(HALFTOON_CANONICAL.keys()) == set(HALFTOON_PREFIXES)

    def test_halftoon_canonical_maps_to_hash_or_b(self):
        assert set(HALFTOON_CANONICAL.values()) == {"#", "b"}


# ---------------------------------------------------------------------------
# Parser: canonical prefix + base combinations
# ---------------------------------------------------------------------------


class TestParserKruisPrefix:
    """'#' prefix (and aliases '+', '♯') on single-slash base."""

    def test_hash_slash(self):
        node = Parser("{#/tekst}").parse().nodes[0]
        assert node.height_modifier == ["#/"]
        assert node.text == "tekst"

    def test_plus_slash_alias(self):
        node = Parser("{+/tekst}").parse().nodes[0]
        assert node.height_modifier == ["+/"]
        assert node.text == "tekst"

    def test_sharp_slash_alias(self):
        node = Parser("{♯/tekst}").parse().nodes[0]
        assert node.height_modifier == ["♯/"]
        assert node.text == "tekst"

    def test_hash_backslash(self):
        node = Parser("{#\\tekst}").parse().nodes[0]
        assert node.height_modifier == ["#\\"]
        assert node.text == "tekst"

    def test_plus_backslash_alias(self):
        node = Parser("{+\\tekst}").parse().nodes[0]
        assert node.height_modifier == ["+\\"]
        assert node.text == "tekst"

    def test_hash_dash(self):
        node = Parser("{#-tekst}").parse().nodes[0]
        assert node.height_modifier == ["#-"]
        assert node.text == "tekst"

    def test_hash_tilde(self):
        node = Parser("{#~tekst}").parse().nodes[0]
        assert node.height_modifier == ["#~"]
        assert node.text == "tekst"

    def test_hash_double_slash(self):
        node = Parser("{#//tekst}").parse().nodes[0]
        assert node.height_modifier == ["#//"]
        assert node.text == "tekst"


class TestParserMolPrefix:
    """'b' prefix (and alias '♭') on various base EHMs."""

    def test_b_slash(self):
        node = Parser("{b/tekst}").parse().nodes[0]
        assert node.height_modifier == ["b/"]
        assert node.text == "tekst"

    def test_flat_slash_alias(self):
        node = Parser("{♭/tekst}").parse().nodes[0]
        assert node.height_modifier == ["♭/"]
        assert node.text == "tekst"

    def test_b_backslash(self):
        node = Parser("{b\\tekst}").parse().nodes[0]
        assert node.height_modifier == ["b\\"]
        assert node.text == "tekst"

    def test_b_dash(self):
        node = Parser("{b-tekst}").parse().nodes[0]
        assert node.height_modifier == ["b-"]
        assert node.text == "tekst"

    def test_b_tilde(self):
        node = Parser("{b~tekst}").parse().nodes[0]
        assert node.height_modifier == ["b~"]
        assert node.text == "tekst"

    def test_b_double_backslash(self):
        node = Parser("{b\\\\tekst}").parse().nodes[0]
        assert node.height_modifier == ["b\\\\"]
        assert node.text == "tekst"


# ---------------------------------------------------------------------------
# Parser: zangelement-char not affected
# ---------------------------------------------------------------------------


class TestZangelementCharUnchanged:
    """'b' and '#' must remain valid zangelement chars when not followed by
    a base-EHM character."""

    def test_b_in_zangelement_no_modifier(self):
        node = Parser("{bloktekst}").parse().nodes[0]
        assert node.height_modifier == []
        assert node.text == "bloktekst"

    def test_b_in_zangelement_with_height_modifier(self):
        node = Parser("{/bloktekst}").parse().nodes[0]
        assert node.height_modifier == ["/"]
        assert node.text == "bloktekst"

    def test_hash_in_zangelement_no_modifier(self):
        node = Parser("{#tekst}").parse().nodes[0]
        assert node.height_modifier == []
        assert node.text == "#tekst"

    def test_b_at_end_of_zangelement(self):
        node = Parser("{tekstb}").parse().nodes[0]
        assert node.height_modifier == []
        assert node.text == "tekstb"

    def test_word_starting_with_b_not_followed_by_base(self):
        """'bidt' must parse as plain zangelement, not mol + 'idt'."""
        node = Parser("{bidt}").parse().nodes[0]
        assert node.height_modifier == []
        assert node.text == "bidt"


# ---------------------------------------------------------------------------
# Parser: compound modifiers containing halftoon prefix
# ---------------------------------------------------------------------------


class TestParserCompoundWithHalftoon:
    def test_compound_backslash_and_plus_backslash(self):
        """{\&+\tekst_&_} — compound height modifier with a halftoon prefix."""
        node = Parser("{\\&+\\tekst_&_}").parse().nodes[0]
        assert node.height_modifier == ["\\", "+\\"]
        assert node.text == "tekst"
        assert node.length_modifier == ["_", "_"]

    def test_halftoon_in_pitch_marker(self):
        doc = Parser("[+\\:]").parse()
        assert doc.nodes[0].height_modifier == ["+\\"]


# ---------------------------------------------------------------------------
# SVG: _split_ehm_token helper
# ---------------------------------------------------------------------------


class TestSplitEhmToken:
    def test_no_prefix(self):
        assert _split_ehm_token("/") == (None, "/")
        assert _split_ehm_token("//") == (None, "//")
        assert _split_ehm_token("\\") == (None, "\\")
        assert _split_ehm_token("-") == (None, "-")
        assert _split_ehm_token("~") == (None, "~")

    def test_canonical_kruis_prefix(self):
        assert _split_ehm_token("#/") == ("#", "/")
        assert _split_ehm_token("#\\") == ("#", "\\")
        assert _split_ehm_token("#-") == ("#", "-")
        assert _split_ehm_token("#//") == ("#", "//")

    def test_alias_kruis_normalized_to_hash(self):
        assert _split_ehm_token("+/") == ("#", "/")
        assert _split_ehm_token("♯/") == ("#", "/")
        assert _split_ehm_token("+\\") == ("#", "\\")

    def test_canonical_mol_prefix(self):
        assert _split_ehm_token("b/") == ("b", "/")
        assert _split_ehm_token("b\\") == ("b", "\\")
        assert _split_ehm_token("b-") == ("b", "-")

    def test_alias_mol_normalized_to_b(self):
        assert _split_ehm_token("♭/") == ("b", "/")
        assert _split_ehm_token("♭\\") == ("b", "\\")

    def test_single_char_not_split(self):
        """A single char like '#' alone must not be split."""
        assert _split_ehm_token("#") == (None, "#")


# ---------------------------------------------------------------------------
# SVG: DEFAULT_PREFIX_SYMBOLS
# ---------------------------------------------------------------------------


class TestDefaultPrefixSymbols:
    def test_kruis_renders_as_plus(self):
        assert DEFAULT_PREFIX_SYMBOLS["#"] == "+"

    def test_mol_renders_as_flat(self):
        assert DEFAULT_PREFIX_SYMBOLS["b"] == "♭"


class TestSVGRendererPrefixSymbols:
    def test_default_symbols_used(self):
        renderer = SVGGlyphRenderer()
        assert renderer.prefix_symbols == DEFAULT_PREFIX_SYMBOLS

    def test_custom_symbols_override(self):
        custom = {"#": "♯", "b": "b"}
        renderer = SVGGlyphRenderer(prefix_symbols=custom)
        assert renderer.prefix_symbols == custom

    def test_render_kruis_slash_produces_plus_text(self):
        renderer = SVGGlyphRenderer(unit=10.0)
        parts = renderer._render_ehm("#/", cx=50, y=20, col_width=20)
        assert any("+" in p for p in parts), "Expected '+' text glyph for '#/'"
        assert any("line" in p for p in parts), "Expected a rising-slash line for '#/'"

    def test_render_mol_slash_produces_flat_text(self):
        renderer = SVGGlyphRenderer(unit=10.0)
        parts = renderer._render_ehm("b/", cx=50, y=20, col_width=20)
        assert any("♭" in p for p in parts), "Expected '♭' text glyph for 'b/'"

    def test_render_plus_backslash_alias(self):
        renderer = SVGGlyphRenderer(unit=10.0)
        parts = renderer._render_ehm("+\\", cx=50, y=20, col_width=20)
        assert any("+" in p for p in parts), "Expected '+' text glyph for '+\\'"
        assert any("fall" in p for p in parts), "Expected a falling-slash line for '+\\'"

    def test_render_base_ehm_no_prefix(self):
        renderer = SVGGlyphRenderer(unit=10.0)
        parts = renderer._render_ehm("/", cx=50, y=20, col_width=20)
        assert not any("text" in p for p in parts), "Plain '/' must not produce prefix text"
        assert any("rise" in p for p in parts)

    def test_render_tilde_empty(self):
        renderer = SVGGlyphRenderer(unit=10.0)
        assert renderer._render_ehm("~", cx=50, y=20, col_width=20) == []
