# Stap 107 - semantische validatie voor meerdere hoogte-markeringen

## Doel

De parser accepteert inmiddels meerdere hoogte-markeringen in documentvolgorde.

Deze stap borgt dat de semantische validator die constructie accepteert.

## Regels

Geldig:

```text
[:] tekst [/:] meer tekst [//:] einde
tekst vóór [:] tekst na
begin [:] midden [\:] einde
gewone tekst zonder hoogte-markering
```

Niet de taak van de semantische validator:

- controleren of `[`-directives syntactisch geldig zijn;
- ongeldige EHM's herkennen;
- bracket-directives zonder `:]` herkennen.

Dat blijft parser-/syntaxvalidatie.

## Besluit

De semantische validator mag niet eisen:

```text
exact één hoogte-markering per document
```

De semantische validator mag ook niet eisen:

```text
eerste token is hoogte-markering
```

## Nog niet gedaan

Nog niet aangepast:

- SVG-rendering;
- MusicXML;
- echte aparte `HeightMarkerNode`;
- volledige migratie van `PitchMarkerNode` naar `HeightMarkerNode`.
