---
title: "CLI: vsa --config"
---

# CLI: `--config`

- [Home](../../../)
- [CLI overzicht](../)
- [Vorige: vsa --version](../version/)

## Waarvoor gebruik je dit?

Gebruik `--config` om instellingen uit een `vsa.toml` bestand te gebruiken.

Dit werkt nu voor:

| Commando | Config gebruikt voor |
|----------|----------------------|
| `vsa validate` | severity-overrides |
| `vsa process` | severity-overrides en renderingconfig |
| `vsa build-markdown` | severity-overrides, renderingconfig en Hugo-output |

## Voorbeeldconfig

```toml
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER = "warning"
```

## Voorbeeld: validate

```cmd
vsa validate examples\expected-fail\empty-final-pitch-marker.vsa --config vsa.toml
```

Als de foutcode op `warning` staat:

```text
WARNING: VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
```

De exitcode is dan `0`.

## Voorbeeld: process

```cmd
vsa process input.md generated\vsa --config vsa.toml
```

Als er alleen warnings zijn, worden SVG-bestanden wel gegenereerd.

## Voorbeeld: build-markdown

```cmd
vsa build-markdown content generated\content static\vsa --config vsa.toml
```

Als er alleen warnings zijn, worden Markdown en SVG-bestanden wel gegenereerd.

## Wat blijft altijd hard?

Syntax-errors blijven altijd `error`.

Voorbeeld:

```text
{onafgesloten
```

Dit blijft de build stoppen, ook als semantische foutcodes als warning zijn geconfigureerd.
