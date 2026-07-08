# Stap 13 - eenvoudige SVG-glyphs

Deze stap vervangt tijdelijke debugtekst door echte SVG-elementen.

Voorbeelden:

```text
/   → schuine lijn omhoog
\   → schuine lijn omlaag
_   → horizontale lijn onder tekst
.   → punt onder tekst
[:] → horizontale toonhoogte-markering
```

Dit is nog niet de definitieve typografie, maar wel de juiste richting:

```text
AST
  ↓
SVGRenderer
  ↓
SVGGlyphRenderer
  ↓
lijnen en punten
```
