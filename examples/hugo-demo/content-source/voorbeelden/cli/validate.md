---
title: "CLI: vsa validate"
---

# CLI: `vsa validate`

- [Home]({{< navbuttons 
    "Weekdagen  | ../weekdagen/"
    "Zondagen   | ../zondagen/"
    "Feesteigen | ../feesteigen/"
>}}../)
- [CLI overzicht](../)
- [Volgende: vsa svg](../svg/)

## Waarvoor gebruik je dit?

Gebruik `vsa validate` om te controleren of VSA-invoer klopt voordat je SVG of Hugo-output maakt.

## Goed voorbeeld

### Input

```text
[:] {/Hei_}{/lig_} is de Heer. [//:]
```

### Commando

```cmd
vsa validate examples\minimal\valid-demo.vsa
```

### Verwachte output

```text
OK
```

## Fout voorbeeld

### Input

```text
{/&\tekst_}
```

### Commando

```cmd
vsa validate examples\expected-fail\semantic-mismatch.vsa
```

### Verwachte output

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```
