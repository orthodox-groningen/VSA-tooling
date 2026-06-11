# Stap 40 - CLI version import fix

De vorige patch gebruikte:

```python
from .version import __version__
```

Maar `src/vsa/version.py` bestaat niet.

De CLI gebruikt nu:

```python
importlib.metadata.version("vsa-tool")
```

met fallback:

```text
0.1.0
```
