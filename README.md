# VSA Parser Skeleton

Dit zipbestand bevat een eerste werkende basis voor:

- AST-structuren;
- parser-skelet;
- lexer-skelet;
- foutafhandeling;
- pytest-tests;
- regressietests.

Doel:

```text
VSA tekst
  ↓
parser
  ↓
AST
```

Nog niet inbegrepen:

- SVG-rendering;
- MusicXML-export;
- semantische validatie;
- Hugo-integratie.

## Aanbevolen eerste stap

Voer uit:

```cmd
scripts\bootstrap.cmd
scripts\test.cmd
```

Daarna:

- implementeer lexer;
- implementeer parser;
- laat regressietests slagen.
