# Architectuuroverzicht

De VSA-tooling verwerkt platte tekst met VSA-scopes en directives naar gestructureerde output, vooral SVG en markdown/Hugo-output.

```text
bronbestand
  ↓
lexer / scanner
  ↓
tokens
  ↓
parser
  ↓
AST
  ↓
validator
  ↓
renderer
  ├── SVG
  ├── JSON
  └── markdown / Hugo
```

## Principes

| Principe                         | Betekenis                                                            |
| -------------------------------- | -------------------------------------------------------------------- |
| Parser vóór renderer             | Syntax en structuur worden bepaald vóór rendering.                   |
| AST als contract                 | Renderer en validator werken op dezelfde expliciete structuur.       |
| Semantiek buiten SVG-code        | Validatieregels horen niet in de renderer thuis.                     |
| Positionele markers              | Hoogte- en controletokens staan als nodes in de documentstroom.      |
| Recoverable validatie            | De validator verzamelt fouten waar mogelijk in plaats van direct te stoppen. |
| Traceerbare consolidatie         | Ontwerpgeschiedenis blijft behouden en wordt niet inhoudelijk gewist. |

## Lagen

| Laag             | Verantwoordelijkheid                                      |
| ---------------- | ---------------------------------------------------------- |
| Lexer / scanner  | Herkennen van tekst, scopes en bracket-tokens.             |
| Parser           | Opbouwen van AST-nodes uit tokens.                         |
| AST              | Interne representatie van documentstructuur.               |
| Validator        | Controleren van semantische consistentie.                  |
| Renderer         | Genereren van SVG, JSON en markdown/Hugo-output.           |
| Publicatie       | Bouwen en controleren van demo- en Pages-output.           |
