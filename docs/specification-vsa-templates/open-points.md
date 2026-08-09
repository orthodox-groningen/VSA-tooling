# Open punten

## Terminologie (bron)

- [ ] Glossaryterm **vsa-template** (of org-brede naam zoals *melodieformule*)
      via PR op `bron/docs/specs/terminologie.md`.
- [ ] Eventueel termen voor *reciteertoon*, *frase-anker* — alleen als ze
      org-breed nodig zijn; anders tool-lokaal houden.

## Pitches / voorbeelden

- [ ] Tenor-octaaf openingsakkoord tropaar toon 4: `sol-1` vs `sol-2` (was C3|C4).
- [ ] Alle templates: graden/`do`/`mode` provisional tot PDF-audit.
- [ ] Sequence-form: tekstlengte vs `len(sequence)` — mapping open.
- [ ] Welke `mode`-identifiers exact (alleen major/minor of ook dorisch, …) —
      gelijk trekken met VSA-implementatie.

## Semantiek / model

- [ ] Stemmen met onderling verschillende ritmes (slur alleen in A/B terwijl
      S/T liggen): nu niet gemodelleerd; uitbreiding eventueel `voices[].events`.
- [ ] Mapping-architectuur: **template-pitches als SATB-waarheid** vs
      **VSA als S-waarheid + template als harmony** — beslissing na meer
      walkthroughs; zie [`mapping-vsa.md`](mapping-vsa.md).
- [ ] Of `open` en eerste `recite` mogen samenvallen tot één event.
- [ ] Normalisatie van anker-labels (`e. st.` vs `e.st.` vs `eerste streek`).

## Tooling (later)

- [ ] CLI `vsa template validate`.
- [ ] Integratie van deze map in `docs/specification/` + MkDocs-nav.
- [ ] MusicXML-export vanuit template (+ optioneel VSA-lyrics).

## Bewust uitgesteld

- Volledige toonboek-transcriptie (alle 8 tonen × genres).
- OMR-pipeline.
