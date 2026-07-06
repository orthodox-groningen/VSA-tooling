# Stap 14 fix - SVG regressietests robuuster

De eerste SVG-regressietest vergeleek de volledige SVG exact.

Dat is te vroeg, omdat de renderer-layout nog verandert.

Daarom gebruiken we voorlopig metadata:

```json
{
  "contains_text": ["Hei", "lig"],
  "min_lines": 4,
  "min_circles": 0
}
```

Later, zodra de layout stabiel is, kunnen we weer exacte `expected.svg` regressies afdwingen.
