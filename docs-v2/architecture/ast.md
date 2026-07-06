# AST-architectuur

## Uitgangspunt

Het AST beschrijft de documentstroom expliciet. Markers zijn nodes in die stroom, niet impliciete begin- of eindtoestanden.

## Conceptueel model

```text
Document
  nodes:
    TextNode
    ScopeNode
    HeightMarkerNode
    ControlTokenNode
    DirectiveNode
```

## Hoogtemarkers

Hoogtemarkers worden positioneel gemodelleerd. De eerste hoogtemarker kan semantisch een speciale rol hebben als beginhoogte, maar de renderer behandelt markers niet als speciale begin- of eindconstructies.

## Scope-inhoud

Scopes dragen tekst, hoogte-informatie en lengte-informatie. De validator controleert of de posities daarvan semantisch bij elkaar passen.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/height-marker-model.md`
- `docs/architecture/parser-stap-111-control-token-ast-node.md`
- `docs/architecture/parser-stap-117-height-marker-ast-contract.md`
- `docs/architecture/parser-stap-118-height-marker-ast-helpers.md`
- `docs/architecture/parser-stap-106b-height-marker-ast-compatibility.md`
