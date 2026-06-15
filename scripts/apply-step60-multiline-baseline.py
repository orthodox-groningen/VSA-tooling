from pathlib import Path

TARGETS = [
    Path("src/vsa/svg_renderer.py"),
    Path("src/vsa/svg_multiline_renderer.py"),
    Path("src/vsa/svg_line_layout.py"),
]

MARKER = "# step60 multiline baseline debug"

def main():
    changed = []

    for path in TARGETS:
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8")

        if MARKER not in text:
            text += "\n\n" + MARKER + "\n"
            path.write_text(text, encoding="utf-8")
            changed.append(path)

    print("Stap 60 apply")
    if changed:
        for path in changed:
            print(f"- aangepast: {path}")
    else:
        print("Geen wijzigingen nodig.")

if __name__ == "__main__":
    main()
