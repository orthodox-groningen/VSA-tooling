from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ORG_ROOT = ROOT.parent
BRON_GLOSSARY = ORG_ROOT / "bron" / "docs" / "specs" / "terminologie.md"
VSA_STUB = ROOT / "docs" / "specs" / "terminologie.md"
CURSOR_RULE = ROOT / ".cursor" / "rules" / "orthodox-groningen-terminologie.mdc"

ORG_REPOS = [
    "bron",
    "catalogus",
    "heiligen",
    "koor",
    "materiaal-met-copyright",
    "paas-agenda-2025",
    "vow",
    "VSA-tooling",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")


def test_bron_has_normative_glossary_with_usage_rules():
    text = read(BRON_GLOSSARY)
    assert BRON_GLOSSARY.is_file()
    for needle in (
        "**Status:** normatief",
        "## 0. Gebruiksregels",
        "**R1 — gedefinieerde term**",
        "Zangstuk → variant → uitvoeringsvorm → representatie",
        "`uitvoeringsvorm-id`",
        "Niet dupliceren",
    ):
        assert needle in text, f"missing in bron glossary: {needle!r}"


def test_vsa_terminologie_is_stub_not_full_copy():
    text = read(VSA_STUB)
    assert "github.com/orthodox-groningen/bron" in text
    assert "stub" in text.lower()
    assert "## 0. Gebruiksregels" not in text
    assert len(text.splitlines()) < 30


def test_zangstuk_identificatie_points_to_bron():
    index = read(ROOT / "docs" / "zangstuk-identificatie.md")
    assert "orthodox-groningen/bron" in index
    assert index.count("| Niveau |") == 0


def test_documentatie_eigendom_in_bron():
    doc = read(ORG_ROOT / "bron" / "docs" / "specs" / "documentatie-eigendom.md")
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


def test_cursor_terminologie_rule_in_all_org_repos():
    missing = []
    for repo in ORG_REPOS:
        rule = ORG_ROOT / repo / ".cursor" / "rules" / "orthodox-groningen-terminologie.mdc"
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
