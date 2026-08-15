# Template-instance rendering — valkuilen

**Doel:** checklist voor agents die verder werken aan vsa-templates →
MSCZ/MXL/PDF. Geen projectgeschiedenis; alleen **probleem → oorzaak → regel**.

Lees dit **vóór** je `scripts/render_vsa_template_musicxml.py`,
`src/vsa/template_instance.py` of corpus-PDF’s wijzigt.

Gerelateerd: [mapping-vsa.md](mapping-vsa.md), [open-points.md](open-points.md),
`collapse_recite_for_print()` in `scripts/render_vsa_template_musicxml.py`.

---

## Twee exportkanalen

| Kanaal                         | Doel                         | Recite-printmodel                                      |
| ------------------------------ | ---------------------------- | ------------------------------------------------------ |
| **MSCZ** (MuseScore / PDF)     | leespartituur                | collapse: `\|\|O\|\|` + slotlettergreep als kwart      |
| **MXL** (Coria e.d.)           | playback / solo per stem     | **geen** collapse — elke syllabe een noot              |

Regel: wijzigingen aan `collapse_recite_for_print` raken **alleen** MSCZ/print.
Coria-export via `render_instance_musicxml` houdt per-syllabe-noten.

---

## Recite-collapse (print)

| Probleem                                            | Oorzaak                                                               | Regel                                                                                                                                                                |
| --------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{moe__}`, `{Ni__}`, `{/en}` verdwijnen in de breve | Heuristieken: “zelfde toonhoogte”, “woord loopt door”, leading absorb | Collapse **alleen** aaneengesloten `role=recite` (ongemarkeerde VSA-syllaben). Elke **VSA-scope** blijft een eigen noot met VSA-duur — nooit breve, nooit opslokken. |
| Te korte recite (`Als de`) op `\|\|O\|\|`           | Collapse bij 1–2 syllaben                                             | Alleen bij **≥ 3** recite-syllaben (`RECITE_COLLAPSE_MIN_SYLLABLES`). Anders aparte kwarten.                                                                         |
| Onduidelijk wat onder de breve hoort                | Te veel speciale gevallen                                             | Simpel: body (alles behalve laatste) onder eerste noot als `\|\|O\|\|`; **laatste** recite-syllabe = kwart; daarna template/cadens ongewijzigd.                      |
| Punt achter de `\|\|O\|\|` (gestippelde whole/breve) | Duur opgeblazen met `dots=1` voor tekstbreedte | Recite-printnoot: altijd **half + `headType` breve + `noStem`**, **`dots=0`**. Nooit dotted whole/longa als “ |     | O   |     | ”.  |
| Lege systemen / “rij rusten” | Maatduur opgeblazen (`longa`, 22/4) zodat MuseScore rare layout maakt | Tekstruimte via **onzichtbare spacer-rusten** + `lyric_ticks` ná de `\|\|O\|\|`, niet via langere notehead-duur. |

Canonieke voorbeelden (T4-11):

- `{/en} het voor-beeld der zacht{moe__}dig{\heid_}` → `en` \| `het voor-beeld der` (`\|\|O\|\|`) \| `zacht` \| `moe` (heel) \| `dig` \| `heid`
- `{/Va}der … pries-ter {Ni__}ko{\laas_}` → `Va` \| `der … pries-` (`\|\|O\|\|`) \| `ter` \| `Ni` (heel) \| `ko` \| `laas`

---

## MuseScore 4 (MSCZ)

| Probleem                                                | Oorzaak                                                               | Regel                                                                                                                                    |
| ------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Binnen-strofe-maatstrepen blijven zichtbaar             | `Measure/endBarLineVisible` wordt **genegeerd**                       | Maatstreep-zichtbaarheid alleen via `<BarLine><subtype>…</subtype><visible>0</visible></BarLine>` **in de voice**. Roundtrip verifiëren. |
| Layout-splits midden in strofe vs “één maat”            | `split_events_for_layout` voor instance                               | Instance: **één maat per strofe**, geen binnen-strofe-knip. Coria idem.                                                                  |
| Recite-lyrics blijven gecentreerd ondanks `<align>left` | MS 4.7: horizontale plaatsing = **`position`**, niet (alleen) `align` | Op recite-lyrics: `<position>left</position>` (+ desgewenst `<align>left,baseline</align>`). `align` alleen = tekstinterne uitlijning.   |
| Maatsoort-getallen zichtbaar                            | TimeSig in maat nodig voor `len`, maar stijl toont ze                 | TimeSig mag in de maat; staff: `showTimeSig=0`, style: `genCourtesyTimesig=0`.                                                           |
| Stokken systematisch S/T omhoog, A/B omlaag             | Twee stemmen per balk                                                 | MSCZ: SA en TB als **één akkoordstem** per balk.                                                                                         |
| “Invisible” rusten of style verdwijnen na opslaan       | MuseScore herschrijft bij save                                        | Niet steunen op roundtrip-behoud van Style; opnieuw genereren vanuit script is bron van waarheid.                                        |

---

## Mapping / hoogten (instance)

| Probleem                           | Oorzaak                                         | Regel                                                                                |
| ---------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------ |
| Stil hold op verkeerde laddergraad | Soft mismatch                                   | **H9:** hoogte-mismatch → harde `TemplateInstanceError`, geen stil hold.             |
| Slotcadens `laatste` vs frase `1`  | Template: `laatste` is mi–re–mi; frase 1 anders | VSA voor `laatste` moet template pitches volgen; parallelle `of`-sporen = open punt. |
| `T.4` / `T.N` als zingbare syllabe | Toon-aanduiding in VSA-regel                    | Geen `T.N` vóór hoogtemarkeringen in corpus; inline-VSA in proza = open punt.        |

---

## Corpus / tooling

| Probleem                            | Oorzaak                                                   | Regel                                                                                           |
| ----------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Verwarring legacy `*.pad-b.*`-namen | Legacy `*.pad-b.*`                                        | Corpus: `T4-XX-….vsa/.mscz/.mxl`; Elia: `examples/elia.*`; formule: `template.mscz`.            |
| PDF in git vs lokaal                | PDF is afgeleide MuseScore-export                         | PDF lokaal regenereren (`render_tropaar_toon4_corpus.py --pdf-only`); niet als bron behandelen. |
| Tests groen, PDF “fout”             | Tests toetsen MSCX-strings, niet visuele MuseScore-layout | Na layout-wijzigingen: PDF/MSCZ **openen in MuseScore** of screenshot; niet alleen pytest.      |

---

## Wat niet opnieuw proberen

1. Leading/trailing “zelfde pitch” of “woord-hold” in `collapse_recite_for_print` om scopes onder de breve te trekken.
2. `endBarLineVisible` op `Measure` voor verborgen maatstrepen in MS4.
3. `longa` / gestippelde whole als recite-duur om lyric-breedte te forceren.
4. Alleen `<align>left,…>` verwachten voor left-attach aan de nootkop in MS 4.7+.
5. Recite-collapse in de Coria-MXL-pipeline.

---

## Regenereren

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
.\.venv\Scripts\python.exe -m pytest tests\test_vsa_template_instance.py tests\test_vsa_template_corpus_mscx.py -q
.\.venv\Scripts\python.exe scripts\render_tropaar_toon4_corpus.py
.\.venv\Scripts\python.exe scripts\render_tropaar_toon4_corpus.py --pdf-only
```
