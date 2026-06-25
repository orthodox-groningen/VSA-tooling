---
title: "CLI: vsa build-markdown"
---

# CLI: `vsa build-markdown`

- [Home]({{< navbuttons 
    "Weekdagen  | ../weekdagen/"
    "Zondagen   | ../zondagen/"
    "Feesteigen | ../feesteigen/"
>}}../)
- [CLI overzicht](../)
- [Vorige: vsa process](../process/)
- [Volgende: vsa --version](../version/)

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
