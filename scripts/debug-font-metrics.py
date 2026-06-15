from vsa.text_metrics import (
    DEFAULT_FONT_FAMILY,
    estimate_text_width,
    get_font_metrics,
    using_real_font_metrics,
)


def main():
    metrics = get_font_metrics(20, DEFAULT_FONT_FAMILY)

    print("VSA font metrics debug")
    print(f"default font : {DEFAULT_FONT_FAMILY}")
    print(f"backend      : {metrics.backend}")
    print(f"font path    : {metrics.font_path}")
    print(f"ascent       : {metrics.ascent}")
    print(f"descent      : {metrics.descent}")
    print(f"real metrics : {using_real_font_metrics(20, DEFAULT_FONT_FAMILY)}")
    print()
    for text in ["iiii", "mmmm", "eeu", "baard", "schon", "DejaVu Sans"]:
        print(f"{text!r}: {estimate_text_width(text, 20)}")


if __name__ == "__main__":
    main()
