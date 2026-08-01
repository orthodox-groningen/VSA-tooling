# Fouten

Ongeldige VSA-invoer en de foutcode die de validator teruggeeft.

## Invoer

```text
{/&\tekst_}
```

## Commando

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa validate examples\expected-fail\semantic-mismatch.vsa
```

## Voorbeeldfout

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

## Uitleg

Er zijn meer hoogteposities dan lengteposities. Beide modifiergroepen moeten
hetzelfde aantal muzikale posities bevatten.

Canonieke fixtures: `examples/expected-fail/semantic-mismatch.vsa` en
`examples/regression/semantic-mismatch/` (met `expected-validation.json`).
