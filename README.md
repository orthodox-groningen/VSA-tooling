# VSA SVG stap 7 - fix

Deze patch herstelt de eerste SVG-renderer.

Problemen opgelost:

- gewone tekst buiten scopes verdwijnt niet meer;
- tijdelijke zwarte debugpunten zijn verwijderd;
- hoogte-modifiers worden voorlopig als tekstuele glyphs boven het zangelement getoond;
- lengte-modifiers worden voorlopig als tekstuele glyphs onder het zangelement getoond;
- toonhoogte-markeringen worden als horizontale lijn weergegeven.

Dit is nog geen definitieve grafische VSA-rendering, maar de inhoudelijke lagen zijn nu correcter:

```text
bovenlaag  = hoogte-modifiers
tekstlaag  = gewone tekst + zangelementen
onderlaag  = lengte-modifiers
```
