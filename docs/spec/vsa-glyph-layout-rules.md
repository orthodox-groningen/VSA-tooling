# VSA Glyph Layout Rules (Draft 2)

## 1. Doel

Dit document beschrijft de layoutregels voor VSA-glyphs.

Het document vult aan:

- `vsa-svg-rendering-spec.md`
- `vsa-glyph-model.md`
- `vsa-spec-v1.md`

De regels in dit document zijn bedoeld als directe basis voor SVG-rendering.

De focus ligt op:
- duidelijke leesbaarheid;
- bruikbaarheid op scherm;
- bruikbaarheid op enige afstand;
- robuuste automatische layout;
- configureerbare stijl.

Deze specificatie is niet bedoeld voor professionele drukwerktypografie.

---

# 2. Glossary

| Term | Betekenis |
|---|---|
| VSA | De tekstuele notatie voor zangtekst, pitchmarkers en muzikale modifiers |
| Renderer | Het onderdeel dat VSA omzet naar zichtbare output, bijvoorbeeld SVG |
| SVG | Scalable Vector Graphics; het uitvoerformaat voor schaalbare tekeningen |
| Glyph | Een zichtbaar teken of vormpje dat door de renderer wordt getekend |
| EHM | Een elementaire hoogtemodifier, bijvoorbeeld `/`, `\` of `///` |
| ELM | Een elementaire lengtemodifier, bijvoorbeeld `_` |
| Bovenglyph | Een glyph boven de gezongen tekst |
| Onderglyph | Een glyph onder de gezongen tekst |
| Pitchmarker | Een constructie zoals `[:]`, `[/:]` of `[\\:]` |
| Zangelement | Een VSA-constructie tussen `{` en `}`, bijvoorbeeld `{/Heer_}` |
| Render-unit | Een ondeelbaar visueel element voor layout en wrapping |
| Glyphgroep | Een groep glyphs die samen bij één render-unit horen |
| Alignment-marker | Het `&`-teken dat glyphs binnen een zangelement visueel koppelt |
| Baseline | De denkbeeldige lijn waarop tekst rust |
| Text box | De visuele ruimte die de tekst inneemt |
| Collision | Een botsing of overlap tussen tekst, glyphs of render-units |
| Wrapping | Het afbreken van render-units naar een volgende regel |
| Overflow | Situatie waarin een render-unit breder is dan de beschikbare regelbreedte |

---

# 3. Visuele uitgangspunten

De VSA-rendering volgt het compacte karakter van Liturgikon-achtige voorbeelden.

Daarin staan hoogte- en lengtemarkeringen:
- dicht bij de tekst;
- compact;
- optisch licht;
- duidelijk gekoppeld aan de betreffende lettergreep of tekstpositie.

Glyphs moeten de tekst ondersteunen, niet domineren.

De belangrijkste visuele prioriteiten zijn:
1. tekst blijft goed leesbaar;
2. glyphs zijn duidelijk herkenbaar;
3. glyphs zitten dicht genoeg op de tekst om erbij te horen;
4. glyphs overlappen niet;
5. de layout blijft compact.

---

# 4. Coordinate system en anchors

## 4.1 Praktische keuze

De renderer gebruikt een baseline-gebaseerd coordinate system.

Elke renderregel heeft:
- een baseline;
- een text-top;
- een text-bottom;
- een line-box.

Dit is voldoende nauwkeurig voor de huidige toepassing en voorkomt onnodige typografische complexiteit.

## 4.2 Anchors

Glyphs worden relatief aan tekst-anchors geplaatst.

Minimale anchors:

| Anchor | Betekenis |
|---|---|
| baseline | lijn waarop tekst rust |
| text-top | bovenkant van de tekst-box |
| text-bottom | onderkant van de tekst-box |
| position-center | horizontaal midden van de muzikale positie |
| unit-left | linkerrand van de render-unit |
| unit-right | rechterrand van de render-unit |

## 4.3 Bovenglyph-positionering

Bovenglyphs worden geplaatst:
- boven de tekst-box;
- dicht bij de tekst;
- relatief aan `text-top`.

Default:

```toml
[rendering.svg.glyphs.upper]
offset-y = -0.30
```

