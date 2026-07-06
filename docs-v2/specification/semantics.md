# Semantiek

Dit document beschrijft de betekenis van syntactisch geldige VSA-notatie.

Bronbasis: `docs/spec/vsa-spec-v1.0.1.md`, aangevuld met latere documenten over hoogte-markeringen en control tokens.

## 5. Semantiek

### 5.1 Overzicht

De VSA-notatie wordt geïnterpreteerd via een gelaagd toonmodel:

```text
blokmetadata (`do`, `mode`, enz.)
    ↓
do-context
    ↓
modus
    ↓
toonladder
    ↓
EHM-sequenties
    ↓
muzikale posities
    ↓
rendering of export
```

De absolute toonhoogte maakt geen deel uit van de VSA-kernsyntax. Zij wordt, indien nodig voor interpretatie of MusicXML-export, geleverd via de blokmetadata.

### 5.2 Muzikale positie

Een muzikale positie is de kleinste muzikale eenheid binnen VSA.

Elke muzikale positie heeft:

- een relatieve toonhoogtebeweging, bepaald door één EHM;
- een duur, bepaald door één ELM;
- een koppeling aan één zangelement.

Een zangelement-scope zonder samengestelde modifiers bevat precies één muzikale positie.

Voorbeeld:

```text
{/tekst_}
```

Dit betekent:

- zangelement: `tekst`;
- toonhoogtebeweging: `/`;
- duur: `_`.

### 5.3 Impliciete modifiers

Als in een scope geen hoogte-modifier aanwezig is, wordt impliciet één `~` gebruikt.

Als in een scope geen lengte-modifier aanwezig is, wordt impliciet één `~` gebruikt.

Voorbeeld:

```text
{tekst}
```

is semantisch gelijk aan:

```text
{~tekst~}
```

Als slechts één van beide modifiers aanwezig is, bepaalt die modifier het aantal muzikale posities. De ontbrekende modifier wordt aangevuld met evenveel `~`-posities.

Voorbeeld:

```text
{/&\tekst}
```

is semantisch gelijk aan:

```text
{/&\tekst~&~}
```

### 5.4 Samengestelde modifiers en melisma

Wanneer een zangelement meerdere muzikale posities bevat, wordt hetzelfde zangelement over meerdere opeenvolgende tonen gezongen. Dit heet een **melisma**.

Een melisma wordt gespecificeerd door 
- een (optionele) hoogte modifier, die is samengesteld uit een rij EHMs die gescheiden zijn door `&`.
- een zangelement
- een (optionele) lengte modifier, die is samengesteld uit een rij ELMs die gescheiden zijn door `&`.

Voor een melisma moet (natuurlijk) altijd tenminste of de hoogte modifier, of de lengte modifier aanwezig zijn; immers, als ze er beide niet zijn is het gewoon een gezongen toon. Als een van beide ontbreekt, wordt hij geacht een rij `~` te zijn (gescheiden door `&`s) met evenveel muzikale posities als de gespecificeerde modifier.

Voorbeelden:

```text
{-&/tekst~&_}
```

Dit bevat twee muzikale posities:

| Positie | EHM | ELM | Betekenis                           |
| :-----: | --- | --- | ----------------------------------- |
| 1       | `-` | `~` | zelfde toonhoogte, standaardduur    |
| 2       | `/` | `_` | één ladderstap omhoog, dubbele duur |

Het zangelement `tekst` wordt over beide posities gezongen.

Als zowel een hoogte-modifier als een lengte-modifier aanwezig zijn, moeten zij hetzelfde aantal muzikale posities bevatten.

### 5.5 Do-context

De do-context is de grondtooncontext waarbinnen relatieve toonhoogtebewegingen worden geïnterpreteerd. In de zangpraktijk wordt deze context doorgaans niet expliciet genoteerd: de koorleid(st)er bepaalt de inzet op basis van de lokale traditie en vaak op basis van de toon waarop priester of diaken inzet. Koorleden volgen die context in de praktijk meestal stilzwijgend.

Voor visuele VSA-rendering hoeft de absolute do-context daarom niet in de zangtekst aanwezig te zijn. Voor MusicXML-export, automatische weergave of afspelen is wel een absolute starttoon nodig. Die wordt gespecificeerd in de Hugo blokmetadata:

```markdown
::: vsa-notatie
do="C4"
mode="major"
:::
```

Hier levert `do="C4"` de absolute starttoon voor interpretatie en export. De toonhoogte-markeringen in de VSA-tekst zelf bevatten uitsluitend relatieve hoogte-modifiers.

### 5.6 Toonladder en toonladdergraden

Binnen een do-context wordt een geordende reeks toonladdergraden afgeleid:

