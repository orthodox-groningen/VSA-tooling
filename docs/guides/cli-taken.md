# CLI-taken

Deze pagina helpt kiezen welk commando bij welke taak hoort.

## Commando kiezen

| Taak                                      | Commando                                                         |
| ----------------------------------------- | ---------------------------------------------------------------- |
| Versie tonen                              | `vsa --version`                                                  |
| VSA controleren                           | `vsa validate <bestand-of-map>`                                  |
| AST bekijken                              | `vsa parse <bestand.vsa> --ast`                                  |
| Eén SVG maken                             | `vsa svg <input.vsa> <output.svg>`                               |
| VSA-blokken in Markdown vinden            | `vsa blocks <bestand.md>`                                        |
| Markdownbestanden verwerken naar SVG      | `vsa process <input> <output>`                                   |
| Hugo-content genereren                    | `vsa build-markdown <content-source> <content-output> <static>`  |
| MusicXML exporteren                       | `vsa musicxml <input.vsa> <output.mxl>`                          |

## Exitcodes

| Exitcode | Betekenis                         |
| -------- | --------------------------------- |
| `0`      | commando succesvol                |
| `1`      | fout gevonden of commando mislukt |

Controle in CMD:

```cmd
echo %ERRORLEVEL%
```

## Veelgebruikte voorbeelden

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

```cmd
vsa blocks examples\minimal\031_markdown_block_metadata.md --json
```

```cmd
vsa musicxml mijn-lied.vsa mijn-lied.mxl
```

## Bronnen

Gebaseerd op:

- `docs/user-guide.md`
- `docs/cli-reference.md`
- `docs/user/musicxml-export.md`
