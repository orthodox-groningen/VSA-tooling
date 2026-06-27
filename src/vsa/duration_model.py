"""
Maps VSA ELM (Enkelvoudige Lengte-Modifier) strings to MusicXML
:class:`~vsa.music.Duration` objects.

The default mapping is specified in VSA-spec §8.2.5::

    ELM  → MusicXML duration
    ~    → kwartnoot  (quarter)
    -    → kwartnoot  (quarter)
    _    → halve noot (half)
    _.   → anderhalve noot (dotted half)
    __   → hele noot  (whole)
    .    → achtste noot (eighth)
    ..   → zestiende noot (16th)

Additional ``duration-model`` values may be registered in the future.
"""

from __future__ import annotations

from .music import Duration


# Default mapping: ELM string → Duration
_DEFAULT_MODEL: dict[str, Duration] = {
    "~":  Duration(note_type="quarter", dots=0),
    "-":  Duration(note_type="quarter", dots=0),
    "_":  Duration(note_type="half",    dots=0),
    "_.": Duration(note_type="half",    dots=1),
    "__": Duration(note_type="whole",   dots=0),
    ".":  Duration(note_type="eighth",  dots=0),
    "..": Duration(note_type="16th",    dots=0),
}

_MODELS: dict[str, dict[str, Duration]] = {
    "default": _DEFAULT_MODEL,
}


class UnknownDurationModel(ValueError):
    pass


class UnknownELM(ValueError):
    pass


def elm_to_duration(elm: str, model: str = "default") -> Duration:
    """Return the :class:`~vsa.music.Duration` for a given ELM string.

    :param elm: The ELM string, e.g. ``"_"``, ``"~"``, ``"_."``.
    :param model: The duration model name (default: ``"default"``).
    :raises UnknownDurationModel: If the model name is not registered.
    :raises UnknownELM: If the ELM string has no mapping in the model.
    """
    try:
        mapping = _MODELS[model]
    except KeyError:
        raise UnknownDurationModel(
            f"Onbekend duration-model: '{model}'. "
            f"Beschikbare modellen: {sorted(_MODELS)}"
        )

    try:
        return mapping[elm]
    except KeyError:
        raise UnknownELM(
            f"Onbekende ELM '{elm}' in model '{model}'. "
            f"Geldige waarden: {sorted(mapping)}"
        )
