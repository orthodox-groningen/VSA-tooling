# Stap 66 - Pillow dependency en CI font setup

Deze stap maakt Pillow expliciet als rendering dependency.

## Toegevoegd

- `requirements-rendering.txt`
- `scripts/install-rendering-deps.cmd`
- `scripts/apply-step66-pillow-dependency-ci.py`
- tests voor dependency/documentatie

## CI

GitHub Actions moet:

```yaml
- name: Install rendering fonts
  run: sudo apt-get update && sudo apt-get install -y fonts-dejavu-core

- name: Install rendering dependencies
  run: python -m pip install -r requirements-rendering.txt
```

## Lokaal

```cmd
scripts\install-rendering-deps.cmd
python scripts\debug-font-metrics.py
```
