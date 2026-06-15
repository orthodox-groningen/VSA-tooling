# Rendering fonts

## Default font

VSA uses **DejaVu Sans** as the default SVG rendering font.

Preferred project-local font path:

```text
assets/fonts/DejaVuSans.ttf
```

## Real font metrics

VSA uses Pillow for real font measurement when available.

Dependency:

```text
Pillow>=10.0
```

Install locally:

```cmd
python -m pip install -r requirements-rendering.txt
```

or:

```cmd
scripts\install-rendering-deps.cmd
```

Check the active backend:

```cmd
python scripts\debug-font-metrics.py
```

Expected when everything works:

```text
backend      : pillow
real metrics : True
```

## GitHub Actions

GitHub Pages serves static HTML/SVG only. Python/Pillow must run during the build
that generates the SVG files.

For Ubuntu-based GitHub Actions builds:

```yaml
- name: Install rendering fonts
  run: sudo apt-get update && sudo apt-get install -y fonts-dejavu-core

- name: Install rendering dependencies
  run: python -m pip install -r requirements-rendering.txt
```

## Reproducibility

Best result:

1. commit `assets/fonts/DejaVuSans.ttf`;
2. include the full DejaVu license in `licenses/DejaVu-Fonts.txt`;
3. use the same font locally and in CI;
4. verify with `scripts/debug-font-metrics.py`.

## Fallbacks

If Pillow or DejaVu Sans is unavailable, VSA falls back to the internal estimator.
That keeps builds working, but visual spacing may differ.
