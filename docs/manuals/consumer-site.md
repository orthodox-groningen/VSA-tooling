# Consumer-site (Hugo)

Een **consumer-site** is een Hugo-site die `vsa-tool` gebruikt om Markdown met
VSA-blokken te valideren en naar SVG/MusicXML te renderen. Dat is de rol van
[VSA-demo](https://github.com/orthodox-groningen/VSA-demo), niet van deze
tooling-repo.

## Waar hoort wat

| Repo                                                           | Rol                           |
| -------------------------------------------------------------- | ----------------------------- |
| **VSA-tooling** (deze docs)                                    | Package, CLI, specs, fixtures |
| **[VSA-demo](https://github.com/orthodox-groningen/VSA-demo)** | Voorbeeld-Hugo-site + Pages   |
| **[bron](https://github.com/orthodox-groningen/bron)**         | Zangstukken en org-specs      |

## Typische keten

```text
content-source/*.md  (+ .vsa)
        ↓
  vsa validate
        ↓
  vsa build-markdown  →  content/ + static/vsa/
        ↓
  hugo
        ↓
  public/  (GitHub Pages)
```

## Lokaal (VSA-demo)

```cmd
cd /d C:\Git\orthodox-groningen\VSA-demo
scripts\bootstrap.cmd
scripts\serve-hugo.cmd
```

Documentatie en scripts: [VSA-demo README](https://github.com/orthodox-groningen/VSA-demo/blob/main/README.md).

## Tooling-kant

- Installatie en CI: [Integratie — reuse](../guides/reuse-vsa-tooling.md)
- CLI: [CLI-taken](../guides/cli-taken.md), [CLI-referentie](../reference/cli.md)
- Navigatie-placeholders (`<!-- VSA-NAV:… -->`): nog beschreven in
  [hugo-navigation-placeholders.md](../guides/hugo-navigation-placeholders.md)
  (toolgedrag; presentatievoorbeeld = VSA-demo)

Oudere pagina’s over de voormalige `examples/hugo-demo/` in deze repo wijzen nu
hierheen of naar VSA-demo.
