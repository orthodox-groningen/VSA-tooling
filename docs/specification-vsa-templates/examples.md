# Voorbeelden

## Library (geldige formules)

Canonieke werkmappen: [`library/`](library/README.md).
Per formule: `template.yaml`, plus afgeleide `template.mscz` (MuseScore) en
`template.mxl` (MusicXML) waar de pijplijn dat al doet; optioneel
`examples/corpus/` en `notes/`.

| Map                                                    | Vorm     | Doel                                |
| ------------------------------------------------------ | -------- | ----------------------------------- |
| [`tropaar-toon-1`](library/tropaar-toon-1/README.md)   | cycle    | `1,2` + `laatste`; bibliotheek `1a` |
| [`tropaar-toon-3`](library/tropaar-toon-3/README.md)   | sequence | vaste volgorde + `2a` + ELM `.`     |
| [`tropaar-toon-4`](library/tropaar-toon-4/README.md)   | cycle    | Elia-mapping + corpus               |
| [`stichier-toon-5`](library/stichier-toon-5/README.md) | cycle    | `1,2,3` + `laatste`; `also_used_as` |
| [`tropaar-toon-5`](library/tropaar-toon-5/README.md)   | alias    | `same_as: stichier-toon-5`          |
| [`vers-toon-1`](library/vers-toon-1/README.md)         | cycle    | vers toon 1; `vl.st.`               |
| [`vers-toon-5`](library/vers-toon-5/README.md)         | cycle    | vers toon 5; ELM `_.`               |

Alle formules: [vsa-templates](vsa-template@) met `pitches_status: provisional`
tot PDF-audit. MusicXML regenereren:

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python scripts\render_vsa_template_musicxml.py --all
```

## Ongeldig (`examples/invalid/`)

| Bestand                                                                         | Code                          |
| ------------------------------------------------------------------------------- | ----------------------------- |
| [`cycle-unknown-phrase.yaml`](examples/invalid/cycle-unknown-phrase.yaml)       | `TEMPLATE-CYCLE-REF`          |
| [`final-in-cycle.yaml`](examples/invalid/final-in-cycle.yaml)                   | `TEMPLATE-FINAL-NOT-IN-CYCLE` |
| [`missing-voice-pitch.yaml`](examples/invalid/missing-voice-pitch.yaml)         | `TEMPLATE-PITCHES`            |
| [`sequence-unknown-phrase.yaml`](examples/invalid/sequence-unknown-phrase.yaml) | `TEMPLATE-SEQUENCE-REF`       |
| [`same-as-missing-target.yaml`](examples/invalid/same-as-missing-target.yaml)   | `TEMPLATE-SAME-AS-REF`        |
| [`bad-duration-elm.yaml`](examples/invalid/bad-duration-elm.yaml)               | `TEMPLATE-DURATION`           |

## Checklist “mag in library/”

- [ ] Schema + documentregels groen
- [ ] `template.mxl` gegenereerd (SA/TB, `senza-misura`)
- [ ] `source` of README verklaart herkomst
- [ ] Onzekere pitches: `pitches_status: provisional`
