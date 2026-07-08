# Parser-stappen

Deze map bevat de oorspronkelijke parser-stap-documenten uit `docs/architecture/`.

De documenten zijn historisch materiaal en blijven ongewijzigd bewaard. Nieuwe of geconsolideerde uitleg hoort thuis in `../architecture/` of `../specification/`.

## Index

| Stap | Bestand                                                              | Titel                                                             | Thema                         |
| ---- | -------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------- |
| 1    | parser-steps/parser-stap-1.md                                        | Parser stap 1                                                     | basis                         |
| 2    | parser-steps/parser-stap-2.md                                        | Parser stap 2                                                     | basis                         |
| 3    | parser-steps/parser-stap-3-fix.md                                    | Parser stap 3 fix                                                 | basis                         |
| 3    | parser-steps/parser-stap-3.md                                        | Parser stap 3                                                     | basis                         |
| 4    | parser-steps/parser-stap-4-markdown-blokken.md                       | Parser stap 4 - Markdown blokken                                  | basis                         |
| 5    | parser-steps/parser-stap-5-validate.md                               | Parser stap 5 - validate commando                                 | basis                         |
| 6    | parser-steps/parser-stap-6-meerdere-fouten.md                        | Parser stap 6 - meerdere fouten                                   | basis                         |
| 7    | parser-steps/parser-stap-7-svg-fix.md                                | SVG stap 7 fix                                                    | basis                         |
| 7    | parser-steps/parser-stap-7-svg.md                                    | Parser stap 7 - SVG rendering                                     | basis                         |
| 8    | parser-steps/parser-stap-8-process.md                                | Stap 8 - Markdown verwerken naar SVG                              | basis                         |
| 9    | parser-steps/parser-stap-9-map-verwerken.md                          | Stap 9 - map verwerken                                            | basis                         |
| 10   | parser-steps/parser-stap-10-process-valideert.md                     | Stap 10 - process valideert vóór SVG-generatie                    | basis                         |
| 11   | parser-steps/parser-stap-11-build-markdown.md                        | Stap 11 - Markdown build met SVG-verwijzingen                     | basis                         |
| 12   | parser-steps/parser-stap-12-ci.md                                    | Stap 12 - CI/build-script                                         | basis                         |
| 13   | parser-steps/parser-stap-13-svg-glyphs.md                            | Stap 13 - eenvoudige SVG-glyphs                                   | SVG/rendering                 |
| 14   | parser-steps/parser-stap-14-svg-regressie-fix.md                     | Stap 14 fix - SVG regressietests robuuster                        | SVG/rendering                 |
| 14   | parser-steps/parser-stap-14-svg-regressie.md                         | Stap 14 - SVG regressietests                                      | SVG/rendering                 |
| 15   | parser-steps/parser-stap-15-scope-grid.md                            | Stap 15 - scope-grid rendering                                    | SVG/rendering                 |
| 16   | parser-steps/parser-stap-16-svg-autosize.md                          | Stap 16 - SVG autosizing                                          | SVG/rendering                 |
| 17   | parser-steps/parser-stap-17-fix-tekst-wrapping.md                    | Stap 17 fix - tekstwrapping                                       | SVG/rendering                 |
| 17   | parser-steps/parser-stap-17-fix2-tekstmetadata.md                    | Stap 17 fix 2 - tekstmetadata in SVG                              | SVG/rendering                 |
| 17   | parser-steps/parser-stap-17-multiline-layout.md                      | Stap 17 - multiline SVG-layout                                    | SVG/rendering                 |
| 18   | parser-steps/parser-stap-18-svg-breedte-cli.md                       | Stap 18 - SVG regelbreedte via CLI                                | SVG/rendering                 |
| 19   | parser-steps/parser-stap-19-validate-map.md                          | Stap 19 - validate op mappen                                      | configuratie/Hugo/CI          |
| 20   | parser-steps/parser-stap-20-configuratie.md                          | Stap 20 - projectconfiguratie                                     | configuratie/Hugo/CI          |
| 21   | parser-steps/parser-stap-21-fix-shortcode-opt-in.md                  | Stap 21 fix - shortcode opt-in                                    | configuratie/Hugo/CI          |
| 21   | parser-steps/parser-stap-21-hugo-shortcodes.md                       | Stap 21 - Hugo shortcodes                                         | configuratie/Hugo/CI          |
| 22   | parser-steps/parser-stap-22-config-output-mode.md                    | Stap 22 - output-mode in vsa.toml                                 | configuratie/Hugo/CI          |
| 23   | parser-steps/parser-stap-23-hugo-workflow.md                         | Stap 23 - Hugo workflow                                           | configuratie/Hugo/CI          |
| 24   | parser-steps/parser-stap-24-github-actions.md                        | Stap 24 - GitHub Actions opschonen                                | configuratie/Hugo/CI          |
| 25   | parser-steps/parser-stap-25-build-artifacts.md                       | Stap 25 - build artifacts                                         | configuratie/Hugo/CI          |
| 26   | parser-steps/parser-stap-26-github-pages.md                          | Stap 26 - GitHub Pages publicatie                                 | configuratie/Hugo/CI          |
| 27   | parser-steps/parser-stap-27-preview-productie.md                     | Stap 27 - preview en productie                                    | configuratie/Hugo/CI          |
| 28   | parser-steps/parser-stap-28-versie-release.md                        | Stap 28 - versie en releasevoorbereiding                          | configuratie/Hugo/CI          |
| 29   | parser-steps/parser-stap-29-documentatie.md                          | Stap 29 - gebruikersdocumentatie                                  | configuratie/Hugo/CI          |
| 29   | parser-steps/parser-stap-29-fix-uitgebreide-documentatie.md          | Stap 29 fix - uitgebreide documentatie                            | configuratie/Hugo/CI          |
| 29   | parser-steps/parser-stap-29-fix2-bruikbare-documentatie.md           | Stap 29 fix 2 - bruikbare documentatie                            | configuratie/Hugo/CI          |
| 30   | parser-steps/parser-stap-30-demo-quality-fix.md                      | Stap 30 - demo quality fix                                        | configuratie/Hugo/CI          |
| 30   | parser-steps/parser-stap-30-demo-site.md                             | Stap 30 - demo/documentatiesite                                   | configuratie/Hugo/CI          |
| 30   | parser-steps/parser-stap-30-doc-test-fix.md                          | Stap 30 - documentatietest fix                                    | configuratie/Hugo/CI          |
| 30   | parser-steps/parser-stap-30-hugo-home-section-fix.md                 | Stap 30 - Hugo home/section layout fix                            | configuratie/Hugo/CI          |
| 30   | parser-steps/parser-stap-30-static-assets-fix.md                     | Stap 30 - static assets fix                                       | configuratie/Hugo/CI          |
| 30   | parser-steps/parser-stap-30-user-doc-tests-fix.md                    | Stap 30 - user docs testfix                                       | configuratie/Hugo/CI          |
| 31   | parser-steps/parser-stap-31-voorbeeldvalidatie-cli-demo.md           | Stap 31 - voorbeeldvalidatie en CLI-demo pagina's                 | configuratie/Hugo/CI          |
| 32   | parser-steps/parser-stap-32-responsive-branch-builds.md              | Stap 32 - responsive demo en branch-aware builds                  | configuratie/Hugo/CI          |
| 32   | parser-steps/parser-stap-32-site-build-test-fix.md                   | Stap 32 - site build workflow testfix                             | configuratie/Hugo/CI          |
| 33   | parser-steps/parser-stap-33-code-fenced-vsa-markers.md               | Stap 33 - VSA markers in Markdown-codeblokken negeren             | configuratie/Hugo/CI          |
| 34   | parser-steps/parser-stap-34-github-pages-svg-url-fix.md              | Stap 34 - GitHub Pages SVG URL fix                                | configuratie/Hugo/CI          |
| 34   | parser-steps/parser-stap-34-links-responsive-fix.md                  | Stap 34 - links en responsive layout fix                          | configuratie/Hugo/CI          |
| 34   | parser-steps/parser-stap-34-regression-fix.md                        | Stap 34 - regressiefix                                            | configuratie/Hugo/CI          |
| 34   | parser-steps/parser-stap-34-shortcode-example-escape-fix.md          | Stap 34 - shortcode voorbeeld escape fix                          | configuratie/Hugo/CI          |
| 34   | parser-steps/parser-stap-34-test-en-link-fix.md                      | Stap 34 - test en link fix                                        | configuratie/Hugo/CI          |
| 35   | parser-steps/parser-stap-35-url-policy-fix.md                        | Stap 35 - URL policy fix                                          | configuratie/Hugo/CI          |
| 36   | parser-steps/parser-stap-36-compatible-pitch-ending.md               | Stap 36 - compatibele pitch-marker eindcontrole                   | validatie/diagnostics         |
| 36   | parser-steps/parser-stap-36-demo-validation-alignment.md             | Stap 36 - demo/validator alignment                                | validatie/diagnostics         |
| 36   | parser-steps/parser-stap-36-example-policy-fix.md                    | Stap 36 - example policy fix                                      | validatie/diagnostics         |
| 36   | parser-steps/parser-stap-36-regression-fix2.md                       | Stap 36 regressiefix 2                                            | validatie/diagnostics         |
| 36   | parser-steps/parser-stap-36-semantic-validator-import-fix.md         | Stap 36 - semantic validator import fix                           | validatie/diagnostics         |
| 36   | parser-steps/parser-stap-36-site-demo-ending-fix.md                  | Stap 36 - site-demo ending fix                                    | validatie/diagnostics         |
| 36   | parser-steps/parser-stap-36-validator-pitch-ending.md                | Stap 36 - validator pitch-marker eindcontrole                     | validatie/diagnostics         |
| 37   | parser-steps/parser-stap-37-diagnostic-severity.md                   | Stap 37 - diagnostic severity                                     | validatie/diagnostics         |
| 37   | parser-steps/parser-stap-37-option-a-semantic-errors.md              | Stap 37 - optie A: semantiek blijft error                         | validatie/diagnostics         |
| 37   | parser-steps/parser-stap-37-severity-policy-note.md                  | Stap 37 - severity policy note                                    | validatie/diagnostics         |
| 37   | parser-steps/parser-stap-37-severity-regression-fix.md               | Stap 37 - severity regressiefix                                   | validatie/diagnostics         |
| 38   | parser-steps/parser-stap-38-config-output-mode-regression-fix.md     | Stap 38 - config output-mode regressiefix                         | validatie/diagnostics         |
| 38   | parser-steps/parser-stap-38-config-severity-overrides.md             | Stap 38 - severity-overrides in config                            | validatie/diagnostics         |
| 38   | parser-steps/parser-stap-38-next-cli-integration.md                  | Volgende stap na stap 38                                          | validatie/diagnostics         |
| 39   | parser-steps/parser-stap-39-next-cli-validation-config.md            | Volgende stap na stap 39                                          | validatie/diagnostics         |
| 39   | parser-steps/parser-stap-39-validation-config-integration.md         | Stap 39 - validation config integration                           | validatie/diagnostics         |
| 40   | parser-steps/parser-stap-40-cli-validate-config.md                   | Stap 40 - CLI validate gebruikt severity-config                   | validatie/diagnostics         |
| 40   | parser-steps/parser-stap-40-cli-version-import-fix.md                | Stap 40 - CLI version import fix                                  | validatie/diagnostics         |
| 40   | parser-steps/parser-stap-40-next-process-build-config.md             | Volgende stap na stap 40                                          | validatie/diagnostics         |
| 41   | parser-steps/parser-stap-41-next-docs-and-cli-reference.md           | Volgende stap na stap 41                                          | validatie/diagnostics         |
| 41   | parser-steps/parser-stap-41-process-build-config-validation.md       | Stap 41 - process/build-markdown gebruiken validation config      | validatie/diagnostics         |
| 42   | parser-steps/parser-stap-42-docs-config-severity.md                  | Stap 42 - documentatie voor severity-config                       | validatie/diagnostics         |
| 43   | parser-steps/parser-stap-43-next-json-diagnostics.md                 | Volgende stap na stap 43                                          | validatie/diagnostics         |
| 43   | parser-steps/parser-stap-43-policy-stabilization.md                  | Stap 43 - policy stabilization                                    | validatie/diagnostics         |
| 43   | parser-steps/parser-stap-43-rich-diagnostics-metadata.md             | Stap 43 - rich diagnostics metadata                               | validatie/diagnostics         |
| 43   | parser-steps/parser-stap-43-validator-usability-fix.md               | Stap 43 - validator usability fix                                 | validatie/diagnostics         |
| 44   | parser-steps/parser-stap-44-optional-final-pitch-marker.md           | Stap 44 - optional final pitch marker                             | validatie/diagnostics         |
| 44   | parser-steps/parser-stap-44-policy-test-and-column-fix.md            | Stap 44 - policy test and column fix                              | validatie/diagnostics         |
| 45   | parser-steps/parser-stap-45-diagnostic-location-and-scope-errors.md  | Stap 45 - diagnostic location and scope errors                    | validatie/diagnostics         |
| 45   | parser-steps/parser-stap-45-final-regression-fix.md                  | Stap 45 - final regression fix                                    | validatie/diagnostics         |
| 45   | parser-steps/parser-stap-45-final-test-expectation-fix.md            | Stap 45 - final test expectation fix                              | validatie/diagnostics         |
| 45   | parser-steps/parser-stap-45-modifier-count-column-fix.md             | Stap 45 - modifier count column fix                               | validatie/diagnostics         |
| 45   | parser-steps/parser-stap-45-prefix-modifier-and-line-offset-fix.md   | Stap 45 - prefix modifier and line offset fix                     | validatie/diagnostics         |
| 46   | parser-steps/parser-stap-46-rendering-specs.md                       | Stap 46 - rendering specs uitgewerkt                              | rendering/spacing             |
| 47   | parser-steps/parser-stap-47-svg-rendering-baseline.md                | Stap 47 - SVG rendering baseline                                  | rendering/spacing             |
| 48   | parser-steps/parser-stap-48-svg-tuning-and-rendering-demo-pages.md   | Stap 48 - SVG tuning en rendering demo pagina's                   | rendering/spacing             |
| 48   | parser-steps/parser-stap-48-test-regression-fix.md                   | Stap 48 - test regression fix                                     | rendering/spacing             |
| 49   | parser-steps/parser-stap-49-svg-whitespace-and-visual-tuning.md      | Stap 49 - SVG whitespace en visuele tuning                        | rendering/spacing             |
| 49   | parser-steps/parser-stap-49-test-regression-fix.md                   | Stap 49 - test regression fix                                     | rendering/spacing             |
| 50   | parser-steps/parser-stap-50-inline-text-flow-renderer.md             | Stap 50 - inline text-flow renderer                               | rendering/spacing             |
| 51   | parser-steps/parser-stap-51-final-pitch-wrap-fix.md                  | Stap 51 - final pitch wrap fix                                    | rendering/spacing             |
| 51   | parser-steps/parser-stap-51-force-apply.md                           | Stap 51 - force apply                                             | rendering/spacing             |
| 51   | parser-steps/parser-stap-51-textflow-overlays.md                     | Stap 51 - textflow overlays                                       | rendering/spacing             |
| 51   | parser-steps/parser-stap-51-wrap-regression-fix.md                   | Stap 51 - wrap regression fix                                     | rendering/spacing             |
| 52   | parser-steps/parser-stap-52-source-aware-spacing.md                  | Stap 52 - source-aware spacing                                    | rendering/spacing             |
| 52   | parser-steps/parser-stap-52-text-split-test-fix.md                   | Stap 52 - text split test fix                                     | rendering/spacing             |
| 53   | parser-steps/parser-stap-53-glyph-overlap-and-filler-tuning.md       | Stap 53 - glyph overlap en filler tuning                          | rendering/spacing             |
| 53   | parser-steps/parser-stap-53-regression-fix.md                        | Stap 53 - regression fix                                          | rendering/spacing             |
| 54   | parser-steps/parser-stap-54-filler-and-optical-gap.md                | Stap 54 - fillerhoogte en optische scope-gap                      | rendering/spacing             |
| 55   | parser-steps/parser-stap-55-wrap-policy-and-optical-flow.md          | Stap 55 - wrap policy en optical flow                             | rendering/spacing             |
| 56   | parser-steps/parser-stap-56-todo-and-newline-wrap-policy.md          | Stap 56 - TODO en newline wrap policy                             | rendering/spacing             |
| 57   | parser-steps/parser-stap-57-preserve-vsa-block-newlines.md           | Stap 57 - preserve VSA block newlines                             | rendering/spacing             |
| 58   | parser-steps/parser-stap-58-real-pipeline-newlines.md                | Stap 58 - echte pipeline-newlines                                 | rendering/spacing             |
| 59   | parser-steps/parser-stap-59-inspect-hugo-svg-usage.md                | Stap 59 - inspect Hugo SVG usage                                  | rendering/spacing             |
| 60   | parser-steps/parser-stap-60-multiline-baseline-debug.md              | Stap 60 - multiline baseline debug                                | rendering/spacing             |
| 61   | parser-steps/parser-stap-61-markdown-hardbreak-newlines.md           | Stap 61 - Markdown hardbreak newlines                             | rendering/spacing             |
| 62   | parser-steps/parser-stap-62-test-expectation-fix.md                  | Stap 62 - test expectation fix                                    | rendering/spacing             |
| 62   | parser-steps/parser-stap-62-text-metrics-spacing.md                  | Stap 62 - text metrics en spacing                                 | rendering/spacing             |
| 63   | parser-steps/parser-stap-63-rendering-spacing-diagnostics.md         | Stap 63 - rendering spacing diagnostics                           | rendering/spacing             |
| 64   | parser-steps/parser-stap-64-real-font-metrics.md                     | Stap 64 - real font metrics                                       | rendering/spacing             |
| 65   | parser-steps/parser-stap-65-dejavu-font-policy.md                    | Stap 65 - DejaVu font policy                                      | rendering/spacing             |
| 66   | parser-steps/parser-stap-66-pillow-dependency-ci.md                  | Stap 66 - Pillow dependency en CI font setup                      | rendering/spacing             |
| 66   | parser-steps/parser-stap-66-test-expectation-fix.md                  | Stap 66 - test expectation fix                                    | rendering/spacing             |
| 67   | parser-steps/parser-stap-67-script-path-fix.md                       | Stap 67 - script path fix                                         | rendering/spacing             |
| 67   | parser-steps/parser-stap-67-spacing-policy-metrics-diagnostics.md    | Stap 67 - spacing policy + metrics diagnostics                    | rendering/spacing             |
| 68   | parser-steps/parser-stap-68-todo-and-hugo-navigation.md              | Stap 68 - TODO en Hugo navigatie                                  | rendering/spacing             |
| 69   | parser-steps/parser-stap-69-revert-broken-navigation.md              | Stap 69 - herstel kapotte navigatie                               | rendering/spacing             |
| 70   | parser-steps/parser-stap-70-ci-rendering-fonts-os-guard.md           | Stap 70 - CI rendering fonts OS guard                             | rendering/spacing             |
| 71   | parser-steps/parser-stap-71-hugo-index-navigation.md                 | Stap 71 - Hugo index-navigatie                                    | Hugo/publicatie               |
| 72   | parser-steps/parser-stap-72-fix-nested-vsa-image-refs.md             | Stap 72 - fix nested VSA image refs                               | Hugo/publicatie               |
| 73   | parser-steps/parser-stap-73-spec-multiple-height-markers.md          | Stap 73 - specificatie meerdere hoogte-markeringen                | Hugo/publicatie               |
| 74   | parser-steps/parser-stap-74-praktijk-moved-asset-tests.md            | Stap 74 - praktijk verplaatst: asset testverwachtingen            | Hugo/publicatie               |
| 75   | parser-steps/parser-stap-75-navigation-praktijk-moved-checks.md      | Stap 75 - navigatie na verplaatsen praktijk                       | Hugo/publicatie               |
| 76   | parser-steps/parser-stap-76-regenerate-missing-vsa-images.md         | Stap 76 - ontbrekende VSA SVG's regenereren                       | Hugo/publicatie               |
| 77   | parser-steps/parser-stap-77-path-normalization-fix.md                | Stap 77 - path normalization fix                                  | Hugo/publicatie               |
| 78   | parser-steps/parser-stap-78-index-nav-blocks-only.md                 | Stap 78 - alleen navigatieblokken in `_index.md`                  | Hugo/publicatie               |
| 79   | parser-steps/parser-stap-79-explicit-nav-placeholders.md             | Stap 79 - expliciete navigatie-placeholders                       | Hugo/publicatie               |
| 80   | parser-steps/parser-stap-80-retire-step78-navigation.md              | Stap 80 - retire step78 navigation model                          | Hugo/publicatie               |
| 81   | parser-steps/parser-stap-81-stabilize-hugo-navigation.md             | Stap 81 - Hugo navigatie stabiliseren                             | Hugo/publicatie               |
| 82   | parser-steps/parser-stap-82-repo-root-detection.md                   | Stap 82 - repo-root detectie                                      | Hugo/publicatie               |
| 83   | parser-steps/parser-stap-83-stop-mutating-workflow-tests.md          | Stap 83 - stop muterende workflow-tests                           | Hugo/publicatie               |
| 84   | parser-steps/parser-stap-84-hugo-link-asset-checker.md               | Stap 84 - Hugo link- en assetchecker                              | Hugo/publicatie               |
| 85   | parser-steps/parser-stap-85-fix-hugo-link-checker-tests.md           | Stap 85 - fix Hugo linkchecker tests                              | Hugo/publicatie               |
| 86   | parser-steps/parser-stap-86-clean-build-regenerate-check.md          | Stap 86 - clean Hugo build, SVG regeneratie, linkcheck            | Hugo/publicatie               |
| 87   | parser-steps/parser-stap-87-hide-legacy-hugo-routes.md               | Stap 87 - legacy Hugo-routes verbergen                            | Hugo/publicatie               |
| 88   | parser-steps/parser-stap-88-restore-build-hugo-cmd.md                | Stap 88 - herstel `build-hugo.cmd`                                | Hugo/publicatie               |
| 89   | parser-steps/parser-stap-89-clean-build-artifacts.md                 | Stap 89 - clean build artifacts                                   | Hugo/publicatie               |
| 90   | parser-steps/parser-stap-90-stop-build-hugo-mutators.md              | Stap 90 - stop build-hugo mutators                                | Hugo/publicatie               |
| 91   | parser-steps/parser-stap-91-multiple-height-marker-specs.md          | Stap 91 - meerdere hoogte-markeringen                             | hoogte-markeringen/directives |
| 92   | parser-steps/parser-stap-92-height-marker-parser-contract.md         | Stap 92 - parsercontract voor meerdere hoogte-markeringen         | hoogte-markeringen/directives |
| 93   | parser-steps/parser-stap-93-fix-step91-spec-test.md                  | Stap 93 - fix stap 91 specificatietest                            | hoogte-markeringen/directives |
| 94   | parser-steps/parser-stap-94-bracket-directive-contract.md            | Stap 94 - bracket-directive contract                              | hoogte-markeringen/directives |
| 95   | parser-steps/parser-stap-95-bracket-directive-scanner.md             | Stap 95 - bracket-directive scanner                               | hoogte-markeringen/directives |
| 96   | parser-steps/parser-stap-96-bracket-token-stream.md                  | Stap 96 - bracket token stream                                    | hoogte-markeringen/directives |
| 97   | parser-steps/parser-stap-97-repair-bracket-token-stream.md           | Stap 97 - repair bracket token stream                             | hoogte-markeringen/directives |
| 98   | parser-steps/parser-stap-98-real-font-metrics-and-step92-test-fix.md | Stap 98 - real font metrics afdwingen + stap 92 test fix          | hoogte-markeringen/directives |
| 99   | parser-steps/parser-stap-99-scripts-cleanup-generated-only.md        | Stap 99 - scripts cleanup en generated-only build                 | hoogte-markeringen/directives |
| 100  | parser-steps/parser-stap-100-marker-only-nav-generation.md           | Stap 100 - marker-only navigatiegeneratie                         | hoogte-markeringen/directives |
| 101  | parser-steps/parser-stap-101-freeze-content-source-scripts.md        | Stap 101 - content-source bevriezen                               | hoogte-markeringen/directives |
| 104  | parser-steps/parser-stap-104-parser-multiple-height-markers.md       | Stap 104 - parseracceptatie voor meerdere hoogte-markeringen      | hoogte-markeringen/directives |
| 105  | parser-steps/parser-stap-105-parser-bracket-token-stream.md          | Stap 105 - parser koppelen aan bracket token stream               | hoogte-markeringen/directives |
| 106a | parser-steps/parser-stap-106a-height-marker-compat-repair.md         | Stap 106a - repair HeightMarker compatibiliteit                   | hoogte-markeringen/directives |
| 106b | parser-steps/parser-stap-106b-height-marker-ast-compatibility.md     | Stap 106b - HeightMarker/PitchMarker AST-compatibiliteit          | hoogte-markeringen/directives |
| 107  | parser-steps/parser-stap-107-semantic-multiple-height-markers.md     | Stap 107 - semantische validatie voor meerdere hoogte-markeringen | hoogte-markeringen/directives |
| 108  | parser-steps/parser-stap-108-svg-multiple-height-markers.md          | Stap 108 - SVG-rendering van meerdere hoogte-markeringen          | hoogte-markeringen/directives |
| 109  | parser-steps/parser-stap-109-wraptoken-dispatch.md                   | Stap 109 - voorbereiding wraptoken dispatch                       | hoogte-markeringen/directives |
| 111  | parser-steps/parser-stap-111-control-token-ast-node.md               | Stap 111 - ControlTokenNode in AST                                | hoogte-markeringen/directives |
| 112  | parser-steps/parser-stap-112-control-token-dispatch.md               | Stap 112 - Control token dispatch                                 | hoogte-markeringen/directives |
| 113  | parser-steps/parser-stap-113-control-token-semantics.md              | Stap 113 - renderer-onafhankelijke control-token semantiek        | hoogte-markeringen/directives |
| 114  | parser-steps/parser-stap-114-dispatch-design.md                      | Stap 114 - Parser dispatch ontwerp                                | hoogte-markeringen/directives |
| 115  | parser-steps/parser-stap-115-directive-framework.md                  | Stap 115 - Directive framework ontwerp                            | hoogte-markeringen/directives |
| 116  | parser-steps/parser-stap-116-control-token-registry.md               | Stap 116 - Control token registry                                 | hoogte-markeringen/directives |
| 117  | parser-steps/parser-stap-117-height-marker-ast-contract.md           | Stap 117 - Height Marker AST Contract                             | hoogte-markeringen/directives |
| 118  | parser-steps/parser-stap-118-height-marker-ast-helpers.md            | Stap 118 - Height marker AST helpers                              | hoogte-markeringen/directives |
| 119  | parser-steps/parser-stap-119-height-marker-parser-contract.md        | Stap 119 - Height Marker Parser Contract                          | hoogte-markeringen/directives |
| 120  | parser-steps/parser-stap-120-height-marker-parser-helpers.md         | Stap 120 - Height marker parser helpers                           | hoogte-markeringen/directives |
| 121  | parser-steps/parser-stap-121-height-marker-validator-contract.md     | Stap 121 - Height Marker Validator Contract                       | hoogte-markeringen/directives |
| 122  | parser-steps/parser-stap-122-validator-height-marker-helpers.md      | Stap 122 - Validator aansluiten op height marker helpers          | hoogte-markeringen/directives |
| 127  | parser-steps/parser-stap-127-pitch-marker-policy-consolidation.md    | Stap 127 - pitch-marker policy consolidatie                       | publicatie/beleid             |
| 128  | parser-steps/parser-stap-128-github-pages-preview.md                 | Stap 128 - automatische GitHub Pages preview                      | publicatie/beleid             |
| 129  | parser-steps/parser-stap-129-gh-pages-preview-production.md          | Stap 129 - GitHub Pages preview en productie via gh-pages         | publicatie/beleid             |
| 130  | parser-steps/parser-stap-130-gh-pages-workflow-tests.md              | Stap 130 - workflowtests voor gh-pages preview/productie          | publicatie/beleid             |
| 131  | parser-steps/parser-stap-131-project-site-baseurl.md                 | Stap 131 - GitHub Pages project-site baseURL                      | publicatie/beleid             |
| 132  | parser-steps/parser-stap-132-demo-site-quality-check.md              | Stap 132 - demo-site kwaliteitscontrole                           | publicatie/beleid             |
| 133  | parser-steps/parser-stap-133-safe-svg-comments.md                    | Stap 133 - veilige SVG-comments                                   | publicatie/beleid             |
| 134  | parser-steps/parser-stap-134-remove-svg-plain-text-comments.md       | Stap 134 - plain-text comments verwijderen uit SVG                | publicatie/beleid             |
| 135  | parser-steps/parser-stap-135-html-comments-policy.md                 | Stap 135 - HTML-commentaar in VSA-notatie                         | publicatie/beleid             |
| 136  | parser-steps/parser-stap-136-vsa-comment-lines-no-whitespace.md      | Stap 136 - comment-only regels zonder extra whitespace            | publicatie/beleid             |
| 137  | parser-steps/parser-stap-137-publication-checks-and-reusable-tool.md | Stap 137 - publicatiechecks en herbruikbare VSA-tool              | publicatie/beleid             |
