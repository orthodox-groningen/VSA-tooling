"""VSA→template-instance: VSA-S-noten → template-events; A/T/B lopen synchroon mee."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .music import Duration, Pitch
from .pitch_resolver import PitchResolver, degree_to_pitch
from .template_mapping import assign_stanzas_to_phrases, select_mapping_plan
from .vsa_stanzas import VsaNote, extract_stanza_notes

_DEGREE_RE = re.compile(r"^(#|b)?(do|re|mi|fa|sol|la|ti)([+-][1-3])?$")
_DEGREE_ORDER = ("do", "re", "mi", "fa", "sol", "la", "ti")
_STEP_SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

CODE_PITCH_MISMATCH = "VSA-TEMPLATE-PITCH-MISMATCH"
CODE_REQUIRED_SKIPPED = "VSA-TEMPLATE-REQUIRED-SLOT-SKIPPED"
CODE_REQUIRED_UNUSED = "VSA-TEMPLATE-REQUIRED-SLOT-UNUSED"


class TemplateInstanceError(Exception):
    """VSA-regel past niet op de template-frase (rijke diagnostiek, vgl. vsa validate)."""

    def __init__(
        self,
        message_nl: str,
        *,
        code: str = "VSA-TEMPLATE-MAPPING",
        hint_nl: str = "",
        source: str = "",
        line: int = 0,
        column: int = 0,
        phrase_id: str = "",
        lyric: str = "",
        note_index: int | None = None,
    ) -> None:
        super().__init__(message_nl)
        self.code = code
        self.message_nl = message_nl
        self.hint_nl = hint_nl
        self.source = source
        self.line = line
        self.column = column
        self.phrase_id = phrase_id
        self.lyric = lyric
        self.note_index = note_index

    def location_label(self) -> str:
        name = Path(self.source).name if self.source else ""
        if name and self.line > 0:
            col = self.column if self.column > 0 else 1
            return f"{name}:{self.line}:{col}"
        if name:
            return name
        parts: list[str] = []
        if self.phrase_id:
            parts.append(f"frase {self.phrase_id!r}")
        if self.note_index is not None:
            parts.append(f"syllabe {self.note_index + 1}")
        if self.lyric:
            parts.append(f"lyric {self.lyric!r}")
        return ", ".join(parts) if parts else "(mapping)"

    def format_compact(self) -> str:
        """Korte regel zoals `vsa validate --summary`."""
        return f"{self.location_label()}: {self.code}"

    def format_lines(self, *, summary: bool = False, source_line: str | None = None) -> list[str]:
        """Uitgebreide of compacte weergave (zelfde geest als `format_validation_message`)."""
        if summary:
            return [self.format_compact()]
        lines = [
            self.location_label(),
            f"ERROR: {self.code}: {self.message_nl}",
        ]
        if source_line is not None and self.column > 0:
            lines.append(source_line)
            lines.append(" " * max(0, self.column - 1) + "^")
        if self.hint_nl:
            lines.append(f"Hint: {self.hint_nl}")
        return lines


@dataclass(frozen=True)
class MappedNote:
    lyric: str
    duration: Duration
    s_pitch: Pitch
    template_event: dict[str, Any]
    syllabic: str = "single"
    show_anchor: bool = False


def midi_of(pitch: Pitch) -> int:
    return 12 * (pitch.octave + 1) + _STEP_SEMI[pitch.step] + int(pitch.alter)


def degree_pitch(degree: str, do: str, mode: str) -> Pitch:
    match = _DEGREE_RE.match(degree)
    if not match:
        raise TemplateInstanceError(
            f"ongeldige laddergraad: {degree!r}",
            code="VSA-TEMPLATE-BAD-DEGREE",
            hint_nl="Gebruik een laddergraad zoals mi, #do of sol-1 in template.yaml.",
        )
    chrom, name, oct_off = match.group(1), match.group(2), match.group(3)
    resolver = PitchResolver.from_metadata({"do": do, "mode": mode})
    idx = _DEGREE_ORDER.index(name)
    shift = int(oct_off) if oct_off else 0
    pitch = degree_to_pitch(resolver._do, idx + 7 * shift, resolver._intervals)
    if chrom == "#":
        return Pitch(step=pitch.step, octave=pitch.octave, alter=pitch.alter + 1)
    if chrom == "b":
        return Pitch(step=pitch.step, octave=pitch.octave, alter=pitch.alter - 1)
    return pitch


def pitches_match(vsa: Pitch, degree: str, do: str, mode: str) -> bool:
    return midi_of(vsa) == midi_of(degree_pitch(degree, do, mode))


def split_phrase_events(
    events: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any] | None, list[dict[str, Any]]]:
    recite_at = next((i for i, ev in enumerate(events) if ev.get("role") == "recite"), None)
    if recite_at is None:
        return list(events), None, []
    return events[:recite_at], events[recite_at], events[recite_at + 1 :]


def map_stanza(
    notes: list[VsaNote],
    phrase: dict[str, Any],
    *,
    do: str,
    mode: str,
    source: str = "",
) -> list[MappedNote]:
    """Koppel één VSA-regel aan de events van één template-frase (H1, H4–H8)."""
    phrase_id = str(phrase.get("id", "?"))
    if not notes:
        raise TemplateInstanceError(
            f"lege VSA-regel voor frase {phrase_id!r}",
            code="VSA-TEMPLATE-EMPTY-STANZA",
            hint_nl="Voeg gezongen tekst toe of verwijder de lege frase uit de toewijzing.",
            source=source,
            phrase_id=phrase_id,
        )
    events = list(phrase.get("events") or [])
    if not events:
        raise TemplateInstanceError(
            f"frase {phrase_id!r} heeft geen events",
            code="VSA-TEMPLATE-EMPTY-PHRASE",
            hint_nl="Vul events in template.yaml voor deze frase.",
            source=source,
            phrase_id=phrase_id,
        )
    prefix, recite, tail = split_phrase_events(events)
    index = 0
    out: list[MappedNote] = []

    for event in prefix:
        index = _take_prefix_event(notes, index, event, out, do, mode)

    if recite is not None:
        while index < len(notes) and not notes[index].scoped:
            out.append(_assign(notes[index], recite, show_anchor=False))
            index += 1
        if not any(n.template_event is recite for n in out) and index < len(notes):
            # Geen ongemarkeerde recite-syllaben: recite-slot overslaan.
            pass

    _map_tail(
        notes,
        index,
        tail,
        out,
        do,
        mode,
        phrase_id=phrase_id,
        source=source,
    )
    return out


def map_vsa_to_template(
    template: dict[str, Any],
    vsa_text: str,
    *,
    source: str = "",
) -> list[tuple[str, list[MappedNote]]]:
    """Volledige instance-mapping: tekstregels → (frase-id, mapped notes)."""
    do = str(template["do"])
    mode = str(template.get("mode", "major"))
    stanzas = extract_stanza_notes(vsa_text, metadata={"do": do, "mode": mode})
    plan = select_mapping_plan(template, len(stanzas))
    phrase_ids = assign_stanzas_to_phrases(plan, len(stanzas))
    by_id = {str(p["id"]): p for p in template["phrases"]}
    mapped: list[tuple[str, list[MappedNote]]] = []
    for pid, notes in zip(phrase_ids, stanzas, strict=True):
        if pid not in by_id:
            raise TemplateInstanceError(
                f"onbekende frase-id {pid!r}",
                code="VSA-TEMPLATE-UNKNOWN-PHRASE",
                hint_nl="Controleer cycle/final in template.yaml t.o.v. het aantal VSA-regels.",
                source=source,
                phrase_id=pid,
            )
        mapped.append(
            (pid, map_stanza(notes, by_id[pid], do=do, mode=mode, source=source))
        )
    return mapped


def _take_prefix_event(
    notes: list[VsaNote],
    index: int,
    event: dict[str, Any],
    out: list[MappedNote],
    do: str,
    mode: str,
) -> int:
    if index >= len(notes):
        return index
    # H1: ongemarkeerde syllaben vallen op recite, niet op prefix (open/link).
    if not notes[index].scoped:
        return index
    matches = pitches_match(notes[index].pitch, event["pitches"]["S"], do, mode)
    if not matches:
        return index
    out.append(_assign(notes[index], event, show_anchor=True))
    return index + 1


def _slot_label(event: dict[str, Any]) -> str:
    degree = str(event.get("pitches", {}).get("S", "?"))
    bits = [degree]
    if event.get("anchor"):
        bits.append(str(event["anchor"]))
    if event.get("optional"):
        bits.append("optional")
    return "/".join(bits)


def _map_tail(
    notes: list[VsaNote],
    index: int,
    tail: list[dict[str, Any]],
    out: list[MappedNote],
    do: str,
    mode: str,
    *,
    phrase_id: str,
    source: str = "",
) -> None:
    event_i = 0
    llgr_from: int | None = next(
        (i for i, ev in enumerate(tail) if ev.get("anchor") == "l.lgr."),
        None,
    )

    def _pitch_mismatch(note: VsaNote, note_i: int, *, remaining: list[dict[str, Any]]) -> TemplateInstanceError:
        got = f"{note.pitch}"
        expected = [
            str(ev.get("pitches", {}).get("S"))
            for ev in remaining
            if not ev.get("optional")
        ]
        lyric = note.lyric or "(melisma)"
        expected_txt = ", ".join(expected) if expected else "—"
        return TemplateInstanceError(
            f"hoogte-mismatch: VSA {lyric!r} = {got}, geen passend template-S-slot "
            f"meer (verwacht o.a. {expected_txt})",
            code=CODE_PITCH_MISMATCH,
            hint_nl=(
                "Pas de VSA-hoogtemarkeringen aan zodat ze de verplichte cadensgraden "
                "van de template volgen, of kies een andere frase/cadenspad."
            ),
            source=source,
            phrase_id=phrase_id,
            lyric=lyric,
            note_index=note_i,
        )

    def _required_skipped(
        note: VsaNote,
        note_i: int,
        *,
        skipped: list[dict[str, Any]],
        matched: dict[str, Any],
    ) -> TemplateInstanceError:
        lyric = note.lyric or "(melisma)"
        skipped_txt = ", ".join(_slot_label(ev) for ev in skipped)
        return TemplateInstanceError(
            f"verplicht template-slot overgeslagen: VSA {lyric!r} = {note.pitch} "
            f"koppelt aan later slot {_slot_label(matched)}, maar slaat verplicht(e) "
            f"tussenslot(s) over ({skipped_txt})",
            code=CODE_REQUIRED_SKIPPED,
            hint_nl=(
                "Neem de overgeslagen toon(en) mee in de VSA (eigen syllabe of hold), "
                "óf markeer die template-events als optional: true als ze op het blad "
                "tussen haakjes staan."
            ),
            source=source,
            phrase_id=phrase_id,
            lyric=lyric,
            note_index=note_i,
        )

    last_consumed_degree: str | None = None

    while index < len(notes):
        note = notes[index]
        if event_i >= len(tail):
            if not out:
                raise TemplateInstanceError(
                    f"cadensnoten zonder template-tail in frase {phrase_id!r}",
                    code="VSA-TEMPLATE-NO-TAIL",
                    hint_nl="Controleer of de frase cadence-events na recite heeft.",
                    source=source,
                    phrase_id=phrase_id,
                    lyric=note.lyric or "",
                    note_index=index,
                )
            last = out[-1].template_event
            if pitches_match(note.pitch, last["pitches"]["S"], do, mode):
                # H6: extra syllabe opzelfde slot-akkoord.
                out.append(_assign(note, last, show_anchor=False))
                index += 1
                continue
            raise _pitch_mismatch(note, index, remaining=[])
        try:
            matched = _next_matching_event(
                note,
                tail,
                event_i,
                do,
                mode,
                last_consumed_degree=last_consumed_degree,
            )
        except _RequiredSkip as exc:
            raise _required_skipped(
                note, index, skipped=exc.skipped, matched=exc.matched
            ) from None
        if matched is None:
            raise _pitch_mismatch(note, index, remaining=tail[event_i:])
        event_i = matched
        event = tail[event_i]
        out.append(_assign(note, event, show_anchor=not any(
            n.template_event is event and n.show_anchor for n in out
        )))
        last_consumed_degree = str(event["pitches"]["S"])
        index += 1
        if index < len(notes) and pitches_match(
            notes[index].pitch, event["pitches"]["S"], do, mode
        ):
            # Zelfde graad: liever volgend zelfde-S-slot vullen (l.st. e.d.)
            # dan eindeloos H6-holden op het eerste slot.
            if event_i + 1 < len(tail) and pitches_match(
                notes[index].pitch, tail[event_i + 1]["pitches"]["S"], do, mode
            ):
                event_i += 1
                continue
            # H6: geen volgend zelfde-S-slot → hold; event_i blijft staan.
            continue
        event_i += 1

    if index >= len(notes) and llgr_from is not None and event_i <= llgr_from:
        event_i = llgr_from
    if notes and event_i < len(tail) and llgr_from is not None and event_i >= llgr_from:
        last_lyric_used = True
        for extra in tail[event_i:]:
            s_pitch = degree_pitch(extra["pitches"]["S"], do, mode)
            out.append(
                MappedNote(
                    lyric="" if last_lyric_used else notes[-1].lyric,
                    duration=Duration(note_type="quarter"),
                    s_pitch=s_pitch,
                    template_event=extra,
                    syllabic="end" if last_lyric_used else "single",
                    show_anchor=extra.get("anchor") == "l.lgr.",
                )
            )
            last_lyric_used = True
        event_i = len(tail)

    # H7: resterende verplichte slots → fout; alleen optional mag stil weg (H4).
    remaining_required = [ev for ev in tail[event_i:] if not ev.get("optional")]
    if remaining_required:
        unused_txt = ", ".join(_slot_label(ev) for ev in remaining_required)
        raise TemplateInstanceError(
            f"verplicht(e) template-slot(s) niet aangedaan in frase {phrase_id!r}: "
            f"{unused_txt}",
            code=CODE_REQUIRED_UNUSED,
            hint_nl=(
                "Breid de VSA-cadens uit zodat elke verplichte laddergraad voorkomt "
                "(syllabe, hold H6, of l.lgr.-melisma H8), of zet optionele slots op "
                "optional: true in de template."
            ),
            source=source,
            phrase_id=phrase_id,
            lyric=notes[-1].lyric if notes else "",
            note_index=len(notes) - 1 if notes else None,
        )


class _RequiredSkip(Exception):
    """Interne sentinel: match gevonden na verplichte tussenslots."""

    def __init__(self, skipped: list[dict[str, Any]], matched: dict[str, Any]) -> None:
        self.skipped = skipped
        self.matched = matched


def _may_skip_intermediate(
    event: dict[str, Any],
    *,
    last_consumed_degree: str | None,
) -> bool:
    """H4/H7: optional altijd; zelfde S als laatst gebruikt = rest van ondergevulde run."""
    if event.get("optional"):
        return True
    degree = str(event.get("pitches", {}).get("S", ""))
    return bool(last_consumed_degree) and degree == last_consumed_degree


def _next_matching_event(
    note: VsaNote,
    tail: list[dict[str, Any]],
    start: int,
    do: str,
    mode: str,
    *,
    last_consumed_degree: str | None = None,
) -> int | None:
    """Zoek slot vanaf ``start``. Andere toon overslaan alleen als optional (H4/H7)."""
    for i in range(start, len(tail)):
        if pitches_match(note.pitch, tail[i]["pitches"]["S"], do, mode):
            skipped = tail[start:i]
            blocked = [
                ev
                for ev in skipped
                if not _may_skip_intermediate(
                    ev, last_consumed_degree=last_consumed_degree
                )
            ]
            if blocked:
                raise _RequiredSkip(skipped=blocked, matched=tail[i])
            return i
    return None


def _assign(note: VsaNote, event: dict[str, Any], *, show_anchor: bool) -> MappedNote:
    duration = note.duration
    if event.get("role") == "recite":
        duration = Duration(note_type="quarter")
    return MappedNote(
        lyric=note.lyric,
        duration=duration,
        s_pitch=note.pitch,
        template_event=event,
        syllabic=note.syllabic,
        show_anchor=show_anchor and bool(event.get("anchor")),
    )
