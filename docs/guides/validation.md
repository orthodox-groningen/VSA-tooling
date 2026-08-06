# Validatie

Gebruik de [validator](@) om te controleren of [VSA-notatie](@bron)-invoer
bruikbaar is voor verdere verwerking.

## Bestand valideren

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

## Map valideren

```cmd
vsa validate examples\consumer-minimal\content-source
```

## Wat wordt gecontroleerd?

| Controle                                                                 | Voorbeeld van fout |
| ------------------------------------------------------------------------ | ------------------ |
| scope is goed afgesloten                                                 | `{tekst`           |
| scope is niet leeg                                                       | `{}`               |
| geen whitespace binnen scope                                             | `{te kst}`         |
| geen losse sluitaccolade                                                 | `tekst}`           |
| [pitch-marker](@) is goed afgesloten                                     | `[//:`             |
| pitch-marker heeft dubbele punt                                          | `[//]`             |
| [hoogte-modifier](@)- en [lengte-modifier](@)-posities passen bij elkaar | `{/&\tekst_}`      |

## Foutoutput lezen

Voorbeeld:

```text
examples\demo.md:blok-1:1:1: VSA-SYNTAX-EMPTY-SCOPE: Scope zonder zangelement.
```

| Deel                     | Betekenis                         |
| ------------------------ | --------------------------------- |
| `examples\demo.md`       | bestand waarin de fout zit        |
| `blok-1`                 | eerste VSA-blok in dat bestand    |
| `1:1`                    | regel en kolom binnen dat blok    |
| `VSA-SYNTAX-EMPTY-SCOPE` | foutcode ([diagnostic](@))        |
| tekst erna               | uitleg                            |

## Severity-overrides

Gebruik [vsa.toml](@) om specifieke semantische meldingen tijdelijk als
[severity](@) `warning` te behandelen.

```toml
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
```

Gebruik:

```cmd
vsa validate bestand.vsa --config vsa.toml
```

Syntaxfouten blijven altijd hard.

## Aanpak bij fouten

| Stap | Actie                                  |
| ---- | -------------------------------------- |
| 1    | Open het genoemde bestand              |
| 2    | Zoek het genoemde `blok-N`             |
| 3    | Kijk naar regel en kolom               |
| 4    | Corrigeer de [VSA-notatie](@bron)      |
| 5    | Draai hetzelfde commando opnieuw       |

## Bronnen

Gebaseerd op:

- `docs/guides/user-guide.md`
- `docs/guides/validation.md`
- `docs/reference/cli.md`
