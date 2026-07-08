# Stap 118 - Height marker AST helpers

## Doel

Hoogte-markeringen blijven voorlopig runtime-compatibel met `PitchMarkerNode`, maar krijgen nu een expliciete helperlaag voor gebruik door validator, rendering en latere export.

## Model

Hoogte-markeringen blijven gewone nodes in de documentstroom.

```text
Document
  TextNode
  PitchMarkerNode / HeightMarkerNode alias
  ScopeNode
  PitchMarkerNode / HeightMarkerNode alias
```

## Helpers

```python
height_marker_refs(document)
height_marker_nodes(document)
first_height_marker(document)
local_height_markers(document)
```

## Rollen

De helperlaag kent twee rollen:

| Rol | Betekenis |
|---|---|
| `start_height` | eerste hoogte-markering in documentvolgorde |
| `local_height` | elke volgende hoogte-markering |

## Belangrijk

Deze stap wijzigt de parser, validator en SVG-renderer niet.

Een echte aparte `HeightMarkerNode` class blijft uitgesteld tot parser, validator, renderer en AST-regressies samen kunnen migreren.
