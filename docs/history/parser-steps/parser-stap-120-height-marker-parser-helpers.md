# Stap 120 - Height marker parser helpers

## Doel

De parser levert hoogte-markeringen al als compatibele nodes.

Deze stap maakt de helperlaag compleet en stabiel, zodat validator, renderer en latere exportcode hoogte-markeringen via één module kunnen vinden.

## Helpers

```python
height_marker_refs(document)
height_marker_nodes(document)
height_markers(document)
iter_height_markers(document)
first_height_marker(document)
last_height_marker(document)
local_height_markers(document)
is_height_marker_node(node)
```

## Compatibiliteit

`height_marker_refs` en `height_marker_nodes` uit stap 118 blijven bestaan.

Nieuwe namen zijn aliases of aanvullingen, geen brekende vervanging.

## Rollen

De helperlaag kent rollen toe in documentvolgorde:

| Marker | Rol |
|---|---|
| eerste marker | `start_height` |
| latere markers | `local_height` |

## Belangrijk

Deze stap verandert geen parsergedrag.

`HeightMarkerNode` blijft voorlopig compatibel met `PitchMarkerNode`.

## Volgende stap

Stap 121 kan de validator op deze helperlaag aansluiten.
