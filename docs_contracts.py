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


def read_doc(name: str) -> str:
    return read(doc(name))


def read_docs(*names: str) -> str:
    return "\n".join(read_doc(name) for name in names)


def assert_terms(text: str, terms: list[str] | tuple[str, ...]) -> None:
    missing = [term for term in terms if term not in text]
    assert missing == []
