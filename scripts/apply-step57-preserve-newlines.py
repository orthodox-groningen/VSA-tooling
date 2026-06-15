from pathlib import Path


CANDIDATES = [
    Path("src/vsa/markdown_processor.py"),
    Path("src/vsa/markdown_builder.py"),
    Path("src/vsa/shortcode_output.py"),
    Path("src/vsa/site_build.py"),
    Path("src/vsa/hugo.py"),
    Path("src/vsa/hugo_demo.py"),
]


REPLACEMENTS = {
    '" ".join(lines)': '"\\n".join(lines)',
    "' '.join(lines)": "'\\n'.join(lines)",
    '" ".join(block_lines)': '"\\n".join(block_lines)',
    "' '.join(block_lines)": "'\\n'.join(block_lines)",
    '" ".join(vsa_lines)': '"\\n".join(vsa_lines)',
    "' '.join(vsa_lines)": "'\\n'.join(vsa_lines)",
}


def main():
    changed = []

    for path in CANDIDATES:
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8")
        original = text

        for old, new in REPLACEMENTS.items():
            text = text.replace(old, new)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(str(path))

    if changed:
        print("Aangepast:")
        for path in changed:
            print(f"- {path}")
    else:
        print("Geen verdachte join-normalisaties gevonden.")

    print("Controleer VSA-block newlines met:")
    print("python -m pytest tests\\test_markdown_vsa_block_newlines.py -v")


if __name__ == "__main__":
    main()
