# VSA SVG Rendering Specification (Draft 2)

## 1. Doel en scope

Dit document beschrijft de SVG-rendering van VSA-notatie.

De [VSA-taalspecificatie](./vsa-spec-v1.md) definieert:

* syntax;
* semantiek;
* validatie.

Dit document definieert uitsluitend:

* visuele presentatie;
* layout;
* typografie;
* glyph-rendering;
* rendering-configuratie.

De rendering-specificatie bepaalt niet de betekenis van VSA-constructies.

---

# 2. Rendering-principes

## 2.1 Algemene principes

SVG-rendering moet:

* goed leesbaar zijn;
* muzikaal scanbaar zijn;
* compact maar luchtig ogen;
* schaalbaar zijn naar verschillende schermgroottes;
* geschikt zijn voor zowel schermweergave als print.

## 2.2 Layoutfilosofie

Default rendering gebruikt:

* links uitgelijnde regels;
* natuurlijke tekstspatiëring;
* compacte muzikale glyphs;
* consistente verticale uitlijning.

Alle regeluitlijningen zijn toegestaan:

* links uitlijnen;
* rechts uitlijnen;
* centreren;
* uitvullen.

Links uitlijnen is de default.

---

# 3. Glossary

| Term             | Betekenis                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| Render-run       | Een visueel opeenvolgend rendering-element zoals vrije tekst, een zangelement of een pitch-marker |
| Zangelement      | Een `{...}` constructie met gezongen tekst en eventuele modifiers                                 |
| Glyph            | Een grafisch teken dat een muzikale eigenschap weergeeft                                          |
| Bovenglyph       | Glyph boven de tekst                                                                              |
| Onderglyph       | Glyph onder de tekst                                                                              |
| Pitch-marker     | Constructie zoals `[:]`                                                                           |
| Alignment-marker | Het `&`-teken dat modifiers visueel koppelt                                                       |
| Wrapping         | Het afbreken van regels                                                                           |
| Layout-engine    | Het onderdeel dat bepaalt waar elementen worden geplaatst                                         |
| Renderer         | Het onderdeel dat SVG genereert                                                                   |

---

# 4. Layoutmodel

## 4.1 Rendering-eenheden

Een VSA-regel wordt gerenderd als een reeks render-runs.

Voorbeelden van render-runs:

* vrije tekst;
* zangelementen;
* pitch-markers;
* whitespace.

## 4.2 Regeluitlijning

De renderer ondersteunt:

* left;
* right;
* center;
* justify.

Default:

* left.

## 4.3 Regelbreedte

De renderer gebruikt een maximale regelbreedte.

Wanneer een regel te breed wordt:

* wordt afgebroken op natuurlijke grenzen;
* blijven zangelementen zoveel mogelijk intact.

## 4.4 Natuurlijke afbreekpunten

Default wrapping gebruikt:

1. expliciete regeleinden;
2. whitespace;
3. interpunctie;
4. grenzen tussen render-runs;
5. optionele interne zangelement-grenzen.

De renderer mag:

* geen modifiers scheiden van hun tekst;
* geen glyphgroepen splitsen.

## 4.5 Woordverbindingen en wrapping

Een expliciete woordverbindingsmarkering verhindert automatische wrapping tussen gekoppelde render-runs.

Voorbeeld:

```text
[:] Heer, {\ont}-{/ferm} U [:]
```

Hier vormt:

```text
{\ont}-{/ferm}
```

één visuele woordgroep.

Automatische wrapping is daarom niet toegestaan:

* tussen `{\ont}` en `-`;
* tussen `-` en `{/ferm}`.

Wel toegestaan:

* na `Heer,`;
* vóór `{\ont}`;
* na `{/ferm}`.

## 4.6 Expliciete wrapcontrole

Naast natuurlijke afbreekpunten kan de gebruiker wrapping expliciet beïnvloeden.

Wrapcontrole moet configureerbaar zijn. Dat betekent:

* de standaardtokens zijn door de renderer gedefinieerd;
* een project mag andere tokens configureren;
* configuratie moet vóór gebruik gevalideerd worden;
* ongeldige configuratie mag niet leiden tot parserfouten of ambigu gedrag.

De renderer moet wraptokens herkennen vóór reguliere VSA-parsing of via een aparte preprocessorlaag.

