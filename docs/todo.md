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

### 1.2 Hoogtemarkeringen validatie

Status: `Geïmplementeerd`

- Elke lokale hoogte-markering (`[X:]` na de eerste) wordt vergeleken met de
  cumulatieve hoogte op basis van alle tussenliggende EHMs van zangelementen.
- Halftoon-prefixen (`+`, `#`, `♯` = +0.5; `b`, `♭` = −0.5) tellen mee.
- Foutcode: `VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH`.
- Foutmelding bevat berekende hoogte, gedeclareerde hoogte, regelnummer, kolom
  en de canonieke correcte markering als directe herstelactie.
- Alle fouten in één blok worden verzameld; validatie stopt niet bij de eerste.
- Ernstigheid is configureerbaar via `severity_overrides`.
- Valse positieven voor ontbrekende of lege eindmarkering worden niet gegeven:
  een afwezige eindmarkering is gewoon geldig.

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

## 2. Document authoring en bron-repo

### 2.1 `:::coria` build-time directive

Status: `Geïmplementeerd`

- `:::coria "melodie.vsa" [label="…"] [mode="auto|html|mxl"]:::` in content-source.
- Pad relatief aan includerende `.md`, zoals `:::include`.
- Resolver: `src/vsa/content_assets.py`; directive: `src/vsa/markdown_coria.py`.
- `.coria.html` siblings worden gekopieerd naar `static/coria/` bij build-markdown.

### 2.2 Veralgemeniseerde `:::include` met exportkanalen

Status: `Open`

Vervolg op `:::coria`: één transclusion-mechanisme met expliciete kanalen, bijv.:

```markdown
:::include svg "melodie.vsa" scale="85%" alt="…":::
:::include coria "melodie.vsa" label="Oefenen in Coria":::
:::include mxl "melodie.vsa":::
```

Doel: minder directive-soorten in bronbestanden; aansluiting op toekomstige
**bron-repo per zangstuk** (één map met `.vsa`, `.coria.html`, `page.md`).
Default sibling-conventie (`bron.vsa` in dezelfde map) kan dan later worden
toegevoegd.

`:::coria` blijft ondersteund als alias of wordt gemigreerd naar `include coria`.

### 2.3 Geneste blok-directives (web-only / keep-together)

Status: `Open` — **bespreek bij volgende ronde output-samenstelling**

Bij Hugo-build (`vsa build-markdown`) faalt content met geneste directives, bijv.:

```text
Geneste directives zijn niet toegestaan: ':::web-only:::' binnen open ':::keep-together:::'
```

Implementatie: `src/vsa/markdown_directives.py` verbiedt nesting expliciet.
In de praktijk komt dit voor wanneer `:::web-only:::` (bijv. Coria-link) binnen
`:::keep-together:::` staat — zie `examples/hugo-demo/content-source/praktijk/zondagen/zondag-toon-1.md`.

Te onderzoeken bij herziening van [spec-vsa-document-samenstellen.md](spec-vsa-document-samenstellen.md):

- Moet nesting toegestaan worden (en zo ja, welke combinaties)?
- Of moet de authoring-conventie worden aangepast (sibling i.p.v. genest)?
- Hoe gedraagt geneste content zich bij `@media print` vs. browser?
