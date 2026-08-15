# Tropaar toon 4

| Veld           | Waarde                                                                                 |
| -------------- | -------------------------------------------------------------------------------------- |
| Template       | [`template.yaml`](template.yaml)                                                       |
| Formule-MSCZ   | [`template.mscz`](template.mscz)                                                       |
| MuseScore-bron | `Template - Tropaar (Toon 4).musicxml` (niet in git)                                   |
| Status pitches | `provisional`                                                                          |
| Mapping        | S=VSA, A/T/B=template ([mapping-vsa.md](../../mapping-vsa.md))                         |

## Voorbeelden

| Bestand                                                | Inhoud                                                |
| ------------------------------------------------------ | ----------------------------------------------------- |
| [`examples/elia.vsa`](examples/elia.vsa)               | Tropaar Profeet Elia (bron)                           |
| [`examples/elia.mscz`](examples/elia.mscz)             | Uitgewerkt (MuseScore)                                |
| [`examples/elia.mxl`](examples/elia.mxl)               | Uitgewerkt (Coria)                                    |
| `examples/corpus/`                                     | 13 Toon-4-stukken: `.vsa` / `.mscz` / `.mxl`          |

Corpus regenereren (PDF blijft lokaal, staat in `.gitignore`):

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python scripts\render_tropaar_toon4_corpus.py
python scripts\render_tropaar_toon4_corpus.py --pdf-only
```

Template-formule:

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python scripts\render_tropaar_toon4_corpus.py --template
```

## Notes

| Bestand                                          | Inhoud                          |
| ------------------------------------------------ | ------------------------------- |
| [`notes/corpus.md`](notes/corpus.md)             | 12 Toon-4-teksten ↔ frase-cycle |
| [`notes/elia-mapping.md`](notes/elia-mapping.md) | Slot-toets Elia regel 1         |

## Status t.o.v. PDF

- Frase-ids, `||O||`-recite, haakjes-optional, `e.st.`/`l.st.` zitten in de
  YAML; de renderer zet ze om naar MSCX.
- Cycle-regel staat in [`template.mscz`](template.mscz) /
  [`template-from-yaml.mscx`](template-from-yaml.mscx).
- Overschrijf niet `Template - Tropaar (Toon 4).*` (menselijke MuseScore-edit).
- Lyrics: DejaVu Sans Condensed 12pt (`LYRIC_FONT_PT` in
  `scripts/render_vsa_template_musicxml.py`).

## Geleerd (kort)

- Één VSA-regel ≈ één template-frase; cycle `1,2,…` + `laatste` houdt.
- Optionals/hold/skip: hypotheses H4–H7 in
  [`../../mapping-vsa.md`](../../mapping-vsa.md).
- Frase 2-recite in deze MuseScore-edit ligt op **fa** (Bb), niet op mi.
