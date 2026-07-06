# Stap 112 - Control token dispatch

## Doel

De parser krijgt een afzonderlijke dispatch-laag voor bracket-tokens.

## Dispatchvolgorde

```text
[<EHM>:]  -> Height marker
[/]       -> Control token
[*]       -> Control token
[/?]      -> Control token
[*?]      -> Control token
anders     -> parserfout
```

## Nog niet geïmplementeerd

- daadwerkelijke parsercode
- SVG-rendering
- MusicXML-rendering

Deze stap legt alleen het contract vast.
