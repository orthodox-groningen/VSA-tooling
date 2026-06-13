# VSA Layout Algorithm Specification (Draft 1)

## 1. Doel

Dit document beschrijft het formele layout-algoritme voor VSA-rendering.

Het algoritme beschrijft de stap van:

```text
VSA AST
→ render-units
→ muzikale posities
→ glyphlayout
→ wrapping
→ SVG-output
```

Dit document vult aan:

- `vsa-svg-rendering-spec.md`
- `vsa-glyph-model.md`
- `vsa-glyph-layout-rules.md`
- `vsa-svg-dom-structure.md`
- `vsa-rendering-config-model.md`

De focus ligt op een praktische, goed leesbare renderer voor scherm en website.

---

# 2. Hoofdprincipes

De renderer moet:

- tekst leesbaar houden;
- glyphs dicht bij de tekst plaatsen;
- glyphs niet laten overlappen;
- render-units ondeelbaar houden;
- links uitlijnen als default;
- deterministic output geven;
- configuratie vóór rendering valideren.

De renderer is niet bedoeld als professionele drukwerk-engine.

---

# 3. Renderpipeline

De renderer doorloopt conceptueel deze fasen:

```text
1. Config laden en valideren
2. AST ontvangen
3. Render-units bouwen
4. Muzikale posities bepalen
5. Tekst meten
6. Glyphgroepen bouwen
7. Minimale breedtes bepalen
8. Anchors oplossen
9. Collisiondetectie uitvoeren
10. Wrapping toepassen
11. Regels positioneren
12. SVG-DOM genereren
```

Elke fase mag extra debug-informatie produceren als een debug-theme actief is.

---

# 4. Fase 1: config laden en valideren

Voor rendering begint, wordt de effectieve configuratie bepaald.

Volgorde:

```text
ingebouwde defaults
→ theme
→ projectconfig
→ user override
→ CLI override
```

De effectieve configuratie wordt gevalideerd.

Ongeldige configuratie stopt rendering met een duidelijke configuratiefout.

Voorbeelden van ongeldige configuratie:

- negatieve glyphbreedte;
- onbekende alignmentwaarde;
- lege kleurwaarde;
- wraptoken dat bestaande VSA-syntax breekt;
- line-gap kleiner dan minimum;
- glyph met nulbreedte.

---

# 5. Fase 2: AST ontvangen

De renderer werkt niet rechtstreeks op ruwe tekst, maar op de geparseerde VSA-structuur.

De AST bevat betekenisvolle constructies zoals:

- vrije tekst;
- zangelement;
- pitchmarker;
- modifiers;
- alignment-markers.

De renderer mag geen syntax herstellen.

Syntaxfouten horen vóór rendering te zijn afgehandeld door parser en validator.

---

# 6. Fase 3: render-units bouwen

Een render-unit is een ondeelbaar visueel layout-element.

Voorbeelden:

```text
vrije tekst
zangelement met glyphs
pitchmarker
non-breaking group
wraptoken
```

Render-units worden niet intern gesplitst tijdens wrapping.

Voorbeeld:

```text
{/ver}
```

blijft altijd één render-unit.

Ook dit blijft één render-unit:

```text
{\&/&/trou-.&.&_}
```

---

# 7. Fase 4: muzikale posities bepalen

Voor SVG-rendering is een muzikale positie een horizontale plaats waarop één glyph of glyphgroep wordt gecentreerd.

De renderer gebruikt muzikale posities voor:

- bovenglyphplaatsing;
- onderglyphplaatsing;
- collisiondetectie;
- minimale breedte van zangelementen;
- alignment-groepen;
- toekomstige MusicXML- en polyfonievoorbereiding.

Een muzikale positie is niet noodzakelijk hetzelfde als:

- een letter;
- een lettergreep;
- een MusicXML-noot;
- een toekomstige SATB-syncpositie.

---

# 8. Fase 5: tekst meten

De renderer meet tekst met:

- actief font;
- actieve font-size;
- actuele renderer-context.

Tekstmeting moet deterministic zijn binnen dezelfde omgeving.

De renderer mag ligatures standaard uitschakelen om voorspelbare meting te krijgen.

Fallbackfonts moeten expliciet in de configuratie kunnen worden opgenomen.

---

# 9. Fase 6: glyphgroepen bouwen

Modifiers worden vertaald naar abstracte glyphgroepen.

Voorbeelden:

