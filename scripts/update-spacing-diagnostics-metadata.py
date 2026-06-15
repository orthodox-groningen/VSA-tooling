from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsa.text_metrics import DEFAULT_FONT_FAMILY, estimate_text_width, get_font_metrics, using_real_font_metrics


PAGE = ROOT / "examples/hugo-demo/content-source/voorbeelden/rendering/spacing-diagnostiek.md"
START = "<!-- VSA-METRICS-START -->"
END = "<!-- VSA-METRICS-END -->"


def main():
    if not PAGE.exists():
        print(f"Niet gevonden: {PAGE}")
        raise SystemExit(1)

    metrics = get_font_metrics(20, DEFAULT_FONT_FAMILY)

    lines = [
        START,
        "## Metrics van deze build",
        "",
        "| Kenmerk | Waarde |",
        "|---|---|",
        f"| Font | `{DEFAULT_FONT_FAMILY}` |",
        f"| Backend | `{metrics.backend}` |",
        f"| Real metrics | `{using_real_font_metrics(20, DEFAULT_FONT_FAMILY)}` |",
        f"| Fontpad | `{metrics.font_path}` |",
        f"| Fontgrootte | `{metrics.font_size}` |",
        f"| Ascent | `{metrics.ascent}` |",
        f"| Descent | `{metrics.descent}` |",
        f"| Breedte `iiii` | `{estimate_text_width('iiii', 20)}` |",
        f"| Breedte `mmmm` | `{estimate_text_width('mmmm', 20)}` |",
        f"| Breedte `eeu` | `{estimate_text_width('eeu', 20)}` |",
        f"| Breedte `baard` | `{estimate_text_width('baard', 20)}` |",
        "",
        END,
    ]

    block = "\n".join(lines)

    text = PAGE.read_text(encoding="utf-8")

    if START in text and END in text:
        before = text.split(START, 1)[0]
        after = text.split(END, 1)[1]
        text = before + block + after
    else:
        insert_after = "# Spacing diagnostiek\n"
        text = text.replace(insert_after, insert_after + "\n" + block + "\n", 1)

    PAGE.write_text(text, encoding="utf-8")
    print(f"Metrics bijgewerkt in {PAGE}")


if __name__ == "__main__":
    main()
