from pathlib import Path


BUILD = Path("scripts/build-hugo.cmd")
LINE = "python scripts\\update-spacing-diagnostics-metadata.py"


def main():
    if BUILD.exists():
        text = BUILD.read_text(encoding="utf-8")
        if LINE not in text:
            marker = "[2/4] Generate Markdown + SVG"
            if marker in text:
                text = text.replace(
                    f"echo {marker}",
                    f"echo {marker}\r\n{LINE}",
                    1,
                )
            else:
                text = text + f"\r\n{LINE}\r\n"
            BUILD.write_text(text, encoding="utf-8")
            print(f"Aangepast: {BUILD}")
        else:
            print(f"Al aanwezig in: {BUILD}")
    else:
        print(f"Niet gevonden: {BUILD}")

    print("Werk metricsblok nu bij:")
    print(LINE)


if __name__ == "__main__":
    main()
