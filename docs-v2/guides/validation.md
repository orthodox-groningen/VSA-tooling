# Validatie

Gebruik validatie om te controleren of VSA-invoer bruikbaar is voor verdere verwerking.

## Bestand valideren

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

## Map valideren

```cmd
vsa validate examples\hugo-demo\content-source
```

## Wat wordt gecontroleerd?

| Controle | Voorbeeld van fout |
|----------|--------------------|
| scope is goed afgesloten | `{tekst` |
| scope is niet leeg | `{}` |
| geen whitespace binnen scope | `{te kst}` |
| geen losse sluitaccolade | `tekst}` |
| pitch-marker is goed afgesloten | `[//:` |
| pitch-marker heeft dubbele punt | `[//]` |
| hoogte- en lengte-modifiers passen semantisch bij elkaar | `{/&\tekst_}` |

## Severity-overrides

Gebruik `vsa.toml` om specifieke semantische meldingen tijdelijk als warning te behandelen.

```toml
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
```

Gebruik:

```cmd
vsa validate bestand.vsa --config vsa.toml
```

Syntaxfouten blijven altijd hard.

## Bronnen

Gebaseerd op:

- `docs/user-guide.md`
- `docs/user-guide-config-severity.md`
- `docs/cli-reference.md`
