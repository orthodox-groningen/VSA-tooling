# Merge candidates

Deze lijst geeft logische samenvoegclusters voor fase 2. Er wordt nog niets verwijderd.

## Specificatiekern

Aantal documenten: 43

| Nr | Document | Huidig type |
|---:|----------|-------------|
| 001 | `docs/AI-REVIEW-PROMPT.md` | specificatie |
| 004 | `docs/architecture/height-marker-model.md` | architectuur |
| 005 | `docs/architecture/height-marker-status.md` | architectuur |
| 012 | `docs/architecture/parser-stap-104-parser-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 014 | `docs/architecture/parser-stap-106a-height-marker-compat-repair.md` | ontwikkelgeschiedenis / parserstap |
| 015 | `docs/architecture/parser-stap-106b-height-marker-ast-compatibility.md` | ontwikkelgeschiedenis / parserstap |
| 016 | `docs/architecture/parser-stap-107-semantic-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 017 | `docs/architecture/parser-stap-108-svg-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 022 | `docs/architecture/parser-stap-113-control-token-semantics.md` | ontwikkelgeschiedenis / parserstap |
| 026 | `docs/architecture/parser-stap-117-height-marker-ast-contract.md` | ontwikkelgeschiedenis / parserstap |
| 027 | `docs/architecture/parser-stap-118-height-marker-ast-helpers.md` | ontwikkelgeschiedenis / parserstap |
| 028 | `docs/architecture/parser-stap-119-height-marker-parser-contract.md` | ontwikkelgeschiedenis / parserstap |
| 030 | `docs/architecture/parser-stap-120-height-marker-parser-helpers.md` | ontwikkelgeschiedenis / parserstap |
| 031 | `docs/architecture/parser-stap-121-height-marker-validator-contract.md` | ontwikkelgeschiedenis / parserstap |
| 032 | `docs/architecture/parser-stap-122-validator-height-marker-helpers.md` | ontwikkelgeschiedenis / parserstap |
| 033 | `docs/architecture/parser-stap-127-pitch-marker-policy-consolidation.md` | ontwikkelgeschiedenis / parserstap |
| 042 | `docs/architecture/parser-stap-135-html-comments-policy.md` | ontwikkelgeschiedenis / parserstap |
| 086 | `docs/architecture/parser-stap-36-compatible-pitch-ending.md` | ontwikkelgeschiedenis / parserstap |
| 092 | `docs/architecture/parser-stap-36-validator-pitch-ending.md` | ontwikkelgeschiedenis / parserstap |
| 113 | `docs/architecture/parser-stap-44-optional-final-pitch-marker.md` | ontwikkelgeschiedenis / parserstap |
| 120 | `docs/architecture/parser-stap-46-rendering-specs.md` | ontwikkelgeschiedenis / parserstap |
| 141 | `docs/architecture/parser-stap-59-inspect-hugo-svg-usage.md` | ontwikkelgeschiedenis / parserstap |
| 161 | `docs/architecture/parser-stap-73-spec-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 181 | `docs/architecture/parser-stap-91-multiple-height-marker-specs.md` | ontwikkelgeschiedenis / parserstap |
| 182 | `docs/architecture/parser-stap-92-height-marker-parser-contract.md` | ontwikkelgeschiedenis / parserstap |
| 183 | `docs/architecture/parser-stap-93-fix-step91-spec-test.md` | ontwikkelgeschiedenis / parserstap |
| 193 | `docs/miscellaneous/liturgikon-uitleg.md` | algemene documentatie |
| 199 | `docs/spec/include-vsa.md` | specificatie |
| 200 | `docs/spec/vsa-comments.md` | specificatie |
| 201 | `docs/spec/vsa-glyph-layout-rules.md` | specificatie |
| 202 | `docs/spec/vsa-glyph-model.md` | specificatie |
| 203 | `docs/spec/vsa-height-markers.md` | specificatie |
| 204 | `docs/spec/vsa-layout-algorithm.md` | specificatie |
| 205 | `docs/spec/vsa-polyphony-proposal.md` | specificatie |
| 206 | `docs/spec/vsa-rendering-config-model.md` | specificatie |
| 207 | `docs/spec/vsa-spec-v1.0.1.md` | specificatie |
| 208 | `docs/spec/vsa-spec-v1.md` | specificatie |
| 209 | `docs/spec/vsa-svg-dom-structure.md` | specificatie |
| 210 | `docs/spec/vsa-svg-rendering-spec.md` | specificatie |
| 211 | `docs/spec-control-tokens.md` | specificatie |
| 212 | `docs/spec-vsa-document-samenstellen.md` | specificatie |
| 213 | `docs/specs/README.md` | specificatie |
| 214 | `docs/specs/terminologie.md` | specificatie |