| VSA | Renderbetekenis |
|---|---|
| `/` | bovenglyph voor stijgende beweging |
| `\` | bovenglyph voor dalende beweging |
| `///` | één samengestelde EHM-glyph |
| `_` | onderglyph / lengte-indicatie |
| `&` | alignmentrelatie binnen glyphgroep |

Alignment-markers creëren standaard geen zware verbindingslijn.

Defaultinterpretatie:

```text
& = compacte gekoppelde glyphgroep
```

Gekoppelde glyphs blijven afzonderlijk herkenbaar.

---

# 10. Fase 7: minimale breedtes bepalen

De minimale breedte van een muzikale positie is:

```text
max(tekstdeelbreedte, glyphbreedte + marge)
```

De minimale breedte van een zangelement is de som van de benodigde posities.

Gevolgen:

- tekst wordt niet samengedrukt;
- glyphs overlappen niet;
- brede glyphstructuren kunnen een zangelement breder maken dan de tekst;
- wrapping gebeurt tussen render-units als de unit niet meer past.

---

# 11. Fase 8: anchors oplossen

Elke renderregel heeft:

- baseline;
- text-top;
- text-bottom;
- line-box.

Glyphs worden geplaatst ten opzichte van anchors.

Minimale anchors:

| Anchor | Betekenis |
|---|---|
| baseline | lijn waarop tekst rust |
| text-top | bovenkant tekst-box |
| text-bottom | onderkant tekst-box |
| position-center | horizontaal midden van muzikale positie |
| unit-left | linkerrand render-unit |
| unit-right | rechterrand render-unit |

---

# 12. Fase 9: collisiondetectie

Collisiondetectie controleert dat tekst, glyphs en units elkaar niet visueel hinderen.

Verboden overlap:

- glyph met glyph;
- glyph met tekst;
- glyph met pitchmarker;
- aangrenzende render-units;
- glyphs tussen regels.

Als collision dreigt, gebruikt de renderer deze volgorde:

```text
1. compacte glyphmetriek toepassen
2. spacing binnen render-unit vergroten
3. render-unit naar volgende regel verplaatsen
4. overflow fallback toepassen
```

---

# 13. Fase 10: wrapping

Wrapping gebeurt alleen tussen render-units.

Prioriteiten:

```text
forced break
→ non-breaking group
→ preferred break
→ natuurlijke afbreekpunten
→ overflow fallback
```

Forced breaks winnen altijd van automatische layout.

Non-breaking groups worden niet intern gesplitst.

Als een non-breaking group breder is dan de maximale regelbreedte, gebruikt de renderer overflow fallback.

---

# 14. Fase 11: regels positioneren

Default regeluitlijning:

```text
left
```

Optioneel:

- right;
- center;
- justify.

Bij justify mogen alleen inter-unit gaps worden uitgerekt.

Niet uitrekken:

- glyphgroepen;
- pitchmarkers;
- interne glyphspacing;
- tekst binnen zangelementen.

---

# 15. Fase 12: SVG-DOM genereren

De renderer genereert SVG volgens `vsa-svg-dom-structure.md`.

Minimaal:

```xml
<svg>
  <g class="vsa-score">
    <g class="vsa-line">
      <g class="vsa-unit">
        ...
      </g>
    </g>
  </g>
</svg>
```

Render-units krijgen eigen `<g>`-groepen.

Glyphs krijgen semantische CSS-klassen.

---

# 16. Renderer diagnostics

De renderer mag diagnostics produceren.

Voorbeelden:

| Code | Betekenis |
|---|---|
| `VSA-RENDER-OVERFLOW` | render-unit past niet binnen max-line-width |
| `VSA-RENDER-COLLISION` | collision kon niet automatisch opgelost worden |
| `VSA-RENDER-UNSUPPORTED-GLYPH` | glyphvorm bestaat niet in theme |
| `VSA-RENDER-CONFIG-ERROR` | ongeldige renderingconfiguratie |

Default:
- overflow is warning;
- configfouten zijn error;
- unsupported glyph is error of warning afhankelijk van fallback.

---

# 17. Determinisme

Bij gelijke input, configuratie en fontomgeving moet de SVG-output gelijk zijn.

Dat is belangrijk voor:

- CI;
- regressietests;
- Git diffs;
- documentatievoorbeelden.

---

# 18. Open ontwerpvragen

Nog nader uit te werken:

- exacte text measurement API;
- debug-theme;
- overflowvisualisatie;
- caching;
- printprofiel;
- MusicXML-layoutmapping.
