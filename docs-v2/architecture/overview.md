# Architectuuroverzicht

De VSA-tooling verwerkt platte tekst met VSA-scopes en directives naar gestructureerde output, vooral SVG en markdown/Hugo-output.

```text
bronbestand
  ↓
lexer
(zet invoertekst om in een reeks betekenisvolle tokens)
  ↓
tokens
(de kleinste betekenisvolle bouwstenen die de parser ontvangt, bijv. `TEXT("De ")` of `EHM_VALUE("//")`)
  ↓
parser 
(bouwt uit de tokens een syntactische boom volgens de grammatica)
  ↓
AST (Abstract Syntax Tree)
(een implementatie-onafhankelijke representatie van de structuur en betekenis van het document)
  ↓
validator 
(controleert of de AST voldoet aan alle semantische en normatieve regels)
  ↓
layout engine 
(bepaalt de abstracte positionering van tekst en notatie-elementen, onafhankelijk van het uiteindelijke uitvoerformaat)
  ↓
renderer
(zet de abstracte layout om naar een concreet uitvoerformaat, zoals)
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