## Parserarchitectuur

Aantal documenten: 185

| Nr | Document | Huidig type |
|---:|----------|-------------|
| 007 | `docs/architecture/parser-fases.md` | architectuur |
| 008 | `docs/architecture/parser-stap-1.md` | ontwikkelgeschiedenis / parserstap |
| 009 | `docs/architecture/parser-stap-10-process-valideert.md` | ontwikkelgeschiedenis / parserstap |
| 010 | `docs/architecture/parser-stap-100-marker-only-nav-generation.md` | ontwikkelgeschiedenis / parserstap |
| 011 | `docs/architecture/parser-stap-101-freeze-content-source-scripts.md` | ontwikkelgeschiedenis / parserstap |
| 012 | `docs/architecture/parser-stap-104-parser-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 013 | `docs/architecture/parser-stap-105-parser-bracket-token-stream.md` | ontwikkelgeschiedenis / parserstap |
| 014 | `docs/architecture/parser-stap-106a-height-marker-compat-repair.md` | ontwikkelgeschiedenis / parserstap |
| 015 | `docs/architecture/parser-stap-106b-height-marker-ast-compatibility.md` | ontwikkelgeschiedenis / parserstap |
| 016 | `docs/architecture/parser-stap-107-semantic-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 017 | `docs/architecture/parser-stap-108-svg-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 018 | `docs/architecture/parser-stap-109-wraptoken-dispatch.md` | ontwikkelgeschiedenis / parserstap |
| 019 | `docs/architecture/parser-stap-11-build-markdown.md` | ontwikkelgeschiedenis / parserstap |
| 020 | `docs/architecture/parser-stap-111-control-token-ast-node.md` | ontwikkelgeschiedenis / parserstap |
| 021 | `docs/architecture/parser-stap-112-control-token-dispatch.md` | ontwikkelgeschiedenis / parserstap |
| 022 | `docs/architecture/parser-stap-113-control-token-semantics.md` | ontwikkelgeschiedenis / parserstap |
| 023 | `docs/architecture/parser-stap-114-dispatch-design.md` | ontwikkelgeschiedenis / parserstap |
| 024 | `docs/architecture/parser-stap-115-directive-framework.md` | ontwikkelgeschiedenis / parserstap |
| 025 | `docs/architecture/parser-stap-116-control-token-registry.md` | ontwikkelgeschiedenis / parserstap |
| 026 | `docs/architecture/parser-stap-117-height-marker-ast-contract.md` | ontwikkelgeschiedenis / parserstap |
| 027 | `docs/architecture/parser-stap-118-height-marker-ast-helpers.md` | ontwikkelgeschiedenis / parserstap |
| 028 | `docs/architecture/parser-stap-119-height-marker-parser-contract.md` | ontwikkelgeschiedenis / parserstap |
| 029 | `docs/architecture/parser-stap-12-ci.md` | ontwikkelgeschiedenis / parserstap |
| 030 | `docs/architecture/parser-stap-120-height-marker-parser-helpers.md` | ontwikkelgeschiedenis / parserstap |
| 031 | `docs/architecture/parser-stap-121-height-marker-validator-contract.md` | ontwikkelgeschiedenis / parserstap |
| 032 | `docs/architecture/parser-stap-122-validator-height-marker-helpers.md` | ontwikkelgeschiedenis / parserstap |
| 033 | `docs/architecture/parser-stap-127-pitch-marker-policy-consolidation.md` | ontwikkelgeschiedenis / parserstap |
| 034 | `docs/architecture/parser-stap-128-github-pages-preview.md` | ontwikkelgeschiedenis / parserstap |
| 035 | `docs/architecture/parser-stap-129-gh-pages-preview-production.md` | ontwikkelgeschiedenis / parserstap |
| 036 | `docs/architecture/parser-stap-13-svg-glyphs.md` | ontwikkelgeschiedenis / parserstap |
| 037 | `docs/architecture/parser-stap-130-gh-pages-workflow-tests.md` | ontwikkelgeschiedenis / parserstap |
| 038 | `docs/architecture/parser-stap-131-project-site-baseurl.md` | ontwikkelgeschiedenis / parserstap |
| 039 | `docs/architecture/parser-stap-132-demo-site-quality-check.md` | ontwikkelgeschiedenis / parserstap |
| 040 | `docs/architecture/parser-stap-133-safe-svg-comments.md` | ontwikkelgeschiedenis / parserstap |
| 041 | `docs/architecture/parser-stap-134-remove-svg-plain-text-comments.md` | ontwikkelgeschiedenis / parserstap |
| 042 | `docs/architecture/parser-stap-135-html-comments-policy.md` | ontwikkelgeschiedenis / parserstap |
| 043 | `docs/architecture/parser-stap-136-vsa-comment-lines-no-whitespace.md` | ontwikkelgeschiedenis / parserstap |
| 044 | `docs/architecture/parser-stap-137-publication-checks-and-reusable-tool.md` | ontwikkelgeschiedenis / parserstap |
| 045 | `docs/architecture/parser-stap-14-svg-regressie-fix.md` | ontwikkelgeschiedenis / parserstap |
| 046 | `docs/architecture/parser-stap-14-svg-regressie.md` | ontwikkelgeschiedenis / parserstap |
| 047 | `docs/architecture/parser-stap-15-scope-grid.md` | ontwikkelgeschiedenis / parserstap |
| 048 | `docs/architecture/parser-stap-16-svg-autosize.md` | ontwikkelgeschiedenis / parserstap |
| 049 | `docs/architecture/parser-stap-17-fix-tekst-wrapping.md` | ontwikkelgeschiedenis / parserstap |
| 050 | `docs/architecture/parser-stap-17-fix2-tekstmetadata.md` | ontwikkelgeschiedenis / parserstap |
| 051 | `docs/architecture/parser-stap-17-multiline-layout.md` | ontwikkelgeschiedenis / parserstap |
| 052 | `docs/architecture/parser-stap-18-svg-breedte-cli.md` | ontwikkelgeschiedenis / parserstap |
| 053 | `docs/architecture/parser-stap-19-validate-map.md` | ontwikkelgeschiedenis / parserstap |
| 054 | `docs/architecture/parser-stap-2.md` | ontwikkelgeschiedenis / parserstap |
| 055 | `docs/architecture/parser-stap-20-configuratie.md` | ontwikkelgeschiedenis / parserstap |
| 056 | `docs/architecture/parser-stap-21-fix-shortcode-opt-in.md` | ontwikkelgeschiedenis / parserstap |
| 057 | `docs/architecture/parser-stap-21-hugo-shortcodes.md` | ontwikkelgeschiedenis / parserstap |
| 058 | `docs/architecture/parser-stap-22-config-output-mode.md` | ontwikkelgeschiedenis / parserstap |
| 059 | `docs/architecture/parser-stap-23-hugo-workflow.md` | ontwikkelgeschiedenis / parserstap |
| 060 | `docs/architecture/parser-stap-24-github-actions.md` | ontwikkelgeschiedenis / parserstap |
| 061 | `docs/architecture/parser-stap-25-build-artifacts.md` | ontwikkelgeschiedenis / parserstap |
| 062 | `docs/architecture/parser-stap-26-github-pages.md` | ontwikkelgeschiedenis / parserstap |
| 063 | `docs/architecture/parser-stap-27-preview-productie.md` | ontwikkelgeschiedenis / parserstap |
| 064 | `docs/architecture/parser-stap-28-versie-release.md` | ontwikkelgeschiedenis / parserstap |
| 065 | `docs/architecture/parser-stap-29-documentatie.md` | ontwikkelgeschiedenis / parserstap |
| 066 | `docs/architecture/parser-stap-29-fix-uitgebreide-documentatie.md` | ontwikkelgeschiedenis / parserstap |
| 067 | `docs/architecture/parser-stap-29-fix2-bruikbare-documentatie.md` | ontwikkelgeschiedenis / parserstap |
| 068 | `docs/architecture/parser-stap-3-fix.md` | ontwikkelgeschiedenis / parserstap |
| 069 | `docs/architecture/parser-stap-3.md` | ontwikkelgeschiedenis / parserstap |
| 070 | `docs/architecture/parser-stap-30-demo-quality-fix.md` | ontwikkelgeschiedenis / parserstap |
| 071 | `docs/architecture/parser-stap-30-demo-site.md` | ontwikkelgeschiedenis / parserstap |
| 072 | `docs/architecture/parser-stap-30-doc-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 073 | `docs/architecture/parser-stap-30-hugo-home-section-fix.md` | ontwikkelgeschiedenis / parserstap |
| 074 | `docs/architecture/parser-stap-30-static-assets-fix.md` | ontwikkelgeschiedenis / parserstap |
| 075 | `docs/architecture/parser-stap-30-user-doc-tests-fix.md` | ontwikkelgeschiedenis / parserstap |
| 076 | `docs/architecture/parser-stap-31-voorbeeldvalidatie-cli-demo.md` | ontwikkelgeschiedenis / parserstap |
| 077 | `docs/architecture/parser-stap-32-responsive-branch-builds.md` | ontwikkelgeschiedenis / parserstap |
| 078 | `docs/architecture/parser-stap-32-site-build-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 079 | `docs/architecture/parser-stap-33-code-fenced-vsa-markers.md` | ontwikkelgeschiedenis / parserstap |
| 080 | `docs/architecture/parser-stap-34-github-pages-svg-url-fix.md` | ontwikkelgeschiedenis / parserstap |
| 081 | `docs/architecture/parser-stap-34-links-responsive-fix.md` | ontwikkelgeschiedenis / parserstap |
| 082 | `docs/architecture/parser-stap-34-regression-fix.md` | ontwikkelgeschiedenis / parserstap |
| 083 | `docs/architecture/parser-stap-34-shortcode-example-escape-fix.md` | ontwikkelgeschiedenis / parserstap |
| 084 | `docs/architecture/parser-stap-34-test-en-link-fix.md` | ontwikkelgeschiedenis / parserstap |
| 085 | `docs/architecture/parser-stap-35-url-policy-fix.md` | ontwikkelgeschiedenis / parserstap |
| 086 | `docs/architecture/parser-stap-36-compatible-pitch-ending.md` | ontwikkelgeschiedenis / parserstap |
| … | Nog 105 documenten | … |

## SVG-rendering

Aantal documenten: 34

| Nr | Document | Huidig type |
|---:|----------|-------------|
| 009 | `docs/architecture/parser-stap-10-process-valideert.md` | ontwikkelgeschiedenis / parserstap |
| 017 | `docs/architecture/parser-stap-108-svg-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 019 | `docs/architecture/parser-stap-11-build-markdown.md` | ontwikkelgeschiedenis / parserstap |
| 022 | `docs/architecture/parser-stap-113-control-token-semantics.md` | ontwikkelgeschiedenis / parserstap |
| 036 | `docs/architecture/parser-stap-13-svg-glyphs.md` | ontwikkelgeschiedenis / parserstap |
| 040 | `docs/architecture/parser-stap-133-safe-svg-comments.md` | ontwikkelgeschiedenis / parserstap |
| 041 | `docs/architecture/parser-stap-134-remove-svg-plain-text-comments.md` | ontwikkelgeschiedenis / parserstap |
| 045 | `docs/architecture/parser-stap-14-svg-regressie-fix.md` | ontwikkelgeschiedenis / parserstap |
| 046 | `docs/architecture/parser-stap-14-svg-regressie.md` | ontwikkelgeschiedenis / parserstap |
| 048 | `docs/architecture/parser-stap-16-svg-autosize.md` | ontwikkelgeschiedenis / parserstap |
| 049 | `docs/architecture/parser-stap-17-fix-tekst-wrapping.md` | ontwikkelgeschiedenis / parserstap |
| 050 | `docs/architecture/parser-stap-17-fix2-tekstmetadata.md` | ontwikkelgeschiedenis / parserstap |
| 051 | `docs/architecture/parser-stap-17-multiline-layout.md` | ontwikkelgeschiedenis / parserstap |
| 052 | `docs/architecture/parser-stap-18-svg-breedte-cli.md` | ontwikkelgeschiedenis / parserstap |
| 073 | `docs/architecture/parser-stap-30-hugo-home-section-fix.md` | ontwikkelgeschiedenis / parserstap |
| 080 | `docs/architecture/parser-stap-34-github-pages-svg-url-fix.md` | ontwikkelgeschiedenis / parserstap |
| 081 | `docs/architecture/parser-stap-34-links-responsive-fix.md` | ontwikkelgeschiedenis / parserstap |
| 121 | `docs/architecture/parser-stap-47-svg-rendering-baseline.md` | ontwikkelgeschiedenis / parserstap |
| 122 | `docs/architecture/parser-stap-48-svg-tuning-and-rendering-demo-pages.md` | ontwikkelgeschiedenis / parserstap |
| 124 | `docs/architecture/parser-stap-49-svg-whitespace-and-visual-tuning.md` | ontwikkelgeschiedenis / parserstap |
| 127 | `docs/architecture/parser-stap-50-inline-text-flow-renderer.md` | ontwikkelgeschiedenis / parserstap |
| 134 | `docs/architecture/parser-stap-53-glyph-overlap-and-filler-tuning.md` | ontwikkelgeschiedenis / parserstap |
| 141 | `docs/architecture/parser-stap-59-inspect-hugo-svg-usage.md` | ontwikkelgeschiedenis / parserstap |
| 156 | `docs/architecture/parser-stap-7-svg-fix.md` | ontwikkelgeschiedenis / parserstap |
| 157 | `docs/architecture/parser-stap-7-svg.md` | ontwikkelgeschiedenis / parserstap |
| 164 | `docs/architecture/parser-stap-76-regenerate-missing-vsa-images.md` | ontwikkelgeschiedenis / parserstap |
| 168 | `docs/architecture/parser-stap-8-process.md` | ontwikkelgeschiedenis / parserstap |
| 175 | `docs/architecture/parser-stap-86-clean-build-regenerate-check.md` | ontwikkelgeschiedenis / parserstap |
| 201 | `docs/spec/vsa-glyph-layout-rules.md` | specificatie |
| 202 | `docs/spec/vsa-glyph-model.md` | specificatie |
| 204 | `docs/spec/vsa-layout-algorithm.md` | specificatie |
| 209 | `docs/spec/vsa-svg-dom-structure.md` | specificatie |
| 210 | `docs/spec/vsa-svg-rendering-spec.md` | specificatie |
| 211 | `docs/spec-control-tokens.md` | specificatie |

