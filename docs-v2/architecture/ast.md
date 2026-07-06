# AST-model

De AST is het interne contract tussen parser, validator en renderer.

## Hoofdconcepten

| Node                       | Betekenis                                                     |
| -------------------------- | ------------------------------------------------------------- |
| `Document`                 | Root-node van het volledige document.                         |
| `TextNode`                 | Gewone tekst buiten of binnen verwerkbare context.            |
| `ScopeNode`                | VSA-scope met tekst en modifiers.                             |
| `PitchMarkerNode`          | Hoogte- of toonmarkering als positionele node.                |
| `ControlTokenNode`         | Control directive zoals wrap- of renderaanwijzing.            |
| `Diagnostic`               | Validatie- of parsermelding met locatie en ernst.             |

## Hoogtemarkers

Hoogtemarkers zijn positionele nodes in de documentstroom.

```text
Document
  nodes:
    PitchMarkerNode("/")
    TextNode("Heer, ")
    ScopeNode(...)
    PitchMarkerNode("\\")
    TextNode("U")
```

De eerste markering kan semantisch een beginhoogte aanduiden, maar rendering blijft positioneel. De renderer mag dus niet afhankelijk zijn van een speciale begin- of eindmarker-case.

## AST-contract

| Regel                             | Reden                                               |
| --------------------------------- | --------------------------------------------------- |
| Nodes blijven expliciet           | Validator en renderer kunnen hetzelfde model lezen. |
| Markers zijn geen wrappers        | Markers horen bij posities, niet bij documentgrenzen. |
| Broninformatie blijft beschikbaar | Diagnostiek moet naar invoerposities verwijzen.     |
| Renderer wijzigt geen AST         | Rendering is output, geen semantische transformatie. |
