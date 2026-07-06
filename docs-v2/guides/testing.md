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

| Map                    | Doel                                      |
| ---------------------- | ----------------------------------------- |
| `examples\minimal`    | geldige, kleine VSA-fragmenten            |
| `examples\edge-cases` | lastige of foutieve gevallen              |
| `examples\regression` | vaste testsets met verwachte uitvoer      |

## Mogelijke testsetstructuur

```text
input.vsa
expected-ast.json
expected-validation.json
expected.svg
expected.musicxml
```

## Testvolgorde

| Stap | Controle                                  |
| ---: | ------------------------------------------ |
|    1 | parse `input.vsa`                          |
|    2 | vergelijk met `expected-ast.json`          |
|    3 | voer validatie uit                         |
|    4 | vergelijk met `expected-validation.json`   |
|    5 | render naar SVG                            |
|    6 | exporteer naar MusicXML                    |

## Belangrijk

Als de specificatie wijzigt, moeten verwachte testuitkomsten bewust worden aangepast.

## Bronnen

Gebaseerd op:

- `docs/testing/testvoorbeelden-en-regressietests.md`
