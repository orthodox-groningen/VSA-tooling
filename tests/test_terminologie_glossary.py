from pathlib import Path
import re

import pytest


ROOT = Path(__file__).resolve().parents[1]
VSA_GLOSSARY = ROOT / "docs" / "glossary.md"
VSA_TERM = ROOT / "docs" / "terminologie" / "vsa.md"
ZANGSTUK_TERM = ROOT / "docs" / "terminologie" / "zangstuk.md"
CURSOR_RULE = ROOT / ".cursor" / "rules" / "orthodox-groningen-terminologie.mdc"

OPTIONAL_SIBLING_ORG_REPOS = (
    "catalogus",
    "heiligen",
    "koor",
    "materiaal-met-copyright",
    "paas-agenda-2025",
    "vow",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")


def resolve_bron_root() -> Path | None:
    """CI: vendor/bron; lokaal monorepo: ../bron."""
    for candidate in (ROOT / "vendor" / "bron", ROOT.parent / "bron"):
        if (candidate / "docs" / "specs" / "terminologie.md").is_file():
            return candidate.resolve()
    return None


def bron_root_or_skip() -> Path:
    root = resolve_bron_root()
    if root is None:
        pytest.skip("bron-checkout niet aanwezig (vendor/bron of sibling ../bron)")
    return root


def iter_repos_with_cursor_rule() -> list[tuple[str, Path]]:
    """Alleen repo's die daadwerkelijk aanwezig zijn (CI ≠ volledige monorepo)."""
    present: list[tuple[str, Path]] = [("VSA-tooling", ROOT)]
    bron = resolve_bron_root()
    if bron is not None:
        present.append(("bron", bron))
    org_root = ROOT.parent
    for repo in OPTIONAL_SIBLING_ORG_REPOS:
        path = org_root / repo
        if path.is_dir():
            present.append((repo, path))
    return present


def test_bron_has_normative_glossary_with_usage_rules():
    bron = bron_root_or_skip()
    glossary = bron / "docs" / "specs" / "terminologie.md"
    text = read(glossary)
    # TermRefs mogen om termen staan; controleer de keten in platte tekst.
    plain = re.sub(r"\[([^\]]+)\]\(@[^)]*\)", r"\1", text)
    for needle in (
        "**Status:** normatief",
        "## 0. Gebruiksregels",
        "**R1 — gedefinieerde term**",
        "Zangstuk → variant → uitvoeringsvorm → representatie",
        "`uitvoeringsvorm-id`",
        "Niet dupliceren",
    ):
        haystack = plain if "→" in needle else text
        assert needle in haystack, f"missing in bron glossary: {needle!r}"


def test_vsa_terminologie_is_local_tev2_glossary_not_bron_copy():
    text = read(VSA_GLOSSARY) + read(VSA_TERM)
    assert '{% hrg="vsa-tooling" %}' in text
    assert "Vereenvoudigde Slavische Accentnotatie" in text
    assert "[VSA](@bron)" in text or "[vsa](@bron)" in text.lower()
    assert (ROOT / "docs" / "terminologie" / "bracket-directive.md").is_file()
    assert "## 0. Gebruiksregels" not in text
    assert "**Status:** normatief" not in text


def test_zangstuk_term_is_local_and_bron_glossary_remains_external():
    text = read(ZANGSTUK_TERM)
    assert "een inhoudelijk afgebakend gezang of muzikale tekst" in text
    assert text.count("| Niveau |") == 0

    bron = bron_root_or_skip()
    bron_glossary = read(bron / "docs" / "specs" / "terminologie.md")
    assert "Zangstuk" in bron_glossary


def test_documentatie_eigendom_in_bron():
    bron = bron_root_or_skip()
    doc = read(bron / "docs" / "specs" / "documentatie-eigendom.md")
    assert "**D1 — één bron**" in doc
    assert "VSA-tooling" in doc


def test_docs_avoid_deprecated_terminology():
    offenders = []
    deprecated = [
        re.compile(r"\buv-id\b"),
        re.compile(r"uitvoeringsalternatief", re.I),
        re.compile(r"variant-id:\s*standaard", re.I),
        re.compile(r"russisch-klomp", re.I),
    ]
    for path in (ROOT / "docs").rglob("*.md"):
        text = read(path)
        for pattern in deprecated:
            if pattern.search(text):
                offenders.append(f"{path.relative_to(ROOT)}: {pattern.pattern}")
    assert offenders == []


def test_cursor_terminologie_rule_in_present_org_repos():
    missing = []
    for repo, base in iter_repos_with_cursor_rule():
        rule = base / ".cursor" / "rules" / "orthodox-groningen-terminologie.mdc"
        if not rule.is_file():
            missing.append(repo)
            continue
        text = read(rule)
        if "bron/docs/specs/terminologie.md" not in text:
            missing.append(f"{repo} (bad content)")
    assert missing == [], f"missing or invalid cursor rule: {missing}"


def test_vsa_cursor_rule_forbids_uv_abbreviation():
    text = read(CURSOR_RULE)
    assert "afkorting `uv`" in text or "`uv`" in text
