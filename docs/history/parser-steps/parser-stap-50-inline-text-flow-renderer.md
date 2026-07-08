# Stap 50 - inline text-flow renderer

Deze stap verandert de SVG-rendering richting normale lopende tekst.

## Belangrijk

- Spaties tellen weer mee in breedtemeting.
- SVG-tekst gebruikt `xml:space="preserve"`.
- Scopes krijgen standaard geen extra gap.
- Glyphs worden overlays boven/onder de tekst.
- Regels en marges zijn compacter.

## Reden

De renderer moet visueel lijken op:

```text
normale tekst met accenten
```

en niet op:

```text
losse muzikale blokken met tekst erin
```
