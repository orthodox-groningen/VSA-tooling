# Stap 34 - regressiefix

Deze patch herstelt regressies uit stap 34.

## Block parser

De parser negeert nog steeds VSA-markers in code fences, maar ondersteunt opnieuw:

```text
do="C4"
mode="minor"
```

en defaults zoals:

```text
do = F4
```

## Linktests

Oude tests verwachtten root-absolute links zoals:

```text
/voorbeelden/basis/
```

maar de demo gebruikt nu bewust relatieve links en Hugo `relURL`.

De tests zijn daarop aangepast.
