# Stap 87 - legacy Hugo-routes verbergen

De linkchecker vond oude routes zoals:

```text
/voorbeelden/praktijk/...
/zondag/...
```

Deze links stonden niet letterlijk in `content-source`. Ze ontstonden doordat Hugo oude content nog als gewone pagina's publiceerde.

Oplossing:

```yaml
draft: true
vsa_nav_exclude: true
```

Script:

```cmd
python scripts\hide-legacy-hugo-routes.py
```
