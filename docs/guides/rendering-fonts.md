# Rendering-fonts

Deze pagina beschrijft de gebruikerskant van fonts bij SVG-rendering.

## Default font

De SVG-renderer gebruikt standaard DejaVu Sans.

Voorkeurspad binnen het project:

```text
assets/fonts/DejaVuSans.ttf
```

## Echte font-metrics

Voor echte fontmeting gebruikt de tool Pillow wanneer dat beschikbaar is.

Installeren:

```cmd
python -m pip install -r requirements-rendering.txt
```

Of:

```cmd
scripts\install-rendering-deps.cmd
```

Controle:

```cmd
python scripts\debug-font-metrics.py
```

Verwachte vorm:

```text
backend      : pillow
real metrics : True
```

## Reproduceerbaarheid

| Stap | Actie                                      |
| ---- | ------------------------------------------ |
| 1    | commit `assets/fonts/DejaVuSans.ttf`       |
| 2    | commit de DejaVu-licentie in `licenses/`   |
| 3    | gebruik lokaal en in CI hetzelfde font     |
| 4    | controleer met `debug-font-metrics.py`     |

## Fallback

Als Pillow of DejaVu Sans ontbreekt, valt de tool terug op een interne schatter.

Dat houdt builds werkend, maar spacing kan visueel afwijken.

## Bronnen

Gebaseerd op:

- `docs/rendering-fonts.md`
