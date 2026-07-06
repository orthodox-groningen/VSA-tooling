# Stap 70 - CI rendering fonts OS guard

GitHub Actions faalde omdat Linux-only fontinstallatie ook op Windows runners draaide.

Fout:

```text
sudo apt-get update && sudo apt-get install -y fonts-dejavu-core
```

Windows heeft geen `sudo`.

## Fix

Alle `Install rendering fonts` stappen krijgen:

```yaml
if: runner.os == 'Linux'
```

## Script

```cmd
python scripts\apply-step70-ci-rendering-fonts-os-guard.py
```

## Tests

```cmd
python -m pytest tests\test_step70_ci_rendering_fonts_os_guard.py -v
```
