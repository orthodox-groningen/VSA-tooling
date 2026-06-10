from dataclasses import dataclass, field
from pathlib import Path

from .block_parser import parse_markdown_blocks
from .parser import Parser
from .semantic_validator import SemanticValidator
from .recoverable_syntax_validator import RecoverableSyntaxValidator
from .errors import VSAError


@dataclass
class ValidationMessage:
    source: str
    code: str
    message_nl: str
    line: int = 1
    column: int = 1


@dataclass
class ValidationResult:
    ok: bool = True
    messages: list[ValidationMessage] = field(default_factory=list)

    def add_error(self, source: str, code: str, message_nl: str, line: int = 1, column: int = 1):
        self.ok = False
        self.messages.append(
            ValidationMessage(
                source=source,
                code=code,
                message_nl=message_nl,
                line=line,
                column=column,
            )
        )


def validate_file(path: str | Path) -> ValidationResult:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    result = ValidationResult()

    if path.suffix.lower() in [".md", ".markdown"]:
        _validate_markdown(path, text, result)
    else:
        _validate_vsa_text(str(path), text, result)

    return result


def _validate_markdown(path: Path, text: str, result: ValidationResult):
    try:
        blocks = parse_markdown_blocks(text)
    except VSAError as exc:
        result.add_error(
            source=str(path),
            code="VSA-BLOCK-PARSE-ERROR",
            message_nl=str(exc),
        )
        return

    for index, block in enumerate(blocks, start=1):
        source = f"{path}:blok-{index}"
        _validate_vsa_text(source, block.body, result)


def _validate_vsa_text(source: str, text: str, result: ValidationResult):
    syntax_diagnostics = RecoverableSyntaxValidator(text).validate()

    for diagnostic in syntax_diagnostics.items:
        result.add_error(
            source=source,
            code=diagnostic.code,
            message_nl=diagnostic.message_nl,
            line=diagnostic.line,
            column=diagnostic.column,
        )

    if syntax_diagnostics.has_errors():
        return

    try:
        document = Parser(text).parse()
    except VSAError as exc:
        result.add_error(
            source=source,
            code="VSA-PARSE-ERROR",
            message_nl=str(exc),
        )
        return

    diagnostics = SemanticValidator(document).validate()

    for diagnostic in diagnostics.items:
        result.add_error(
            source=source,
            code=diagnostic.code,
            message_nl=diagnostic.message_nl,
            line=diagnostic.line,
            column=diagnostic.column,
        )
