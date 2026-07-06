# Stap 106b - HeightMarker/PitchMarker AST-compatibiliteit

## Doel

Deze stap legt expliciet vast dat `HeightMarkerNode` voorlopig een alias blijft van `PitchMarkerNode`.

## Reden

Een echte aparte `HeightMarkerNode` brak bestaande onderdelen:

- parserregressies;
- SVG-layout;
- SVG-rendering;
- bestaande AST-serialisatie.

Daarom blijft de runtime-compatibiliteit voorlopig:

```python
HeightMarkerNode is PitchMarkerNode
```

## Afspraak

Totdat renderer, validator en AST-regressiebestanden samen worden gemigreerd:

- parser mag hoogte-markeringen blijven leveren als `PitchMarkerNode`;
- `HeightMarkerNode` mag als terminologische alias bestaan;
- `to_dict()` blijft `"PitchMarkerNode"` serialiseren;
- SVG-rendering blijft pitchmarker-klassen gebruiken.

## Later

Een echte aparte `HeightMarkerNode` kan pas in een eigen migratiestap waarin tegelijk worden aangepast:

- AST-regressies;
- parser-tests;
- semantic validator;
- SVG layout;
- SVG renderer;
- SVG rendering tests;
- documentatie.