## 4.6.1 Forced line break

Een forced line break dwingt een nieuwe renderregel af.

Standaard voorgestelde syntax:

```text
[/]
[*]
```

Voorbeeld:

```text
[:] Eerste regel [/] tweede regel [:]
```

Betekenis:

* render vóór `[/]`;
* start daarna een nieuwe SVG-regel;
* `[/]` zelf wordt niet zichtbaar gerenderd.

Alternatief:

```text
[:] Eerste regel [*] tweede regel [:]
```

`[/]` en `[*]` zijn beide forced line break markers.

Het verschil tussen beide markers kan later renderer- of exportafhankelijk worden gebruikt.

Voor MusicXML-rendering kan dit bijvoorbeeld relevant zijn:

* `[/]` = systeem-/regelbreuk;
* `[*]` = sterker structureel breekpunt;
* mapping naar maatstrepen of systeemindeling wordt later gespecificeerd.

## 4.6.2 Preferred breakpoint

Een preferred breakpoint geeft aan waar de renderer bij voorkeur mag afbreken als wrapping nodig is.

Standaard voorgestelde syntax:

```text
[/?]
[*?]
```

Voorbeeld:

```text
[:] Dit is een lange zin [/?] met een voorkeurspunt [:]
```

Betekenis:

* renderer mag hier afbreken als dat nodig is;
* als afbreken niet nodig is, blijft `[/?]` onzichtbaar.

`[*?]` kan worden gebruikt als sterker preferred breakpoint dan `[/?]`.

Voorbeeld:

```text
[:] Eerste frase [/?] vervolg [*?] nieuw tekstdeel [:]
```

Mogelijke interpretatie:

* `[/?]` = gewoon voorkeursbreekpunt;
* `[*?]` = sterk voorkeursbreekpunt.

De exacte prioriteitsweging is renderer-configuratie.

## 4.6.3 Waarom niet `[:]`

`[:]` wordt niet gebruikt als standaard wraptoken.

Reden:

* `[:]` is al een pitch-marker;
* toekomstige pitch-markers kunnen mogelijk ook midden in een muziekstuk voorkomen;
* hergebruik van dezelfde tokenvorm voor wrapping zou parserambiguïteit veroorzaken.

Daarom gebruiken wraptokens expliciet herkenbare vormen zoals:

```text id="l0umsv"
[/]
[*]
[/?]
[*?]
```

Deze zijn:

* visueel onderscheidbaar;
* semantisch expliciet;
* uitbreidbaar voor toekomstige renderers.

---

## 4.6.4 Non-breaking group

Een non-breaking group voorkomt automatische wrapping binnen een groep.

Standaard voorgestelde syntax:

```text id="ux4x0q"
[= ... =]
```

Voorbeeld:

```text id="lixr7x"
[:] [= Heer, {\ont}-{/ferm} U =] [:]
```

Betekenis:

* de inhoud binnen `[= ... =]` blijft op één renderregel;
* als de groep te breed is, mag de renderer pas buiten de groep wrappen;
* de markers `[=` en `=]` worden niet zichtbaar gerenderd.

Non-breaking groups zijn bedoeld voor:

* korte vaste tekstgroepen;
* samengestelde woorden;
* woordgroepen die visueel bij elkaar moeten blijven;
* constructies met zichtbare woordverbindingen zoals `{\ont}-{/ferm}`.

---

## 4.6.5 Zichtbare woordverbindingen

Een zichtbare woordverbindingsmarkering zoals `-` legt standaard een non-breaking relatie tussen omliggende render-runs.

Voorbeeld:

```text id="r3x4y4"
[:] Heer, {\ont}-{/ferm} U [:]
```

Hier vormt:

```text id="scy4w0"
{\ont}-{/ferm}
```

één visuele woordgroep.

Automatische wrapping is daarom niet toegestaan:

* tussen `{\ont}` en `-`;
* tussen `-` en `{/ferm}`.

Wel toegestaan:

* na `Heer,`;
* vóór `{\ont}`;
* na `{/ferm}`.

Als een gebruiker toch expliciet na een zichtbaar koppelteken wil afbreken, kan dat met een forced line break:

```text id="u9okbh"
[:] Heer, {\ont}-[/]{/ferm} U [:]
```

De forced line break marker wordt niet zichtbaar gerenderd.

