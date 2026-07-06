# Stap 106a - repair HeightMarker compatibiliteit

## Probleem

Een echte aparte `HeightMarkerNode` brak bestaande parser-, renderer- en SVG-tests.

De huidige renderer en validator herkennen hoogte-markeringen nog via `PitchMarkerNode`.

## Besluit

`HeightMarkerNode` blijft voorlopig een compatibele alias:

```python
HeightMarkerNode = PitchMarkerNode
```

Een echte aparte class komt pas nadat renderer, validator en regressie-AST's gelijktijdig zijn gemigreerd.

## Status

Stap 106 wordt hiermee teruggebracht tot terminologische voorbereiding, zonder runtime-typewijziging.
