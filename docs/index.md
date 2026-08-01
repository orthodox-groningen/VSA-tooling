# VSA-tooling — documentatie

Welkom bij de documentatie van de **VSA-toolchain**: parser, validatie, SVG- en
MusicXML-export, Markdown-build en hergebruik in andere repositories.

## Wat vind je hier

| Sectie            | Inhoud                                                                      |
| ----------------- | --------------------------------------------------------------------------- |
| **Starten**       | Eerste stappen met de CLI                                                   |
| **Handleidingen** | Taakgerichte uitleg — begin bij [Handleidingen](manuals/index.md)           |
| **Specificatie**  | Normatieve VSA-taal- en toolcontracts                                       |
| **Referentie**    | Naslag + [voorbeelden](reference/voorbeelden/index.md) en fixtures          |
| **Integratie**    | `vsa-tool` importeren in andere repo's en CI                                |
| **Plannen**       | Ontwikkelplannen — *niet normatief*                                         |

## Wat is dit *niet*

| Repo / site                                                | Rol                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------ |
| [bron](https://github.com/orthodox-groningen/bron)         | Org-specs en zangstukken (single source of truth)                  |
| [VSA-demo](https://github.com/orthodox-groningen/VSA-demo) | Hugo-presentatiesite / voorbeeldconsumer                           |
| **Deze site**                                              | Documentatie van de **tool**, geen liturgische browsable catalogus |

Org-terminologie en zangstuk-formaat staan in
[bron — specificaties](https://orthodox-groningen.github.io/bron/specs/); hier
alleen toolgedrag en hoe je de CLI gebruikt.

> **URL-cutover:** docs staan op `/` (`main`) en `/preview/` (andere branches).
> Oude paden `/docs/` en `/docs-preview/` zijn vervangen. Presentatie:
> [VSA-demo](https://orthodox-groningen.github.io/VSA-demo/).

## Lokaal bekijken

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
python -m pip install -r requirements-docs.txt
scripts\docs-serve.cmd
```

Of: `python -m mkdocs serve` na installatie van de docs-dependencies.

## Snel naar de tool

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\bootstrap.cmd
vsa --version
vsa validate examples\minimal\050_svg_demo.vsa
```
