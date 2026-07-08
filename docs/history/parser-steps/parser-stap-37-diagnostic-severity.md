# Stap 37 - diagnostic severity

Deze stap introduceert severity-levels.

## Nieuwe severity's

```text
error
warning
```

## Gedrag

| Severity | Exitcode beïnvloedt? |
|---|---|
| error | ja |
| warning | nee |

## Huidige mapping

### Syntax

```text
error
```

### Semantiek

Voorlopig:

```text
warning
```

## Voorbereiding op configuratie

Later kan bijvoorbeeld:

```toml
[vsa.validation]
empty-final-pitch-marker = "warning"
```

worden ondersteund.
