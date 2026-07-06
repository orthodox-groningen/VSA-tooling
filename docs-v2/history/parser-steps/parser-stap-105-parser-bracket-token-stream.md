# Stap 105 - parser koppelen aan bracket token stream

## Doel

De parser gebruikt voor hoogte-markeringen dezelfde bracket-token infrastructuur als toekomstige bracket-directives.

## Wijziging

`Parser._parse_pitch_marker()` gebruikt nu:

```python
bracket_token_stream(...)
```

De parser accepteert alleen tokens met:

```text
kind = pitch_marker
```

Andere bracket-directives, zoals `[_:]` of `[/&\:]`, worden als ongeldige hoogte-markering afgewezen.

## Resultaat

- `:]` blijft één bracket-directive eindtoken;
- meerdere hoogte-markeringen blijven ondersteund;
- tekst vóór, tussen en na markers blijft behouden;
- toekomstige bracket-directives kunnen op dezelfde infrastructuur voortbouwen.

## Nog niet gedaan

- overige bracket-directives implementeren;
- validatorregels voor meerdere hoogte-markeringen aanpassen;
- SVG-rendering voor meerdere hoogte-markeringen controleren.
