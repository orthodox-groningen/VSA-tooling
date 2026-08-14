# Mapping VSA ↔ vsa-template (experimenteel)

Status: **hypotheses + architectuurkeuze pad B**; geen normatieve VSA 1.0-wijziging.

Implementatie: [`src/vsa/template_mapping.py`](../../src/vsa/template_mapping.py)
(frase-toewijzing) en [`src/vsa/pad_b.py`](../../src/vsa/pad_b.py) (event-niveau,
pad B).

## Doel

Beschrijven hoe een [VSA](@)-tekstblok (melodie **S**) op
[template-events](template-event@) van een [vsa-template](@) landt, zodat
**A, T en B** uit de template meegenomen kunnen worden naar een afgeleide
(bijv. MusicXML) — zonder lyrics in de template-syntax te stoppen.

## Architectuur: pad B (besloten)

| Stem      | Toonhoogte / contour                         | Ritme / optional / split-merge        |
| --------- | -------------------------------------------- | ------------------------------------- |
| **S**     | uit [VSA](@) + [do-context](@)               | uit VSA (scopes, ELMs, syllaben)      |
| **A/T/B** | uit template-[laddergraden](laddergraad@)    | **zelfde** eventkeuzes als voor S     |

## Tekstregels → template-frasen

Elke VSA-regel (gescheiden door `*`) is één **tekstfrase**. De mapper wijst
regels in volgorde toe aan [template-frase](template-frase@)-ids.

### Legacy (nog ondersteund)

| Vorm            | YAML                         | Betekenis                                      |
| --------------- | ---------------------------- | ---------------------------------------------- |
| cycle-form      | `cycle` + `final`            | cyclisch herhalen tot één regel resteert       |
| sequence-form   | `sequence`                   | vaste volgorde, geen herhaling                 |

`cycle: ["1", "2"]` + `final: laatste` compileert naar:

```yaml
text_mapping:
  - repeat: ["1", "2"]
    until: final
  - phrase: laatste
```

### `text_mapping` (algemeen)

Lijst van **stappen** (in volgorde):

| Stap        | YAML-vorm                                      | Effect                                    |
| ----------- | ---------------------------------------------- | ----------------------------------------- |
| enkel       | `phrase: "1"`                                  | één tekstregel → frase `1`                |
| reeks       | `sequence: ["1", "3", "2a"]`                   | vaste reeks, één regel per id             |
| herhaling   | `repeat: ["2", "3"]` + `until`                 | cyclisch toewijzen tot stopconditie       |

#### `until: final`

Herhaal het patroon **cyclisch** over zoveel regels als nodig, zodat de
**tail** (alle stappen ná deze `repeat`) precies overblijft. Typisch eindigt
de tail op `phrase: laatste`.

**Geen eis** dat het aantal regels vóór `laatste` een veelvoud van `k` is.
Bij `k = 2` en `n = 7` regels: `1, 2, 1, 2, 1, 2, laatste`.

#### `until: { remaining: N }`

Stop met herhalen wanneer nog **N** regels over zijn; die vallen op de tail
(meestal `sequence: [...]`). Voorbeeld tropaar toon 1 (variant met slot
`1, 1a, 1a, 2`):

```yaml
- repeat: ["1", "2"]
  until:
    remaining: 4
- sequence: ["1", "1a", "1a", "2"]
```

### Voorbeelden (bladnotatie → `text_mapping`)

| Blad / gewoonte                         | `text_mapping` |
| --------------------------------------- | -------------- |
| `\|\|: 1, 2 :\|\| laatste`              | `repeat [1,2] until final` + `phrase laatste` |
| `1 \|\|: 2, 3 :\|\| laatste`          | `phrase 1` + `repeat [2,3] until final` + `phrase laatste` |
| `1, 3, 1, 2, 3, 1, 2a, 4`               | `sequence: [1, 3, 1, 2, 3, 1, 2a, 4]` |
| `1, 2, 3, \|\|: 4, 5, 3a :\|\| laatste` | `sequence [1,2,3]` + `repeat [4,5,3a] until final` + `phrase laatste` |

## `mapping_plans` (meerdere plannen)

Als één template op het blad **meerdere cycle-notaties** heeft (bijv. tropaar
toon 1), of de toewijzing **afhangt van het aantal tekstregels**:

