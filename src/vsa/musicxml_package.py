"""Write MusicXML output as plain XML (``.musicxml``) or compressed MXL (``.mxl``)."""

from __future__ import annotations

import zipfile
from pathlib import Path

_MXL_CONTAINER = """\
<?xml version="1.0" encoding="UTF-8"?>
<container>
  <rootfiles>
    <rootfile full-path="score.xml"/>
  </rootfiles>
</container>
"""

_MXL_SUFFIX = ".mxl"
_MUSICXML_SUFFIX = ".musicxml"

_KNOWN_SUFFIXES = frozenset({_MXL_SUFFIX, _MUSICXML_SUFFIX, ".xml"})


def musicxml_output_suffix(*, format_name: str | None = None, path: Path | None = None) -> str:
    """Return ``.mxl`` (default) or ``.musicxml`` from *format_name* or *path*."""
    if path is not None:
        suffix = path.suffix.lower()
        if suffix == _MXL_SUFFIX:
            return _MXL_SUFFIX
        if suffix in (_MUSICXML_SUFFIX, ".xml"):
            return _MUSICXML_SUFFIX
    if format_name == "musicxml":
        return _MUSICXML_SUFFIX
    return _MXL_SUFFIX


def write_musicxml_output(path: Path, xml: str) -> None:
    """Write *xml* to *path* as ``.musicxml`` or ``.mxl`` (ZIP with ``score.xml``)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() == _MXL_SUFFIX:
        _write_mxl(path, xml)
    else:
        path.write_text(xml, encoding="utf-8")


def _write_mxl(path: Path, xml: str) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("META-INF/container.xml", _MXL_CONTAINER)
        archive.writestr("score.xml", xml)
