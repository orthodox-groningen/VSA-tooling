# Traceerbaarheid specificatie

Status: **werkversie voor fase 2**.

Dit document legt vast uit welke bestaande documenten de geconsolideerde specificatie is opgebouwd.

De oorspronkelijke documenten in `docs/` blijven voorlopig leidend bij twijfel.

## Bronnen per nieuw specificatiedocument

| Nieuw document | Primaire bronnen | Opmerking |
|---|---|---|
| `README.md` | `docs/spec/vsa-spec-v1.md`, `docs/spec/vsa-spec-v1.0.1.md`, `docs/specs/terminologie.md` | Overzicht en scope van de specificatie. |
| `syntax.md` | `docs/spec/vsa-spec-v1.md`, `docs/spec/vsa-height-markers.md`, `docs/spec/spec-control-tokens.md`, `docs/spec/vsa-comments.md` | Bronsyntaxis, scopes, markeringen en control tokens. |
| `semantics.md` | `docs/spec/vsa-spec-v1.md`, `docs/spec/vsa-height-markers.md`, `docs/spec/vsa-glyph-model.md`, `docs/spec/zangstuk-identificatie.md` | Betekenis, validatie en muzikale interpretatie. |
| `directives.md` | `docs/spec/include-vsa.md`, `docs/spec/vsa-comments.md`, `docs/spec/spec-control-tokens.md`, `docs/architecture/parser-stap-111-control-token-ast-node.md`, `docs/architecture/parser-stap-112-control-token-dispatch.md`, `docs/architecture/parser-stap-113-control-token-semantics.md` | Include, commentaar en bracket-/control-directives. |
| `rendering.md` | `docs/spec/vsa-svg-rendering-spec.md`, `docs/spec/vsa-svg-dom-structure.md`, `docs/spec/vsa-layout-algorithm.md`, `docs/spec/vsa-glyph-layout-rules.md`, `docs/spec/vsa-rendering-config-model.md` | SVG-rendering, layout, DOM-structuur en glyphregels. |
| `cli.md` | `docs/user-guide.md`, `docs/user-guide-config-severity.md`, `docs/spec/vsa-spec-v1.md` | CLI-gebruik, output en foutgedrag. |

## Reviewregels

- Nieuwe specificatietekst mag inhoud uit meerdere oude documenten combineren.
- Bij inhoudelijk conflict krijgt de meest normatieve bron voorrang.
- Ontwerpgeschiedenis wordt niet in de specificatie opgenomen, maar blijft beschikbaar in `history/`.
- Open punten blijven herkenbaar en worden niet stilzwijgend normatief gemaakt.
- Als een bron niet volledig verwerkt is, moet dat hier of in het betreffende specificatiedocument zichtbaar blijven.

## Nog te controleren in fase 2

- Of `vsa-spec-v1.md` en `vsa-spec-v1.0.1.md` volledig inhoudelijk zijn verwerkt.
- Of control tokens definitief normatief genoeg zijn voor `directives.md`.
- Of MusicXML-export in deze specificatie hoort of later een eigen `reference/musicxml.md` krijgt.
- Of polyfonie uitsluitend historisch/proposal blijft of als toekomstige extensie wordt benoemd.
