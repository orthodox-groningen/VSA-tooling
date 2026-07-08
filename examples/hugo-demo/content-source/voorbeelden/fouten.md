---
title: "Fouten"
---

# Fouten

Een voorbeeld van ongeldige VSA-invoer en de foutmelding die de validator teruggeeft.

{{< navbuttons
    "Vorige: Multiline | ../multiline/"
    "Voorbeelden | ../"
    "Volgende: Markdown | ../markdown/"
>}}

## Invoer

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

## Uitleg

Er zijn meer hoogteposities dan lengteposities.

## Oplossing

Zorg dat beide modifiergroepen hetzelfde aantal muzikale posities bevatten.
