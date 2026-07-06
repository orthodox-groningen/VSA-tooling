# Stap 113 - renderer-onafhankelijke control-token semantiek

## Doel

Deze stap legt de betekenis van control tokens vast zonder parserwijziging.

De parser herkent deze tokens dus nog niet als syntax.

## Mapping

| Token | Abstracte meaning |
|---|---|
| `[*]` | `phrase_rest` |
| `[/]` | `phrase_boundary` |
| `[*?]` | `optional_phrase_rest` |
| `[/?]` | `optional_phrase_boundary` |

## Renderer-onafhankelijk

De `meaning` is geen directe renderopdracht.

Voorbeelden:

### SVG

Een SVG-renderer kan een control token configureren als:

- zichtbaar teken;
- harde regelbreuk;
- zachte regelbreuk;
- geen uitvoer.

### MusicXML

Een MusicXML-renderer kan dezelfde abstracte `meaning` configureren als:

- breath mark;
- barline;
- system break;
- geen uitvoer.

## Belangrijke beperking

Deze stap activeert de syntax nog niet.

Dus bestaande parsercontracten blijven gelden:

```text
[/] is voorlopig geen geldige parser-token.
[*] is voorlopig geen geldige parser-token.
[/?] is voorlopig geen geldige parser-token.
[*?] is voorlopig geen geldige parser-token.
```

## Volgende stap

Een latere parserstap moet expliciet beslissen hoe deze tokens worden gedispatched zonder te conflicteren met:

```text
[<EHM>:]
```
