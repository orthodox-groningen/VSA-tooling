# Opdracht: Technische revisie van de VSA-specificaties

## Doel van deze revisie

Verhoog de:

- formele kwaliteit;
- interne consistentie;
- onderhoudbaarheid;
- bruikbaarheid als referentiespecificatie.

Behoud daarbij volledig de bestaande ontwerpfilosofie, architectuur en semantiek.

---

# Technische revisie van de VSA-specificaties

Voer een grondige technische revisie uit van de meegeleverde VSA-specificaties (Vereenvoudigde Slavische Accentnotatie). Gedraag je als technisch redacteur van een formele standaard (vergelijkbaar met een RFC of W3C-specificatie), niet als auteur die een nieuw ontwerp maakt.

## Hoofddoel

Verbeter de kwaliteit, consistentie en formaliteit van de documentatie, terwijl de bestaande ontwerpfilosofie, architectuur en semantiek volledig behouden blijven.

## Algemene uitgangspunten

Deze revisie is een **kwaliteitsverbetering**, geen herontwerp.

Behoud daarom expliciet:

- de conceptuele helderheid;
- de architectuur;
- de uitbreidbaarheid;
- de scheiding van verantwoordelijkheden;
- de modulaire opbouw;
- de leesbaarheid;
- de bestaande terminologie;
- de bestaande semantiek;
- de bestaande ontwerpfilosofie.

Voeg geen nieuwe functionaliteit toe tenzij daar expliciet om wordt gevraagd.

## Belangrijkste ontwerpregel

Bij twijfel geldt altijd:

> Behoud van de bestaande betekenis is belangrijker dan verbetering van de formulering.

Verander daarom nooit ongemerkt de betekenis van een specificatie.

Bij meerdere mogelijke verbeteringen verdient altijd de verbetering de voorkeur die de specificatie objectiever, eenduidiger en beter onderhoudbaar maakt, zonder de conceptuele eenvoud of uitbreidbaarheid te verminderen.

## Architectuur

Behoud de bestaande scheiding tussen onder andere:

- taal (syntax);
- semantiek;
- AST;
- abstract glyph model;
- layout;
- rendering;
- SVG;
- configuratie;
- validatie.

Voorkom dat verantwoordelijkheden door elkaar gaan lopen.

## Consistentie

Controleer alle documenten op:

- terminologie;
- definities;
- naamgeving;
- verwijzingen;
- hoofdstukstructuur;
- versieverwijzingen;
- voorbeelden;
- grammatica;
- notatie;
- spelling.

Maak alle documenten onderling volledig consistent.

## Structuur

Verbeter waar nodig:

- hoofdstukindeling;
- volgorde van onderwerpen;
- kruisverwijzingen;
- nummering;
- definities;
- begrippenlijsten.

Consolideer overlappende tekst wanneer dat de leesbaarheid verbetert.

Verwijder daarbij nooit informatie; integreer deze op de juiste plaats.

Herstructureer documenten uitsluitend wanneer dit aantoonbaar de onderhoudbaarheid of begrijpelijkheid verbetert.

Verplaats geen tekst uitsluitend vanwege een esthetische voorkeur.

Streef ernaar dat ieder specificatiedocument één primaire verantwoordelijkheid heeft.

Voorkom overlap tussen documenten, tenzij deze bewust wordt toegepast ten behoeve van de leesbaarheid of terminologische toelichting.

## Formalisering

Formaliseer uitsluitend waar dat de specificatie eenduidiger maakt.

Bij voorkeur door:

- formele definities;
- beslisregels;
- tabellen;
- normatieve formuleringen;
- expliciete semantische regels;
- duidelijke invoer-/uitvoerbeschrijvingen.

Formaliseer niet om het formaliseren.

## Normatieve taal

Maak duidelijk onderscheid tussen:

- normatieve tekst (MUST, SHALL, REQUIRED, enz.);
- informatieve tekst;
- voorbeelden;
- toelichtingen.

Indien nuttig mag ieder document expliciet een status krijgen, bijvoorbeeld:

- Normative;
- Informative;
- Example;
- Design Notes.

## Voorbeelden

Verbeter voorbeelden wanneer dat de specificatie verduidelijkt.

Voeg waar nuttig extra voorbeelden toe, zoals:

- minimale voorbeelden;
- typische praktijkvoorbeelden;
- randgevallen;
- foutgevallen;
- validatiefouten.

Voorbeelden mogen nooit in strijd zijn met de normatieve tekst.

## Leesbaarheid

Verbeter:

- formuleringen;
- zinsbouw;
- opsommingen;
- kopjes;
- definities;
- overgangen tussen onderwerpen.

Houd de tekst technisch, precies en compact.

Schrijf voor technisch onderlegde lezers.

Vermijd overmatige uitleg van basisbegrippen.

De specificatie is een technisch referentiedocument, geen tutorial.

Markdown-tabellen moeten zowel in een webbrowser als in een platte teksteditor (zoals VS Code) goed leesbaar zijn.

Daarom geldt:

