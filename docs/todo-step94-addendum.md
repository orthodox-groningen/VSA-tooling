# TODO addendum stap 94

Toevoegen aan `docs/todo.md` onder parser:

## Bracket-directive dispatch

Status: `Gespecificeerd`

Besluit:

- hoogte-markering blijft `[<EHM>:]`;
- `:]` is één eindtoken van een bracket-directive;
- niet tokenizen als losse `:` en `]`;
- niet overstappen op `{<EHM>:}`;
- parser moet later bracket-token dispatch krijgen.
