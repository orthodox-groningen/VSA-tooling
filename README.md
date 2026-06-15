# Stap 67 - script path fix

Fix voor:

```text
ModuleNotFoundError: No module named 'vsa'
```

Het script `update-spacing-diagnostics-metadata.py` voegt nu zelf `src` toe aan `sys.path`, zodat het vanuit de repo-root werkt.
