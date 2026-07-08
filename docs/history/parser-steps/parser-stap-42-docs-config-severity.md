# Stap 42 - documentatie voor severity-config

Stap 42 documenteert het gedrag dat in stap 39-41 is geïmplementeerd.

## Werkend

```cmd
vsa validate bestand.vsa --config vsa.toml
vsa process input.md generated\vsa --config vsa.toml
vsa build-markdown content generated\content static\vsa --config vsa.toml
```

## Config

```toml
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
```

## Policy

Zonder config blijft semantiek `error`.

Met config kan een specifieke semantische foutcode `warning` worden.

Syntax-errors blijven altijd `error`.
