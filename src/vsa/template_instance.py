"""VSA→template-instance: VSA-S-noten → template-events; A/T/B lopen synchroon mee."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .music import Duration, Pitch
from .pitch_resolver import PitchResolver, degree_to_pitch
from .template_mapping import assign_stanzas_to_phrases, select_mapping_plan
from .vsa_stanzas import VsaNote, extract_stanza_notes

_DEGREE_RE = re.compile(r"^(#|b)?(do|re|mi|fa|sol|la|ti)([+-][1-3])?$")
_DEGREE_ORDER = ("do", "re", "mi", "fa", "sol", "la", "ti")
_STEP_SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


class TemplateInstanceError(Exception):
    """VSA-regel past niet op de template-frase."""


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
        raise TemplateInstanceError(f"bad ladder degree: {degree!r}")
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
) -> list[MappedNote]:
    """Koppel één VSA-regel aan de events van één template-frase (H1, H4–H8)."""
    if not notes:
        raise TemplateInstanceError("empty stanza")
    events = list(phrase.get("events") or [])
    if not events:
        raise TemplateInstanceError(f"phrase {phrase.get('id')!r} has no events")
    prefix, recite, tail = split_phrase_events(events)
    index = 0
    out: list[MappedNote] = []
    phrase_id = str(phrase.get("id", "?"))

    for event in prefix:
        index = _take_prefix_event(notes, index, event, out, do, mode)

    if recite is not None:
        while index < len(notes) and not notes[index].scoped:
            out.append(_assign(notes[index], recite, show_anchor=False))
            index += 1
        if not any(n.template_event is recite for n in out) and index < len(notes):
            # Geen ongemarkeerde recite-syllaben: skip recite (H7).
            pass

    _map_tail(
        notes, index, tail, out, do, mode, phrase_id=phrase_id
    )
    return out


def map_vsa_to_template(
    template: dict[str, Any],
    vsa_text: str,
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
            raise TemplateInstanceError(f"unknown phrase id {pid!r}")
        mapped.append(
            (pid, map_stanza(notes, by_id[pid], do=do, mode=mode))
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


def _map_tail(
    notes: list[VsaNote],
    index: int,
    tail: list[dict[str, Any]],
    out: list[MappedNote],
    do: str,
    mode: str,
    *,
    phrase_id: str | None = None,
) -> None:
    event_i = 0
    llgr_from: int | None = next(
        (i for i, ev in enumerate(tail) if ev.get("anchor") == "l.lgr."),
        None,
    )
    where = f"frase {phrase_id!r}" if phrase_id is not None else "frase"

    def _pitch_mismatch(note: VsaNote, *, remaining: list[dict[str, Any]]) -> TemplateInstanceError:
        got = f"{note.pitch}"
        expected = [
            str(ev.get("pitches", {}).get("S"))
            for ev in remaining
            if not ev.get("optional")
        ]
        lyric = note.lyric or "(melisma)"
        return TemplateInstanceError(
            f"hoogte-mismatch in {where}: VSA {lyric!r} = {got}, "
            f"geen passend template-S-slot meer "
            f"(verwacht o.a. {expected or '—'})"
        )

    while index < len(notes):
        note = notes[index]
        if event_i >= len(tail):
            if not out:
                raise TemplateInstanceError(f"cadensnoten zonder template-tail in {where}")
            last = out[-1].template_event
            if pitches_match(note.pitch, last["pitches"]["S"], do, mode):
                # H6: extra syllabe opzelfde slot-akkoord.
                out.append(_assign(note, last, show_anchor=False))
                index += 1
                continue
            raise _pitch_mismatch(note, remaining=[])
        matched = _next_matching_event(note, tail, event_i, do, mode)
        if matched is None:
            # Geen stil hold meer op het vorige akkoord bij verkeerde hoogte
            # (was: T4-08 mi–fa–mi op template mi–re–mi).
            raise _pitch_mismatch(note, remaining=tail[event_i:])
        event_i = matched
        event = tail[event_i]
        out.append(_assign(note, event, show_anchor=not any(
            n.template_event is event and n.show_anchor for n in out
        )))
        index += 1
        if index < len(notes) and pitches_match(
            notes[index].pitch, event["pitches"]["S"], do, mode
        ):
            # H6: zelfde graad → hold; event_i blijft staan.
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


def _next_matching_event(
    note: VsaNote,
    tail: list[dict[str, Any]],
    start: int,
    do: str,
    mode: str,
) -> int | None:
    for i in range(start, len(tail)):
        if pitches_match(note.pitch, tail[i]["pitches"]["S"], do, mode):
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
