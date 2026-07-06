# Stap 77 - path normalization fix

`regenerate-missing-vsa-images.py` werkte goed vanuit de echte build,
maar de tests gaven relatieve paden door.

Fix:

```python
html = normalize_path(html)
rel = html.relative_to(PUBLIC.resolve())
```

Daarmee werken relatieve én absolute paden.
