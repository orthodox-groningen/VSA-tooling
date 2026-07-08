# Overzicht

VSA (Vereenvoudigde Slavische Accentnotatie) is een tekstgebaseerde domeinspecifieke taal (Domain-Specific Language, DSL) voor het beschrijven van Slavische accentnotatie. De taal definieert een eenduidige, machineleesbare en menselijk leesbare notatie waarmee zangstukken kunnen worden vastgelegd, gevalideerd en gerenderd. De specificatie beschrijft uitsluitend de taal en haar semantiek.

## Status

Dit document consolideert de algemene specificatie-informatie uit de bestaande VSA-documentatie.

De tekst hieronder is overgenomen en samengebracht uit de bestaande specificatie, met behoud van betekenis.

## 1. Inleiding

<!-- ter herinnering: http://www.ivanmoody.co.uk/orthodoxliturgylinks.htm bevat allerlei links over orthodoxe liturgie -->

De Slavisch‑orthodoxe zangtraditie kent een lange geschiedenis van **staffloze neumen­notatie**, waarvan de bekendste vorm de klassieke **Znamenny‑notatie** is. Deze notatie gebruikt ideografische tekens (*kriuki* of *znamëna*) om melodische beweging, formules en expressie vast te leggen zonder exacte toonhoogtes. Een toegankelijke introductie is te vinden op [Znamenny chant](https://en.wikipedia.org/wiki/Znamenny_chant), en een overzicht van historische notatievormen op [Znamenny musical notation](https://en.wikipedia.org/wiki/Znamenny_notation).

Hoewel deze officiële systemen rijk en complex zijn, ontstonden er in parochies ook **vereenvoudigde, mondeling overgeleverde markeersystemen**. Deze systemen — vaak bestaande uit gestapelde streepjes boven de tekst en horizontale lijnen onder syllaben — dienden als praktische hulpmiddelen om **richting**, **accent** en **duur** van de zang aan te geven. Ze zijn echter **niet gestandaardiseerd**, **niet officieel gedocumenteerd**, en verschillen per regio, koorleider of lokale traditie. [Appendix 1](#appendix-1) bevat de uitleg zoals die werd gegeven in het Nederlandse Liturgikon. 

Dit document introduceert een formele codificatie van deze praktijkgerichte notatie: de **Vereenvoudigde Slavische Accentnotatie (VSA‑notatie)**. VSA is geen vervanging van historische kriuki- of znamenny-notatie, maar een lichte, consistente en reproduceerbare manier om Slavisch‑orthodoxe congregatiezang digitaal te noteren.

Het doel is een notatie die:

- eenvoudig te leren is voor zangers zonder gespecialiseerde opleiding;
- aansluit bij bestaande parochiële praktijk;
- formeel definieerbaar is in een grammatica;
- betrouwbaar te parseren, valideren en renderen is;
- bruikbaar is in tekstgebaseerde workflows, statische websites en automatische renderers of weergavecomponenten;
- voldoende semantische informatie bevat voor conversie naar symbolische muziekformaten zoals MusicXML.

VSA beschrijft melodische beweging binnen een modaal toonstelsel waarin stapgrootten niet uniform zijn en afhankelijk zijn van de gekozen grondtoon: de `do` van de toonladder.

---

## 3. Terminologie

| Term                   | Betekenis                                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AST                    | Abstract Syntax Tree. Een interne boom- of objectstructuur die het resultaat is van parsing.                                                                                                 |
| Absolute toonhoogte    | Een expliciete toonhoogteaanduiding voor interpretatie of export, bijvoorbeeld `C4` of `F#3`; dit hoort in blokmetadata, niet in een toonhoogte-markering.                                   |
| Blok                   | zie: Hugo markdown blok                                                                                                                                                                      |
| Do-context             | De grondtooncontext waarbinnen relatieve toonhoogtebewegingen worden geïnterpreteerd. De do-context bestaat uit de grondtoon (`do`) en de modus                                              |
| Duur                   | Interne representatie van de duur van een muzikale positie.                                                                                                                                  |
| EHM                    | Enkelvoudige Hoogte-Modifier. Een elementaire hoogte-instructie, bestaande uit een optionele halftoon-prefix (`#`, `b` of alias) gevolgd door een basisbeweging zoals `/`, `\\`, `-` of `~`. |
| ELM                    | Enkelvoudige Lengte-Modifier. Een elementaire duurinstructie zoals `_`, `__`, `.`, `..`, `-` of `~`.                                                                                         |
| Export                 | Het omzetten van gevalideerde VSA-notatie naar een extern formaat zoals MusicXML.                                                                                                            |
| Glyph                  | De grafische representatie van een EHM of ELM.                                                                                                                                               |
| Grid                   | Het renderobject voor één zangelement-scope. Het bestaat uit een bovenrij, tekstlaag en onderrij.                                                                                            |
| Hoogte-modifier        | Een rij EHMs die melodische beweging specificeert.                                                                                                                                           |
| Hugo markdown blok     | De tekst `::: vsa-notatie`, gevolgd door een lijst van parameters, een zangstuk, en `:::`                                                                                                    |
| Kolom                  | De grafische representatie van één muzikale positie binnen een grid.                                                                                                                         |
| Ladderstap             | Een overgang van één toonladdergraad naar de volgende of vorige graad.                                                                                                                       |
| Lengte-modifier        | Een rij ELMs die de duur van muzikale posities specificeert.                                                                                                                                 |
| Mappingstrategie       | De implementatiekeuze waarmee relatieve toonladderbewegingen worden omgezet naar concrete toonhoogten.                                                                                       |
| Melisma                | Het zingen van één zangelement over meerdere opeenvolgende muzikale posities.                                                                                                                |
| Modus                  | De intervalstructuur van een toonladder. De modus bepaalt welke overgangen grote of kleine stappen zijn. Voorbeelden zijn 'majeur' en 'mineur'.                                              |
| Modifier               | Verzamelnaam voor een hoogte-modifier of lengte-modifier.                                                                                                                                    |
| Muzikale positie       | De kleinste muzikale eenheid binnen een zangstuk. Een muzikale positie representeert precies één gezongen toon met een relatieve toonhoogte en een duur.                                     |
| Muzikale tijdlijn      | De geordende reeks muzikale posities van een zangstuk.                                                                                                                                       |
| Node                   | Een element binnen een AST-structuur.                                                                                                                                                        |
| Parser                 | Een component die VSA-tekst omzet naar een AST of andere interne representatie.                                                                                                              |
| Toonhoogte             | Interne representatie van een concrete toonhoogte.                                                                                                                                           |
| PitchMarkerNode        | AST-node die een toonhoogte-markering representeert; deze bevat geen absolute toonhoogte.                                                                                                    |
| Positie                | Verkorte schrijfwijze voor muzikale positie.                                                                                                                                                 |
| Renderen               | Het omzetten van gevalideerde VSA-notatie naar een visuele of symbolische representatie zoals SVG, HTML, PDF of MusicXML.                                                                    |
| Renderlaag             | Eén van de drie visuele lagen van een rendering: bovenlaag, tekstlaag of onderlaag.                                                                                                          |
| Samengestelde modifier | Een modifier die uit meerdere EHMs of ELMs bestaat, gescheiden door `&`.                                                                                                                     |
| Scope                  | Verkorte schrijfwijze voor zangelement-scope.                                                                                                                                                |
| ScopeNode              | AST-node die een zangelement-scope representeert.                                                                                                                                            |
| Semantische validatie  | Controle of syntactisch geldige VSA-notatie ook voldoet aan de betekenisregels van VSA.                                                                                                      |
| Standaardduur          | De basisduur van een muzikale positie waarvan alle ELM-duurwaarden worden afgeleid.                                                                                                          |
| Syntax-validatie       | Controle of invoer voldoet aan de grammaticale regels van VSA.                                                                                                                               |
| Toonhoogte-markering   | Een speciale constructie aan het begin of einde van een zangstuk waarmee een een relatieve hoogte-modifier worden vastgelegd.                                                                |
| Toonhoogtebeweging     | Een relatieve verandering van toonhoogte zoals beschreven door een EHM.                                                                                                                      |
| Toonladdergraad        | Een positie binnen de toonladder, bijvoorbeeld `do`, `re`, `mi`, `fa`, `sol`, `la`, `ti`.                                                                                                    |
| VSA-markering          | Iedere syntactische constructie waarmee muzikale informatie aan tekst wordt gekoppeld, zoals scopes, modifiers en toonhoogte-markeringen.                                                    |
| VSA-zangstuk           | Een tekst die gezongen kan worden, zoals een tropaar of kondak, en in VSA is opgeschreven.                                                                                                   |
| Zangelement            | De tekst waaraan muzikale informatie wordt gekoppeld. Dit is vaak een lettergreep, maar kan ook een kleiner of groter tekstfragment zijn.                                                    |
| Zangelement-scope      | Een gemarkeerd tekstdeel tussen `{` en `}`. Een scope bevat achtereenvolgens een optionele hoogte-modifier, exact één zangelement en een optionele lengte-modifier.                          |
| Zangstuk               | Zie: VSA-zangstuk                                                                                                                                                                            |

---