## Hugo en publicatie

Aantal documenten: 32

| Nr | Document | Huidig type |
|---:|----------|-------------|
| 006 | `docs/architecture/pages-enable-fix.md` | architectuur |
| 034 | `docs/architecture/parser-stap-128-github-pages-preview.md` | ontwikkelgeschiedenis / parserstap |
| 035 | `docs/architecture/parser-stap-129-gh-pages-preview-production.md` | ontwikkelgeschiedenis / parserstap |
| 037 | `docs/architecture/parser-stap-130-gh-pages-workflow-tests.md` | ontwikkelgeschiedenis / parserstap |
| 038 | `docs/architecture/parser-stap-131-project-site-baseurl.md` | ontwikkelgeschiedenis / parserstap |
| 039 | `docs/architecture/parser-stap-132-demo-site-quality-check.md` | ontwikkelgeschiedenis / parserstap |
| 044 | `docs/architecture/parser-stap-137-publication-checks-and-reusable-tool.md` | ontwikkelgeschiedenis / parserstap |
| 056 | `docs/architecture/parser-stap-21-fix-shortcode-opt-in.md` | ontwikkelgeschiedenis / parserstap |
| 057 | `docs/architecture/parser-stap-21-hugo-shortcodes.md` | ontwikkelgeschiedenis / parserstap |
| 059 | `docs/architecture/parser-stap-23-hugo-workflow.md` | ontwikkelgeschiedenis / parserstap |
| 060 | `docs/architecture/parser-stap-24-github-actions.md` | ontwikkelgeschiedenis / parserstap |
| 062 | `docs/architecture/parser-stap-26-github-pages.md` | ontwikkelgeschiedenis / parserstap |
| 063 | `docs/architecture/parser-stap-27-preview-productie.md` | ontwikkelgeschiedenis / parserstap |
| 071 | `docs/architecture/parser-stap-30-demo-site.md` | ontwikkelgeschiedenis / parserstap |
| 073 | `docs/architecture/parser-stap-30-hugo-home-section-fix.md` | ontwikkelgeschiedenis / parserstap |
| 078 | `docs/architecture/parser-stap-32-site-build-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 080 | `docs/architecture/parser-stap-34-github-pages-svg-url-fix.md` | ontwikkelgeschiedenis / parserstap |
| 083 | `docs/architecture/parser-stap-34-shortcode-example-escape-fix.md` | ontwikkelgeschiedenis / parserstap |
| 091 | `docs/architecture/parser-stap-36-site-demo-ending-fix.md` | ontwikkelgeschiedenis / parserstap |
| 122 | `docs/architecture/parser-stap-48-svg-tuning-and-rendering-demo-pages.md` | ontwikkelgeschiedenis / parserstap |
| 141 | `docs/architecture/parser-stap-59-inspect-hugo-svg-usage.md` | ontwikkelgeschiedenis / parserstap |
| 154 | `docs/architecture/parser-stap-68-todo-and-hugo-navigation.md` | ontwikkelgeschiedenis / parserstap |
| 159 | `docs/architecture/parser-stap-71-hugo-index-navigation.md` | ontwikkelgeschiedenis / parserstap |
| 170 | `docs/architecture/parser-stap-81-stabilize-hugo-navigation.md` | ontwikkelgeschiedenis / parserstap |
| 173 | `docs/architecture/parser-stap-84-hugo-link-asset-checker.md` | ontwikkelgeschiedenis / parserstap |
| 174 | `docs/architecture/parser-stap-85-fix-hugo-link-checker-tests.md` | ontwikkelgeschiedenis / parserstap |
| 175 | `docs/architecture/parser-stap-86-clean-build-regenerate-check.md` | ontwikkelgeschiedenis / parserstap |
| 176 | `docs/architecture/parser-stap-87-hide-legacy-hugo-routes.md` | ontwikkelgeschiedenis / parserstap |
| 177 | `docs/architecture/parser-stap-88-restore-build-hugo-cmd.md` | ontwikkelgeschiedenis / parserstap |
| 180 | `docs/architecture/parser-stap-90-stop-build-hugo-mutators.md` | ontwikkelgeschiedenis / parserstap |
| 191 | `docs/hugo-navigation-placeholders.md` | architectuur |
| 192 | `docs/hugo-site-structure.md` | architectuur |

## CI en tests

Aantal documenten: 38

| Nr | Document | Huidig type |
|---:|----------|-------------|
| 001 | `docs/AI-REVIEW-PROMPT.md` | specificatie |
| 002 | `docs/architecture/ci-pytest-fix.md` | architectuur |
| 003 | `docs/architecture/ci-reliability.md` | architectuur |
| 029 | `docs/architecture/parser-stap-12-ci.md` | ontwikkelgeschiedenis / parserstap |
| 037 | `docs/architecture/parser-stap-130-gh-pages-workflow-tests.md` | ontwikkelgeschiedenis / parserstap |
| 045 | `docs/architecture/parser-stap-14-svg-regressie-fix.md` | ontwikkelgeschiedenis / parserstap |
| 046 | `docs/architecture/parser-stap-14-svg-regressie.md` | ontwikkelgeschiedenis / parserstap |
| 059 | `docs/architecture/parser-stap-23-hugo-workflow.md` | ontwikkelgeschiedenis / parserstap |
| 072 | `docs/architecture/parser-stap-30-doc-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 075 | `docs/architecture/parser-stap-30-user-doc-tests-fix.md` | ontwikkelgeschiedenis / parserstap |
| 078 | `docs/architecture/parser-stap-32-site-build-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 084 | `docs/architecture/parser-stap-34-test-en-link-fix.md` | ontwikkelgeschiedenis / parserstap |
| 114 | `docs/architecture/parser-stap-44-policy-test-and-column-fix.md` | ontwikkelgeschiedenis / parserstap |
| 117 | `docs/architecture/parser-stap-45-final-test-expectation-fix.md` | ontwikkelgeschiedenis / parserstap |
| 123 | `docs/architecture/parser-stap-48-test-regression-fix.md` | ontwikkelgeschiedenis / parserstap |
| 125 | `docs/architecture/parser-stap-49-test-regression-fix.md` | ontwikkelgeschiedenis / parserstap |
| 132 | `docs/architecture/parser-stap-52-source-aware-spacing.md` | ontwikkelgeschiedenis / parserstap |
| 133 | `docs/architecture/parser-stap-52-text-split-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 145 | `docs/architecture/parser-stap-62-test-expectation-fix.md` | ontwikkelgeschiedenis / parserstap |
| 146 | `docs/architecture/parser-stap-62-text-metrics-spacing.md` | ontwikkelgeschiedenis / parserstap |
| 147 | `docs/architecture/parser-stap-63-rendering-spacing-diagnostics.md` | ontwikkelgeschiedenis / parserstap |
| 150 | `docs/architecture/parser-stap-66-pillow-dependency-ci.md` | ontwikkelgeschiedenis / parserstap |
| 151 | `docs/architecture/parser-stap-66-test-expectation-fix.md` | ontwikkelgeschiedenis / parserstap |
| 153 | `docs/architecture/parser-stap-67-spacing-policy-metrics-diagnostics.md` | ontwikkelgeschiedenis / parserstap |
| 158 | `docs/architecture/parser-stap-70-ci-rendering-fonts-os-guard.md` | ontwikkelgeschiedenis / parserstap |
| 161 | `docs/architecture/parser-stap-73-spec-multiple-height-markers.md` | ontwikkelgeschiedenis / parserstap |
| 162 | `docs/architecture/parser-stap-74-praktijk-moved-asset-tests.md` | ontwikkelgeschiedenis / parserstap |
| 167 | `docs/architecture/parser-stap-79-explicit-nav-placeholders.md` | ontwikkelgeschiedenis / parserstap |
| 172 | `docs/architecture/parser-stap-83-stop-mutating-workflow-tests.md` | ontwikkelgeschiedenis / parserstap |
| 174 | `docs/architecture/parser-stap-85-fix-hugo-link-checker-tests.md` | ontwikkelgeschiedenis / parserstap |
| 183 | `docs/architecture/parser-stap-93-fix-step91-spec-test.md` | ontwikkelgeschiedenis / parserstap |
| 188 | `docs/architecture/parser-stap-98-real-font-metrics-and-step92-test-fix.md` | ontwikkelgeschiedenis / parserstap |
| 202 | `docs/spec/vsa-glyph-model.md` | specificatie |
| 204 | `docs/spec/vsa-layout-algorithm.md` | specificatie |
| 209 | `docs/spec/vsa-svg-dom-structure.md` | specificatie |
| 210 | `docs/spec/vsa-svg-rendering-spec.md` | specificatie |
| 212 | `docs/spec-vsa-document-samenstellen.md` | specificatie |
| 215 | `docs/testing/testvoorbeelden-en-regressietests.md` | specificatie |

