from __future__ import annotations

from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsa.text_metrics import DEFAULT_FONT_FAMILY, estimate_text_width, get_font_metrics, using_real_font_metrics


START = "<!-- VSA-METRICS-START -->"
END = "<!-- VSA-METRICS-END -->"
DEFAULT_PAGE = Path("generated/hugo/content/voorbeelden/rendering/spacing-diagnostiek.md")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update spacing diagnostics metrics block.")
    parser.add_argument("page", nargs="?", default=str(DEFAULT_PAGE))
    args = parser.parse_args()

    page = Path(args.page)
    if not page.is_absolute():
        page = ROOT / page

    if not page.exists():
        print(f"Niet gevonden: {page}")
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
    text = page.read_text(encoding="utf-8")

    if START in text and END in text:
        before = text.split(START, 1)[0]
        after = text.split(END, 1)[1]
        text = before + block + after
    else:
        text = text.rstrip() + "\n\n" + block + "\n"

    page.write_text(text, encoding="utf-8")
    print(f"Metrics bijgewerkt in {page}")


if __name__ == "__main__":
    main()
