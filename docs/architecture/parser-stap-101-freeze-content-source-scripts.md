# Stap 101 - content-source bevriezen

## Probleem

Oude eenmalige scripts konden redactionele broncontent in `examples\hugo-demo\content-source` herschrijven.

Voorbeelden van ongewenste wijzigingen:

- frontmatter titel wijzigen;
- markdown headings toevoegen;
- handmatige navigatie vervangen;
- `VSA-NAV` scaffolding invoegen.

## Besluit

`content-source` is handmatige broncontent.

Buildscripts mogen daaruit lezen, maar niet automatisch redactionele inhoud wijzigen.

## Toegestaan

Generated output mag worden gewijzigd in:

```text
generated\hugo\content
generated\hugo\static
examples\hugo-demo\content
examples\hugo-demo\static
examples\hugo-demo\public
```

## Niet toegestaan

Automatisch schrijven naar:

```text
examples\hugo-demo\content-source
```
