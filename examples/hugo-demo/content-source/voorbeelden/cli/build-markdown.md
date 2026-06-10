---
title: "CLI: vsa build-markdown"
---

# CLI: `vsa build-markdown`

- [Home](/)
- [CLI overzicht](/voorbeelden/cli/)
- [Vorige: vsa process](/voorbeelden/cli/process/)
- [Volgende: vsa --version](/voorbeelden/cli/version/)

## Waarvoor gebruik je dit?

Dit is het belangrijkste commando voor Hugo.

Het maakt:

1. gegenereerde Markdown;
2. gegenereerde SVG-bestanden.

## Commando

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content examples\hugo-demo\static\vsa
```

## Verwachte output

```text
Markdownbestand(en) geschreven
SVG-bestand(en) geschreven
```

## Wat betekent elk pad?

| Parameter | Voorbeeld | Betekenis |
|-----------|-----------|-----------|
| `<input-dir>` | `examples\hugo-demo\content-source` | bron-Markdown |
| `<output-dir>` | `generated\content` | gegenereerde Markdown |
| `<assets-dir>` | `examples\hugo-demo\static\vsa` | gegenereerde SVG's voor Hugo |

## Outputvorm

Standaard:

```html
<img class="vsa-notation" src="/vsa/..." alt="VSA notatie">
```

Met shortcode:

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content examples\hugo-demo\static\vsa --output-mode shortcode
```

Geeft:

```go-html-template
{{< vsa src="/vsa/..." >}}
```
