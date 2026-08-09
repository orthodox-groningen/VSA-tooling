# `vsa process` — SVG's genereren uit Markdown

Genereer SVG-bestanden uit [VSA-blokken](@) in één of meer Markdownbestanden,
zonder de Markdown zelf te herschrijven.

## Synopsis

```text
vsa process [-h] [--config CONFIG] [--no-validate] [--max-line-width MAX_LINE_WIDTH] input output_dir
```

## Beschrijving

`vsa process` zoekt [VSA-blokken](@) in `input` — één Markdownbestand of,
recursief, een map met Markdownbestanden — en rendert elk blok naar een los
SVG-bestand in `output_dir`. Er wordt **geen** Markdown gegenereerd of
aangepast; gebruik daarvoor [`vsa build-markdown`](build-markdown.md).

Standaard controleert `vsa process` eerst op [geldige VSA-notatie](@) in alle
gevonden blokken (dezelfde controles als [`vsa validate`](validate.md)) voordat
het rendert. Bij een validatiefout stopt het commando en worden er geen SVG's
geschreven. Gebruik `--no-validate` om die stap tijdelijk over te slaan tijdens
debuggen — voor normaal gebruik laat je validatie aan staan.

## Argumenten en opties

| Naam                                | Verplicht | Betekenis                                              | Default                                       | Beperkingen                                            |
| ----------------------------------- | --------- | ------------------------------------------------------ | --------------------------------------------- | ------------------------------------------------------ |
| `input`                             | Ja        | Markdownbestand of map met Markdownbestanden.          | —                                             | Moet bestaan.                                          |
| `output_dir`                        | Ja        | Map waarin SVG-bestanden worden geschreven.            | —                                             | Wordt automatisch aangemaakt als hij nog niet bestaat. |
| `--config CONFIG`                   | Nee       | Pad naar een alternatief `vsa.toml`.                   | Auto-detectie van `vsa.toml`                  | —                                                      |
| `--no-validate`                     | Nee       | Sla de validatiestap over.                             | Uit (validatie staat aan)                     | —                                                      |
| `--max-line-width MAX_LINE_WIDTH`   | Nee       | Maximale SVG-regelbreedte.                             | `max-line-width` uit `vsa.toml`, anders `800` | Getal (float)                                          |
| `-h`, `--help`                      | Nee       | Toon hulp voor dit subcommando.                        | —                                             | —                                                      |

## Output

- **stdout**: `<n> SVG-bestand(en) gegenereerd`, gevolgd door één regel per
  geschreven bestand (`- <pad>`).
- **Bestanden**: alléén SVG-bestanden in `output_dir`, benoemd als
  `<bestandsnaam-zonder-extensie>-block-<n>.svg`.
- Er wordt geen Markdown herschreven of aangemaakt.

## Exit status

| Exitcode | Betekenis                                                   |
| -------- | ----------------------------------------------------------- |
| `0`      | Alle gevonden [VSA-blokken](@) succesvol gerenderd.         |
| `1`      | Validatiefout (zonder `--no-validate`), of een andere fout. |

## Voorbeelden — succes

```cmd
vsa process examples\minimal\030_markdown_block_minimal.md tmp\process-out
```

Voorbeeldinvoer (`examples\minimal\030_markdown_block_minimal.md`):

```markdown
# Voorbeeld

::: vsa-notatie
[:] {tekst} [:]
:::
```

Verwachte output:

```text
1 SVG-bestand(en) gegenereerd
- tmp\process-out\030_markdown_block_minimal-block-1.svg
```

Het bestand `tmp\process-out\030_markdown_block_minimal-block-1.svg` wordt
aangemaakt; `tmp\process-out` wordt automatisch aangemaakt als het nog niet
bestaat.

## Voorbeelden — falen

Sommige bestanden in `examples\minimal\` zijn bewust SVG-renderdemo's met een
semantische hoogte-mismatch (zie de notitie bij [`vsa svg`](svg.md)). Draai je
`vsa process` op de hele map, dan stopt de validatiestap het commando:

```cmd
vsa process examples\minimal tmp\process-out
```

Verwachte output (verkort):

```text
021_hugo_block_with_metadata.md:2:32
ERROR: VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH: computed = marker + 2
do="F4"
                               ^
031_markdown_block_metadata.md:4:32
ERROR: VSA-SEMANTIC-HEIGHT-MARKER-MISMATCH: computed = marker + 2
do="C4"
                               ^
```

Exitcode: `1`. Er worden geen SVG's geschreven.

Fix: corrigeer de gemelde [VSA-blokken](@) (zie [`vsa validate`](validate.md) voor
de foutcodes), of beperk `input` tot bestanden die al geldig zijn. Gebruik
`--no-validate` alleen tijdelijk om te zien hoe de SVG's er ondanks de fout
uit zouden zien.

## Wanneer gebruiken?

Gebruik `vsa process` als je:

- alleen SVG's wilt, zonder Hugo-Markdown te genereren;
- wilt controleren hoe de SVG's van een reeks Markdownbestanden eruitzien;
- nog geen `output-dir`/`assets-dir`-structuur voor Hugo wilt opzetten.

## Zie ook

- [`vsa validate`](validate.md) — dezelfde controles die `process` standaard uitvoert.
- [`vsa build-markdown`](build-markdown.md) — SVG's + Hugo-Markdown in één stap.
- [`vsa blocks`](blocks.md) — [VSA-blokken](@) inspecteren vóór het genereren.
- Workflow-uitleg: [svg-export.md](../../guides/svg-export.md)
