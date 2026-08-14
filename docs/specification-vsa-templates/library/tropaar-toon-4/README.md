# Tropaar toon 4

| Veld             | Waarde                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------- |
| Template         | [`template.yaml`](template.yaml)                                                       |
| MuseScore-bron   | [`Template - Tropaar (Toon 4).musicxml`](Template%20-%20Tropaar%20(Toon%204).musicxml) |
| Spiegel          | [`template.musicxml`](template.musicxml) (kopie van MuseScore-export)                  |
| YAML → MuseScore | [`template-from-yaml.mscx`](template-from-yaml.mscx) (Style + VBox; open dit)          |
| Status pitches   | `provisional` (menselijk t.o.v. PDF; YAML ↔ MusicXML)                                  |
| Architectuur     | pad B (S=VSA, A/T/B=template)                                                          |

## Voorbeelden

| Bestand                                                              | Inhoud                                             |
| -------------------------------------------------------------------- | -------------------------------------------------- |
| [`examples/elia.vsa`](examples/elia.vsa)                             | Tropaar Profeet Elia (S)                           |
| [`examples/elia.pad-b.mscz`](examples/elia.pad-b.mscz)               | Stap 2: Elia pad B (S=VSA, A/T/B=template, lyrics) |
| [`examples/elia-r1-pad-b.musicxml`](examples/elia-r1-pad-b.musicxml) | Regel 1 SATB-bewijs (handmatig, historisch)        |
| [`examples/corpus/`](examples/corpus/)                               | Stap 1: uitgevouwen formule-MSCX (12 stukken)      |

Uitgevouwen formule (stap 1):

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python scripts\render_tropaar_toon4_corpus.py
```

Elia pad B (stap 2) — VSA-parser + event-mapper, alle 7 regels:

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python scripts\render_tropaar_toon4_corpus.py --pad-b
```

## Notes

| Bestand                                          | Inhoud                          |
| ------------------------------------------------ | ------------------------------- |
| [`notes/corpus.md`](notes/corpus.md)             | 12 Toon-4-teksten ↔ frase-cycle |
| [`notes/elia-mapping.md`](notes/elia-mapping.md) | Slot-toets Elia regel 1         |

## Status t.o.v. PDF

- Frase-ids, `||O||`-recite, haakjes-optional, `e.st.`/`l.st.` zitten in de
  YAML; de renderer zet ze om naar MSCX.
- Cycle-regel `||: 1, 2 :|| laatste` staat na de laatste maat in een HBox
  (met spacer-HBox ervoor) in [`template-from-yaml.mscx`](template-from-yaml.mscx);
  VBox alleen als er te weinig ruimte is. MusicXML/MXL kan Style/HBox/VBox niet
  vasthouden; zie [`../README.md`](../README.md).
- Gegenereerde MSCX: 1 G-sleutel (SA) + 1 F-sleutel (TB); recite als stemloze
  brevis (`headType breve`), halfnoot (2 tellen), geen symbool erboven;
  cycle-herhalingstekens (`startRepeat` / `endRepeat`); frase-ankerpijl op
  `y="-1.3"`.
- PDF: exporteer in MuseScore vanuit
  [`template-from-yaml.mscx`](template-from-yaml.mscx) of
  [`template-from-yaml.mscz`](template-from-yaml.mscz). Overschrijf niet
  `Template - Tropaar (Toon 4).*`.
- Pad-B-lyrics: DejaVu Sans Condensed 12pt (zelfde als staff text). Grootte:
  constante `LYRIC_FONT_PT` in `scripts/render_vsa_template_musicxml.py`.

## Geleerd (kort)

- Één VSA-regel ≈ één template-frase; cycle `1,2,…` + `laatste` houdt.
- Optionals/hold/skip: zie hypotheses H4–H7 in
  [`../../../mapping-vsa.md`](../../../mapping-vsa.md).
- Frase 2-recite in deze MuseScore-edit ligt op **fa** (Bb), niet op mi.
