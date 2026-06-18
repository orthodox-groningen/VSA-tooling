---
title: "Foutvoorbeelden"
---

# Foutvoorbeelden

- [Home](../../)
- [Vorige: Multiline](../multiline/)
- [Volgende: Markdown](../markdown/)

## Ongeldige invoer

```text
{/&\tekst_}
```

## Commando

```cmd
vsa validate examples\expected-fail\semantic-mismatch.vsa
```

## Voorbeeldfout

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

## Wat betekent dat?

Er zijn meer hoogteposities dan lengteposities.

## Hoe los je dat op?

Zorg dat beide modifiergroepen hetzelfde aantal muzikale posities bevatten.
