# Stap 56 - TODO en newline wrap policy

Deze stap voegt `docs/todo.md` toe en corrigeert de SVG-layoutpolicy.

## Gekozen voor nu

Wel:

- CR;
- LF;
- CRLF;
- bron-newline als harde regelgrens.

Niet:

- `[/]`;
- `[*]`;
- `[/?]`;
- `[*?]`.

Die tokens vragen eerst om bracket-token dispatch in de parser.
