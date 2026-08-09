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
  ├── duration: VSA-ELM (~ | - | _ | _. | __ | . | ..)
  ├── optional: bool
  ├── anchor: e.st. | l.st. | vl.st. | null
  └── pitches: { S, A, T, B }   # laddergraden t.o.v. do
```

## Concepten

### VsaTemplate

Eén document dat één formulevariant beschrijft (bijv. tropaarmelodie toon 4).
Komt overeen met één herbruikbaar melodisch type, niet met één concreet
zangstuk-met-tekst.

### Phrase

Genaamde melodische eenheid. Ids: `"1"`, `"2"`, `"1a"`, `"2a"`, `"laatste"`, …

Frasen mogen in de bibliotheek staan zonder in `cycle`/`final`/`sequence` te
horen (alternatieven voor mapping).

### Cycle, final, sequence, same_as

- **cycle-form:** `cycle` + `final` (herhaling tot slotfrase).
- **sequence-form:** `sequence` (vaste volgorde, bijv. toon 3).
- **alias-form:** `same_as` (andere template is de melodische bron).

Semantiek: zie [`semantics.md`](semantics.md).

### Event

Kleinste muzikale stap binnen een frase. Alle stemmen delen dezelfde
ritmische/role-structuur (homofone formule); afwijkende stemritmes
(slurs op alleen A/B) zijn een **open punt**.

### Role

| Role       | Betekenis                                              |
| ---------- | ------------------------------------------------------ |
| `open`     | Openingsaanhef (vaak zelfde pitch als recite)          |
| `recite`   | Reciteertoon: duur dekt een variabel aantal syllaben   |
| `cadence`  | Vaste cadens- of slotstap                              |
| `link`     | Verbinding / overgangsnoot (vaak tevens `optional`)    |

### Anchor

Optioneel label dat op het blad als tekstanker fungeert (`e. st.`, `l. st.`,
`vl. st.`). In YAML genormaliseerd zonder spaties: `e.st.`, `l.st.`, `vl.st.`.

### Pitch

Laddergraad t.o.v. `do` (`mi`, `sol-1`, `#re`, …), niet scientific pitch per stem.
Absolute toonhoogte volgt uit `do` + `mode` + graad (zoals VSA).

## Relatie tot org-terminologie

| Metamodel     | Org-term (bron)                                      | Opmerking                                                                      |
| ------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| VsaTemplate   | (nieuw)                                              | glossary-PR nodig                                                              |
| —             | zangstuk / variant / uitvoeringsvorm / representatie | template is géén van deze niveaus; het is een herbruikbare formulebeschrijving |

Zie [`open-points.md`](open-points.md) voor glossary-acties.
