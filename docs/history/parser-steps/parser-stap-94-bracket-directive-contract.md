# Stap 94 - bracket-directive contract

## Besluit

Voor hoogte-markeringen gebruiken we de bestaande bracketvorm:

```text
[<EHM>:]
```

Dit wordt gezien als een gespecialiseerde bracket-directive.

## Tokenmodel

De parser moet het einde van de directive zien als één eindtoken:

```text
:]
```

Dus niet als twee losse syntaxelementen:

```text
:
]
```

## Reden

Hierdoor kan later extra syntax tussen `[` en `:]` worden toegevoegd zonder dat de parser hoeft te raden of `:` en `]` apart bedoeld zijn.

## Geen overstap naar `{<EHM>:}`

Voor nu stappen we niet over op:

```text
{<EHM>:}
```

Redenen:

- `{...}` is al in gebruik voor scopes en gezongen tekst/modifiers;
- `[...:]` onderscheidt control/directive-syntax duidelijker van gezongen tekst;
- bracket-token dispatch was al een open parserpunt;
- latere directive-uitbreidingen passen natuurlijker in bracket-syntax.

## Implicatie

Een hoogte-markering is:

```text
"[" + <EHM> + ":]"
```

Niet:

```text
"[" + <EHM> + ":" + "]"
```