- geef alle cellen binnen een kolom dezelfde breedte;
- scheid iedere cel met minimaal één spatie van de kolomdelimiter `|`;
- zorg dat de scheidingsregel (de tweede regel van de tabel) dezelfde kolombreedtes aanhoudt;
- houd de uitlijning consequent binnen de gehele tabel.

## Wat nadrukkelijk NIET mag gebeuren

Niet:

- nieuwe functionaliteit ontwerpen;
- bestaande semantiek wijzigen;
- ontwerpbeslissingen vervangen door persoonlijke voorkeuren;
- architectuur vereenvoudigen ten koste van uitbreidbaarheid;
- documenten herschrijven omdat dat "mooier leest";
- informatie verwijderen omdat deze dubbel lijkt.

Indien informatie dubbel voorkomt, consolideer deze zonder betekenisverlies.

## Controlepunten

Controleer expliciet:

- interne consistentie;
- volledigheid;
- tegenstrijdigheden;
- ontbrekende definities;
- impliciete aannames;
- normatieve inconsistenties;
- uitbreidbaarheid;
- onderhoudbaarheid.

Voer na afloop een eindcontrole uit waarin expliciet wordt bevestigd dat:

- geen semantiek is gewijzigd;
- geen functionaliteit is toegevoegd;
- geen informatie verloren is gegaan;
- alle kruisverwijzingen correct zijn;
- alle voorbeelden nog geldig zijn.

## Ontwerpfilosofie

Behoud de centrale ontwerpfilosofie:

- semantiek vóór rendering;
- abstracte modellen vóór implementatie;
- scheiding tussen parser, AST, renderer en layout;
- implementatie-onafhankelijke specificaties;
- toekomstvaste uitbreidbaarheid.

## Werkwijze

Voer de revisie iteratief uit.

Begin iedere revisie met een analyse van de bestaande documenten.

Identificeer:

- inconsistenties;
- ontbrekende definities;
- mogelijke verbeteringen;
- noodzakelijke nieuwe terminologiebestanden;
- noodzakelijke kruisverwijzingen.

Bedenk daarna wat je wilt wijzigen, en vraag je bij iedere wijziging vraag je jezelf af:

1. Blijft de semantiek identiek?
2. Wordt de specificatie objectief beter?
3. Verbetert de consistentie?
4. Verbetert de onderhoudbaarheid?
5. Blijft de uitbreidbaarheid behouden?

Indien één van deze vragen met "nee" moet worden beantwoord, voer de wijziging niet uit.

## Resultaat

Lever op:

1. de volledig gereviseerde documenten;
2. een overzicht van alle aangebrachte wijzigingen;
3. de motivatie per wijzigingscategorie;
4. eventuele resterende aandachtspunten.

Beschouw de bestaande specificatie als het gezaghebbende ontwerp. De taak is deze specificatie te verfijnen, te formaliseren en te verduidelijken, zonder haar ontwerpprincipes of betekenis aan te tasten.

---

# Voorgestelde bestandsindeling

Deze bestandsindeling is het gewenste uitgangspunt. Wijk hiervan alleen af na uitdrukkelijke toestemming van de gebruiker.

```text
specification/
├── index.md
│
├── 01-introduction.md        # Doel, scope, uitgangspunten
├── 02-concepts.md            # Kernbegrippen en architectuuroverzicht
├── 03-language.md            # De VSA-syntax
├── 04-semantics.md           # Betekenis van alle constructies
├── 05-parser.md              # Parserregels, AST, EBNF
├── 06-validation.md          # Validatieregels en foutafhandeling
├── 07-glyph-model.md         # Abstract glyphmodel
├── 08-layout.md              # Layout-algoritme
├── 09-rendering.md           # Renderer, onafhankelijk van SVG
├── 10-svg.md                 # SVG-specifieke uitwerking
├── 11-configuration.md       # Configuratiebestanden en overrides
├── 12-cli.md                 # Commandoregelinterface
├── 13-examples.md            # Referentievoorbeelden
├── 14-extension-points.md    # Toekomstige uitbreidingen (zoals polyfonie)
├── 15-glossary.md            # Begrippenlijst
│
├── appendices/
│   ├── grammar-ebnf.md
│   ├── reference-tables.md
│   ├── migration.md
│   └── design-rationale.md
│
├── terminology/
│   ├── <term1>.md            # Description of <term1> in TEv2 style
│   ├── <term2>.md
│   └── ...
│
└── assets/
    ├── figures/
    └── examples/
```

---

## Terminologie (TEv2)

### Normatieve referentie

https://tno-terminology-design.github.io/tev2-specifications/

Gebruik TEv2 overeenkomstig deze specificatie, tenzij de gebruiker expliciet anders aangeeft.

### Rol van TEv2 binnen VSA

De VSA-specificatie is de primaire bron van waarheid.

TEv2 ondersteunt de specificatie; zij vervangt deze niet en vormt ook niet de bron waaruit de specificatie wordt gegenereerd.

De terminologie dient om belangrijke concepten, relaties en eventueel later patterns eenduidig vast te leggen en beter begrijpelijk te maken.

### Gebruik van TEv2

