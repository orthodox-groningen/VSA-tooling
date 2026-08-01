# VSA-tooling gebruiken vanuit andere repositories

Deze pagina is de **integratiehandleiding**: hoe je `vsa-tool` in een andere repo
installeert en in CI gebruikt. Volledig werkend voorbeeld:
[VSA-demo](https://github.com/orthodox-groningen/VSA-demo).

## Direct met `pip`

```cmd
python -m pip install "vsa-tool[rendering] @ git+https://github.com/orthodox-groningen/VSA-tooling.git@main"
```

Voor productie bij voorkeur een **tag** i.p.v. `@main`, bijvoorbeeld `@v0.1.0`
(wanneer die bestaat).

Daarna:

```cmd
vsa --version
vsa validate content
vsa svg input.vsa output.svg
```

Markdown + SVG:

```cmd
vsa build-markdown content generated\content generated\static\vsa --assets-url-prefix /vsa
```

Extra `[rendering]` is nodig voor SVG (Pillow + fonts in het package/repo).

## Minimale consumer-layout

```text
mijn-repo/
  content/                 # of content-source/
    voorbeeld.md           # Markdown met ::: vsa-notatie
  generated/               # build-output (niet committen)
  .github/workflows/
    render.yml             # zie hieronder
```

Geen Hugo verplicht: alleen `validate` / `svg` / `musicxml` volstaat voor
batchconversie. Hugo (of MkDocs) komt pas bij een publicatiesite — zie
[Consumer-site](../manuals/consumer-site.md).

## In GitHub Actions (render)

```yaml
name: Render VSA

on:
  push:
  workflow_dispatch:

jobs:
  vsa:
    uses: orthodox-groningen/VSA-tooling/.github/workflows/vsa-render-reusable.yml@main
    with:
      input_dir: content
      output_dir: generated/vsa/content
      assets_dir: generated/vsa/static/vsa
      assets_url_prefix: /vsa
      output_mode: img
```

De workflow valideert en uploadt gegenereerde Markdown/SVG als artifact.

## GitHub Pages deploy

Na een site-build upload je het artifact en roep je de herbruikbare
deploy-workflow aan. Die draait `check-publication-output.py` (tenzij
overgeslagen) en pusht via `peaceiris/actions-gh-pages@v3` naar `gh-pages`.

**Repo-instelling:** Settings → Pages → Deploy from a branch → `gh-pages` → `/`
(niet “GitHub Actions”).

```yaml
name: Deploy site

on:
  push:

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # … bouw naar public/ …
      - uses: actions/upload-artifact@v4
        with:
          name: pages-site
          path: public
          if-no-files-found: error

  deploy:
    needs: build
    uses: orthodox-groningen/VSA-tooling/.github/workflows/pages-deploy-reusable.yml@main
    with:
      artifact_name: pages-site
      publish_dir: site
      destination_dir: preview
      url_prefix: /mijn-repo/preview/
      pages_url: https://orthodox-groningen.github.io/mijn-repo/preview/
    permissions:
      contents: write
```

| Input                    | Verplicht            | Toelichting                                      |
| ------------------------ | -------------------- | ------------------------------------------------ |
| `artifact_name`          | ja                   | Naam van `upload-artifact` in de build-job       |
| `publish_dir`            | nee (default `site`) | Downloadpad; moet `index.html` bevatten          |
| `destination_dir`        | nee                  | `preview` voor preview; leeg voor productie-root |
| `url_prefix`             | ja                   | Publiek pad voor linkcheck, bv. `/koor/preview/` |
| `keep_files`             | nee (default `true`) | `true` als preview en productie `gh-pages` delen |
| `skip_publication_check` | nee                  | Alleen als de caller zelf al heeft gecontroleerd |
| `pages_url`              | nee                  | URL in log na deploy                             |
| `vsa_tooling_ref`        | nee (default `main`) | Ref voor check-script                            |

Productie-deploy (root van `gh-pages`, preview-map behouden):

```yaml
  deploy:
    needs: build
    uses: orthodox-groningen/VSA-tooling/.github/workflows/pages-deploy-reusable.yml@main
    with:
      artifact_name: pages-site
      publish_dir: site
      url_prefix: /mijn-repo/
      pages_url: https://orthodox-groningen.github.io/mijn-repo/
    permissions:
      contents: write
```

## Referentie-implementaties

| Repo                                                                         | Wat je ziet                       |
| ---------------------------------------------------------------------------- | --------------------------------- |
| [VSA-demo](https://github.com/orthodox-groningen/VSA-demo)                   | Volledige Hugo-consumer + Pages   |
| Deze repo `docs-pages.yml`                                                   | MkDocs tool-docs op Pages         |
| [bron docs-pages](https://github.com/orthodox-groningen/bron)                | MkDocs + dezelfde deploy-reusable |

## Org-grenzen (D1)

Installeer de tool hier; **dupliceer geen** org-specs. Terminologie en
zangstuk-formaat: [bron — specs](https://orthodox-groningen.github.io/bron/specs/).
