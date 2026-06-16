# TODO addendum stap 75

Toevoegen aan `docs/todo.md` onder demo-site:

## Hugo link/asset checker opnemen in build

Status: `Open`

De checker:

```cmd
python scripts\check-hugo-links-and-assets.py
```

moet later structureel in de build/CI worden opgenomen, nadat bekend is dat alle pagina's correct gegenereerd worden.

Controleert:

- interne `href` links;
- `<img src>` assets;
- ontbrekende SVG's;
- verkeerde paden na directorywijzigingen.
