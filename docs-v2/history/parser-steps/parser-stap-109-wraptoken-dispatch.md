# Stap 109 - voorbereiding wraptoken dispatch

## Doel

De parser gebruikt nu bracket-directives met het expliciete eindtoken `:]`.

Voordat wraptokens zoals:

- `[/]`
- `[*]`
- `[/?]`
- `[*?]`

worden toegevoegd, moet bracket-token dispatch centraal plaatsvinden.

## Resultaat van stap 109

- architectuur vastgelegd;
- regressietest toegevoegd;
- nog geen functionele wijziging.

## Volgende stap

Stap 110 implementeert daadwerkelijke dispatch van bracket-tokens.
