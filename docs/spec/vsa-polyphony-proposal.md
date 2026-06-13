# Voorstel voor toekomstige meerstemmige uitbreiding van VSA

{{ Maak de volgende wijzigingen (gooi geen dingen weg die niet veranderd/aangepast zijn, omdat die allemaal ooit een doel hadden en er dus niet voor niets staan. Je moet zeker weten dat als je iets niet meer opneemt, dat een doublure is, of dat je hetzelfde op een betere/duidelijk manier verwoordt voor het lezerspubliek! Laat het weten als je tegen grenzen aanloopt die het je onmogelijk maken deze taak te volbrengen, en wat ik daar aan kan doen.):
1. 
}}

## Uitgangspunt

De huidige VSA-notatie richt zich op een melodische hoofdstem waarbij de melodie direct boven en onder de tekst wordt genoteerd.

In de orthodoxe praktijk bestaan echter meestal meerdere stemmen (S, A, T, B) die dezelfde tekst zingen, vaak met min of meer vergelijkbare ritmische structuur en (vooral) afwijkende toonhoogtebewegingen. Ook is de orthodoxe praktijk dat zangstukken als troparen, kondaken, stichieren e.d. een klein aantal melodielijnen hebben die cyclisch worden uitgevoerd over het (grotere aantal) strofes van zo'n zangstuk, met nog een of twee melodielijnen die voor de laatste (twee) strofe(s) word(en) gebruikt.

Doelen van een toekomstige uitbreiding:

- de hoeveelheid typwerk minimaliseren voor beheerders die andere teksten op een bestaande melodie willen schrijven;
- minimale duplicatie van tekst;
- behoud van synchronisatie tussen stemmen;
- compatibiliteit met bestaande VSA-notatie;
- ondersteuning van formulematige orthodoxe zangpraktijk.

---

## Kernidee

De melodische hoofdstem wordt de canonieke bron.

Andere stemmen worden beschreven als overlays of afwijkingen op dezelfde muzikale tijdlijn.

Tekstsegmenten worden expliciet gekoppeld aan genummerde placeholders.

Voorbeeld:

{{voorbeeld eerst nog beter uitwerken zodat het klopt}}

```markdown
S: ${1} {/&/${2}_&_} {\\${2}} {~${3}-} {}
A: {\${1}_} {-${2}} {~${3}-}
T: {-${1}_} {\${2}} {~${3}-}
B: {\\${1}_} {\\${2}} {~${3}-}
```

Tekstsegmenten:

```text
1=Ter
2=wijl
3=de steen door de israëlie
4=ten
5=ver
6=ze
7=geld
8=was
```

Alle stemmen blijven hierdoor automatisch tekstueel synchroon.

---

## Betekenis van placeholders

Een placeholder representeert een tekstsegment dat op een muzikale positie wordt geprojecteerd.

De mappinglaag koppelt:

```text
placeholder -> tekstsegment
```

aan:

```text
muzikale positie -> EHM + ELM
```

Hierdoor kunnen:

- dezelfde teksten over meerdere stemmen worden verdeeld;
- melodische formules worden hergebruikt;
- SATB-structuren compact worden beschreven.

---

## Rol van `~` en `-`

De modifiers `~` en `-` blijven beide belangrijk.

### `~`

Betekenis:

- semantisch aanwezig;
- standaardtoon of standaardduur;
- renderer toont geen glyph (of onzichtbaar).

### `-`

Betekenis:

- semantisch gelijk aan standaardtoon of standaardduur;
- renderer toont een zichtbare glyph.

Daardoor kunnen implementaties per stem bepalen:

- welke muzikale posities expliciet zichtbaar zijn;
- welke alleen structureel aanwezig zijn.

---

## Relatie met orthodoxe toon-/glaspraktijk

Orthodoxe tonen (glas 1 t/m 8) functioneren vaak als formulebibliotheken.

Een toekomstige uitbreiding van VSA kan daarom werken met:

```text
toon/glas
    -> melodieformules
        -> tekstprojectie
            -> SATB-overlays
```

Daardoor hoeven melodieën niet steeds volledig opnieuw genoteerd te worden.

---

## Status

Dit document beschrijft een toekomstig uitbreidingsvoorstel voor VSA.

Het maakt nadrukkelijk geen onderdeel uit van de huidige eenstemmige VSA-specificatie.
