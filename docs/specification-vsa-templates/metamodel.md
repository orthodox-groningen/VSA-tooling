# Metamodel

## Overzicht

```text
VsaTemplate
  ├── metadata (do, mode, duration-model?, genre, tone, …)
  ├── form A: cycle + final
  ├── form B: sequence
  ├── form C: same_as (alias)
  └── phrases: [ Phrase, … ]

Phrase
  ├── id: string
  └── events: [ Event, … ]

Event
  ├── role: open | recite | cadence | link
  ├── duration: VSA-ELM (~ | - | -. | ~. | _ | _. | __ | . | ..)
  ├── optional: bool
  ├── anchor: e.st. | l.st. | vl.st. | l.lgr. | null
  └── pitches: { S, A, T, B }   # laddergraden t.o.v. do

  of:
    └── [ { id?, events: [ Event, … ] }, … ]   # ≥2 cadenspaden; VSA kiest via hoogte
```

## Concepten

### VsaTemplate

Zie [vsa-template](@): één document = één formulevariant (bijv. tropaarmelodie
toon 4), geen concreet [zangstuk](@bron).

### Template-frase

Zie [template-frase](@). Ids: `"1"`, `"2"`, `"1a"`, `"laatste"`, …
Bibliotheekfrasen mogen buiten `cycle`/`final`/`sequence` staan.

### Cycle, final, sequence, same_as

- **cycle-form:** herhaling tot slotfrase.
- **sequence-form:** vaste volgorde.
- **alias-form:** `same_as` naar ander template-id.

Semantiek: [semantics.md](semantics.md).

### Template-event

Zie [template-event](@). Homofone tijdlijn; stem-autonome ritmes zijn open.

### Role / reciteertoon / frase-anker

Zie [reciteertoon](@) en [frase-anker](@).

### Laddergraad

Zie [laddergraad](@). Absolute toonhoogte = [do-context](@) + graad.

## Relatie tot org-terminologie

| Metamodel         | Org-term (bron)                                               | Opmerking                         |
| ----------------- | ------------------------------------------------------------- | --------------------------------- |
| [vsa-template](@) | (tool-term)                                                   | lokaal in `docs/terminologie/`    |
| —                 | [zangstuk](@bron) / variant / uitvoeringsvorm / representatie | template is géén van deze niveaus |

Zie [open-points.md](open-points.md) voor eventuele latere glossary-PR op bron.