`offset-y` is relatief aan de fontgrootte.

Negatieve waarden staan boven de tekst.

## 4.4 Onderglyph-positionering

Onderglyphs worden geplaatst:
- onder de tekst;
- dicht bij de baseline;
- zonder letterstaarten te kruisen.

Default:

```toml
[rendering.svg.glyphs.lower]
offset-y = 0.18
```

De renderer mag de onderglyph iets lager plaatsen als het font veel descenders heeft.

---

# 5. Render-units

Voor layout gebruikt de renderer ondeelbare render-units.

Voorbeelden:

```text
vrije tekst
zangelement met glyphs
pitchmarker
non-breaking group
wraptoken
```

Een zangelement met glyphs is één render-unit.

Voorbeeld:

```text
{/ver}
```

mag niet over twee regels worden verdeeld.

Ook een complex zangelement blijft ondeelbaar:

```text
{\&/&/trou-.&.&_}
```

Pitchmarkers zijn ook ondeelbare render-units.

Voorbeeld:

```text
[/:]
```

mag niet gesplitst worden.

---

# 6. Muzikale positie

## 6.1 Renderingdefinitie

Voor SVG-rendering is een muzikale positie de horizontale plaats waarop één glyph of glyphgroep wordt gecentreerd ten opzichte van tekst.

Een muzikale positie is dus een layoutbegrip.

Het is niet noodzakelijk hetzelfde als:
- een letter;
- een lettergreep;
- een MusicXML-noot;
- een toekomstige SATB-syncpositie.

## 6.2 Waarvoor gebruikt de renderer muzikale posities?

De renderer gebruikt muzikale posities om te beslissen:
- waar bovenglyphs komen;
- waar onderglyphs komen;
- hoe breed een zangelement minimaal moet zijn;
- waar alignment-groepen optisch worden geplaatst;
- of glyphs elkaar raken;
- of een render-unit te breed wordt voor de regel.

## 6.3 Breedte van een muzikale positie

De breedte van een muzikale positie wordt bepaald door:

```text
max(tekstdeelbreedte, glyphbreedte + minimale marge)
```

Dus:
- korte tekst met brede glyph krijgt extra ruimte;
- lange tekst met smalle glyph wordt niet samengedrukt;
- glyphs mogen niet overlappen.

## 6.4 Breedte van een render-unit

De breedte van een zangelement is de som van de benodigde muzikale posities.

Als de glyphstructuur breder is dan de tekst:
- wordt de render-unit breder;
- blijft de tekst leesbaar;
- wordt wrapping toegepast als de render-unit niet meer op de regel past.

---

# 7. Wrapping

De renderer mag afbreken tussen render-units volgens de wrapping-regels uit de SVG-rendering-spec.

Een render-unit wordt niet intern gesplitst.

Als een render-unit te breed is voor de resterende regelruimte, wordt deze naar de volgende regel verplaatst.

Als een render-unit op zichzelf breder is dan de maximale regelbreedte, gebruikt de renderer fallbackgedrag.

Default fallback:

```text
overflow toestaan + warning diagnostic
```

Andere mogelijke fallbackstrategieën:
- schaalreductie;
- overflow-indicator;
- debugmelding;
- expliciete foutmelding.

---

# 8. Glyph-overlap

Glyphs mogen standaard niet overlappen.

Dit geldt voor:
- bovenglyphs onderling;
- onderglyphs onderling;
- bovenglyphs en tekst;
- onderglyphs en tekst;
- pitchmarkers en tekst;
- glyphs van aangrenzende render-units.

Als overlap dreigt, probeert de renderer in deze volgorde:

1. compacte glyphmetriek toepassen;
2. horizontale spacing binnen de render-unit vergroten;
3. render-unit naar de volgende regel verplaatsen;
4. fallbackgedrag toepassen.

De renderer mag glyphs niet laten samenvallen om ruimte te besparen.

---

# 9. Elementaire hoogtemodifiers en stacking

## 9.1 Eén EHM is één glyph

Een EHM wordt als één glyph gerenderd.

Voorbeeld:

```text
/
```

is één glyph.

Ook dit is één EHM en dus één glyph:

