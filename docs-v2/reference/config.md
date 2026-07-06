# Configuratiereferentie

## `vsa.toml`

Projectdefaults worden vastgelegd in `vsa.toml`.

```toml
[rendering]
max-line-width = 800

[hugo]
assets-url-prefix = "/vsa"
output-mode = "img"

[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
```

## Defaults

| Instelling           | Default | Betekenis                    |
| -------------------- | ------- | ---------------------------- |
| `max-line-width`     | `800`   | Maximale SVG-regelbreedte    |
| `assets-url-prefix`  | `/vsa`  | URL-prefix voor SVG-assets   |
| `output-mode`        | `img`   | Markdown-uitvoer als `<img>` |

## Voorrang

```text
CLI-optie
  ↓
vsa.toml
  ↓
default
```

## Severity-overrides

Gebruik severity-overrides om specifieke semantische meldingen tijdelijk als waarschuwing te behandelen.

```toml
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
```

| Waarde    | Betekenis                              |
| --------- | -------------------------------------- |
| `error`   | Validatie faalt                        |
| `warning` | Melding tonen, verwerking mag doorgaan |

## Commando-ondersteuning

| Commando             | Gebruikt severity-config? |
| -------------------- | ------------------------- |
| `vsa validate`       | Ja                        |
| `vsa process`        | Ja                        |
| `vsa build-markdown` | Ja                        |
| `vsa svg`            | Nee                       |
| `vsa blocks`         | Nee                       |
| `vsa parse`          | Nee                       |

## Hard blijvende fouten

Syntax-errors blijven altijd `error`.

Voorbeeld:

```text
{onafgesloten
```
