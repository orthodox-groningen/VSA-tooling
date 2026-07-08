# Status en roadmap

Dit document is het actuele kompas voor VSA-tooling. Historische stapdocumenten blijven in `docs/architecture/`, maar dit bestand vat samen wat nu werkt, wat beperkt werkt en wat de nuttigste volgende stappen zijn.

## Korte samenvatting

VSA-tooling is in de fase van werkende engine naar bruikbaar authoring- en publicatiegereedschap.

De parser, validator, SVG-renderer, MusicXML-export en Hugo-buildketen zijn aanwezig. De belangrijkste resterende waarde zit in workflow-afwerking: duidelijker documenteren, document-directives beslissen, randgevallen expliciet specificeren en de parochie-/bronpublicatie gladder maken.

## Werkt nu

| Onderdeel | Status | Opmerking |
| --- | --- | --- |
| VSA parser | Werkend | Ondersteunt tekst, scopes, modifiers en hoogte-markeringen. |
| Syntaxvalidatie | Werkend | Meldt meerdere fouten waar mogelijk. |
| Semantische validatie | Werkend | Onder andere modifier-aantallen en hoogte-marker-controles; het bekende voorbeeld met een foute laatste marker wordt gedetecteerd. |
| Meerdere hoogte-markeringen | Werkend | Parser, validator en SVG-rendering ondersteunen dit. |
| SVG-rendering | Werkend | Inclusief multiline/wrapping, spacingbeleid en regressietests. |
| MusicXML/MXL-export | Werkend | Beschikbaar via `vsa musicxml`; profielen voor playback/engraving. |
| Markdown VSA-blokken | Werkend | `::: vsa-notatie` wordt gevonden, gevalideerd en verwerkt. |
| Hugo build-markdown | Werkend | Genereert Markdown en SVG-assets voor Hugo. |
| `:::include` | Werkend | Ondersteunt markdown, VSA, assets en exporttypes `svg`, `coria`, `mxl`. |
| `:::coria` | Werkend | Blijft ondersteund als build-time directive/alias. |
| Print/web directives | Werkend met beperking | `web-only`, `print-only`, `keep-together`; nesting is nog niet toegestaan. |
| Parochie-lokaal model | Werkend in demo | `lokaal/`, manifeststructuur en voorbeeldincludes zijn aanwezig. |
| Catalogus-resolutie | Werkend | `vsa resolve-catalogus` zet `zoek=` om naar `bron:` of `lokaal:`. |
| Hugo-demo | Werkend als testbed | Combineert praktijkmateriaal, documentatie, layouts en publicatieketen. |

## Beperkt of kwetsbaar

| Onderdeel | Status | Waarom dit aandacht vraagt |
| --- | --- | --- |
| README/projectingang | Verbeterd, maar jong | De README is nu herschreven; hij moet actueel blijven bij workflow-keuzes. |
| Roadmap | Nieuw gecentraliseerd | Dit document vervangt nog niet automatisch alle oude todo's. |
| Directive-nesting | Open besluit | `web-only` binnen `keep-together` faalt nu bewust; praktijkmateriaal wil dit soms wel. |
| Enkele hoogte-marker | Specificatie expliciteren | De eerste marker geldt nu als beginhoogte. Als er maar een marker in een blok staat, is dat dus geen controleerbare eindmarker. |
| Commentaar in VSA | Deels opgelost | HTML-commentaar en comment-only regels zijn aangepakt, maar een compleet commentaarmodel is nog nuttig. |
| `bron:` met Coria/MXL | Beperkt | SVG op `bron:` werkt; Coria/MXL buiten `content-root` is nog niet glad. |
| AST/source maps | Later | Nodig voor betere foutposities, editor-integratie en eventueel roundtrip tooling. |
| Editor-ondersteuning | Niet aanwezig | VS Code highlighting en foutmarkering zouden dagelijks gebruik veel prettiger maken. |

## Open ontwerpbesluiten

### 1. Geneste document-directives

Nu is nesting verboden. Dat voorkomt ambiguiteit, maar botst met natuurlijke authoring, bijvoorbeeld een Coria-link of `web-only` content binnen een `keep-together` blok.

Te beslissen:

- Welke combinaties mogen genest worden?
- Is nesting semantisch nodig, of volstaat een sibling-conventie?
- Hoe moet nesting zich gedragen in browserweergave en bij print?
- Moet `keep-together` alleen layout sturen, of ook inhoudsgroepen vormen?

### 2. Commentaarmodel

Gebruikers moeten foutieve of experimentele VSA kunnen bespreken zonder dat validatie stukloopt op voorbeeldtekst.

Te beslissen:

- Welke regelcommentaar-syntax hoort bij VSA?
- Is blokcommentaar nodig?
- Wordt commentaar bewaard in AST/source maps of volledig genegeerd?
- Hoe gedragen comments zich binnen Markdown VSA-blokken?

