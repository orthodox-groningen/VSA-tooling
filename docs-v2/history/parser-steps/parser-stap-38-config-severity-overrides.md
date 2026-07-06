# Stap 38 - severity-overrides in config

Deze stap leest severity-overrides uit config.

## Configvorm

```toml
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER = "warning"
```

## Standaardgedrag

Zonder config blijft semantiek:

```text
error
```

## Status

Deze stap sluit de config nog niet aan op alle CLI-commando's.

Dat is bewust.

Eerst bewijzen we:

- config lezen werkt;
- validator overrides accepteert;
- defaultgedrag stabiel blijft.
