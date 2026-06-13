# VSA Glyph Model Specification (Draft 1)

## 1. Doel

Dit document beschrijft het abstracte glyphmodel voor VSA-rendering.

Het glyphmodel vormt de brug tussen:

* de VSA-semantiek;
* layoutberekening;
* concrete SVG-rendering;
* toekomstige exportformaten zoals MusicXML.

Het glyphmodel definieert:

* glyph-typen;
* positionering;
* metriek;
* anchors;
* verbindingen;
* schaalgedrag;
* theming;
* configuratie.

Het glyphmodel definieert niet:

* parsergedrag;
* syntax;
* semantische validatie.

Zie:

* [VSA-taalspecificatie](vsa-spec-v1.md)
* [VSA SVG Rendering Specification](vsa-svg-rendering-spec.md)

---

# 2. Architectuur

## 2.1 Drie renderlagen

De renderer bestaat conceptueel uit drie lagen:

```text id="a7zqfc"
VSA AST
→ abstract glyph layout
→ concrete SVG primitives
```

### Laag 1 — Semantische representatie

De parser en AST kennen alleen muzikale intentie.

Voorbeelden:

* stijgend;
* dalend;
* vlak;
* verlengd;
* verbonden;
* pitch-referentie.

Deze laag kent geen:

* pixels;
* SVG paths;
* kleuren;
* fonts.

---

### Laag 2 — Abstract glyphmodel

De renderer vertaalt semantiek naar abstracte glyph-objecten.

Voorbeelden:

* `UpperGlyph`
* `LowerGlyph`
* `ConnectorGlyph`
* `PitchMarkerGlyph`

Deze laag definieert:

* vormcategorieën;
* metriek;
* anchors;
* verbindingen;
* layoutgedrag.

---

### Laag 3 — Concrete rendering

Pas in deze laag ontstaan concrete SVG-elementen zoals:

```text id="3rm2ti"
<line>
<path>
<polyline>
<circle>
```

Deze laag is renderer-specifiek.

---

# 3. Muzikale posities

## 3.1 Basisprincipe

De renderer werkt primair met muzikale posities en niet met letters.

Voorbeeld:

```text id="f8x1n7"
{/He_}
```

heeft:

* één muzikale positie;
* een tekstbreedte;
* een glyphstructuur.

---

## 3.2 Positie-eenheden

Elke muzikale positie heeft:

* een horizontale breedte;
* een center-anchor;
* een optische bounding box.

Positiebreedte hoeft niet gelijk te zijn aan tekstbreedte.

---

## 3.3 Positiegroepen

Verbonden glyphgroepen kunnen meerdere muzikale posities omvatten.

Voorbeeld:

```text id="yxq3u3"
{/&/&\He_&_&_}
```

vormt één verbonden glyphgroep.

---

# 4. Glyphfamilies

## 4.1 Upper glyphs

Upper glyphs representeren:

* stijging;
* daling;
* vlakke beweging;
* korte ornamenten.

Bronsymbolen:

