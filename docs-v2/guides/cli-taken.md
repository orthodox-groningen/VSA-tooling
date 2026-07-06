# CLI-taken

Deze pagina beschrijft welk commando je gebruikt voor welke taak.

| Taak | Commando |
|------|----------|
| Versie tonen | `vsa --version` |
| VSA controleren | `vsa validate <bestand-of-map>` |
| AST bekijken | `vsa parse <bestand.vsa> --ast` |
| SVG maken | `vsa svg <input.vsa> <output.svg>` |
| VSA-blokken in Markdown vinden | `vsa blocks <bestand.md>` |
| Markdownbestanden verwerken naar SVG | `vsa process <input> <output>` |
| Hugo-content genereren | `vsa build-markdown <content-source> <content-output> <static-output>` |

## Exitcodes

| Exitcode | Betekenis |
|----------|-----------|
| `0` | commando succesvol |
| `1` | fout gevonden of commando mislukt |

Controle in CMD:

```cmd
echo %ERRORLEVEL%
```

## Bronnen

Gebaseerd op:

- `docs/user-guide.md`
- `docs/cli-reference.md`
