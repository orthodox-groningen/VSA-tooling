# TODO lijst

Deze lijst is geconsolideerd uit `docs/todo.md` en alle `docs/todo-stepXX-addendum.md` bestanden.

Statuswaarden: `Open`, `In uitvoering`, `Later`, `Afgerond`, `Gespecificeerd`, `Geïmplementeerd`.

## 1. Parser, syntax en validatie

### 1.1 Meerdere hoogte-markeringen en bracket-directives

Status: `In uitvoering`

- Meerdere hoogte-markeringen per `vsa-notatie` blok zijn toegestaan.
- Hoogte-markering blijft `[<EHM>:]`; `:]` is één eindtoken van een bracket-directive.
- Niet tokenizen als losse `:` en `]`; niet overstappen op `{<EHM>:}`.
- Tekst vóór, tussen en na hoogte-markeringen is toegestaan.
- Parser moet bracket-token dispatch krijgen.
- `src/vsa/bracket_directive.py` en `src/vsa/bracket_token_stream.py` zijn geïsoleerd geïmplementeerd.
- Nog doen: EHM-set koppelen aan bestaande definitie, parseracceptatie, AST-representatie, validatorregels en SVG-rendering.

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

Status: `In uitvoering`

Bracket-token dispatch moet worden geïmplementeerd voordat andere bracket-tokens ondersteund kunnen worden zoals:

- `[/]`
- `[*]`
- `[/?]`
- `[*?]`

Deze tokens zijn nog niet ondersteund.

## 2. SVG-rendering en fontmetrics

### 2.1 Spacing, glyphs en woordclusters

Status: `In uitvoering`

- Natuurlijke spacing tussen tekst en zangelementen.
- Geen overlap; woordspaties behouden; geen `deHeerheeft`.
- EHM/ELM-posities verder finetunen.
- Woord-georiënteerde layoutfase later onderzoeken voor woorden zoals `me{\de}{/eeu_}wi{\ge}`.

### 2.2 Filler-lines en wrapping

Status: `In uitvoering`

- Filler-lines op tekst/dash-hoogte, niet op EHM-hoogte.
- Bron-newlines blijven harde bronregelgrenzen.
- Wraptokens `[/]`, `[*]`, `[/?]`, `[*?]` wachten op bracket-token dispatch.

### 2.3 Newline-beleid

Status: `In uitvoering`

Controleer consequent gedrag van:

- CR
- LF
- CRLF

in parser, validator, markdown-processor en Hugo-pipeline.

Verboden voor VSA-source:

```python
" ".join(lines)
source.replace("\n", " ")
```

Toegestaan:

```python
"\n".join(lines)
source.replace("\r\n", "\n").replace("\r", "\n")
```

### 2.4 Real font metrics

Status: `Geïmplementeerd / Open eindcontrole`

- Build gebruikt `.venv\Scripts\python.exe` indien aanwezig.
- Build faalt als real font metrics niet actief zijn.
- Later controleren: CI, README, licenties, DejaVu Sans, Pillow en fallbackbeleid.

### 2.5 Diagnostische renderingpagina's

Status: `In uitvoering`

Gerichte demo-pagina's blijven nodig voor spacing, overlap, glyph-posities, filler-lines, pitchmarkers, wrapping en Markdown-hardbreaks.

## 3. Hugo-site, navigatie en build-output

### 3.1 Content-source bevriezen

Status: `Geïmplementeerd`

- `examples/hugo-demo/content-source` is redactionele broncontent.
- Scripts mogen daar niet automatisch frontmatter, titels, headings of vrije markdown herschrijven.
- Navigatie/spacing-metadata worden alleen in `generated/hugo/content` bijgewerkt.

### 3.2 Marker-only navigatie

Status: `Geïmplementeerd`

- Gebruiker plaatst zelf `VSA-NAV:*` markers.
- Alleen het corresponderende `VSA-NAV-GENERATED:*` blok wordt vervangen.
- Vrije markdown vóór/na markers blijft ongemoeid.

### 3.3 Linkchecker en SVG-assets

Status: `In uitvoering`

- Linkchecker structureel in build/CI opnemen zodra site-inhoud stabiel is.
- SVG assetnamen en HTML refs moeten actuele relatieve paden gebruiken.
- Oude routes `/zondag/` en `/voorbeelden/praktijk/` definitief afhandelen.

### 3.4 Demo-site afronden

Status: `Open`

- Alle pagina’s nalopen op tekst, links, voorbeelden en responsive gedrag.
- CLI-demo’s en handleiding actualiseren.
- `examples/hugo-demo/content`, `examples/hugo-demo/public`, `examples/hugo-demo/static/vsa` en `generated` blijven build-output.

## 4. Tests, CI en releasehygiëne

### 4.1 Repo hygiene

Status: `In uitvoering`

- Oude `todo-stepXX-addendum.md` bestanden zijn in deze lijst verwerkt en kunnen weg.
- Oude migratie-/apply-tests samenvoegen in `test_repo_hygiene.py`.
- `retry.cmd` is verouderd; gebruik `scripts/test.cmd`.
- Tests mogen working tree niet muteren.

### 4.2 CI en workflows

Status: `Open`

- Linux-commando’s alleen op Linux runners.
- Rendering dependencies platformonafhankelijk houden.
- CI font-metrics eindcontrole met Pillow/DejaVu.

## 5. Later

### 5.1 MusicXML-export

Status: `Later`

AST → MusicXML, inclusief begin-pitchmarkers, regeleindes, control tokens, alignment en validatie.

### 5.2 Multi-voice en sync placeholders

Status: `Later`

SATB, placeholders, gedeelde ritmische structuur en tekstueel sync houden van stemmen.

### 5.3 Editor tooling

Status: `Later`

VS Code extension, syntax highlighting, live validation, hover diagnostics en quick fixes.
