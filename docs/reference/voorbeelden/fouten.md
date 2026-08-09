# Fouten

Ongeldige VSA-invoer en de foutcode die de validator teruggeeft.

## Invoer

Fixture: `examples/docs-walkthroughs/validate-unclosed-scope.vsa`

```text
{tekst
```

## Commando

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa validate examples\docs-walkthroughs\validate-unclosed-scope.vsa
```

## Voorbeeldfout

```text
validate-unclosed-scope.vsa:1:1
ERROR: VSA-SYNTAX-UNCLOSED-SCOPE: Scope zonder afsluitende accolade.
{tekst
^
```

## Uitleg

De scope is niet afgesloten. Sluit af met `}`, bijvoorbeeld `{tekst}`.

Voor een semantische mismatch (hoogte- vs. lengteposities) zie
`examples/expected-fail/semantic-mismatch.vsa` en
`examples/regression/semantic-mismatch/` (met `expected-validation.json`).
