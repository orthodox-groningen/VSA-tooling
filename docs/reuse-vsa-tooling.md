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

## Aanbevolen vervolg

Voor productiegebruik is een getagde versie beter dan `@main`, bijvoorbeeld:

```text
@v0.1.0
```
