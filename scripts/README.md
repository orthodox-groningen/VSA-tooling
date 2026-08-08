# Scripts voor VSA Tooling

Deze map bevat de actieve scripts voor lokaal ontwikkelen en CI.

Belangrijk: scripts mogen redactionele `content-source` niet herschrijven.
CI gebruikt `examples\consumer-minimal\content-source`. Generated navigatie alleen in
`generated\...\content`.

## Actieve scripts

| Script                                   | Doel                                                              |
| ---------------------------------------- | ----------------------------------------------------------------- |
| `bootstrap.cmd`                          | virtuele omgeving maken en dependencies installeren               |
| `docs-serve.cmd`                         | MkDocs docs-site lokaal serveren (zonder TEv2)                    |
| `docs-serve-tev2.cmd`                    | TEv2-preprocess + MkDocs serve op `generated/`                    |
| `docs-build.cmd`                         | `mkdocs build --strict` zonder TEv2                               |
| `docs-build-tev2.cmd`                    | TEv2-pipeline + TermRef-check + `mkdocs build --strict`           |
| `docs-tev2-run.cmd`                      | Alleen TEv2-preprocess (aanroep door build/serve-tev2)            |
| `prepare-tev2-docs.py`                   | Staging-tree `generated/docs` voor TEv2                           |
| `check-tev2-termrefs.py`                 | Faalt bij onopgeloste TermRefs in generated Markdown              |
| `test.cmd`                               | alle tests uitvoeren                                              |
| `test-verbose.cmd`                       | tests uitvoeren met extra uitvoer                                 |
| `ci.cmd`                                 | lokale CI: pytest + consumer-minimal validate/build-markdown      |
| `clean.cmd`                              | tijdelijke build- en testbestanden verwijderen                    |
| `debug-font-metrics.py`                  | fontmetrics inspecteren                                           |
| `assert-real-font-metrics.py`            | build laten falen als Pillow/DejaVu real metrics niet actief zijn |
| `check-publication-output.py`            | publicatie-output controleren (Pages deploy)                      |
| `update-nav-placeholders.py`             | gegenereerde navigatie bijwerken in generated content             |
| `update-spacing-diagnostics-metadata.py` | spacingdiagnostiek bijwerken in generated content                 |

## Verouderde scripts

Zie:

```cmd
type scripts\OBSOLETE_SCRIPTS.md
```

`retry.cmd` is verouderd. Gebruik:

```cmd
scripts\test.cmd
```
