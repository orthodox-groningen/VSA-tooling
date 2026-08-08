# `vsa svg` — één VSA-bestand naar SVG renderen

Render één VSA-bronbestand naar één SVG-afbeelding.

## Synopsis

```text
vsa svg [-h] [--config CONFIG] [--max-line-width MAX_LINE_WIDTH] input output
```

## Beschrijving

`vsa svg` leest één `.vsa`-bestand, lost `@include-vsa` op indien aanwezig,
parset de VSA-notatie en rendert het resultaat naar een SVG-bestand. Dit
commando verwerkt **geen** Markdownblokken — voor Markdown met VSA-blokken
gebruik je [`vsa process`](process.md) of [`vsa build-markdown`](build-markdown.md).

`vsa svg` valideert de invoer niet expliciet vooraf; een parsefout leidt tot
een foutmelding en exitcode `1`. Draai bij twijfel eerst
[`vsa validate`](validate.md).

## Argumenten en opties

| Naam                              | Verplicht | Betekenis                                                   | Default                                       | Beperkingen                     |
| --------------------------------- | --------- | ----------------------------------------------------------- | --------------------------------------------- | ------------------------------- |
| `input`                           | Ja        | VSA-bronbestand dat gelezen wordt.                          | —                                             | Moet bestaan.                   |
| `output`                          | Ja        | SVG-bestand dat wordt aangemaakt of overschreven.           | —                                             | Bovenliggende map moet bestaan. |
| `--config CONFIG`                 | Nee       | Pad naar een alternatief `vsa.toml`.                        | Auto-detectie van `vsa.toml`                  | —                               |
| `--max-line-width MAX_LINE_WIDTH` | Nee       | Maximale SVG-regelbreedte voordat wordt afgebroken.         | `max-line-width` uit `vsa.toml`, anders `800` | Getal (float)                   |
| `-h`, `--help`                    | Nee       | Toon hulp voor dit subcommando.                             | —                                             | —                               |

## Output

- **stdout**: `SVG geschreven naar: <output>` bij succes.
- **Bestand**: `output` wordt aangemaakt (of overschreven als het al bestaat).
- Geen Markdown wordt gelezen of geschreven.

## Exit status

| Exitcode | Betekenis                            |
| -------- | ------------------------------------ |
| `0`      | SVG succesvol geschreven.            |
| `1`      | Bestand niet gevonden, of parsefout. |

## Voorbeelden — succes

```cmd
vsa svg examples\minimal\050_svg_demo.vsa tmp\demo.svg
```

Verwachte output:

```text
SVG geschreven naar: tmp\demo.svg
```

Het bestand `tmp\demo.svg` wordt aangemaakt (map `tmp\` moet al bestaan).
Bekijk het resultaat direct:

```cmd
start tmp\demo.svg
```

Met een aangepaste regelbreedte:

```cmd
vsa svg examples\minimal\100_multiline_demo.vsa tmp\demo-smal.svg --max-line-width 400
```

```text
SVG geschreven naar: tmp\demo-smal.svg
```

!!! note "Validatie vs. SVG"
    `examples\minimal\050_svg_demo.vsa` faalt op `vsa validate` (semantische
    hoogte-mismatch), maar rendert wel gewoon met `vsa svg` — dit commando
    voert geen semantische controle uit. Draai `vsa validate` eerst als je
    zeker wilt zijn van [geldige VSA-notatie](@).

## Voorbeelden — falen

```cmd
vsa svg pad\dat\niet\bestaat.vsa tmp\demo.svg
```

Verwachte output (stderr):

```text
[Errno 2] No such file or directory: 'pad\\dat\\niet\\bestaat.vsa'
```

Exitcode: `1`.

Fix: controleer het invoerpad, bijvoorbeeld met `dir`.

Bij een kapotte VSA-syntax (bijv. een onafgesloten scope) geeft `vsa svg`
een parsefout op stderr. Fix: draai eerst `vsa validate <input>` om de exacte
foutlocatie en foutcode te zien.

## Zie ook

- [`vsa validate`](validate.md) — controleer VSA-notatie vóór het renderen.
- [`vsa process`](process.md) — SVG's genereren uit meerdere Markdownbestanden.
- [`vsa build-markdown`](build-markdown.md) — SVG's + Hugo-Markdown in één stap.
- Workflow-uitleg: [svg-export.md](../../guides/svg-export.md)
- Bron-contract (SVG als exporttype): [conversie-vsa-svg](https://orthodox-groningen.github.io/bron/reference/conversie-vsa-svg/), [exporttype-svg](https://orthodox-groningen.github.io/bron/reference/exporttype-svg/)
