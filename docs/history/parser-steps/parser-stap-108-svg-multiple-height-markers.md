# Stap 108 - SVG-rendering van meerdere hoogte-markeringen

## Doel

De parser en semantische validator accepteren meerdere hoogte-markeringen.

Deze stap borgt dat de SVG-rendering ze ook allemaal zichtbaar houdt.

## Verwachting

Voor:

```text
[:] tekst [/:] meer [//:] einde
```

moet SVG-rendering bevatten:

- drie `vsa-pitch-marker` units;
- drie `vsa-pitch-marker-dash` lijnen;
- hoogte-glyphs voor de niet-lege hoogte-markeringen;
- tekst vóór, tussen en na hoogte-markeringen.

## Besluit

Voorlopig blijven SVG-klassen en AST-serialisatie de bestaande naam `pitch-marker` gebruiken.

Een latere echte migratie naar `height-marker` namen mag alleen als parser, validator, renderer, CSS en tests tegelijk worden aangepast.
