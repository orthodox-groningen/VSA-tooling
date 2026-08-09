# Testvoorbeelden en regressietests voor VSA-tooling

Deze map bevat kleine [VSA](@)-[fixtures](@) die bedoeld zijn om [parser](@), [validator](@), [renderer](@) en exporter stap voor stap te kunnen bouwen en testen.

De voorbeelden zijn bewust klein gehouden. Grote echte [zangstukken](@bron) zijn nuttig als eindtest, maar kleine gevallen zijn veel beter voor debugging.

## Indeling

```text
examples/
├── minimal/
├── edge-cases/
└── regression/
```

## `examples/minimal`

Deze map bevat geldige, kleine VSA-fragmenten.

Doel:

- [parser](@) controleren;
- [AST](@)-vorm controleren;
- eenvoudige rendering controleren;
- eenvoudige MusicXML-export voorbereiden.

## `examples/edge-cases`

Deze map bevat bewust lastige gevallen.

Doel:

- syntaxfouten herkennen;
- semantische fouten herkennen;
- foutmeldingen controleren.

De naam van elk bestand geeft aan wat er getest wordt.

## `examples/regression`

Deze map bevat testsets met vaste verwachte uitvoer.

Elke testmap kan later deze structuur krijgen:

```text
input.vsa
expected-ast.json
expected-validation.json
expected.svg
expected.musicxml
```

Voor versie 1 zijn vooral `input.vsa`, `expected-ast.json` en `expected-validation.json` belangrijk.

## Teststrategie

Aanbevolen volgorde:

1. parse `input.vsa`;
2. vergelijk resultaat met `expected-ast.json`;
3. voer validatie uit;
4. vergelijk resultaat met `expected-validation.json`;
5. render later naar SVG;
6. exporteer later naar MusicXML.

## Belangrijk

De bestanden zijn bedoeld als startpunt. Als de specificatie wijzigt, moeten ook de verwachte testuitkomsten worden aangepast.
