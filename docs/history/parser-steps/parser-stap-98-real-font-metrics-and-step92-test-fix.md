# Stap 98 - real font metrics afdwingen + stap 92 test fix

`build-hugo.cmd` gebruikt `.venv\Scripts\python.exe` als die bestaat.

Na `update-spacing-diagnostics-metadata.py` draait:

```cmd
scripts\assert-real-font-metrics.py
```

Als real metrics niet actief zijn, stopt de build.

De stap-92 test is aangepast aan de huidige formulering: `_` is geen EHM.
