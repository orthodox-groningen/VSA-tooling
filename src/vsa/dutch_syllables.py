"""Nederlandse lettergrepen voor reciteer-tekst (één syllabe = één kwart)."""

from __future__ import annotations

import re

_VOWELS = set("aeiouyáéíóúäëïöüÿ")
_DIPHTHONGS = (
    "aa",
    "ee",
    "oo",
    "uu",
    "ae",
    "ai",
    "au",
    "ei",
    "eu",
    "ie",
    "ij",
    "oe",
    "oi",
    "ou",
    "ui",
)
_ONSETS = (
    "sch",
    "ch",
    "ck",
    "ng",
    "nk",
    "qu",
    "th",
    "ph",
    "st",
    "sp",
    "sl",
    "sm",
    "sn",
    "sk",
    "sf",
    "tr",
    "dr",
    "kr",
    "gr",
    "pr",
    "br",
    "fr",
    "vr",
    "pl",
    "bl",
    "kl",
    "fl",
    "gl",
    "cl",
    "tw",
    "dw",
    "kw",
    "zw",
)
_PUNCT_TRAIL = re.compile(r"^(.*?)(\W*)$", re.UNICODE)


def recite_syllables(token: str) -> list[tuple[str, str]]:
    """Splits een ongemarkeerd woord in (lyric, syllabic) voor reciteerkwarten.

    Bestaande koppeltekens in VSA (`voor-beeld`) blijven leidend.
    """
    match = _PUNCT_TRAIL.match(token)
    core, punct = (match.group(1), match.group(2)) if match else (token, "")
    if not core:
        return [(token, "single")]
    if "-" in core:
        parts = [p for p in core.split("-") if p]
    else:
        parts = split_dutch_word(core)
    if not parts:
        return [(token, "single")]
    if punct:
        parts[-1] = parts[-1] + punct
    return _with_syllabic(parts)


def split_dutch_word(word: str) -> list[str]:
    """Onset-maximalisatie tussen klinkerkernen (diftonen blijven bijeen)."""
    if len(word) <= 2:
        return [word]
    nuclei = _nuclei(word.lower())
    if len(nuclei) <= 1:
        return [word]
    cuts: list[int] = []
    for (_, end_a), (start_b, _) in zip(nuclei, nuclei[1:]):
        cluster = word[end_a:start_b]
        keep = _onset_len(cluster.lower())
        cuts.append(start_b - keep)
    parts: list[str] = []
    prev = 0
    for cut in cuts:
        if cut <= prev:
            continue
        parts.append(word[prev:cut])
        prev = cut
    parts.append(word[prev:])
    return [p for p in parts if p]


def _nuclei(word: str) -> list[tuple[int, int]]:
    found: list[tuple[int, int]] = []
    i = 0
    while i < len(word):
        if word[i : i + 2] in _DIPHTHONGS:
            found.append((i, i + 2))
            i += 2
            continue
        if word[i] in _VOWELS:
            found.append((i, i + 1))
        i += 1
    return found


_UNBREAKABLE = ("sch", "ch")


def _onset_len(cluster: str) -> int:
    """Hoeveel medeklinkers horen bij de volgende syllabe."""
    if not cluster:
        return 0
    for chunk in _UNBREAKABLE:
        if cluster.endswith(chunk):
            return len(chunk)
    for onset in _ONSETS:
        if cluster.endswith(onset) and len(cluster) > len(onset):
            return len(onset)
    return 1


def _with_syllabic(parts: list[str]) -> list[tuple[str, str]]:
    if len(parts) == 1:
        return [(parts[0], "single")]
    out: list[tuple[str, str]] = []
    for i, part in enumerate(parts):
        if i == 0:
            out.append((part, "begin"))
        elif i == len(parts) - 1:
            out.append((part, "end"))
        else:
            out.append((part, "middle"))
    return out
