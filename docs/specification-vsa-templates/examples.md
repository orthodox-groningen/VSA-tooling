# Voorbeelden

## Geldig (`examples/valid/`)

| Bestand                                                           | Vorm      | Doel                                              |
| ----------------------------------------------------------------- | --------- | ------------------------------------------------- |
| [`tropaar-toon-1.yaml`](examples/valid/tropaar-toon-1.yaml)       | cycle     | `1,2` + `laatste`; bibliotheek `1a`               |
| [`tropaar-toon-3.yaml`](examples/valid/tropaar-toon-3.yaml)       | sequence  | vaste volgorde + `2a` + `eighth`                  |
| [`tropaar-toon-4.yaml`](examples/valid/tropaar-toon-4.yaml)       | cycle     | `1,2` + `laatste`; optional link                  |
| [`stichier-toon-5.yaml`](examples/valid/stichier-toon-5.yaml)     | cycle     | `1,2,3` + `laatste`; `also_used_as: tropaar`      |
| [`tropaar-toon-5.yaml`](examples/valid/tropaar-toon-5.yaml)       | alias     | `same_as: stichier-toon-5`                        |
| [`vers-toon-1.yaml`](examples/valid/vers-toon-1.yaml)             | cycle     | vers toon 1; `vl.st.`                             |
| [`vers-toon-5.yaml`](examples/valid/vers-toon-5.yaml)             | cycle     | vers toon 5                                       |

Alle pitches: `pitches_status: provisional` (menselijke audit nodig).

## Ongeldig (`examples/invalid/`)

| Bestand                                                                            | Code                          |
| ---------------------------------------------------------------------------------- | ----------------------------- |
| [`cycle-unknown-phrase.yaml`](examples/invalid/cycle-unknown-phrase.yaml)          | `TEMPLATE-CYCLE-REF`          |
| [`final-in-cycle.yaml`](examples/invalid/final-in-cycle.yaml)                      | `TEMPLATE-FINAL-NOT-IN-CYCLE` |
| [`missing-voice-pitch.yaml`](examples/invalid/missing-voice-pitch.yaml)            | `TEMPLATE-PITCHES`            |
| [`sequence-unknown-phrase.yaml`](examples/invalid/sequence-unknown-phrase.yaml)    | `TEMPLATE-SEQUENCE-REF`       |
| [`same-as-missing-target.yaml`](examples/invalid/same-as-missing-target.yaml)      | `TEMPLATE-SAME-AS-REF`        |
| [`bad-duration-elm.yaml`](examples/invalid/bad-duration-elm.yaml)                  | `TEMPLATE-DURATION`           |

## Walkthroughs (niet normatief)

| Bestand                                                                                           | Doel                         |
| ------------------------------------------------------------------------------------------------- | ---------------------------- |
| [`walkthroughs/elia-tropaar-toon-4.md`](examples/walkthroughs/elia-tropaar-toon-4.md)             | Mapping VSA ↔ template       |

## Checklist “voorbeeld mag in valid/”

- [ ] Schema + documentregels groen
- [ ] Geen velden buiten de syntax
- [ ] `source` of commentaar verklaart herkomst
- [ ] Onzekere pitches: `pitches_status: provisional`
