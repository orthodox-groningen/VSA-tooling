# Stap 16 - SVG autosizing

Deze stap verwijdert de vaste SVG-breedte van `1200px`.

De breedte wordt nu berekend op basis van:

```text
linkermarge
+ breedte van TextNodes
+ breedte van ScopeNodes
+ breedte van PitchMarkerNodes
+ rechtermarge
```

De SVG krijgt ook een `viewBox`.

## Waarom

Voor Hugo en Markdown is een vaste breedte onhandig.

Een korte regel zoals:

```text
{tekst}
```

moet geen enorm brede SVG opleveren.

## Later

Nog toe te voegen:

- automatische regelafbreking;
- echte fontmeting;
- responsive CSS.
