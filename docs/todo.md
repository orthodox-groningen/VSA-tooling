# TODO lijst

Statuswaarden:

- `Open`: nog doen.
- `In uitvoering`: actief onderwerp.
- `Later`: bewust geparkeerd.
- `Afgerond`: gedaan, maar historisch nuttig.

## 1. Parser en validator

### 1.1 Hoogte-controle bij laatste hoogte-marker

Status: `Open`

Het volgende is fout, maar wordt nog niet gedetecteerd:

```vsa
[//:] aap{/noot}{/mies}, [:]
```

Gewenst:

- validator controleert of eindtoon klopt;
- foutmelding noemt bestand, regel, kolom en concrete herstelactie.

### 1.2 Pitchmarkers strenger controleren

Status: `Open`

Uitbreiden met:

- strengere checks op begin-pitchmarker;
- strengere checks op eind-pitchmarker;
- eindtoon;
- metadata waar relevant.

### 1.3 Specificatie-change voor `+/`, `+\`, `- /`, `-\`

Status: `Open`

Liturgikon, p.247, derde regel van onderen, heeft vermoedelijk een notatie die suggereert dat `+` en `-` als halve-stap modifiers bruikbaar kunnen zijn.

Te onderzoeken:

- `+` in een EHM betekent halve stap erbij;
- `-` in een EHM betekent halve stap eraf;
- `/+` of `+\` zou dan syntactisch geldig kunnen zijn;
- `+` op zichzelf zou mogelijk ook geldig zijn.

Actie:

- Liturgikon-voorbeeld opnieuw bekijken (zwaar gebruikt bij 'zaligsprekingen' op pp. 54-55);
- syntax en semantiek specificeren;
- parser uitbreiden;
- validator uitbreiden;
- rendering bepalen.

### 1.4 Commentaar niet valideren

Status: `Open`

Het moet mogelijk zijn om in commentaarblokken of regelcommentaar ongeldige syntax of semantiek te beschrijven.

Te specificeren:

- regelcommentaar;
- blokcommentaar;
- gedrag binnen markdown;
- gedrag binnen `vsa-notatie`;
- validator moet commentaar overslaan.

### 1.5 Bracket-token dispatch in parser

Status: `Open`

Huidige parser behandelt alles tussen `[ ... ]` als pitchmarker. Daardoor conflicteren wraptokens zoals `[/?]` implementatietechnisch, ook al zijn ze conceptueel anders bedoeld.

Toekomstige oplossing:

- token-dispatch vóór pitchmarker-parsing;
- meerdere bracket-token families;
- pitchmarkers;
- wrap/control tokens;
- voorbereiding op MusicXML/control tokens;
- voorbereiding op alignment/control tokens.

Belangrijk:

- `[:]` blijft pitchmarker;
- `[/]`, `[*]`, `[/?]`, `[*?]` worden nog niet ondersteund totdat bracket-token dispatch is geïmplementeerd.

## 2. Muzikale semantiek

Status: `Later`

Uitbreidingen:

- toonhoogte-continuïteit;
- bereikcontrole;
- verboden overgangspatronen;
- alignment-validatie;
- multi-voice voorbereiding.

## 3. AST en formalisering

Status: `Later`

De AST is nu nog pragmatisch. Later verbeteren met:

- expliciete node-typen;
- spans/ranges;
- source maps;
- roundtrip parsing;
- betere mapping van parserfouten naar bronposities;
- betere ondersteuning voor rendering en MusicXML.

## 4. SVG-rendering

Status: `In uitvoering`

Algemene doelen:

- normale lopende tekst met muzikale overlays;
- links uitlijnen;
- geen tweezijdig uitvullen als default;
- natuurlijke spacing tussen tekst en zangelementen;
- glyphs als accenten boven/onder de tekst;
- duidelijke en compacte regelafstand;
- configureerbare rendering.

### 4.1 Spacing en typografie

Status: `In uitvoering`

Aandachtspunten:

- woordspaties behouden;
- geen overlap tussen aangrenzende tekst en zangelementen;
- optische spacing tussen aanpalende scopes;
- compactere spacing waar mogelijk;
- geen samenplakken zoals `deHeerheeft`.

### 4.2 Glyph-posities

Status: `In uitvoering`

Aandachtspunten:

- EHM-positie is nu visueel acceptabel;
- ELMs mogen iets lager als ze staarten van `ij`, `p`, `g`, `j` raken;
- stacked EHMs moeten goed onderscheidbaar blijven;
- single-EHM glyphs niet woordbreed maken;
- multi-EHM scopes moeten voldoende ruimte krijgen.

### 4.3 Filler-lines

Status: `In uitvoering`

Gewenst:

- filler-lines op tekst/dash-hoogte;
- niet op EHM-hoogte;
- stoppen vóór de volgende render-unit;
- bruikbaar bij bijvoorbeeld `geo____` en `geschon___ken`.

### 4.4 Afbreekpolicy

Status: `In uitvoering`

Nu ondersteunen:

- CR;
- LF;
- CRLF;
- bron-newlines zijn harde bronregelgrenzen;
- renderer mag tekst uit twee bronregels niet samenvoegen;
- wrapping mag alleen binnen één bronregel;
- niet afbreken midden in woorden.

Nog niet ondersteunen:

- `[/]`;
- `[*]`;
- `[/?]`;
- `[*?]`.

Deze tokens wachten op bracket-token dispatch.

### 4.5 Renderingconfiguratie

Status: `Open`

Er moet een config-specificatie komen waarin gebruikers voorkeuren kunnen opgeven, zoals:

- kleur bovenglyphs;
- kleur onderglyphs;
- font;
- fontgrootte;
- regelafstand;
- glyphbreedtes;
- glyphhoogtes;
- spacing;
- wrapgedrag.

Config moet vóór gebruik gevalideerd worden.

## 5. CLI professionaliseren

Status: `Open`

Gewenst:

1. Betere foutmeldingen:
   - wat is fout;
   - waar is het fout;
   - wat moet de gebruiker concreet doen;
   - bruikbaar voor non-techies.
2. Correcte terminologie:
   - `&` is geen modifierteken;
   - onderscheid tussen zangelement, EHM, ELM, tekstgedeelte, etc.
3. Uitgebreidere `--help`.
4. `vsa <command> --help` met:
   - inputs;
   - outputs;
   - parameters;
   - locaties;
   - exitcodes;
   - voorbeelden.
5. Mogelijk `vsa <errorcode> --help`.
6. Helpteksten praktisch nuttig maken.
7. Geen Python tracebacks tonen.
8. Waar mogelijk meerdere fouten verzamelen in één run.

## 6. Demo-site afronden

Status: `Open`

Taken:

1. Nieuwe README maken voor de repo.
2. Repo opruimen.
3. Alle pagina’s nalopen op:
   - tekst;
   - links;
   - voorbeelden;
   - mobiel;
   - tablet.
4. Controleren dat alle VSA-commando’s:
   - een eigen Hugo-demo pagina hebben;
   - in de handleiding staan;
   - syntax, inputs, outputs en parameters beschrijven.
5. Onderzoeken of de Hugo-demo interactieve parameters kan ondersteunen:
   - SVG-breedte;
   - renderingvariabelen;
   - keuzeopties.
6. Referentie v1 en gebruikershandleiding actualiseren op basis van codewijzigingen.
7. Handleiding slim laten verwijzen naar Hugo-demo voorbeelden.

## 7. MusicXML-export

Status: `Later`

Grote stap:

```text
AST → MusicXML
```

Aandachtspunten:

- begin-pitchmarker waarschijnlijk relevant;
- regeleindes mogelijk mappen op maatstrepen;
- wrap/control tokens mogelijk relevant;
- alignment en ritmische structuur voorbereiden;
- validatie vooraf noodzakelijk.

## 8. Multi-voice en sync placeholders

Status: `Later`

Eerder idee voor major release:

- placeholders;
- stem-sync;
- gedeelde ritmische structuur;
- SATB;
- tekstueel in sync houden van meerdere stemmen.

## 9. Editor tooling

Status: `Later`

Mogelijke uitbreidingen:

- VS Code extension;
- syntax highlighting;
- live validation;
- hover diagnostics;
- quick fixes.
