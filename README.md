# VSA Parser stap 2

Deze stap voegt toe:

- tokens;
- lexer;
- diagnostics;
- syntax-validator;
- regel/kolom-informatie;
- strengere syntax-validatie.

## Nieuwe architectuur

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
syntax validator
```

## Testen

Alle tests:

```cmd
scripts\test.cmd
```

Alleen lexer:

```cmd
python -m pytest tests\test_lexer.py -v
```

Alleen syntax-validatie:

```cmd
python -m pytest tests\test_syntax_validation.py -v
```

CLI AST-output:

```cmd
vsa examples\minimal\013_height_and_length.vsa --ast
```
