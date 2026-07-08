# Stap 111 - ControlTokenNode in AST

## Doel

Control tokens krijgen een eigen AST-node voordat parserdispatch wordt gebouwd.

## Node

```python
ControlTokenNode(
    token="[/]",
    meaning="phrase_boundary",
    start=...,
    end=...,
)
```

## Abstracte betekenissen

| Token | Meaning |
|---|---|
| `[*]` | `phrase_rest` |
| `[/]` | `phrase_boundary` |
| `[*?]` | `optional_phrase_rest` |
| `[/?]` | `optional_phrase_boundary` |

## Belangrijk

Deze node legt nog geen renderergedrag vast.

SVG, MusicXML en andere renderers vertalen `meaning` later zelf naar concrete output.

## Nog niet gedaan

- parserdispatch;
- validatorregels;
- SVG-rendering;
- MusicXML-export.
