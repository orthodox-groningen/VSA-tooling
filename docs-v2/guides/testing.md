# Testvoorbeelden en regressietests

Gebruik kleine voorbeelden om parser, validator, renderer en exporter gericht te testen.

## Indeling

```text
examples/
├── minimal/
├── edge-cases/
└── regression/
```

## Doel per map

| Map | Doel |
|-----|------|
| `examples\minimal` | geldige, kleine VSA-fragmenten |
| `examples\edge-cases` | lastige of foutieve gevallen |
| `examples\regression` | vaste testsets met verwachte uitvoer |

## Testvolgorde

1. Parse `input.vsa`.
2. Vergelijk met `expected-ast.json`.
3. Voer validatie uit.
4. Vergelijk met `expected-validation.json`.
5. Render naar SVG.
6. Exporteer later naar MusicXML.

## Bronnen

Gebaseerd op:

- `docs/testing/testvoorbeelden-en-regressietests.md`
