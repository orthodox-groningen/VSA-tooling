---
title: "CLI: vsa parse"
---

# CLI: `vsa parse`

- [Home](/)
- [CLI overzicht](/voorbeelden/cli/)
- [Vorige: vsa blocks](/voorbeelden/cli/blocks/)
- [Volgende: vsa process](/voorbeelden/cli/process/)

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

## Zonder `--ast`

```cmd
vsa parse examples\minimal\scope-demo.vsa
```

Verwachte output:

```text
OK
```

## Wanneer nuttig?

Voor normale gebruikers is `vsa validate` meestal genoeg.

Gebruik `parse --ast` vooral bij debugging of regressietests.
