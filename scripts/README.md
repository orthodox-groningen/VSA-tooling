# Scripts voor VSA Tooling

Deze map bevat de actieve scripts voor lokaal ontwikkelen en CI.

Belangrijk: scripts mogen `examples\hugo-demo\content-source` niet redactioneel herschrijven.
Generated navigatie en spacing-metadata worden alleen bijgewerkt in `generated\...\content`.

## Actieve scripts

| Script                                   | Doel                                                              |
| ---------------------------------------- | ----------------------------------------------------------------- |
| `bootstrap.cmd`                          | virtuele omgeving maken en dependencies installeren               |
| `docs-serve.cmd`                         | MkDocs docs-site lokaal serveren (`requirements-docs.txt`)        |
| `test.cmd`                               | alle tests uitvoeren                                              |
| `test-verbose.cmd`                       | tests uitvoeren met extra uitvoer                                 |
| `clean.cmd`                              | tijdelijke build- en testbestanden verwijderen                    |
| `build-hugo.cmd`                         | Hugo-demo schoon bouwen                                           |
| `serve-hugo.cmd`                         | lokale Hugo-preview starten                                       |
| `build-preview.cmd`                      | preview-output bouwen                                             |
| `build-production.cmd`                   | productie-kandidaat bouwen                                        |
| `check-hugo-links-and-assets.py`         | gegenereerde Hugo-output op dode links/assets controleren         |
| `debug-font-metrics.py`                  | fontmetrics inspecteren                                           |
| `assert-real-font-metrics.py`            | build laten falen als Pillow/DejaVu real metrics niet actief zijn |
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
