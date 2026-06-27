"""Build Coria play URLs for hosted MusicXML/MXL files."""

from __future__ import annotations

from urllib.parse import quote

CORIA_PLAY_BASE = "https://coria.nl/play_from_url"
DEFAULT_CORIA_BACK = "coria.nl"


def coria_play_url(
    score_url: str,
    *,
    back: str = DEFAULT_CORIA_BACK,
) -> str:
    """Return a Coria URL that opens *score_url* in the part-selection screen.

    *score_url* must be an absolute HTTPS URL to a ``.mxl`` or ``.musicxml``
    file that Coria can fetch (publicly reachable; localhost does not work).

    Coria endpoint documented in the wild as::

        https://coria.nl/play_from_url?back=coria.nl&url=<encoded-url>
    """
    return (
        f"{CORIA_PLAY_BASE}?back={quote(back, safe='')}"
        f"&url={quote(score_url, safe='')}"
    )
