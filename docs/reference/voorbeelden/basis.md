# Basis

Klein voorbeeld van VSA-invoer en SVG-rendering.

## Invoer

```text
[:] {/Hei_}{/lig_} is de Heer. [//:]
```

## Uitleg

| Onderdeel     | Betekenis                 |
| ------------- | ------------------------- |
| `[:]`         | openings-pitch-marker     |
| `{/Hei_}`     | scope met hoogte-modifier |
| `is de Heer.` | gewone tekst              |
| `[\\:]`       | afsluitende pitch-marker  |

## Commando

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa svg examples\minimal\valid-demo.vsa generated\docs-demo-basis.svg
```

## Verwachte output

```text
SVG geschreven naar: generated\docs-demo-basis.svg
```

Gerelateerde fixture: `examples/regression/svg-basic/input.vsa`.
