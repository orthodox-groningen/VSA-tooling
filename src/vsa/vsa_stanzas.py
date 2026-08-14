"""VSA-tekst → noten per tekstregel (`*` / `**` als frasegrens)."""

from __future__ import annotations

from dataclasses import dataclass, replace

from .ast import Document, PitchMarkerNode, ScopeNode, TextNode
from .dutch_syllables import recite_syllables
from .duration_model import elm_to_duration
from .music import Duration, Pitch
from .musicxml_renderer import _PUNCT_ONLY_RE
from .parser import Parser
from .pitch_resolver import PitchResolver
from .yaml_frontmatter import parse_vsa_frontmatter

_STANZA_MARKERS = frozenset({"*", "**"})


@dataclass(frozen=True)
class VsaNote:
    lyric: str
    pitch: Pitch
    duration: Duration
    scoped: bool
    syllabic: str = "single"
    ehm: str = "~"
    elm: str = "~"


def parse_vsa_source(text: str) -> tuple[dict, Document]:
    """Frontmatter + AST. Frontmatter-sleutels (do/mode) worden strings."""
    meta, body = parse_vsa_frontmatter(text)
    flat = {str(k): str(v) for k, v in meta.items()}
    return flat, Parser(body).parse()


def extract_stanza_notes(
    text: str,
    *,
    metadata: dict[str, str] | None = None,
) -> list[list[VsaNote]]:
    """Eén lijst noten per VSA-regel (frase).

    Lettergrepen die in VSA aan elkaar geplakt zijn (``{En_}gel``,
    ``pro{fe_}{\\ten_}``) vormen één woord → begin/middle/end voor streepjes.
    Spaties (en strofe-markers) breken het woord.
    """
    file_meta, document = parse_vsa_source(text)
    meta = dict(file_meta)
    if metadata:
        meta.update(metadata)
    resolver = PitchResolver.from_metadata(meta)
    duration_model = meta.get("duration-model", "default")
    for node in document.nodes:
        if isinstance(node, PitchMarkerNode):
            resolver.apply_start_marker(node.ehm)
            break
    stanzas: list[list[VsaNote]] = []
    current: list[VsaNote] = []
    word: list[VsaNote] = []

    def flush_word() -> None:
        if not word:
            return
        current.extend(_with_word_syllabics(word))
        word.clear()

    def close_stanza() -> None:
        flush_word()
        if current:
            stanzas.append(list(current))
            current.clear()

    def append_punct(token: str) -> None:
        """Leesteken plakt aan de laatste lettergreep met tekst."""
        target = word if word else current
        for i in range(len(target) - 1, -1, -1):
            if target[i].lyric:
                target[i] = replace(target[i], lyric=target[i].lyric + token)
                return

    for node in document.nodes:
        if isinstance(node, PitchMarkerNode):
            continue
        if isinstance(node, TextNode):
            _consume_text(
                node.text,
                resolver=resolver,
                duration_model=duration_model,
                word=word,
                flush_word=flush_word,
                close_stanza=close_stanza,
                append_punct=append_punct,
            )
            continue
        if isinstance(node, ScopeNode):
            hm = node.height_modifier or ["~"]
            lm = node.length_modifier or ["~"]
            if len(hm) > 1 and len(lm) == 1:
                lm = lm * len(hm)
            if len(lm) > 1 and len(hm) == 1:
                hm = hm * len(lm)
            n_pos = len(hm)
            for i, (ehm, elm) in enumerate(zip(hm, lm)):
                pitch = resolver.resolve_ehm(ehm)
                dur = elm_to_duration(elm, model=duration_model)
                lyric = node.text if i == 0 else ""
                syllabic = "single"
                if n_pos > 1:
                    if i == 0:
                        syllabic = "begin"
                    elif i == n_pos - 1:
                        syllabic = "end"
                    else:
                        syllabic = "middle"
                word.append(
                    VsaNote(
                        lyric=lyric,
                        pitch=pitch,
                        duration=dur,
                        scoped=True,
                        syllabic=syllabic,
                        ehm=ehm,
                        elm=elm,
                    )
                )
            continue
    close_stanza()
    return stanzas


def _consume_text(
    text: str,
    *,
    resolver: PitchResolver,
    duration_model: str,
    word: list[VsaNote],
    flush_word,
    close_stanza,
    append_punct,
) -> None:
    """Spaties breken woorden; tokens zonder voorafgaande spatie plakken aan het woord."""
    i = 0
    n = len(text)
    while i < n:
        if text[i].isspace():
            flush_word()
            i += 1
            continue
        j = i
        while j < n and not text[j].isspace():
            j += 1
        token = text[i:j]
        i = j
        if token in _STANZA_MARKERS:
            flush_word()
            close_stanza()
            continue
        if _PUNCT_ONLY_RE.match(token):
            append_punct(token)
            continue
        pitch = resolver.current_pitch
        dur = elm_to_duration("~", model=duration_model)
        for lyric, _syllabic in recite_syllables(token):
            word.append(
                VsaNote(
                    lyric=lyric,
                    pitch=pitch,
                    duration=dur,
                    scoped=False,
                )
            )


def _with_word_syllabics(notes: list[VsaNote]) -> list[VsaNote]:
    """Zet begin/middle/end op lettergrepen mét tekst binnen één woord."""
    lyric_idxs = [i for i, note in enumerate(notes) if note.lyric]
    if len(lyric_idxs) <= 1:
        return list(notes)
    out = list(notes)
    n_lyric = len(lyric_idxs)
    for rank, idx in enumerate(lyric_idxs):
        if rank == 0:
            syl = "begin"
        elif rank == n_lyric - 1:
            syl = "end"
        else:
            syl = "middle"
        out[idx] = replace(out[idx], syllabic=syl)
    return out
