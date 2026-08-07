# TEv2 in tool-docs

VSA-tooling gebruikt TEv2 voor **tool-termen** (parser, renderer, includes, …) in
`docs/terminologie/`. Org-termen uit [bron](https://orthodox-groningen.github.io/bron/specs/terminologie/)
worden via `termselection: "*@bron"` in de lokale MRG/HRG opgenomen (D1: bron blijft
canoniek). Lokale curated texts kunnen een term herdefiniëren; dan wint die voor
`[term](@)`, terwijl `[term](@bron)` de org-definitie blijft.

## Lokaal

Installeer de TEv2-tools (eenmalig):

```cmd
npm install -g @tno-terminology-design/trrt @tno-terminology-design/hrgt @tno-terminology-design/mrgt @tno-terminology-design/mrg-import
```

Volledige pipeline (staging → mrg-import → mrgt/hrgt/trrt → MkDocs):

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\docs-build-tev2.cmd
```

`mrg-import` haalt de bron-MRG op (nodig voor `*@bron` in `docs/saf.yaml`).
Lokaal gebruikt `prepare-tev2-docs.py` indien aanwezig de sibling-checkout
`..\bron\docs` (werkt om een Windows-bug in mrg-import met GitHub-URLs heen);
CI blijft de GitHub-`scopedir` gebruiken.

Alleen glossary-stappen zonder MkDocs: `npm run tev2:docs` (roept dezelfde build aan).

## CI

`docs-pages.yml` (elke push) en `docs-build.yml` (PR / handmatig) draaien de volle
keten inclusief `mrg-import` vóór `mkdocs build --strict` (CI checkt `bron` uit of
gebruikt sibling/`vendor`). Op push alleen `docs-pages.yml`, zodat TEv2+MkDocs niet
dubbel draait. Pages committeert gegenereerde `docs/mrgs/mrg.vsa-tooling*.yaml`
met `[skip ci]` (geen CI-cascade).

## TermRefs schrijven

- Tool-termen: `[parser](@)`, `[validator](@)`, …
- Geïmporteerde org-termen zonder lokale herdefinitie: `[exporttype](@)` (of
  `[exporttype](@bron)` — zelfde entry via bron-scope).
- Termen die **lokaal hergedefinieerd** zijn (`zangstuk`, `vsa`, …):
  - `[zangstuk](@)` → definitie in deze repo
  - `[zangstuk](@bron)` → definitie in scope `bron`

Beide vormen blijven bruikbaar. In lokale curated texts voor gedeelde termen
verwijzen we naar `@bron` met een TermRef, zonder de bron-definitie te kopiëren.
Lokale `vsa.md` houdt alleen form phrases `vsa` / `vsa's`, zodat
`[vsa-notatie](@)` en `[vsa-tooling](@)` uniek naar de bron-entries resolven.

Voorbeeld: [exporttype](@) is een geïmporteerde org-term; [zangstuk](@) is de
lokale herdefinitie, terwijl [zangstuk](@bron) naar scope `bron` wijst.

## Hugo / presentatie

TEv2 in de demosite hoort bij [VSA-demo](https://github.com/orthodox-groningen/VSA-demo)
(daar desgewenst deferred). Deze handleiding gaat alleen over **MkDocs tool-docs**.
