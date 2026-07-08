# VSA-tooling

VSA-tooling is de gereedschapskist voor het schrijven, controleren, renderen en publiceren van VSA-notatie.

De repository bevat een Python CLI (`vsa`) en een Hugo-demo/publicatieketen. Samen maken die het mogelijk om VSA-bronmateriaal te gebruiken in Markdown, SVG-notatiebeelden te genereren, MusicXML/MXL te exporteren, zangdocumenten samen te stellen en praktijkmateriaal te publiceren.

## Waarvoor is deze repo?

De repo ondersteunt drie samenhangende workflows.

| Workflow | Doel |
| --- | --- |
| VSA-notatie | VSA-bronnen valideren, parsen en renderen naar SVG of MusicXML/MXL. |
| Markdown en Hugo | Markdown met `::: vsa-notatie`, `:::include`, `:::coria` en print/web-directives omzetten naar publiceerbare Hugo-content. |
| Parochie- en bronmateriaal | Lokale en bron-zangstukken via logische verwijzingen opnemen in samenstellingen, inclusief catalogus-resolutie met `zoek=`. |

De tool is dus niet alleen een renderer. Het project groeit naar een authoring- en publicatieketen voor kerkzangmateriaal: van bronbestand naar controleerbare notatie, oefenmateriaal, website en printbare output.

## Huidige status

De kern is werkend en behoorlijk gedekt door regressietests. De belangrijkste functies zijn aanwezig:

- VSA valideren: `vsa validate`
- VSA naar SVG renderen: `vsa svg`
- VSA naar MusicXML/MXL exporteren: `vsa musicxml`
- VSA-blokken in Markdown inspecteren: `vsa blocks`
- Markdown verwerken naar SVG-assets: `vsa process`
- Hugo-content bouwen: `vsa build-markdown`
- Catalogusverwijzingen oplossen: `vsa resolve-catalogus`
- Hugo-demo lokaal bouwen en serveren met scripts in `scripts/`

De projectrichting en actuele open punten staan in [docs/status-en-roadmap.md](docs/status-en-roadmap.md).

## Snel starten

De voorbeelden hieronder gaan uit van Windows en een shell in de repository-root.

```cmd
scripts\bootstrap.cmd
vsa --version
```

Controleer een voorbeeldbestand:

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

Maak een SVG:

```cmd
vsa svg examples\minimal\050_svg_demo.vsa output.svg
```

Bouw de Hugo-demo:

```cmd
scripts\build-hugo.cmd
scripts\serve-hugo.cmd
```

## Belangrijke mappen

| Pad | Inhoud |
| --- | --- |
| `src/vsa/` | Python package met parser, validators, renderers, markdownverwerking en CLI. |
| `tests/` | Unit- en regressietests voor parser, validatie, rendering, Hugo en workflows. |
| `examples/minimal/` | Kleine VSA-voorbeelden voor testen en uitleg. |
| `examples/regression/` | Vastgelegde input/output-cases voor regressies. |
| `examples/hugo-demo/` | Demo-site, praktijkmateriaal, lokale zangstukken, layouts en publicatieconfiguratie. |
| `docs/` | Gebruikersdocs, specs, architectuurstappen en roadmap. |
| `scripts/` | Windows-scripts voor bootstrap, tests, build, preview, productie en Hugo-server. |

## Documentatie

| Document | Gebruik |
| --- | --- |
| [docs/user-guide.md](docs/user-guide.md) | Taakgerichte uitleg voor gebruikers van de tool. |
| [docs/cli-reference.md](docs/cli-reference.md) | Referentie van de `vsa` CLI-commando's. |
| [docs/status-en-roadmap.md](docs/status-en-roadmap.md) | Actuele projectstatus, beperkingen en nuttige volgende stappen. |
| [docs/spec-vsa-document-samenstellen.md](docs/spec-vsa-document-samenstellen.md) | Specificatie voor document-samenstelling met Markdown-directives. |
| [docs/parochie-lokaal-vsa.md](docs/parochie-lokaal-vsa.md) | VSA-specifieke uitleg voor parochie-lokaal materiaal en catalogus-includes. |
| [docs/spec/](docs/spec/) | VSA-specificaties voor syntax, rendering, comments en glyph-model. |
| [docs/architecture/](docs/architecture/) | Historische ontwerp- en implementatiestappen. |

## CLI-overzicht

```text
vsa validate <bestand-of-map>
vsa parse <bestand.vsa> --ast
vsa blocks <bestand.md> --json
vsa svg <input.vsa> <output.svg>
vsa musicxml <input> <output>
vsa process <bestand-of-map> <output-dir>
vsa build-markdown <input-dir> <output-dir> <assets-dir>
vsa resolve-catalogus <bestand.md> --content-root <map> --bron-root <map>
```

Zie [docs/cli-reference.md](docs/cli-reference.md) voor details.

## Ontwikkelen

Draai tijdens ontwikkeling:

```cmd
scripts\test.cmd
```

Draai voor een bredere lokale controle:

```cmd
scripts\ci.cmd
```

De repo bevat veel historische stapdocumenten. Die blijven nuttig als achtergrond, maar de actuele status hoort in [docs/status-en-roadmap.md](docs/status-en-roadmap.md).
