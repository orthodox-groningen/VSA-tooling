# VSA configuratie: severity-overrides

Deze pagina vult de gebruikershandleiding aan.

## Waarvoor gebruik je dit?

Gebruik severity-overrides als je sommige semantische aandachtspunten tijdelijk als waarschuwing wilt behandelen.

Standaard blijft semantiek hard:

```text
semantic diagnostic = error
```

Met config kun je specifieke foutcodes zachter maken:

```text
semantic diagnostic = warning
```

## Voorbeeld `vsa.toml`

```toml
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
```

## Geldige severity-waarden

| Waarde | Betekenis |
|--------|-----------|
| `error` | validatie faalt |
| `warning` | melding tonen, maar verwerking mag doorgaan |

## Welke commando's gebruiken dit?

| Commando | Werkt met severity-config? |
|----------|-----------------------------|
| `vsa validate` | ja |
| `vsa process` | ja |
| `vsa build-markdown` | ja |
| `vsa svg` | nee, parseert/render rechtstreeks |
| `vsa blocks` | nee, inspecteert blokken |
| `vsa parse` | nee, toont parseroutput |

## Validate

```cmd
vsa validate bestand.vsa --config vsa.toml
```

Bij alleen warnings:

```text
WARNING: VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

De exitcode is dan `0`.

Bij errors blijft de exitcode `1`.

## Process

```cmd
vsa process input.md generated\vsa --config vsa.toml
```

Bij alleen warnings worden SVG-bestanden gegenereerd.

## Build-markdown

```cmd
vsa build-markdown content generated\content static\vsa --config vsa.toml
```

Bij alleen warnings worden Markdown en SVG-bestanden gegenereerd.

## Wat blijft altijd hard?

Syntax-errors blijven altijd `error`.

Dat betekent:

```text
{onafgesloten
```

blijft validatie en generatie stoppen.

## Praktisch advies

Gebruik warnings tijdelijk bij migratie of experimenten.

Gebruik errors voor CI, demo-sites en publicatie wanneer de notatie stabiel moet zijn.


## Verouderde pitchmarker-foutcodes

De oude foutcodes `VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER` en `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` zijn obsolete.

Een ontbrekende eindmarkering is toegestaan. Een eindmarkering `[:]` is geldig en betekent neutrale hoogte, equivalent aan `[-:]` c.q. `[~:]`.
