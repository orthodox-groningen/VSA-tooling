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
- [x] Hoogte-mismatch in cadens → `PadBError` (geen stil hold); zie H9 in
      [mapping-vsa.md](mapping-vsa.md).
- [ ] **Parallelle template-sporen (`of`):** één frase mag 2+ cadens-/slot-
      paden declareren (bijv. `mi–re–mi` **of** `mi–mi–fa`). De VSA kiest
      impliciet welk spoor; een pad dat de template niet faciliteert blijft
      een hoogte-mismatch-fout. Zo kunnen meerdere [uitvoeringsvorm](@)-en
      in één template zonder aparte YAML-bestanden.
- [ ] Of `open` en eerste recite mogen samenvallen.
- [ ] Normalisatie anker-labels (`e. st.` vs `e.st.`).
- [ ] H4/H5/H6/H7 operationeel maken: optional, split/merge, hold, skip parallel op SATB.

## Tooling (later)

- [ ] CLI `vsa template validate`.
- [ ] MusicXML-export vanuit template (+ optioneel VSA-lyrics).

## Layout / print (MSCZ)

- [x] **Reciteertoon in uitgewerkte MSCZ (print):** recite-reeks → één breve
      (`||O||`) met daaronder de tekst; **laatste lettergreep** van het
      recitatief krijgt een eigen gewone noot (overgang naar cadens). Coria-MXL
      blijft per-syllabe-noten. Zie `collapse_recite_for_print()` in
      `scripts/render_vsa_template_musicxml.py`.

## Publicatie / UX (later)

- [ ] **Inline gerenderde VSA in proza:** toon-aanduiding e.d. (`T.4` vóór een
      hoogte-markering) hoort niet meer als zingbare tekst in de VSA-regel.
      Zoek een manier om een klein VSA-fragment (alleen hoogtemarkering +
      eventueel `Amen`) in een tekstregel/markdown te plaatsen — bruikbaar op
      tablet/pc/telefoon én op print — zonder dat de SVG/lyric-pipeline die
      letters als syllaben meeneemt.
