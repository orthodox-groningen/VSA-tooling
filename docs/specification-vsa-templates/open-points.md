# Open punten

## Terminologie

- [x] Lokale curated texts: [vsa-template](@), [template-frase](@),
      [template-event](@), [frase-id](@), [frase-anker](@), [formulelabel](@),
      [reciteertoon](@), [laddergraad](@), [do-context](@).
- [ ] Eventueel org-brede namen via glossary-PR op **bron** (als termen
      repo-overschrijdend moeten zijn).

## Pitches / voorbeelden

- [ ] Tenor-octaaf openingsakkoord tropaar toon 4: `sol-1` vs `sol-2` (was C3|C4).
- [ ] Alle templates: graden/`do`/`mode` provisional tot PDF-audit.
- [ ] Sequence-form: tekstlengte vs `len(sequence)` — handmatig bij `text_mapping`.
- [x] Frase-toewijzing: `text_mapping` + `mapping_plans` + mapper
      ([`template_mapping.py`](../../src/vsa/template_mapping.py)).
- [ ] `l.lgr.`-anker in stichier-template + event-mapping (H8).
- [ ] Welke `mode`-identifiers exact — gelijk trekken met VSA-implementatie.

## Semantiek / model

- [ ] Stemmen met onderling verschillende ritmes (buiten parallel split/merge).
- [x] Mapping-architectuur: **pad B** (S uit VSA, A/T/B uit template) —
      zie [mapping-vsa.md](mapping-vsa.md).
- [ ] Of `open` en eerste recite mogen samenvallen.
- [ ] Normalisatie anker-labels (`e. st.` vs `e.st.`).
- [ ] H4/H5/H6/H7 operationeel maken: optional, split/merge, hold, skip parallel op SATB.

## Tooling (later)

- [ ] CLI `vsa template validate`.
- [ ] MusicXML-export vanuit template (+ optioneel VSA-lyrics).

## Bewust uitgesteld

- Volledige toonboek-transcriptie (alle 8 tonen × genres).
- OMR-pipeline.
