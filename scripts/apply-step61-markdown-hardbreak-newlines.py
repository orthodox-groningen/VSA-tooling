from pathlib import Path

TARGETS = [
    Path("src/vsa/markdown_newline_policy.py"),
    Path("src/vsa/markdown_vsa_blocks.py"),
    Path("src/vsa/svg_line_layout.py"),
]

def main():
    print("Stap 61 is file-based toegepast via de zip.")
    print("Controleer met:")
    print("python -m pytest tests\\test_svg_step61_markdown_hardbreaks.py -v")
    for path in TARGETS:
        print(f"- {path}: {'OK' if path.exists() else 'ONTBREEKT'}")

if __name__ == "__main__":
    main()
