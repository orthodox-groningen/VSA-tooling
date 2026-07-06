# Parserarchitectuur

De parser zet VSA-brontekst om naar een AST. De verwerking verloopt bewust in fasen: eerst syntactische structuur, daarna semantische validatie, daarna rendering.

```text
tekst
  ↓
lexer / bracket-scanner
  ↓
tokens
  ↓
parser
  ↓
AST
```

## Kernverantwoordelijkheden

| Onderdeel          | Verantwoordelijkheid                                      |
| ------------------ | ---------------------------------------------------------- |
| Tekstscanner       | Gewone tekst behouden, inclusief relevante spacing.        |
| Scopeparser        | `{...}`-scopes herkennen en als scopes modelleren.         |
| Modifierparser     | Hoogte- en lengtemodifiers binnen scopes herkennen.        |
| Bracket-dispatch   | `[...]`-tokens routeren naar het juiste parserpad.         |
| AST-opbouw         | Nodes maken zonder renderlogica.                           |
| Foutlokalisatie    | Posities bewaren voor bruikbare diagnostiek.               |

## Parserbeleid

De parser moet geen semantische reparaties uitvoeren die later onzichtbaar worden. Als invoer syntactisch herkenbaar is maar inhoudelijk problematisch, hoort dat bij de validator.

Niet doen:

- markers tekstueel voorbewerken voordat de parser ze ziet;
- begin- of eindmarkers speciaal behandelen in de renderer;
- semantische fouten onderdrukken door parser-rewrites;
- scope-inhoud renderen voordat de AST compleet is.

Wel doen:

- bracket-tokens vroeg herkennen;
- expliciete AST-nodes maken;
- bronposities bewaren;
- parsercontracten klein en testbaar houden.
