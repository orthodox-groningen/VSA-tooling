# TEv2 in tool-docs

VSA-tooling gebruikt TEv2 voor **tool-termen** (parser, renderer, includes, …) in
`docs/terminologie/`. Org-termen (zangstuk, variant, uitvoeringsvorm, …) blijven
canoniek in [bron — terminologie](https://orthodox-groningen.github.io/bron/specs/terminologie/)
(D1). Deze repo importeert de bron-MRG zodat TermRefs naar org-termen kunnen
resolven zonder een tweede normatieve glossary.

## Lokaal

Installeer de TEv2-tools (eenmalig):

```cmd
npm install -g @tno-terminology-design/trrt @tno-terminology-design/hrgt @tno-terminology-design/mrgt @tno-terminology-design/mrg-import
```

Volledige pipeline (staging → mrgt/hrgt/trrt → MkDocs):

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\docs-build-tev2.cmd
```

`mrg-import` (bron-MRG) is lokaal standaard uit. Zet aan met:

```cmd
set TEV2_RUN_IMPORT=1
scripts\docs-build-tev2.cmd
```

Alleen glossary-stappen zonder MkDocs: `npm run tev2:docs` (roept dezelfde build aan).

## CI

`docs-build.yml` en `docs-pages.yml` draaien de volle keten inclusief `mrg-import`
vóór `mkdocs build --strict`. Pages committeert gegenereerde
`docs/mrgs/mrg.vsa-tooling*.yaml`.

## TermRefs schrijven

Voor tool-termen: `[VSA](@)` of een form phrase die in `docs/terminologie/` staat.
Voor org-termen: bij voorkeur `[zangstuk](@bron)` (of form phrase uit bron) —
niet opnieuw definiëren in deze repo.

## Hugo / presentatie

TEv2 in de demosite hoort bij [VSA-demo](https://github.com/orthodox-groningen/VSA-demo)
(daar desgewenst deferred). Deze handleiding gaat alleen over **MkDocs tool-docs**.
