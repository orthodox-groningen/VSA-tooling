# Stap 43 - validator usability fix

Deze stap corrigeert validatorgedrag op basis van praktijkbestanden.

## Final pitchmarker

Leeg is toegestaan:

```text
[:]
```

Aan het einde betekent dit hetzelfde als:

```text
[-:]
```

Daarom is deze regel verwijderd:

```text
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
```

## Regels en kolommen

Parserfouten met een karakterpositie worden nu omgerekend naar regel/kolom
binnen het Markdownbestand.

Oud:

```text
bestand.md:blok-1:1:1
```

Nieuw:

```text
bestand.md:5:12
```

## Vrije tekst

Buiten scopes en pitchmarkers mag gewone tekst `/`, `\` en `//` bevatten.

De structurele VSA-tekens blijven:

```text
{ } [ ]
```
