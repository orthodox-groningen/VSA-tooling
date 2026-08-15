# Open punten — vsa-templates

Checklist voor verdere chats. Afgevinkt = gedaan in deze branch/sessies.
Onder **Werklijst** staan de open items (nog ongeordend).

Valkuilen bij MSCZ/MXL: [rendering-pitfalls.md](rendering-pitfalls.md).
Mappingcontract: [mapping-vsa.md](mapping-vsa.md).

---

## Gedaan (niet opnieuw oppakken)

- [x] Lokale curated texts: [vsa-template](@), [template-frase](@),
      [template-event](@), [frase-id](@), [frase-anker](@), [formulelabel](@),
      [reciteertoon](@), [laddergraad](@), [do-context](@).
- [x] Frase-toewijzing: `text_mapping` + `mapping_plans` +
      [`template_mapping.py`](https://github.com/orthodox-groningen/VSA-tooling/blob/main/src/vsa/template_mapping.py).
- [x] Mapping-architectuur **VSA→template-instance** (S uit VSA, A/T/B uit
      template) — zie [mapping-vsa.md](mapping-vsa.md);
      implementatie [`template_instance.py`](https://github.com/orthodox-groningen/VSA-tooling/blob/main/src/vsa/template_instance.py)
      (geen “pad B”-jargon meer).
- [x] Hoogte-mismatch → harde `TemplateInstanceError` (H9); geen stil hold.
- [x] Tropaar-toon-4 corpus-pipeline: `.vsa` / `.mscz` / `.mxl` + lokale PDF;
      CLI `scripts/render_tropaar_toon4_corpus.py`.
- [x] Recite-print (MSCZ): ≥3 ongemarkeerde recite → `||O||` + laatste als
      kwart; **VSA-scopes** eigen noten; Coria-MXL zonder collapse.
- [x] Instance-layout: één maat per strofe; MS4-maatstrepen via voice-
      `<BarLine visible=0>`; geen dots op `||O||`; MuseScore
      `<position>left</position>` voor recite-lyrics.
- [x] Valkuilen-doc + links in README / AGENTS / MkDocs:
      [rendering-pitfalls.md](rendering-pitfalls.md).
- [x] PDF-export uit git geweerd (afgeleide); lokaal via `--pdf-only`.
- [x] Spot-check PDF’s tropaar-toon-4 corpus: recite/scopes/layout kloppen
      (menselijke audit).

---

## Werklijst (volgende chat — ongeordend)

### Terminologie / org

- [ ] Eventueel org-brede namen via glossary-PR op **bron** (als termen
      repo-overschrijdend moeten zijn).

### Templates / pitches

- [ ] **Tenor-octaaf openingsakkoord (tropaar toon 4):** in `template.yaml`
      staat tenor vaak als `sol-1`. Controleren tegen het bronblad/PDF of dat
      het juiste oktaaf is t.o.v. `do: F4` (historisch twijfelpunt was
      klinkend C3 vs C4). Zo nodig YAML + corpus-export bijwerken.
- [ ] Overige templates (niet alleen tropaar-toon-4): graden/`do`/`mode`
      provisional tot PDF-/partituur-audit.
- [ ] **`mode` in template-YAML vs VSA:** vastleggen welke waarden mogen
      (`major` / `minor` / …) en die laten matchen met wat de VSA-parser/
      pitch-resolver accepteert — geen stille afwijking tussen template en
      `.vsa`-frontmatter.
- [ ] **Sequence-form en aantal tekstregels:** bij
      `sequence: ["1", "2", "3"]` horen precies drie VSA-regels (`*`-frasen).
      Nu handmatig; later valideren of duidelijke fout als het aantal niet
      klopt. (Bij `text_mapping` / `mapping_plans` hetzelfde idee:
      lengte tekst ↔ gevraagde frase-reeks.)
- [ ] `l.lgr.`-anker in stichier-template + event-mapping (H8): anker markeert
      start van een slotmelisma; dat event **plus alle volgende** events in
      de frase vallen op de laatste VSA-syllabe.

### Semantiek / mapping

- [ ] Stemmen met onderling verschillende ritmes (buiten parallel
      split/merge); dat doen we pas als de noodzaak hiervoor is gebleken.
- [ ] **Parallelle template-sporen (`of`):** één frase mag 2+ cadens-/slot-
      paden (bijv. `mi–re–mi` **of** `mi–fa–mi`). VSA kiest impliciet;
      onbekend pad → hoogte-mismatch. Meerdere [uitvoeringsvorm](@)-en in
      één template zonder aparte YAML’s.
- [ ] **`open` vs eerste recite:** template heeft vaak twee events (open +
      recite) op dezelfde toon. Beslissen/documenteren: blijven het twee
      events (mapper slaat open over als VSA meteen reciteert — huidig
      gedrag H1), of mag YAML één samengevoegd event zijn? Geen stille
      dubbele noot in de partituur.
- [ ] Normalisatie anker-labels (`e. st.` vs `e.st.`). Canoniek overal
      `e.st.` (en dezelfde vorm voor `l.st.`, `vl.st.`, `l.lgr.`).
- [x] **Instance-foutmeldingen zoals `vsa validate`:** compacte + uitgebreide
      vorm (`format_compact` / `format_lines`); frase + syllabe + lyric;
      foutcode; wat er mis is; `Hint:`-herstel. Bronpad/regel/kolom zodra
      de VSA-noten posities krijgen. Geldt voor H7/H9 e.d.
- [ ] **Mapping-hypotheses H4–H7 echt in de instance-mapper** (zie
      [mapping-vsa.md](mapping-vsa.md)):
      - **H4** optional-events: mee als VSA dat slot gebruikt, anders weg
        (prefix-link + optional tussenslots) — deels gedaan;
      - **H5** duur split/merge: VSA-S stuurt; A/T/B parallel — nog open;
      - **H6** hold + vullen van opeenvolgende zelfde-S-slots — gedaan;
      - **H7** andere toon overslaan alleen via `optional`; verplicht ongebruikt
        aan het eind → fout; rest van ondergevulde zelfde-S-run mag weg —
        gedaan.

### Tooling / export

- [ ] CLI `vsa template validate`.
- [ ] MusicXML-export vanuit **formule**-template (+ optioneel VSA-lyrics),
      naast bestaande instance-export.
- [ ] Andere genres/tonen: zelfde instance-pipeline als tropaar-toon-4
      (corpus + render-script of generiek maken).

### Layout / print (polish)

- [ ] Lyric-dichtheid: krappe overgangen cadens ↔ volgende recite (soms
      bijna plakken); spacer-/`lyricsMinDistance`-fijnregeling.
- [ ] Visuele check of melisma-extender onder recite-tekst storend is;
      eventueel ticks/spacers bijstellen.
- [ ] **Recite-tekst t.o.v. `||O||`:** de **eerste** lettergreep van de
      tekst onder de reciteertoon uitlijnen op de nootkop (gecentreerd op
      die noot); de rest van de recitaltekst volgt naar rechts.
- [ ] **Spatiering binnen recite-tekst:** geen grote lege gap tussen het
      einde van de recitaltekst en de volgende (cadens)lettergreep.
      Die “rest-ruimte” verdelen over de spaties *tussen* de lettergrepen
      van de recitaltekst, zodat de tekst visueel gelijkmatig doorloopt.
- [ ] Formuleblad (`template.mscz`) vs instance: documenteren wat wel/niet
      in git hoort en hoe CI/lokaal regenereert.

### Publicatie / UX

- [ ] **Inline gerenderde VSA in proza:** toon-aanduiding e.d. (`T.4`) hoort
      niet als zingbare tekst in de VSA-regel. Klein VSA-fragment (alleen
      hoogtemarkering + eventueel `Amen`) in markdown/proza — tablet/pc/
      telefoon én print — zonder SVG/lyric-pipeline die letters als
      syllaben meeneemt.