```yaml
mapping_plans:
  - id: standard
    label: "||: 1, 2 :|| laatste"
    when:
      default: true
    steps:
      - repeat: ["1", "2"]
        until: final
      - phrase: laatste
  - id: extended-close
    label: "||: 1, 2 :|| 1, 1a, 1a, 2"
    when:
      stanza_count: 5
    steps:
      - repeat: ["1", "2"]
        until:
          remaining: 4
      - sequence: ["1", "1a", "1a", "2"]
```

Selectie: `select_mapping_plan(doc, stanza_count)` — eerste plan waarvan
`when` matcht; anders plan met `when.default: true`.

| `when`-sleutel       | Match                                    |
| -------------------- | ---------------------------------------- |
| `default: true`      | fallback                                 |
| `stanza_count`       | exact aantal regels                      |
| `stanza_count_mod`   | `{ mod: 3, remainder: 0 }` → `n % 3 == 0` |
| `stanza_count_min`   | minimaal n regels                        |
| `stanza_count_max`   | maximaal n regels                        |

Voorbeeld **3n regels** met prefix + cycle + afwijkende slot:

```yaml
- id: triple
  when:
    stanza_count_mod:
      mod: 3
      remainder: 0
  steps:
    - phrase: "1"
    - repeat: ["2", "3", "1"]
      until: final
    - phrase: "2a"
    - phrase: laatste
```

## Frase-ankers (inclusief melisma)

| Anchor (YAML) | Bladlabel | Bedoeling                                      |
| ------------- | --------- | ---------------------------------------------- |
| `e.st.`       | `e. st.`  | eerste streek / inzet                            |
| `l.st.`       | `l. st.`  | laatste streek op cadensnoot                    |
| `vl.st.`      | `vl. st.` | voorlaatste streek                             |
| `l.lgr.`      | `l. lgr.` | start van het **slotmelisma** (laatste lettergreep) |

`l.lgr.` wijst naar een noot **waar nog noten achteraan komen**. Vanaf dat
event tot het einde van de [template-frase](template-frase@) horen **alle**
noten bij de **laatste lettergreep** van de tekst — één syllabe over meerdere
template-events (melisma). In VSA hoort dat te blijken als één [zangelement](@)
met meerdere [muzikale posities](@) (`&` in de modifiers).

## Hypotheses (event-niveau)

| #   | Hypothese                                                                                         |
| --- | ------------------------------------------------------------------------------------------------- |
| H1  | Ongemarkeerde VSA-syllaben vóór cadens-scopes vallen op recite.                                   |
| H2  | Cadens-scopes corresponderen met `cadence`-events, vaak bij `l.st.` of erna.                      |
| H3  | `{/…}` aan het begin van een regel kan `e.st.` van frase `2` (of vergelijkbaar) zijn.             |
| H4  | `optional: true` events: mee als VSA-S dat slot gebruikt, anders weg — voor **alle** stemmen.     |
| H5  | Split/merge van duren wordt gestuurd door VSA-S en parallel op A/T/B gezet.                       |
| H6  | Blijft VSA-S op dezelfde graad voor extra syllaben, dan **houden** A/T/B hetzelfde slot-akkoord.  |
| H7  | Trailing template-slots die VSA-S niet aandoet, worden voor alle stemmen **overgeslagen**.        |
| H8  | `l.lgr.`: start van een slotmelisma — geankerd event **plus alle volgende** events in de frase op de laatste VSA-syllabe. |

## Corpus en detail

Library-werkmappen: [`library/`](library/README.md).

Corpus Toon 4:
[`library/tropaar-toon-4/notes/corpus.md`](library/tropaar-toon-4/notes/corpus.md).

Elia regel 1 (pad B + MusicXML):
[`library/tropaar-toon-4/notes/elia-mapping.md`](library/tropaar-toon-4/notes/elia-mapping.md).

## Wat deze laag niet doet

- Geen nieuwe VSA-syntax voor SATB (SATB blijft in de template).
- Geen automatische keuze tussen plannen op inhoud van de tekst (alleen
  `stanza_count` / expliciet `plan_id`); inhoudelijke keuze blijft redactie.
