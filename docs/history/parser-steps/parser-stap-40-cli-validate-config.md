# Stap 40 - CLI validate gebruikt severity-config

Deze stap sluit de validatieconfig aan op de CLI.

## Gebruik

```cmd
vsa validate bestand.vsa --config vsa.toml
```

## Config

```toml
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
```

## Gedrag

Zonder config:

```text
semantische diagnostic = error
exitcode = 1
```

Met config:

```text
specifieke semantische diagnostic = warning
exitcode = 0
```

Syntax-errors blijven altijd fatal.

## Let op

Deze stap sluit config nog niet aan op `process` en `build-markdown`.
Die gebruiken nog hun bestaande validatiepad.
