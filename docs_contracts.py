import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
GUIDES = DOCS / "guides"
REFERENCE = DOCS / "reference"
SPECIFICATION = DOCS / "specification"
ARCHITECTURE = DOCS / "architecture"
HISTORY = DOCS / "history"
ADDENDA = HISTORY / "addenda"
PARSER_STEPS = HISTORY / "parser-steps"
TERMINOLOGIE = DOCS / "terminologie"

# TEv2 TermRefs: [showtext](@), [showtext](@bron), [showtext](term@), …
_TERMREF_RE = re.compile(r"\[([^\]]+)\]\([^)\n]*@[a-z0-9_:-]*\)", re.IGNORECASE)


CANONICAL_DOCS = {
    "architecture_parser": ARCHITECTURE / "parser.md",
    "architecture_rendering": ARCHITECTURE / "rendering.md",
    "cli_reference": REFERENCE / "cli.md",
    "cli_spec": SPECIFICATION / "cli.md",
    "config_reference": REFERENCE / "config.md",
    "diagnostics_reference": REFERENCE / "diagnostics.md",
    "outputs_reference": REFERENCE / "outputs.md",
    "quick_start_guide": GUIDES / "quick-start.md",
    "rendering_fonts_guide": GUIDES / "rendering-fonts.md",
    "rendering_spec": SPECIFICATION / "rendering.md",
    "syntax_spec": SPECIFICATION / "syntax.md",
    "todo_addendum": ADDENDA / "todo.md",
    "validation_guide": GUIDES / "validation.md",
    "validation_spec": SPECIFICATION / "validation.md",
}


def doc(name: str) -> Path:
    return CANONICAL_DOCS[name]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _read_cli_reference_bundle() -> str:
    parts = [read(REFERENCE / "cli.md")]
    cli_dir = REFERENCE / "cli"
    if cli_dir.is_dir():
        for path in sorted(cli_dir.glob("*.md")):
            parts.append(read(path))
    return "\n".join(parts)


def read_doc(name: str) -> str:
    if name == "cli_reference":
        return _read_cli_reference_bundle()
    return read(doc(name))


def read_docs(*names: str) -> str:
    return "\n".join(read_doc(name) for name in names)


def plain_docs_text(text: str) -> str:
    """Replace TEv2 TermRefs with their showtext for content-contract matching."""
    return _TERMREF_RE.sub(r"\1", text)


def assert_terms(text: str, terms: list[str] | tuple[str, ...]) -> None:
    plain = plain_docs_text(text)
    missing = [term for term in terms if term not in text and term not in plain]
    assert missing == [], missing
