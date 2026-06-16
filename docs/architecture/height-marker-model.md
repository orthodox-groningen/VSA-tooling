# Architectuurnotitie: hoogte-marker-model

## Probleem

De oude benadering behandelt hoogte-markeringen impliciet alsof ze vooral begin- of eindmarkeringen zijn.

Dat past niet meer bij het gewenste model.

## Nieuw model

Hoogte-markeringen zijn positionele nodes in de documentstroom.

De eerste markering heeft semantisch een speciale rol: beginhoogte.

Rendering maakt geen onderscheid.

## Gewenste AST-richting

```text
Document
  nodes:
    TextNode("Heer, ")
    HeightMarkerNode("/")
    TextNode("ontferm ")
    ScopeNode(...)
    HeightMarkerNode("\")
    TextNode("U")
```

Naamgeving mag in de code afwijken, maar het concept moet blijven:

```text
marker als node, niet als wrapper rond document
```

## Geen quick-and-dirty

Niet doen:

- speciale cases voor eerste/laatste marker in renderer;
- markers verplaatsen naar begin/eind;
- parserfouten onderdrukken door tekstueel voorbewerken;
- semantiek in SVG-code stoppen.

Wel doen:

- parsermodel helder maken;
- validator over nodes laten lopen;
- rendering puur positioneel houden;
- MusicXML later apart uitwerken.
