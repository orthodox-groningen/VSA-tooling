# Stap 37 - severity regressiefix

Deze patch herstelt regressies na introductie van severity-levels.

## Belangrijk onderscheid

`has_errors()` blijft backward-compatible:

```text
zijn er diagnostics?
```

Nieuwe methode:

```text
has_fatal_errors()
```

betekent:

```text
zijn er diagnostics met severity error?
```

## Validation runner

`ValidationResult.ok` wordt alleen `False` bij echte errors.

Warnings worden verzameld maar laten validatie slagen.

## Documentatie

De volledige `docs/user-guide.md` is hersteld en uitgebreid met een sectie over warnings/errors.