---

## 4.6.6 Configuratie van wraptokens

Wraptokens moeten configureerbaar zijn.

Voorbeeld:

```toml id="z0v6lg"
[rendering.svg.wrapping.tokens]
forced-line-break = ["[/]", "[*]"]
preferred-break = ["[/?]", "[*?]"]
nonbreaking-start = "[="
nonbreaking-end = "=]"
```

Configuratieregels:

* tokens mogen niet leeg zijn;
* tokens mogen elkaar niet ambigu overlappen;
* tokens mogen bestaande VSA-syntax niet breken;
* tokens moeten vóór gebruik gevalideerd worden;
* bij ongeldige configuratie stopt de renderer met een duidelijke configuratiefout.

---

## 4.6.7 Geldige uitbreidbare tokenvormen

Uitbreidbare tokens moeten:

* syntactisch duidelijk herkenbaar zijn;
* niet conflicteren met bestaande VSA-constructies;
* parserambiguïteit vermijden;
* toekomstvast zijn.

Aanbevolen strategie:

* gebruik bracket-gebaseerde tokens;
* gebruik expliciete prefixsymbolen;
* reserveer bestaande VSA-tokenfamilies.

Goede voorbeelden:

```text id="x4kgv8"
[/]
[*]
[/?]
[*?]
[= ... =]
```

Minder geschikte voorbeelden:

```text id="6q2t4r"
[:]
[?]
[-]
```

omdat deze:

* lijken op bestaande of toekomstige pitch-markers;
* semantisch onvoldoende onderscheidend zijn;
* ambigu kunnen worden bij uitbreiding van de taal.

---

## 4.6.8 Vooruitblik: uitbreidbare layout- en exporttokens

Dezelfde uitbreidingsprincipes moeten later ook gelden voor:

* MusicXML-layouttokens;
* editor directives;
* exporthints;
* interactieve rendering;
* synchronisatie-aanwijzingen;
* multi-voice layout.

Voorbeelden van toekomstige toepassingen:

* systeemafbrekingen;
* maatstructuurhints;
* frasegrenzen;
* repetitiemarkeringen;
* layoutprioriteiten.

Daarom moeten tokens worden behandeld als een uitbreidbaar namespace-systeem en niet als losse ad-hoc markeringen.

De exacte formele uitbreidingsregels worden later apart gespecificeerd.

---

# 5. Tekst en spacing

## 5.1 Basisafstand

Tussen render-runs moet een minimale horizontale afstand bestaan.

Doel:

* voorkomen dat tekst en glyphs tegen elkaar aan staan;
* visuele rust creëren.

## 5.2 Whitespace

Normale spaties in vrije tekst blijven behouden.

Extra renderer-spacing komt bovenop de tekstuele spacing.

## 5.3 Zangelementen

Een zangelement bestaat visueel uit:

* gezongen tekst;
* bovenglyphs;
* onderglyphs.

De tekst vormt altijd het visuele ankerpunt.

## 5.4 Smalle tekst versus brede muzikale structuur

Als:

```text
TB < Σ W[i]
```

waarbij:

* `TB` = tekstbreedte;
* `Σ W[i]` = totale breedte van de muzikale posities;

dan behoudt het zangelement standaard zijn normale typografische breedte.

Default gedrag:

* tekst wordt gecentreerd;
* resterende ruimte wordt rechts opgevuld met een horizontale lijn.

Alternatieve configureerbare strategieën:

* fill-line;
* left-align;
* center-no-fill;
* stretch-text;
* proportional-spacing.

Default:

* fill-line.

---

# 6. Pitch-markers

## 6.1 Algemene vorm

Pitch-markers worden compact weergegeven.

De horizontale markerlijn:

* is korter dan de volledige positiebreedte;
* oogt als een kleine muzikale markering;
* staat los van de tekst.

## 6.2 Spacing

Pitch-markers krijgen extra ruimte:

* vóór de volgende tekst;
* na voorafgaande tekst.

Pitch-markers mogen niet “vastplakken” aan woorden.

## 6.3 Eind-pitch-markers

Eind-pitch-markers gebruiken dezelfde visuele stijl als begin-pitch-markers.

---

# 7. Hoogte- en lengteglyphs

## 7.1 Bovenglyphs

Bovenglyphs:

* zijn compact;
* lijken visueel op kleine accenttekens;
* staan dicht boven de tekst.

Bovenglyphs mogen niet:

* extreem breed zijn;
* te hoog boven de tekst zweven.

## 7.2 Onderglyphs

Onderglyphs:

* functioneren visueel vergelijkbaar met underlines;
* staan dicht onder de tekst;
* kruisen geen letterstaarten.

Onderglyphs hoeven niet de volledige positiebreedte te beslaan.

## 7.3 Configureerbare glyphs

Gebruikers moeten glyph-rendering kunnen aanpassen.

Voorbeelden:

* breedte;
* hoogte;
* offsets;
* lijnstijl;
* kleur;
* SVG-shapes;
* alternatieve glyphsymbolen.

De renderer moet daarom werken met een abstract glyphmodel en niet met hardcoded vormen.

## 7.4 Alignment-markers

Het `&`-teken is een alignment-marker.

Alignment-markers koppelen modifiers visueel aan elkaar zodat:

* muzikale continuïteit zichtbaar wordt;
* glyphgroepen als één geheel ogen;
* muzikale posities optisch uitgelijnd blijven.

Voorbeelden:

* verbonden stijgende lijnen;
* doorlopende lengte-indicatoren;
* gekoppelde accentgroepen.

De exacte visuele interpretatie is renderer-afhankelijk.

---

# 8. Verticale layout

## 8.1 Regelafstand

Regelafstand moet configureerbaar zijn.

De regelafstand moet:

* voldoende ruimte geven voor bovenglyphs;
* voorkomen dat glyphs tussen regels botsen.

## 8.2 Verticale offsets

Boven- en onderglyphs gebruiken configureerbare verticale offsets.

---

# 9. Typografie

## 9.1 Fonts

De renderer ondersteunt configureerbare fonts.

De default-font moet:

* goed leesbaar zijn;
* Unicode ondersteunen;
* geschikt zijn voor liturgische tekst.

## 9.2 Fontgrootte

Tekstgrootte moet configureerbaar zijn.

Glyphgroottes schalen relatief mee.

---

# 10. Kleuren

## 10.1 Defaults

Default rendering:

* bovenglyphs zwart;
* onderglyphs rood;
* tekst zwart.

## 10.2 Configureerbaarheid

Kleuren moeten configureerbaar zijn.

---

# 11. Configuratie

## 11.1 Configuratiebron

SVG-rendering-configuratie wordt opgenomen in `vsa.toml`.

## 11.2 Default-configuratie

De renderer levert een ingebouwde default-configuratie.

## 11.3 User overrides

Gebruikers mogen:

* een eigen configbestand opgeven;
* alleen specifieke waarden overriden;
* meerdere configuratielagen combineren.

Configuratie werkt volgens cascading overrides:

1. ingebouwde defaults;
2. projectconfig;
3. user-config;
4. CLI-overrides.

## 11.4 Voorbeeldconfiguratie

```toml
[rendering.svg]
alignment = "left"
font-family = "Noto Serif"
font-size = 24
line-gap = 18
text-gap = 6
max-line-width = 900

[rendering.svg.pitch-marker]
dash-width-factor = 0.55
gap-before-text = 10

[rendering.svg.glyphs]
upper-color = "black"
lower-color = "red"
upper-width-factor = 0.65
lower-width-factor = 0.80
upper-offset = -8
lower-offset = 5

[rendering.svg.layout]
narrow-text-strategy = "fill-line"
```

---

# 12. Responsiveness

SVG-rendering moet:

* schaalbaar zijn;
* mobiel bruikbaar blijven;
* horizontale overflow minimaliseren.

SVG-output moet correct functioneren op:

* desktop;
* tablet;
* telefoon;
* smalle foldable schermen.

---

# 13. Open ontwerpvragen

Nog nader te bepalen:

* exacte glyphvormen;
* automatische wrapping-strategieën;
* printoptimalisatie;
* multi-voice rendering;
* interactieve SVG-functionaliteit;
* zoomgedrag;
* exportprofielen.

## 13.1 Prioriteit

De volgende onderwerpen moeten relatief vroeg worden uitgewerkt:

* wrapping-strategieën;
* glyphmodel;
* configuratie-architectuur.

De overige onderwerpen kunnen later worden uitgewerkt.
