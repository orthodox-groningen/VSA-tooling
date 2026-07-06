# Stap 45 - final regression fix

De laatste regressies waren testverwachtingen.

## Nieuwe werkelijkheid

```text
{fout/}
```

geeft niet meer:

```text
VSA-PARSE-ERROR
```

maar de specifiekere code:

```text
VSA-SYNTAX-MODIFIER-IN-SUNG-TEXT
```

## Modifier-count locatie

De testverwachting is afgestemd op het regelnummer dat de validator werkelijk
rapporteert voor het VSA-blok.
