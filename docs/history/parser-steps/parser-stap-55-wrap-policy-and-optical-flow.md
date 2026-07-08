# Stap 55 - wrap policy en optical flow

Deze stap implementeert de afgesproken afbreekpolicy in de SVG-layout.

## Afbreekpolicy

| Constructie | Betekenis |
|---|---|
| CR/LF/CRLF | harde bronregelgrens |
| `[/]` | forced line break |
| `[*]` | forced line break / sterkere sectiebreuk |
| `[/?]` | preferred break |
| `[*?]` | preferred break / sterker voorkeursbreekpunt |
| `[:]` | pitchmarker, geen wrap-token |

## Regels

- Geen afbreking midden in woorden.
- Bronregels worden niet samengevoegd.
- Wrapping gebeurt alleen binnen een bronregel.
- Bronspaties blijven render-units.