```text
do → re → mi → fa → sol → la → ti → do
```

Deze graden vormen een cyclische structuur.

De afstand tussen opeenvolgende graden is niet uniform. De stapstructuur wordt bepaald door de gekozen modus.

### 5.7 Modusdefinitie

Een modus definieert de intervalstructuur van de toonladder binnen een do-context.

Een modus specificeert voor elke overgang tussen opeenvolgende graden of deze overgang een grote stap of een kleine stap is.

De zeven overgangen zijn:

```text
do→re, re→mi, mi→fa, fa→sol, sol→la, la→ti, ti→do
```

Een modus kan worden weergegeven als een patroon van zeven staptypen:

```text
G = grote stap
K = kleine stap
```

#### Majeurmodus

In de majeurmodus zijn de kleine stappen:

- `mi → fa`;
- `ti → do`.

Representatie:

```text
G G K G G G K
```

#### Natuurlijke mineurmodus

In de natuurlijke mineurmodus zijn de kleine stappen:

- `re → mi`;
- `sol → la`.

Representatie:

```text
G K G G K G G
```

#### Andere modi

Andere modi kunnen worden gedefinieerd door het stappatroon te wijzigen.

Voorbeelden:

```text
Dorisch:   G K G G G K G
Frygisch:  K G G G K G G
Lydisch:   G G G K G G K
```

De do-context bepaalt dus het startpunt. De modus bepaalt de interne structuur van de toonladder.

### 5.8 Interpretatie van EHMs

Een EHM is een operator op de actuele toonladderpositie. Een EHM bestaat uit een optionele halftoon-prefix en een basisbeweging. Het semantische effect is:

```
netto beweging = basisbeweging + prefix_delta
```

waarbij `prefix_delta` gelijk is aan +½ toon voor prefix `#` (of alias `+`, `♯`) en −½ toon voor prefix `b` (of alias `♭`).

#### Basisbewegingen

| EHM     | Semantisch effect            |
| ------- | ---------------------------- |
| `/`     | verplaats één graad omhoog   |
| `//`    | verplaats twee graden omhoog |
| `///`   | verplaats drie graden omhoog |
| `////`  | verplaats vier graden omhoog |
| `/////` | verplaats vijf graden omhoog |
| `\`     | verplaats één graad omlaag   |
| `\\`    | verplaats twee graden omlaag |
| `\\\`   | verplaats drie graden omlaag |
| `\\\\`  | verplaats vier graden omlaag |
| `\\\\\` | verplaats vijf graden omlaag |
| `-`     | behoud de huidige toonhoogte |
| `~`     | behoud de huidige toonhoogte |

#### Halftoon-prefix combinaties (voorbeelden)

| EHM  | Basisbeweging | Prefix | Netto effect                  |
| ---- | ------------- | ------ | ----------------------------- |
| `#/` | +1 graad      | +½     | +1 graad + ½ toon omhoog      |
| `b/` | +1 graad      | −½     | +1 graad − ½ toon (= +½ toon) |
| `#\` | −1 graad      | +½     | −1 graad + ½ toon (= −½ toon) |
| `b\` | −1 graad      | −½     | −1 graad − ½ toon             |
| `#-` | 0 graden      | +½     | +½ toon (chromatisch omhoog)  |
| `b-` | 0 graden      | −½     | −½ toon (chromatisch omlaag)  |

EHMs worden sequentieel toegepast. Bij blokmetadata `do="C4"` en `mode="major"` produceert de EHM-reeks `/`, `\\`, `///` de toonreeks:

```text
C4 → D4 → B3 → E4
```

Hierbij wordt uitgegaan van opeenvolgende toonladderstappen binnen de gekozen modus.

### 5.9 Geldigheid van halftoon-prefix combinaties

Een EHM met halftoon-prefix is semantisch geldig als het resulterende interval (basisbeweging ± ½ toon) zinvol is binnen de do-context en modus. Een prefix mag nooit standalone voorkomen; hij moet altijd onmiddellijk voorafgaan aan een basisbeweging.

Semantische geldigheid vereist dat:

1. de basisbeweging zelf geldig is binnen de huidige toonladderpositie en modus;
2. de aanvullende ½ toon een gedefinieerd interval oplevert (de modus staat een dergelijke chromatische aanpassing toe).

Als aan voorwaarde 2 niet is voldaan, is de EHM een semantische fout.

Voorbeeld van zo'n semantische fout:

```text
::: vsa-notatie
do="C4"
mode="major"

[//:] {#/tekst}
:::
```

