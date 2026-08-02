# `vsa parse` — parserstructuur bekijken

Toon de interne parserstructuur (AST) van één VSA-bestand, of controleer
alleen of de parser het bestand kan lezen.

## Synopsis

```text
vsa parse [-h] [--ast] path
```

## Beschrijving

`vsa parse` leest één VSA-bestand (`.vsa`), lost `@include-vsa` op indien
aanwezig, en voert het door de parser. Dit commando is bedoeld voor
parserdebugging en het maken van regressietests — niet voor dagelijkse
controle (gebruik daarvoor [`vsa validate`](validate.md)).

Zonder `--ast` toont het commando alleen `OK` als het bestand gelezen kan
worden. Met `--ast` verschijnt de volledige interne structuur (Abstract
Syntax Tree) als JSON.

`vsa parse` doet geen semantische controle (zoals de modifier-aantallen-check
van `validate`); het toont alleen of de parser het bestand structureel kan
verwerken.

## Argumenten en opties

| Naam             | Verplicht | Betekenis                                                 | Default | Beperkingen   |
| ---------------- | --------- | --------------------------------------------------------- | ------- | ------------- |
| `path`           | Ja        | VSA-bronbestand (`.vsa`).                                 | —       | Moet bestaan. |
| `--ast`          | Nee       | Toon de interne structuur als JSON in plaats van `OK`.    | Uit     | —             |
| `-h`, `--help`   | Nee       | Toon hulp voor dit subcommando.                           | —       | —             |

## Output

- **stdout**: zonder `--ast` de tekst `OK`; met `--ast` een JSON-document met
  `type: "Document"` en een lijst `nodes`.
- **stderr**: foutmelding bij een `@include-vsa`-fout (zie hieronder).
- Er worden geen bestanden geschreven.

## Exit status

| Exitcode | Betekenis                                                |
| -------- | -------------------------------------------------------- |
| `0`      | Bestand kon gelezen en geparsed worden.                  |
| `1`      | Fout bij het oplossen van een `@include-vsa`-verwijzing. |

## Voorbeelden — succes

```cmd
vsa parse examples\minimal\050_svg_demo.vsa --ast
```

Voorbeeldinvoer:

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

Verwachte output (verkort):

```json
{
  "type": "Document",
  "nodes": [
    { "type": "PitchMarkerNode", "height_modifier": [] },
    { "type": "TextNode", "text": " " },
    { "type": "ScopeNode", "height_modifier": ["/"], "text": "Hei", "length_modifier": ["_"] },
    { "type": "ScopeNode", "height_modifier": ["/"], "text": "lig", "length_modifier": ["_"] },
    { "type": "TextNode", "text": " is de Heer. " },
    { "type": "PitchMarkerNode", "height_modifier": [] },
    { "type": "TextNode", "text": "\n" }
  ]
}
```

Zonder `--ast`:

```cmd
vsa parse examples\minimal\050_svg_demo.vsa
```

```text
OK
```

Merk op dat `vsa parse` hier `OK` teruggeeft ondanks dat `vsa validate`
op dit bestand een semantische fout meldt — `parse` controleert alleen de
parserstructuur, niet de semantiek.

## Voorbeelden — falen

Als het bestand een onopgeloste `@include-vsa`-verwijzing bevat (bijvoorbeeld
naar een niet-bestaand bestand), meldt het commando dit op stderr:

```text
pad\naar\bestand.vsa: <Nederlandse foutmelding over de include>
```

Exitcode: `1`.

Fix: controleer het pad achter `@include-vsa` en of het doelbestand bestaat.

## Wanneer gebruiken?

| Situatie                                            | Gebruik `vsa parse`?         |
| --------------------------------------------------- | ---------------------------- |
| Gewone eindcontrole                                 | Nee — gebruik `vsa validate` |
| Parserdebugging                                     | Ja                           |
| Regressietest maken                                 | Ja                           |
| Controleren of tekst als `TextNode` wordt gezien    | Ja                           |

## Zie ook

- [`vsa validate`](validate.md) — volledige controle inclusief semantiek.
- [`vsa blocks`](blocks.md) — AST per VSA-blok in een Markdownbestand (`--json`).
- Handleiding: [gebruikershandleiding §8](../../guides/user-guide.md)
- Outputreferentie (AST-vorm): [outputs.md](../outputs.md)