* `/`
* `\`
* `-`
* `~`

Visuele eigenschappen:

* compact;
* accentachtig;
* dicht boven de tekst.

---

## 4.2 Lower glyphs

Lower glyphs representeren:

* lengte;
* duur;
* onderstructuren.

Visuele eigenschappen:

* underline-achtig;
* compact;
* dicht onder de tekst.

Lower glyphs mogen:

* korter zijn dan de volledige positiebreedte;
* afgeronde uiteinden gebruiken;
* variabele diktes gebruiken.

---

## 4.3 Connector glyphs

Connector glyphs ontstaan uit alignment-markers (`&`).

Connector glyphs:

* verbinden omliggende glyphs;
* creëren visuele continuïteit;
* beïnvloeden layout.

Connector glyphs zijn geen zelfstandige muzikale posities.

Voorbeeld:

```text id="1o4h5l"
{/&/&\He_&_&_}
```

Hier ontstaan:

* meerdere upper glyphs;
* meerdere lower glyphs;
* connectorlijnen tussen de glyphs.

---

## 4.4 Structural glyphs

Structural glyphs representeren:

* pitch-markers;
* wraptokens;
* layoutmarkeringen;
* toekomstige exporthints.

Voorbeelden:

* `[:]`
* `[/]`
* `[/?]`

Niet alle structural glyphs hoeven zichtbaar te renderen.

---

# 5. Glyph anchors

## 5.1 Doel

Glyphs worden relatief gepositioneerd via anchors.

Dit voorkomt:

* hardcoded pixelplaatsing;
* typografische inconsistentie;
* schaalproblemen.

---

## 5.2 Standaard anchors

De renderer ondersteunt minimaal:

| Anchor          | Betekenis                       |
| --------------- | ------------------------------- |
| baseline        | tekstbaseline                   |
| text-top        | bovenkant van tekst             |
| text-bottom     | onderkant van tekst             |
| position-center | centrum van muzikale positie    |
| glyph-center    | centrum van glyph               |
| upper-anchor    | default anchor voor bovenglyphs |
| lower-anchor    | default anchor voor onderglyphs |

---

## 5.3 Anchor-relaties

Glyphs worden relatief geplaatst ten opzichte van anchors.

Voorbeeld:

```text id="mqzq6j"
upper-glyph.y = text-top + upper-offset
```

---

# 6. Glyphmetriek

## 6.1 Relatieve metriek

Glyphs gebruiken relatieve metriek.

Niet aanbevolen:

* vaste pixels;
* absolute SVG-afstanden.

Aanbevolen:

* relatieve schaalfactoren;
* font-gerelateerde units;
* renderer-scalars.

---

## 6.2 Glyph properties

Elke glyph kan eigenschappen hebben zoals:

```text id="jj8h6f"
width
height
stroke-width
offset-x
offset-y
opacity
join-style
cap-style
```

---

## 6.3 Voorbeeldconfiguratie

```toml id="q1ovql"
[rendering.svg.glyphs.upper.rise]
width-factor = 0.65
height-factor = 0.80
stroke-width = 1.2
offset-y = -7
```

---

# 7. Glyphlayout

## 7.1 Layoutfasen

Glyphlayout gebeurt in meerdere fasen:

```text id="3ncl1p"
AST
→ musical positions
→ glyph grouping
→ anchor resolution
→ spacing
→ SVG output
```

---

## 7.2 Optische compensatie

De renderer mag optische compensatie toepassen.

Voorbeelden:

* iets bredere glyphs bij kleine fonts;
* verticale correctie bij cursieve fonts;
* smallere connectors bij dichte tekst.

---

## 7.3 Compactheid

Glyphlayout moet:

* compact blijven;
* visueel luchtig blijven;
* niet botsen met omliggende regels.

---

# 8. Scaling

## 8.1 Schaalgedrag

Glyphs schalen relatief mee met:

* font-size;
* DPI;
* exportresolutie;
* viewportgrootte.

---

## 8.2 Minimumgroottes

Renderers mogen minimale:

* lijndiktes;
* glyphgroottes;
* offsets;

afdwingen om leesbaarheid te behouden.

---

# 9. Theming

## 9.1 Renderer-themes

Dezelfde VSA-inhoud moet met verschillende renderstijlen gerenderd kunnen worden.

Voorbeelden:

* classic;
* minimal;
* liturgikon;
* debug;
* high-contrast.

---

## 9.2 Theme-inhoud

Een theme kan bepalen:

* glyphvormen;
* kleuren;
* spacing;
* offsets;
* stroke-stijlen;
* connectorgedrag;
* pitch-markerstijl.

---

## 9.3 Theme-overrides

Themes mogen:

* defaults leveren;
* gedeeltelijk overridden worden;
* gecombineerd worden met user-config.

---

# 10. Configureerbaarheid

## 10.1 Configuratieprincipes

Glyphrendering moet configureerbaar zijn.

Gebruikers moeten onder andere kunnen aanpassen:

* breedte;
* hoogte;
* offsets;
* kleuren;
* lijnstijlen;
* connectorstijl;
* glyphvormen.

---

## 10.2 Geldige configuratie

Glyphconfiguratie moet:

* vóór gebruik gevalideerd worden;
* parserambiguïteit vermijden;
* rendercrashes voorkomen;
* consistente anchors behouden.

Bij ongeldige configuratie moet:

* een duidelijke configuratiefout ontstaan;
* rendering stoppen;
* de foutlocatie vermeld worden.

---

## 10.3 SVG-shape overrides

Renderers mogen alternatieve SVG-vormen ondersteunen.

Voorbeelden:

* custom SVG paths;
* alternatieve lijnvormen;
* ornamentsets;
* kalligrafische glyphs.

Dit vereist een abstract glyphmodel en geen hardcoded SVG-primitives.

---

# 11. Toekomstige uitbreidingen

## 11.1 MusicXML

Het glyphmodel moet later gekoppeld kunnen worden aan:

* MusicXML;
* maatstructuren;
* frasegrenzen;
* systeemindeling.

Daarom moeten glyphs semantisch interpreteerbaar blijven.

---

## 11.2 Multi-voice rendering

Toekomstige renderers kunnen:

* meerdere stemmen;
* syncgroepen;
* gedeelde muzikale posities;

ondersteunen.

---

## 11.3 Interactieve rendering

Toekomstige SVG-renderers kunnen:

* hoverinformatie;
* debugging overlays;
* clickable glyphs;
* synchronized playback;

ondersteunen.

Het glyphmodel moet dit niet blokkeren.

---

# 12. Open ontwerpvragen

Nog nader te bepalen:

* exacte glyphvormen;
* connectoralgoritmen;
* automatische optische compensatie;
* glyphcollision-resolutie;
* printoptimalisatie;
* kalligrafische rendering;
* MusicXML-mappingdetails;
* SATB-layoutregels.