Als de actuele positie op `mi` staat en de overgang `mi → fa` al een kleine stap is, dan brengt `#/` de melodie een extra ½ toon buiten de toonladder. Als de modus hiervoor geen gedefinieerde subpositie heeft, is dit een semantische fout.

De onderscheiding tussen een halftoon-prefix op een basisbeweging en een zelfstandige chromatische aanpassing (`#-`, `b-`) heeft ook semantisch gevolgen voor MusicXML-export: `b-` beschrijft een chromatische verschuiving op de huidige positie, terwijl `b/` een combinatie is van een ladderstap en een halvering.

### 5.10 Interpretatie van ELMs

Een ELM bepaalt de duur van één muzikale positie ten opzichte van de standaardduur.

| ELM  | Duur                |
| ---- | ------------------- |
| `-`  | 1 × standaardduur   |
| `~`  | 1 × standaardduur   |
| `_`  | 2 × standaardduur   |
| `_.` | 3 x standaardduur   |
| `__` | 4 × standaardduur   |
| `.`  | 1/2 × standaardduur |
| `..` | 1/4 × standaardduur |

Voor MusicXML-export wordt de standaardduur gemapt naar een kwartnoot, tenzij extern anders gespecificeerd.

### 5.11 Absolute en relatieve toonhoogte

VSA legt toonhoogten primair relatief vast. Elke muzikale positie bevat een EHM die de toonhoogteverandering ten opzichte van de voorgaande muzikale positie specificeert.

Een absolute toonhoogte kan nodig zijn voor interpretatie, validatie of MusicXML-export, maar staat niet in de toonhoogte-markering. Zij wordt via blokmetadata geleverd.

Voorbeeld:

```markdown
::: vsa-notatie
do="C4"
mode="major"

[:] {\O}, {/Hei__}{\&/li}{/ge} {\&/God__&__}
:::
```

produceert, bij interpretatie in majeur met `C4` als `do`, de toonreeks:

```text
B3 C4 B3 C4 D4 C4 D4
```

### 5.12 Toonhoogte-markeringen

Een toonhoogte-markering bevat alleen een relatieve hoogte-modifier en geeft daarmee aan op welke toonladdergraad de zang zicht bevindt ten opzichte van de do-context op de positie van die toonhoggte markering.

Elke hoogte-markering geeft een (toon)hoogte aan ten opzichte van de basistoon ('do').

Voor de eerste hoogte-markering wordt de hoogte (of basistoon) extern gegeven. 
In de praktijk van het zingen wordt dit aangegeven door de koorlei(st)er.
Binnen de context van conversies, bijvoorbeeld naar MusicXML, wordt dat gespecificeerd 
door de feitelijke conversie - dat is buiten de scope van VSA.

Elke volgende hoogte-markering geeft aan dat de zang op die positie op die hoogte moet zitten. 
Een latere hoogte-markering vervangt dus niet de eerdere markering als documentstructuur, maar introduceert een nieuwe pitch-positie in dezelfde melodische lijn.

Het is een gangbare praktijk om voor een zangstuk een hoogte-markering te schrijven,
en om dit ook aan het eind van een zangstuk te doen (ter controle voor zangers).
Indien twee zangstukken elkaar opvolgen, kan dat vanuit VSA perspectief dan ook
gezien worden als een enkel zangstuk met tussenliggende hoogte-markeringen.


 Een beginmarkering `[:]` betekent dat de zang op de do-context begint. Een markering `[//:]` betekent dat de zang twee ladderstappen boven de do-context begint.

Een eindmarkering kan worden gebruikt als visuele afsluiting en als semantische eindcontrole. Een ontbrekende eindmarkering is toegestaan en betekent dat er geen expliciete eindtooncontrole is genoteerd. Een eindmarkering `[:]` is niet leeg in semantische zin: zij betekent dat de zang op de do-context eindigt en is equivalent aan `[-:]` c.q. `[~:]`. Een markering `[//:]` betekent dat de zang twee ladderstappen boven de do-context eindigt. Een implementatie mag een aanwezige eindmarkering controleren tegen de berekende eindtoon van het zangstuk.

### 5.13 Tekstmarkeringen buiten scopes

Bepaalde tekstfragmenten buiten scopes kunnen door implementaties semantisch worden geïnterpreteerd.

| Tekst | Betekenis                    | MusicXML           |
| :---: | ---------------------------- | ------------------ |
| `*`   | rustpunt of ademhaling       | ademteken          |
| `/`   | frasescheiding of maatstreep | maatstreep         |
| `//`  | sterke frasescheiding        | dubbele maatstreep |

Deze markeringen maken geen deel uit van de kernsyntax van VSA-scopes,
maar mogen door renderers of weergavecomponenten en exporteurs semantisch worden verwerkt.

---
