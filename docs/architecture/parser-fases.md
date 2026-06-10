# Parserfases

Aanbevolen implementatievolgorde:

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
  ↓
syntax-validatie
```

## Eerste doel

Deze onderdelen werkend krijgen:

- `TextNode`
- `ScopeNode`
- `PitchMarkerNode`
- `Document`

Nog geen semantiek.

## Daarna

Pas later toevoegen:

- semantische validatie;
- SVG-rendering;
- MusicXML-export.
