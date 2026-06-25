---
title: "CLI: vsa parse"
---

# CLI: `vsa parse`

- [Home]({{< navbuttons 
    "Weekdagen  | ../weekdagen/"
    "Zondagen   | ../zondagen/"
    "Feesteigen | ../feesteigen/"
>}}../)
- [CLI overzicht](../)
- [Vorige: vsa blocks](../blocks/)
- [Volgende: vsa process](../process/)

## Waarvoor gebruik je dit?

Gebruik `vsa parse --ast` om te zien hoe de parser de VSA-invoer intern begrijpt.

## Input

```text
{/Hei_}
```

## Commando

```cmd
vsa parse examples\minimal\scope-demo.vsa --ast
```

## Verwachte output

```json
{
  "type": "Document",
  "nodes": [
    {
      "type": "ScopeNode",
      "height_modifier": ["/"],
      "text": "Hei",
      "length_modifier": ["_"]
    }
  ]
}
```
