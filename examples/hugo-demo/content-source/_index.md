---
title: "VSA Tool Demo"
---

# VSA Tool Demo

Welkom bij de interactieve demo- en documentatiesite van de VSA Tool.

## Wat kun je hier bekijken?

| Onderdeel | Beschrijving |
|------------|--------------|
| [Basisvoorbeelden](voorbeelden/basis/) | eenvoudige VSA-notatie |
| [Multiline voorbeelden](voorbeelden/multiline/) | automatische regelafbreking |
| [Foutvoorbeelden](voorbeelden/fouten/) | validatiefouten en diagnose |
| [Markdown/Hugo](voorbeelden/markdown/) | Markdown + SVG generatie |
| [CLI demo's](voorbeelden/cli/) | voorbeelden van commando-output |
| [Rendering](voorbeelden/rendering/) | renderer- en layoutvoorbeelden |

## Belangrijkste workflow

```text
VSA
  ↓
validate
  ↓
svg/build-markdown
  ↓
Hugo/GitHub Pages
```

## Snelle voorbeelden

### Controleer VSA

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

### Maak SVG

```cmd
vsa svg examples\minimal\050_svg_demo.vsa output.svg
```

### Bouw Hugo-content

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content examples\hugo-demo\static\vsa
```
