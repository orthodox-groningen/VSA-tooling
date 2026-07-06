# Parserarchitectuur

## Doel

De parser zet platte VSA-tekst om naar een AST dat geschikt is voor validatie en rendering.

## Fasen

```text
tekst
  ↓
lexer
  ↓
tokens
  ↓
parser
  ↓
AST
```

## Basiselementen

De parser moet in ieder geval deze onderdelen herkennen:

- vrije tekst;
- scopes `{...}`;
- pitch/height markers zoals `[:]`, `[/:]`, `[//:]`;
- lengte- en hoogtemodifiers binnen scopes;
- bracket-directives en control tokens.

## Dispatch

Bracketconstructies worden niet als losse speciale gevallen behandeld. De parser gebruikt een dispatchmodel waarin markers, directives en control tokens elk hun eigen herkenning en AST-representatie krijgen.

## Parsergrens

De parser controleert structuur. Betekenisvolle regels zoals aantallen posities, severity en herstelbare fouten horen in de validator.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/parser-fases.md`
- `docs/architecture/parser-stap-105-parser-bracket-token-stream.md`
- `docs/architecture/parser-stap-109-wraptoken-dispatch.md`
- `docs/architecture/parser-stap-112-control-token-dispatch.md`
- `docs/architecture/parser-stap-114-dispatch-design.md`
- `docs/architecture/parser-stap-119-height-marker-parser-contract.md`
- `docs/architecture/parser-stap-120-height-marker-parser-helpers.md`
