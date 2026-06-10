---
title: "Foutvoorbeelden"
---

# Foutvoorbeelden

- [Home](/)
- [Vorige: Multiline](/voorbeelden/multiline/)
- [Volgende: Markdown](/voorbeelden/markdown/)

## Ongeldige invoer

```text
{/&\tekst_}
```

## Commando

```cmd
vsa validate examples\site-demo-invalid
```

## Voorbeeldfout

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

## Wat betekent dat?

Er zijn meer hoogteposities dan lengteposities.

### Hoogte

```text
/ en \
```

### Lengte

```text
_
```

## Hoe los je dat op?

Zorg dat beide modifiergroepen hetzelfde aantal muzikale posities bevatten.
