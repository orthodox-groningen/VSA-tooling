# VSA-tooling gebruiken vanuit andere repositories

## Direct met `pip`

In een andere repository kan de tool rechtstreeks vanaf GitHub worden geïnstalleerd:

```cmd
python -m pip install "vsa-tool[rendering] @ git+https://github.com/orthodox-groningen/VSA-tooling.git@main"
```

Daarna is het commando beschikbaar:

```cmd
vsa --version
vsa validate content
vsa svg input.vsa output.svg
```

Voor Markdown + SVG-generatie:

```cmd
vsa build-markdown content generated\content generated\static\vsa --assets-url-prefix /vsa
```

## In GitHub Actions

Een andere repository kan de herbruikbare workflow aanroepen:

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

De workflow valideert de VSA-bronnen en uploadt de gegenereerde Markdown/SVG als artifact.

## GitHub Pages deploy

Na een lokale site-build (Hugo, MkDocs, …) upload je het artifact en roep je de
herbruikbare deploy-workflow aan. Die draait `check-publication-output.py` (tenzij
overgeslagen) en pusht via `peaceiris/actions-gh-pages@v3` naar `gh-pages`.

**Repo-instelling:** Settings → Pages → Deploy from a branch → `gh-pages` → `/` (niet
"GitHub Actions").

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

Referentie-implementatie in deze repo: `pages-preview.yml` en `pages-demo.yml`.

## Aanbevolen vervolg

Voor productiegebruik is een getagde versie beter dan `@main`, bijvoorbeeld:

```text
@v0.1.0
```
