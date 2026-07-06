# Architectuuroverzicht

## Verwerkingsketen

```text
Markdown / VSA-tekst
  ↓
Lexer / tokenizer
  ↓
Parser
  ↓
AST
  ↓
Semantische validatie
  ↓
Renderers
  ├─ SVG
  ├─ Markdown/Hugo
  └─ JSON/diagnostics
```

## Ontwerpprincipe

De parser bouwt een expliciet documentmodel op. Semantische betekenis wordt daarna door de validator gecontroleerd. Rendering blijft zo veel mogelijk positioneel en mag geen semantische reparaties uitvoeren.

## Laagverdeling

| Laag | Verantwoordelijkheid |
|------|----------------------|
| Tokenizer | Herkennen van tekst, scopes, markers en directives |
| Parser | Opbouwen van het AST |
| Validator | Controleren van syntactisch geldige maar semantisch problematische constructies |
| Renderer | Omzetten naar SVG, Markdown, Hugo of JSON |
| Publicatie | Controleren en publiceren van gegenereerde output |

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/parser-fases.md`
- `docs/architecture/height-marker-model.md`
- `docs/architecture/parser-stap-37-diagnostic-severity.md`
- `docs/architecture/parser-stap-46-rendering-specs.md`
- `docs/architecture/parser-stap-137-publication-checks-and-reusable-tool.md`
