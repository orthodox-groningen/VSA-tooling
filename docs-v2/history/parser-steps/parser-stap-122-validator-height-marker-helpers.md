# Stap 122 - Validator aansluiten op height marker helpers

## Doel

De semantische validator gebruikt voortaan de centrale helperlaag voor hoogte-markeringen.

## Wijziging

Bij initialisatie verzamelt de validator:

```python
self.height_markers = height_marker_refs(document)
```

en exposeert dat intern via:

```python
validator._height_markers()
```

## Gedrag

Deze stap verandert nog geen validatieregels.

Wel is nu vastgelegd dat latere validatorregels niet rechtstreeks naar `PitchMarkerNode` of `HeightMarkerNode` hoeven te kijken.

## Volgende stap

Stap 123 kan daadwerkelijke hoogte-marker validatieregels toevoegen, bijvoorbeeld:

- meerdere markers blijven toegestaan;
- eerste marker is `start_height`;
- latere markers zijn `local_height`;
- eindcontrole gebruikt `last_height_marker`.
