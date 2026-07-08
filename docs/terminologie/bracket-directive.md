---
slug: bracket-directive
term: bracket-directive
termType: concept
glossaryTerm: Bracket-directive
glossaryText: "een tekstfragment dat als afzonderlijk VSA-token tussen `[` en `]` voorkomt en door bracket-dispatch wordt geclassificeerd voordat de inhoudelijke parsing verdergaat."
glossaryAlias: Bracket-token
formPhrases:
  - bracket-directive
  - bracket-directives
  - bracket-token
  - bracket-tokens
---

# Bracket-directive

Bracket-directives zijn de `[...]`-tokens die de parser eerst routeert naar een specifiek parserpad, bijvoorbeeld pitch-marker, control-token, onbekende directive of syntaxfout.
