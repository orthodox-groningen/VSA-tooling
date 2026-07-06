# Stap 45 - diagnostic location and scope errors

Deze stap verbetert foutmeldingen voor zangelementen.

## Nieuwe specifieke syntaxmeldingen

```text
VSA-SYNTAX-EMPTY-SUNG-TEXT
VSA-SYNTAX-INVALID-ALIGNMENT-MARKER
VSA-SYNTAX-MODIFIER-IN-SUNG-TEXT
```

## Voorbeelden

```text
{\\}
```

geeft:

```text
VSA-SYNTAX-EMPTY-SUNG-TEXT
```

```text
{&\ken__}
```

geeft:

```text
VSA-SYNTAX-INVALID-ALIGNMENT-MARKER
```

```text
{fout/}
```

geeft:

```text
VSA-SYNTAX-MODIFIER-IN-SUNG-TEXT
```

`VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH` probeert nu het concrete zangelement te lokaliseren.