```text
///
```

Het is dus niet een stack van drie losse glyphs.

## 9.2 Leesbaarheid

Een glyph voor `///` moet duidelijk herkenbaar zijn, ook op enige afstand.

Default rendering mag bestaan uit drie duidelijk onderscheidbare schuine streepjes.

Toekomstige themes mogen alternatieve glyphvormen gebruiken.

Voorbeeld van een mogelijk alternatief:

```text
/3
```

of een compactere gestileerde vorm.

Deze alternatieven zijn niet voor de eerste renderer vereist, maar het glyphmodel mag ze niet blokkeren.

## 9.3 Geen whitespace-stacking

Een constructie zoals:

```text
~~~
```

wordt niet als zinvolle EHM-stack beschouwd.

Als `~` later een betekenis heeft, moet die betekenis afzonderlijk worden gespecificeerd.

Voor nu geldt:
- `///` kan één samengestelde EHM-glyph zijn;
- `~~~` is geen stapel van whitespace-glyphs.

---

# 10. Gekoppelde glyphs en alignment-markers

## 10.1 Betekenis van `&`

Alignment-markers (`&`) koppelen glyphs visueel.

Default betekent `&`:

```text
compacte gekoppelde glyphgroep
```

Niet:

```text
teken altijd een expliciete connectorlijn
```

## 10.2 Visueel gedrag

Gekoppelde glyphs:
- blijven afzonderlijk herkenbaar;
- staan compact bij elkaar;
- vormen één optische groep;
- worden samen gewrapped;
- worden samen gecontroleerd op collisions.

Gekoppelde glyphs mogen niet:
- volledig samenvallen;
- versmelten tot één onleesbare lijn;
- visueel losraken van hun groep.

## 10.3 Voorbeeld

```text
{\&/ver}
```

bevat gekoppelde hoogte-informatie.

```text
{\&/&/trou-.&.&_}
```

bevat meerdere gekoppelde glyphs die als groep moeten ogen, maar waarvan de afzonderlijke glyphposities zichtbaar blijven.

## 10.4 Connectorvorm

De default connectorvorm is impliciet.

Dat wil zeggen:
- de verbinding ontstaat door nabijheid, gedeelde uitlijning en compacte spacing;
- er wordt standaard geen zware expliciete verbindingslijn getekend.

Themes mogen later expliciete connectorlijnen toevoegen.

---

# 11. Bovenglyphs

Bovenglyphs staan dicht boven de tekst.

Visuele regels:
- ze hebben het karakter van kleine accenttekens;
- ze zijn korter dan de volledige tekstbreedte;
- ze zweven niet hoog boven de tekst;
- samengestelde bovenglyphs blijven compact;
- onderscheidbaarheid gaat vóór extreme compactheid.

Default richtwaarden:

```toml
[rendering.svg.glyphs.upper]
width-factor = 0.60
offset-y = -0.30
stroke-width-factor = 0.055
```

Waarbij waarden relatief zijn ten opzichte van de fontgrootte of positiehoogte.

---

# 12. Onderglyphs

Onderglyphs staan dicht onder de tekst.

Visuele regels:
- ze lijken op onderstreping;
- ze kruisen geen letterstaarten;
- ze zijn korter dan de volledige positiebreedte;
- ze blijven optisch verbonden met de tekst.

Default richtwaarden:

```toml
[rendering.svg.glyphs.lower]
width-factor = 0.80
offset-y = 0.18
stroke-width-factor = 0.055
```

De renderer mag onderglyphs iets lager plaatsen bij fonts met lange descenders.

---

# 13. Pitchmarkers

## 13.1 Rendering

Pitchmarkers worden gerenderd als compacte tekstachtige symbolen.

Een pitchmarker bestaat visueel uit:
- een korte horizontale markerlijn;
- optioneel een EHM-glyph erboven.

Voorbeeld:

```text
[:]
```

is een compacte horizontale marker.

Voorbeeld:

```text
[/:]
```

bestaat uit:
- horizontale marker;
- bovenglyph voor `/`.

## 13.2 Positionering

De EHM-glyph van een pitchmarker staat lateraal en verticaal zoals een bovenglyph, maar hoort bij de pitchmarker zelf.

