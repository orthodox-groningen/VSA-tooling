# Fixtures-catalogus (correct / incorrect)

Canonieke bronnen staan onder `examples/`. Deze pagina **citeert** die paden;
wijzig golden files alleen via tests, niet door deze docs te “updaten” zonder
de [fixture](@).

## Correct (geldig of met verwachte SVG)

| [Fixture](@)                                  | Invoer (samenvatting)                | Verwacht                |
| --------------------------------------------- | ------------------------------------ | ----------------------- |
| `examples/regression/scope-plain/`            | `{tekst}`                            | syntax valid            |
| `examples/regression/scope-up-double-length/` | `{/tekst_}`                          | syntax valid            |
| `examples/regression/pitch-marker/`           | `[:] {tekst}`                        | syntax valid            |
| `examples/regression/pitch-markers/`          | `[:] {tekst} [:]`                    | syntax + semantic valid |
| `examples/regression/compound-melisma/`       | `{/&\&/tekst_&~&~}`                  | syntax + semantic valid |
| `examples/regression/svg-basic/`              | `[:] {/Hei_}{/lig_} is de Heer. [:]` | SVG-regressie           |
| `examples/regression/svg-dots/`               | `{tekst..}`                          | SVG-regressie           |
| `examples/minimal/`                           | diverse kleine `.vsa`                | handmatige / CLI-checks |

Leesvoorbeeld: [Basis](voorbeelden/basis.md).

## Incorrect (bewust ongeldig)

### Regressie met golden validation

| [Fixture](@)                                        | Invoer        | Foutcode                               |
| --------------------------------------------------- | ------------- | -------------------------------------- |
| `examples/regression/invalid-empty-scope/`          | `{}`          | `VSA-SYNTAX-EMPTY-SCOPE`               |
| `examples/regression/invalid-unbalanced-modifiers/` | `{/&\tekst_}` | `VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH` |
| `examples/regression/semantic-mismatch/`            | `{/&\tekst_}` | `VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH` |

### Expected-fail (validator moet afkeuren)

| Bestand                                                 | Doel (kort)                  |
| ------------------------------------------------------- | ---------------------------- |
| `examples/expected-fail/semantic-mismatch.vsa`          | modifier-telling mismatch    |
| `examples/expected-fail/empty-scope.vsa`                | lege [scope](@)              |
| `examples/expected-fail/unclosed-scope.vsa`             | niet-gesloten [scope](@)     |
| `examples/expected-fail/missing-final-pitch-marker.vsa` | ontbrekende eind-pitchmarker |
| `examples/expected-fail/empty-final-pitch-marker.vsa`   | lege eind-pitchmarker        |

Leesvoorbeeld: [Fouten](voorbeelden/fouten.md).

### Edge-cases

Map `examples/edge-cases/` bevat aanvullende lastige of foutieve `.vsa`-bestanden
voor gerichte tests (zie [Testen en regressie](../guides/testing-and-regression.md)).

## Zelf draaien

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa validate examples\regression\compound-melisma\input.vsa
vsa validate examples\expected-fail\semantic-mismatch.vsa
scripts\test.cmd
```
