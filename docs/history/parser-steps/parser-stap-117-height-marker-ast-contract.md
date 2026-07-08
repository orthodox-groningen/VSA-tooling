# Stap 117 - Height Marker AST Contract

## Doel

De resterende hoogte-marker implementatie vastzetten voordat parser- en validatorwerk begint.

## AST-model

Hoogte-markeringen zijn gewone nodes in de documentstroom.

```text
Document
  TextNode
  HeightMarkerNode
  ScopeNode
  HeightMarkerNode
  TextNode
```

Niet:

```text
Document(start_marker, body, end_marker)
```

## Semantiek

Eerste hoogte-marker:

```text
start_height
```

Vervolg hoogte-markeringen:

```text
local_height
```

## Rendering

SVG maakt geen onderscheid tussen:

- eerste hoogte-marker
- latere hoogte-marker

Iedere marker wordt positioneel gerenderd.