De EHM-glyph van een pitchmarker komt visueel later dan de bovenglyphs boven gewone tekst.

Dat betekent:
- pitchmarker-glyphs mogen iets hoger of anders gecentreerd worden;
- ze blijven compact;
- ze mogen niet vastplakken aan tekst.

## 13.3 Context

Pitchmarkers kunnen in verschillende contexten verschillende semantische betekenis hebben.

Voor SVG-rendering geldt:
- als er een pitchmarker staat, render dan het compacte symbool;
- interpreteer niet de volledige muzikale betekenis;
- laat validatie aan validatorregels;
- laat MusicXML-betekenis aan MusicXML-exportregels.

## 13.4 Spacing

Pitchmarkers zijn ondeelbare render-units.

Default spacing:

```toml
[rendering.svg.pitch-marker]
gap-before = 0.35
gap-after = 0.35
dash-width-factor = 0.45
```

De horizontale markerlijn is compact.

---

# 14. Spacing tussen render-units

De renderer gebruikt minimale horizontale spacing tussen render-units.

Default:

```toml
[rendering.svg.spacing]
text-gap = 0.20
scope-gap = 0.12
pitch-marker-gap = 0.35
```

Deze waarden zijn relatief ten opzichte van de fontgrootte.

Spacing mag worden vergroot om overlap te voorkomen.

Spacing mag niet worden uitgerekt om regels tweezijdig uit te vullen, tenzij expliciet geconfigureerd.

---

# 15. Regelafstand

Regelafstand moet voldoende ruimte bieden voor:
- bovenglyphs;
- onderglyphs;
- samengestelde glyphs;
- pitchmarkers.

Default:

```toml
[rendering.svg.lines]
line-gap = 1.35
min-line-gap = 1.15
```

De regelafstand is configureerbaar.

---

# 16. Layoutprioriteiten

Bij conflicten gebruikt de renderer deze prioriteit:

1. syntax correct renderen;
2. tekst leesbaar houden;
3. glyphs niet laten overlappen;
4. render-units ondeelbaar houden;
5. compacte layout behouden;
6. regelbreedte respecteren.

Dit betekent dat de renderer liever een regel eerder afbreekt dan glyphs laat overlappen.

---

# 17. Debug rendering

Een debug-theme mag tonen:
- render-unit boundaries;
- glyph bounding boxes;
- anchors;
- collision boxes;
- wrap candidates;
- overflow;
- muzikale posities.

Dit is bedoeld voor ontwikkeling en correctie van praktijkvoorbeelden.

---

# 18. Configuratie

Glyph-layout wordt configureerbaar via `vsa.toml`.

Voorbeeld:

```toml
[rendering.svg]
font-size = 24
alignment = "left"
max-line-width = 900

[rendering.svg.spacing]
text-gap = 0.20
scope-gap = 0.12
pitch-marker-gap = 0.35

[rendering.svg.lines]
line-gap = 1.35
min-line-gap = 1.15

[rendering.svg.glyphs.upper]
width-factor = 0.60
offset-y = -0.30
stroke-width-factor = 0.055
color = "black"

[rendering.svg.glyphs.lower]
width-factor = 0.80
offset-y = 0.18
stroke-width-factor = 0.055
color = "red"

[rendering.svg.pitch-marker]
gap-before = 0.35
gap-after = 0.35
dash-width-factor = 0.45
```

---

# 19. Config-validatie

Renderingconfiguratie moet vóór gebruik worden gevalideerd.

Ongeldig zijn bijvoorbeeld:
- negatieve glyphbreedtes;
- lege kleurwaarden;
- onbekende alignment-waarden;
- niet-numerieke offsets;
- line-gap kleiner dan minimum;
- glyphs met nulbreedte;
- tokens die VSA-syntax breken.

Bij ongeldige configuratie stopt rendering met een duidelijke configuratiefout.

---

# 20. Open ontwerpvragen

Nog nader uit te werken:
- exacte defaultwaarden na visuele test;
- fallback bij extreem brede render-units;
- debug-theme;
- relatie met MusicXML-layout;
- printprofiel;
- alternatieve glyphvormen per theme.
