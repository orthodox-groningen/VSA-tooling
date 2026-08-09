---
slug: ast
term: ast
termType: concept
glossaryTerm: Abstract Syntax Tree
glossaryAbbr: AST
glossaryText: "een expliciete nodeboom die door de [parser](@) uit [VSA](@)-invoer wordt geproduceerd en die [validator](@) en [renderer](@) zonder semantische herinterpretatie kunnen lezen."
glossaryAlias: Syntactische boom
formPhrases:
  - ast
  - asts
  - abstract syntax tree
  - abstract syntax trees
  - syntactische boom
  - syntactische bomen
---

# AST

De AST / [syntactische boom](@) legt de documentstructuur vast nadat de
[parser](@) tokens heeft verwerkt. [Validator](@) en [renderer](@) lezen
dezelfde structuur; de [renderer](@) mag de AST niet wijzigen om semantiek te
repareren.

Goede/valide voorbeelden van AST zijn:
- Nodeboom uit de [parser](@) voor [validator](@)/[renderer](@)
- Bronlocaties behouden in nodes

Geen goede/niet valide voorbeelden van AST zijn:
- Een losse logregel of platte brontekst
- Semantische reparaties door de [renderer](@)
