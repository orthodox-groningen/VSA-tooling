from pathlib import Path
import re


TARGETS = [
    Path("src/vsa/markdown_processor.py"),
    Path("src/vsa/markdown_builder.py"),
    Path("src/vsa/shortcode_output.py"),
    Path("src/vsa/site_build.py"),
    Path("src/vsa/site_builder.py"),
    Path("src/vsa/hugo.py"),
    Path("src/vsa/hugo_demo.py"),
    Path("src/vsa/demo_pages.py"),
    Path("src/vsa/cli.py"),
]


REPLACEMENTS = [
    ('" ".join(lines)', '"\\n".join(lines)'),
    ("' '.join(lines)", "'\\n'.join(lines)"),
    ('" ".join(block_lines)', '"\\n".join(block_lines)'),
    ("' '.join(block_lines)", "'\\n'.join(block_lines)"),
    ('" ".join(vsa_lines)', '"\\n".join(vsa_lines)'),
    ("' '.join(vsa_lines)", "'\\n'.join(vsa_lines)"),
    ('" ".join(source_lines)', '"\\n".join(source_lines)'),
    ("' '.join(source_lines)", "'\\n'.join(source_lines)"),
    ('.replace("\\n", " ")', ''),
    (".replace('\\n', ' ')", ''),
    ('.replace("\\r\\n", " ")', '.replace("\\r\\n", "\\n")'),
    (".replace('\\r\\n', ' ')", ".replace('\\r\\n', '\\n')"),
    ('.replace("\\r", " ")', '.replace("\\r", "\\n")'),
    (".replace('\\r', ' ')", ".replace('\\r', '\\n')"),
]


def patch_file(path: Path) -> bool:
    if not path.exists():
        return False

    text = path.read_text(encoding="utf-8")
    original = text

    for old, new in REPLACEMENTS:
        text = text.replace(old, new)

    # Specifieke markdown fence extractors gebruiken soms splitlines()
    # en daarna join met spatie via tijdelijke variabelen. Voeg een lichte
    # bescherming toe: als er Parser(...) in dezelfde file staat, normaliseer
    # CR/CRLF naar LF vlak vóór Parser-aanroepen.
    if "Parser(" in text and "preserve_vsa_source_newlines" not in text:
        text = (
            "from .markdown_newline_policy import preserve_vsa_source_newlines\n"
            + text
            if "from .markdown_newline_policy import preserve_vsa_source_newlines" not in text
            else text
        )

        text = re.sub(
            r"Parser\((?P<expr>[a-zA-Z_][a-zA-Z0-9_]*)\)",
            r"Parser(preserve_vsa_source_newlines(\g<expr>))",
            text,
        )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True

    return False


def main():
    changed = []

    for path in TARGETS:
        if patch_file(path):
            changed.append(path)

    print("Stap 58 pipeline newline patch")
    if changed:
        print("Aangepast:")
        for path in changed:
            print(f"- {path}")
    else:
        print("Geen automatische wijzigingen gevonden.")
        print("Zoek handmatig naar join/replace-normalisatie in src/vsa.")

    print()
    print("Controlecommando's:")
    print('findstr /s /n /c:"join(lines)" src\\vsa\\*.py')
    print('findstr /s /n /c:"replace(\\"\\\\n\\", \\" \\")" src\\vsa\\*.py')
    print('python -m pytest tests\\test_real_pipeline_newlines.py -v')


if __name__ == "__main__":
    main()
