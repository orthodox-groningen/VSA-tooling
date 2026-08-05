# VSA-tooling — documentatie

Welkom bij de documentatie van de **VSA-toolchain**: parser, validatie, SVG- en
MusicXML-export, Markdown-build en hergebruik in andere repositories.

## Wat vind je hier

| Sectie                                              | Wat je er vindt                                                                                         |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [Starten](getting-started/README.md)                | Eerste stappen: omgeving, `vsa --version`, valideren en een SVG maken.                                  |
| [Handleidingen](manuals/index.md)                   | Taakgerichte uitleg (CLI-taken, validatie, export, consumer-site).                                      |
| [Specificaties](specification/README.md)            | Normatieve VSA-taal- en toolcontracts.                                                                  |
| [Referentie](reference/README.md)                   | Naslag: voorbeelden, CLI man-pagina’s, tokens, diagnostics en outputs.                                  |
| [Integratie](integratie/index.md)                   | `vsa-tool` importeren in andere repo’s en CI; TEv2 in tool-docs.                                        |
| [Terminologie](terminologie/index.md)               | Tool-lokale begrippen; org-brede glossary staat in bron.                                                |
| [Plannen](plans/README.md)                          | Ontwikkelplannen. Die zijn niet normatief; bij twijfel gelden specificatie en handleidingen.            |

## Waar hoort wat?

| Vraag                                                      | Ga naar                                                                                      |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Org-specs, zangstuk-formaat, glossary                      | [bron — documentatie](https://orthodox-groningen.github.io/bron/)                            |
| Hoe gebruik ik de VSA-CLI of bouw ik een consumer-site?    | [Handleidingen](manuals/index.md) of [Starten](getting-started/README.md)                    |
| Wat moet de taal/tool formeel doen?                        | [Specificaties](specification/README.md)                                                     |

## Wat is dit *niet*

| Repo / site                                                | Rol                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------ |
| [bron](https://orthodox-groningen.github.io/bron/)         | Org-specs en zangstukken (single source of truth)                  |
| [VSA-demo](https://orthodox-groningen.github.io/VSA-demo/) | Hugo-presentatiesite / voorbeeldconsumer                           |
| **Deze site**                                              | Documentatie van de **tool**, geen liturgische browsable catalogus |

> **URL-cutover:** docs staan op `/` (`main`) en `/preview/` (andere branches).
> Oude paden `/docs/` en `/docs-preview/` zijn vervangen.

## Lokaal bekijken

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python -m pip install -r requirements-docs.txt
scripts\docs-serve.cmd
```

## Snel naar de tool

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\bootstrap.cmd
vsa --version
vsa validate examples\minimal\050_svg_demo.vsa
```
