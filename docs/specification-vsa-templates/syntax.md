# Syntax

Canonieke bronvorm: **YAML**. Structurele toetsing:
[`schema/vsa-template.schema.json`](schema/vsa-template.schema.json).

Toonhoogte- en duurmodel sluiten aan op VSA 1.0 (`do`/`mode`, ELMs). Zie
[`docs/specification/semantics.md`](../specification/semantics.md) §5.5–5.10.

## Topniveau

Elk document is **één** van drie vormen:

1. **cycle-form** — `cycle` + `final`;
2. **sequence-form** — `sequence`;
3. **alias-form** — `same_as`.

### Cycle-form

```yaml
spec_version: draft-v0
id: tropaar-toon-4
genre: tropaar
tone: 4
do: F4                             # scientific pitch van de do (zoals VSA)
mode: major                        # major | minor | dorian | phrygian | lydian | …
duration-model: default            # optioneel; zelfde betekenis als VSA
pitches_status: provisional
source: "…"
also_used_as: [stichier]
cycle: ["1", "2"]
final: laatste
phrases:
  - id: "1"
    events: [ ... ]
```

`key_signature` is **niet** meer het toonhoogtemodel; eventueel alleen als
niet-normatieve bladnotitie (af te leiden uit `do`+`mode`).

### Sequence-form / alias-form

Zelfde `do` / `mode` (verplicht). Alias heeft geen `phrases`.

## Event

```yaml
- role: recite
  duration: "~"                    # VSA-ELM; zie tabel
  optional: false
  anchor: l.st.
  pitches:
    S: mi                          # laddergraad t.o.v. do
    A: do
    T: sol-1
    B: do-1
```

### Duration (VSA-ELM)

Standaardduur ↔ kwartnoot bij `duration-model: default` (zoals VSA).

| ELM  | Semantiek (VSA)       | MusicXML (default) |
| ---- | --------------------- | ------------------ |
| `~`  | 1 × standaardduur     | quarter            |
| `-`  | 1 × standaardduur     | quarter            |
| `_`  | 2 × standaardduur     | half               |
| `_.` | 3 × standaardduur     | dotted half        |
| `__` | 4 × standaardduur     | whole              |
| `.`  | ½ × standaardduur     | eighth             |
| `..` | ¼ × standaardduur     | 16th               |

`role: recite` = variabel aantal syllaben; elke syllabe krijgt typisch `duration: "~"`.
De breve/“box” op het blad is **geen** aparte ELM, maar de recite-rol.

### Pitches (laddergraden)

Per stem een graad t.o.v. `do`, optioneel chromatisch en octaafverschuiving:

```text
pitch := ['#' | 'b'] degree [ '+' n | '-' n ]
degree := 'do' | 're' | 'mi' | 'fa' | 'sol' | 'la' | 'ti'
n := 1..3
```

Voorbeelden (bij `do: F4`, `mode: major`):

| String   | Betekenis                          |
| -------- | ---------------------------------- |
| `do`     | F4                                 |
| `mi`     | A4                                 |
| `fa`     | Bb4                                |
| `sol-1`  | C4                                 |
| `do-1`   | F3                                 |
| `#re`    | G♯ (chromatisch)                   |

### Regels (syntactisch)

1. Frase-ids uniek; mogen `1a` / `2a` bevatten.
2. Cycle- / sequence- / alias-form zoals eerder.
3. Elk event: `role`, `duration` (ELM), `pitches` met S/A/T/B.
4. `do` matcht scientific pitch `^[A-G](#|b)?[0-9]$`.
5. `mode` is een niet-lege identifier (minimaal `major` / `minor`; overige
   modi zoals in VSA-semantiek).
6. `anchor` ∈ {`e.st.`, `l.st.`, `vl.st.`} indien aanwezig.

## Wat syntax niet uitdrukt

- Syllabe-tekst / VSA-scopes (mapping).
- SVG-/MusicXML-layout.
- Ongelijke ritmes per stem.
