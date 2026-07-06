# Stap 38 - config output-mode regressiefix

Stap 38 verving `config.py` en verloor daardoor bestaande validatie op:

```toml
[hugo]
output-mode = "..."
```

Deze patch herstelt:

```text
img
shortcode
```

als enige geldige waarden.

Onbekende waarden geven weer:

```text
ValueError
```
