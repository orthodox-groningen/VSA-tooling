# CLI-referentie

## Algemene uitgangspunten

De voorbeelden gaan uit van de repository-root.

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
```

## Exitcodes

| Exitcode | Betekenis                              |
| -------: | -------------------------------------- |
|      `0` | Commando succesvol                     |
|      `1` | Fout gevonden of commando mislukt      |

Controleer in CMD de laatste exitcode met:

```cmd
echo %ERRORLEVEL%
```

## Commando-overzicht

| Commando                                      | Doel                                             |
| --------------------------------------------- | ------------------------------------------------ |
| `vsa --version`                               | Toon de geïnstalleerde versie                    |
| `vsa validate <bestand-of-map>`               | Valideer `.vsa`- en Markdown-invoer             |
| `vsa parse <bestand.vsa> --ast`               | Toon parseroutput / AST                          |
| `vsa blocks <bestand.md> [--json]`            | Vind VSA-blokken in Markdown                     |
| `vsa svg <input.vsa> <output.svg>`            | Render één VSA-bestand naar SVG                  |
| `vsa process <bestand-of-map> <output-dir>`   | Genereer SVG's uit Markdownblokken              |
| `vsa build-markdown <input> <output> <assets>`| Genereer Hugo-Markdown en SVG-assets             |

## `vsa --version`

```cmd
vsa --version
```

Voorbeeldoutput:

```text
vsa 0.1.0
```

## `vsa validate <bestand-of-map>`

```cmd
vsa validate <bestand-of-map>
```

| Input          | Voorbeeld                           | Gedrag                                      |
| -------------- | ----------------------------------- | ------------------------------------------- |
| `.vsa` bestand | `examples\minimal\050_svg_demo.vsa` | Controleert één VSA-bestand                 |
| `.md` bestand  | `pagina.md`                         | Controleert VSA-blokken in Markdown         |
| Map            | `examples\consumer-minimal\content-source` | Zoekt recursief naar `.vsa`, `.md`, `.markdown` |

Succesoutput:

```text
OK
```

Foutoutput:

```text
bron:regel:kolom: FOUTCODE: uitleg
```

## `vsa parse <bestand.vsa> --ast`

```cmd
vsa parse <bestand.vsa> --ast
```

| Parameter        | Verplicht | Betekenis                         |
| ---------------- | --------- | --------------------------------- |
| `<bestand.vsa>`  | Ja        | VSA-bronbestand                   |
| `--ast`          | Nee       | Toon interne structuur als JSON   |

Gebruik dit vooral voor parserdebugging en regressietests.

## `vsa blocks <bestand.md> [--json]`

```cmd
vsa blocks <bestand.md>
vsa blocks <bestand.md> --json
```

| Parameter       | Verplicht | Betekenis                              |
| --------------- | --------- | -------------------------------------- |
| `<bestand.md>`  | Ja        | Markdownbestand                        |
| `--json`        | Nee       | Toon metadata, body en AST per blok    |

## `vsa svg <input.vsa> <output.svg>`

```cmd
vsa svg <input.vsa> <output.svg>
```

| Optie                      | Default             | Betekenis                  |
| -------------------------- | ------------------- | -------------------------- |
| `--max-line-width <getal>` | `vsa.toml` of `800` | Maximale SVG-regelbreedte  |

Dit commando verwerkt geen Markdownblokken.

## `vsa process <bestand-of-map> <output-dir>`

```cmd
vsa process <bestand-of-map> <output-dir>
```

| Optie                      | Default             | Betekenis                  |
| -------------------------- | ------------------- | -------------------------- |
| `--no-validate`            | Niet actief         | Validatie overslaan        |
| `--max-line-width <getal>` | `vsa.toml` of `800` | Maximale SVG-regelbreedte  |

De output bestaat alleen uit SVG-bestanden.

## `vsa build-markdown <input-dir> <output-dir> <assets-dir>`

```cmd
vsa build-markdown <input-dir> <output-dir> <assets-dir>
```

| Parameter      | Verplicht | Betekenis                              |
| -------------- | --------- | -------------------------------------- |
| `<input-dir>`  | Ja        | Bronmap met handgeschreven Markdown    |
| `<output-dir>` | Ja        | Doelmap voor gegenereerde Markdown     |
| `<assets-dir>` | Ja        | Doelmap voor gegenereerde SVG's        |

| Optie                         | Default             | Betekenis                  |
| ----------------------------- | ------------------- | -------------------------- |
| `--assets-url-prefix <prefix>`| `vsa.toml` of `/vsa`| URL-prefix in Markdown     |
| `--max-line-width <getal>`    | `vsa.toml` of `800` | Maximale SVG-regelbreedte  |
| `--output-mode img`           | `vsa.toml` of `img` | Gebruik `<img>`            |
| `--output-mode shortcode`     | `vsa.toml` of `img` | Gebruik Hugo-shortcode     |

## Scripts

| Script                         | Doel                                  |
| ------------------------------ | ------------------------------------- |
| `scripts\bootstrap.cmd`        | Installeert lokale omgeving           |
| `scripts\test.cmd`             | Draait tests                          |
| `scripts\ci.cmd`               | Draait lokale CI                      |
| `scripts\ci.cmd`               | Lokale CI (pytest + consumer-minimal) |
| `scripts\docs-serve.cmd`       | MkDocs docs lokaal serveren           |

## Diagnosevolgorde

```cmd
vsa validate <input>
scripts\test.cmd
vsa blocks <bestand.md> --json
vsa svg <bestand.vsa> output.svg
start output.svg
```
