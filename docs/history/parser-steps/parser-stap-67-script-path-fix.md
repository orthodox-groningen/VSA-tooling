# Stap 67 - script path fix

`update-spacing-diagnostics-metadata.py` werd soms uitgevoerd met globale Python.
Dan was `src/vsa` niet importeerbaar.

Het script voegt nu zelf `src` toe aan `sys.path`.