### 3. Control tokens

Tokens zoals `[/]`, `[*]`, `[/?]` en `[*?]` zijn gespecificeerd als toekomstige syntax voor frasegrenzen en adempauzes, maar nog niet ondersteund als volwaardige renderer-directives.

Te beslissen:

- Welke abstracte betekenissen zijn definitief?
- Wat doen SVG en MusicXML per token?
- Welke configuratie is nodig per renderer?
- Hoe blijven bestaande hoogte-markeringen eenduidig gescheiden van control tokens?

### 4. Parochie-/bronworkflow

De richting is duidelijk: sjabloon of sessie met `zoek=`, resolver, validatie, build-markdown, Hugo, print/web-output. De praktische workflow kan nog eenvoudiger.

Te beslissen:

- Wanneer gebeurt `resolve-catalogus`: apart commando, automatisch, of beide?
- Waar komt resolved output te staan?
- Hoe gaan we om met ambiguiteit: strict fout, lijst, of interactieve keuze?
- Hoe worden `bron:` assets voor Coria/MXL beschikbaar gemaakt?

## Nuttigste volgende stappen

### Stap 1: directive-nesting beslissen en vastleggen

Doel: een duidelijke regel voor `web-only`, `print-only`, `keep-together`, `include` en `coria` in samengestelde documenten.

Waarom: deze keuze bepaalt hoe auteurs echte liturgische documenten schrijven.

Resultaat:

- Update van `docs/spec-vsa-document-samenstellen.md`.
- Tests voor toegestane en verboden combinaties.
- Eventuele implementatie in `src/vsa/markdown_directives.py`.

### Stap 2: parochie-workflow glad maken

Doel: van sjabloon/sessie naar preview/print zonder handmatige tussenstappen die makkelijk fout gaan.

Waarom: hier zit de meeste praktische waarde voor dagelijks gebruik.

Resultaat:

- Heldere voorbeeldworkflow in docs.
- Betere checks op open `zoek=`.
- Duidelijke outputlocatie voor resolved bestanden.
- Indien nodig: helper-script voor resolve + validate + build.

### Stap 3: commentaarmodel afronden

Doel: veilige commentaarvormen voor uitleg, voorbeeldfouten en tijdelijke notities in VSA-bronnen.

Waarom: auteurs moeten kunnen documenteren zonder validatie te saboteren.

Resultaat:

- Specificatie in `docs/spec/vsa-comments.md`.
- Validator/parser-regels.
- Regressietests voor comments met anders ongeldige VSA.

### Stap 4: hoogte-marker randgevallen expliciet specificeren

Doel: vastleggen dat de eerste hoogte-marker de beginhoogte is en dat een blok met maar een marker geen eindcontrole heeft.

Waarom: de validator werkt voor meerdere markers, maar de randgevallen moeten in de specificatie even helder zijn als in de code.

Resultaat:

- Specificatie of gebruikersdocumentatie bijwerken.
- Regressietest toevoegen of aanwijzen voor het bekende voorbeeld met een foute laatste marker.
- Eventueel `docs/to-do-van-mij.md` verder opschonen zodra het persoonlijke todo-bestand wordt geconsolideerd.

### Stap 5: editor-ondersteuning voorbereiden

Doel: syntax highlighting en later foutmarkering voor VSA in VS Code.

Waarom: dit verlaagt de invoerdrempel sterk.

Resultaat:

- TextMate grammar of VS Code extension-skelet.
- Highlighting voor scopes, hoogte-markeringen, modifiers, comments en directives.
- Eventueel later: CLI diagnostics naar editor diagnostics.

## Later

| Onderwerp | Waarom later |
| --- | --- |
| AST-formalisering met spans/source maps | Belangrijk, maar pas echt nodig voor editor tooling en complexere refactors. |
| Roundtrip parsing | Waardevol voor automatische transformaties, niet nodig voor huidige publicatieketen. |
| AI-versnelde invoer met `|`-scheidingen | Interessant, maar afhankelijk van stabiele notatie- en validatieregels. |
| SATB/beginakkoord-rendering | Muzikaal nuttig, maar vraagt eerst een duidelijk model en renderersemantiek. |
| Volledige TEv2-conceptuele integratie | Eerst demo-ervaring opdoen en bepalen welke terminologie echt helpt. |

## Relatie tot oude todo's

- `docs/todo.md` blijft de geconsolideerde historische todo-lijst.
- `docs/to-do-van-mij.md` blijft persoonlijke input en ruwe signalen bevatten.
- `docs/architecture/` blijft de implementatiegeschiedenis bewaren.
- Dit document is leidend voor actuele prioriteit en projectstatus.

Als een oud todo-punt opnieuw actief wordt, hoort het hier in een van deze categorieen terecht te komen: `werkt nu`, `beperkt`, `open besluit`, `nuttigste volgende stappen` of `later`.