- identificeer belangrijke concepten die in aanmerking komen voor een TEv2-termbestand;
- maak of wijzig alleen een afzonderlijk terminologiebestand voor concepten en relaties die:
  - regelmatig in de specificatie voorkomen;
  - essentieel zijn voor het begrijpen van de architectuur;
  - of waarvan een eenduidige betekenis belangrijk is;
- wanneer tijdens een revisie een veelgebruikte term of frase wordt aangetroffen waarvoor nog geen terminologiebestand bestaat, overweeg dan een nieuw terminologiebestand aan te maken indien dit de consistentie en onderhoudbaarheid verbetert;
- niet ieder zelfstandig naamwoord of werkwoord-frase hoeft een TEv2-concept te worden.

### Terminologiebestanden

- maak bij ieder nieuw terminologiebestand direct een zo volledig én actueel mogelijke TEv2-header (frontmatter), conform de op dat moment geldende TEv2-specificatie voor Curated Text Files:
  https://tno-terminology-design.github.io/tev2-specifications/docs/specs/files/curated-text-file
- houd de frontmatter van bestaande terminologiebestanden tijdens iedere revisie actueel en volledig;
- vul alle vooraf gedefinieerde header-velden in waarvoor betrouwbare informatie beschikbaar is;
- laat een vooraf gedefinieerd header-veld alleen leeg wanneer de benodigde informatie niet uit de specificatie of de terminologie kan worden afgeleid;
- gebruik de vooraf gedefinieerde header-velden overeenkomstig de betekenis die eraan wordt gegeven in de TEv2-specificatie;
- onderhoud ook velden zoals `formPhrases` actief wanneer tijdens de revisie nieuwe grammaticale varianten, synoniemen of aliases worden aangetroffen die naar hetzelfde concept verwijzen:
  https://tno-terminology-design.github.io/tev2-specifications/docs/terms/form-phrase

### Gebruik van TermRefs

- gebruik overal consistente terminologie;
- iedere term of frase (inclusief aliases en Form Phrases) waarvoor een terminologiebestand bestaat, moet in de specificatie worden voorzien van een TEv2 TermRef;
- gebruik daarbij de standaard TEv2 TermRef-notatie;
- geef, waar mogelijk, de voorkeur aan Form Phrases zodat de zichtbare tekst en de TermRef samenvallen (bijvoorbeeld `[bronnen](@)` in plaats van `[bronnen](bron@)`);
- gebruik een expliciete TermRef (zoals `[bronnen](bron@)`) alleen wanneer geen geschikte Form Phrase bestaat of wanneer dat om andere redenen noodzakelijk is;
- wanneer een expliciete TermRef nodig blijkt omdat een Form Phrase ontbreekt, overweeg dan of die Form Phrase aan het betreffende terminologiebestand moet worden toegevoegd;
- controleer dat alle termen waarvoor een terminologiebestand bestaat, consequent met een TEv2 TermRef zijn aangeduid.

### Wijzigen van terminologie

- wijzig de formele definitie of de formele criteria van een term alleen na uitdrukkelijke toestemming van de gebruiker;
- achtergrondinformatie, voorbeelden, toelichtingen en verwijzingen in een terminologiebestand mogen zonder toestemming worden uitgebreid, mits de formele definitie of de formele criteria daardoor niet veranderen;
- verwijder bestaande terminologiebestanden alleen na uitdrukkelijk verzoek of toestemming van de gebruiker.
- Wanneer een wijziging in de terminologie gevolgen heeft voor de specificatie (of omgekeerd), werk beide consistent bij.

### Samenhang tussen specificatie en terminologie

- voorkom dat dezelfde definitie op meerdere plaatsen onafhankelijk wordt onderhouden;
- voeg waar nuttig verwijzingen toe tussen specificatie en terminologie;
- verplaats terminologische achtergrondinformatie niet automatisch uit de specificatie; beide documenttypen mogen elkaar aanvullen;
- accepteer dat beperkte doublures mogen bestaan wanneer zij verschillende doelen dienen (normatieve specificatie versus terminologische toelichting);
- houd de terminologie in één platte map `terminology/`; introduceer geen submappen tenzij de gebruiker daar expliciet om vraagt;
- terminologiebestanden mogen naar elkaar verwijzen, maar vormen geen hiërarchie die de structuur van de specificatie bepaalt.

### Inhoud van een terminologiebestand

- beschouw een terminologiebestand niet als een woordenboekitem, maar als een kennisdocument dat naast de formele beschrijving ook achtergrond, motivatie, voorbeelden, toelichting en verwijzingen naar de specificatie mag bevatten;
- een terminologiebestand hoeft niet direct volledig uitgewerkt te zijn; het mag gedurende de ontwikkeling organisch uitgroeien, terwijl de formele definitie en formele criteria vanaf het begin stabiel blijven.

### Conflicten met bestaande VSA-specs

Bij tegenstrijdigheden tussen deze prompt en de bestaande VSA-specificatie geldt:

- de bestaande VSA-specificatie heeft voorrang voor inhoudelijke ontwerpbeslissingen;
- deze prompt heeft voorrang voor de wijze waarop de revisie wordt uitgevoerd.