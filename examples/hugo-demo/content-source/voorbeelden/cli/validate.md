---
title: "CLI: vsa validate"
---

# CLI: `vsa validate`

- [Home](/)
- [CLI overzicht](/voorbeelden/cli/)
- [Volgende: vsa svg](/voorbeelden/cli/svg/)

## Waarvoor gebruik je dit?

Gebruik `vsa validate` om te controleren of VSA-invoer klopt voordat je SVG of Hugo-output maakt.

## Goed voorbeeld

### Input

```text
[:] {/Hei_}{/lig_} is de Heer. [\\:]
```

### Commando

```cmd
vsa validate examples\minimal\valid-demo.vsa
```

### Verwachte output

```text
OK
```

### Betekenis

De notatie is syntactisch en semantisch geldig.

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

### Wat doe je daarna?

Controleer of hoogte- en lengteposities hetzelfde aantal muzikale posities bevatten.
