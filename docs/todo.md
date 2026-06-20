# TODO lijst

Deze lijst is geconsolideerd uit `docs/todo.md` en alle `docs/todo-stepXX-addendum.md` bestanden.

Statuswaarden: `Open`, `In uitvoering`, `Later`, `Afgerond`, `Gespecificeerd`, `Geïmplementeerd`.

## 1. Parser, syntax en validatie

### 1.1 Meerdere hoogte-markeringen en bracket-directives

Status: `Geïmplementeerd`

- Meerdere hoogte-markeringen per `vsa-notatie` blok zijn toegestaan.
- Hoogte-markering blijft `[<EHM>:]`; `:]` is één eindtoken van een bracket-directive.
- Niet tokenizen als losse `:` en `]`; niet overstappen op `{<EHM>:}`.
- Tekst vóór, tussen en na hoogte-markeringen is toegestaan.
- Parser gebruikt bracket-directives voor hoogte-markeringen.
- `src/vsa/bracket_directive.py` en `src/vsa/bracket_token_stream.py` zijn geïmplementeerd.
- Voor meerdere hoogte-markeringen binnen één blok is parseracceptatie geregeld.
- AST-representatie voor meerdere hoogte-markeringen moet stabiel en expliciet gedocumenteerd blijven.
- validatorregels voor meerdere hoogte-markeringen zijn vastgelegd en moeten compatibel blijven met bestaande validatie.
- SVG-rendering van meerdere hoogte-markeringen moet stabiel blijven en regressies voorkomen.
Voorbeeld:

```text
voortekst [:] tekst {/zin_} [/:] meer {/tekst_} [//:] natekst.
```

### 1.2 Eindtoon en pitchmarker-validatie

Status: `Open`

- Eindtoon bij laatste hoogte-marker detecteren.
- Begin- en eind-pitchmarkers strenger controleren.
- Foutmelding moet bestand, regel, kolom en concrete herstelactie noemen.

### 1.3 Halve-stap modifiers en commentaar

Status: `Open`

- Onderzoeken of `+`, `-`, `/+`, `+\` syntactisch/semantisch nodig zijn.
- Commentaarvormen specificeren; validator moet commentaar overslaan.

### 1.4 AST-formalisering

Status: `Later`

- Expliciete node-typen, spans/ranges, source maps, roundtrip parsing en betere foutposities.

### 1.5 Bracket-token dispatch

Status: `Later`

Bracket-token dispatch is nodig voordat andere bracket-tokens ondersteund kunnen worden, zoals:

- `[/]`
- `[*]`
- `[/?]`
- `[*?]`

Voorbeelden:

```text
Tekst [/] volgende frase
Tekst [*] adempauze
Tekst [/?] optionele frasegrens
Tekst [*?] optionele adempauze
```

Deze tokens zijn momenteel nog niet ondersteund.

Hun exacte semantiek wordt later vastgesteld per renderer (SVG, MusicXML en eventuele toekomstige renderers). Voorlopig worden zij uitsluitend als gereserveerde toekomstige syntax beschouwd.

### 1.6 Newline-policy

Status: `Open`

- CR, LF en CRLF moeten consistent worden behandeld in parsing, validatie en rendering.
- Bronregelgrenzen moeten behouden blijven zodat bronregelgrenzen correct kunnen worden gerapporteerd in diagnostiek.