## Voorbeelden en gebruikersdocumentatie

Aantal documenten: 14

| Nr | Document | Huidig type |
|---:|----------|-------------|
| 039 | `docs/architecture/parser-stap-132-demo-site-quality-check.md` | ontwikkelgeschiedenis / parserstap |
| 070 | `docs/architecture/parser-stap-30-demo-quality-fix.md` | ontwikkelgeschiedenis / parserstap |
| 071 | `docs/architecture/parser-stap-30-demo-site.md` | ontwikkelgeschiedenis / parserstap |
| 076 | `docs/architecture/parser-stap-31-voorbeeldvalidatie-cli-demo.md` | ontwikkelgeschiedenis / parserstap |
| 077 | `docs/architecture/parser-stap-32-responsive-branch-builds.md` | ontwikkelgeschiedenis / parserstap |
| 083 | `docs/architecture/parser-stap-34-shortcode-example-escape-fix.md` | ontwikkelgeschiedenis / parserstap |
| 087 | `docs/architecture/parser-stap-36-demo-validation-alignment.md` | ontwikkelgeschiedenis / parserstap |
| 088 | `docs/architecture/parser-stap-36-example-policy-fix.md` | ontwikkelgeschiedenis / parserstap |
| 091 | `docs/architecture/parser-stap-36-site-demo-ending-fix.md` | ontwikkelgeschiedenis / parserstap |
| 122 | `docs/architecture/parser-stap-48-svg-tuning-and-rendering-demo-pages.md` | ontwikkelgeschiedenis / parserstap |
| 192 | `docs/hugo-site-structure.md` | architectuur |
| 215 | `docs/testing/testvoorbeelden-en-regressietests.md` | specificatie |
| 222 | `docs/user-guide-config-severity.md` | handleiding / voorbeeld |
| 223 | `docs/user-guide.md` | handleiding / voorbeeld |

