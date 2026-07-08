# Stap 41 - process/build-markdown gebruiken validation config

Stap 40 sloot severity-config aan op:

```cmd
vsa validate
```

Stap 41 trekt dit door naar:

```cmd
vsa process
vsa build-markdown
```

## Voorbeeld

```toml
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
```

```cmd
vsa process input.md generated\vsa --config vsa.toml
vsa build-markdown content generated\content static\vsa --config vsa.toml
```

## Gedrag

Zonder config blijven semantische diagnostics hard.

Met config kunnen specifieke semantische diagnostics warning worden, waardoor generatie mag doorgaan.
