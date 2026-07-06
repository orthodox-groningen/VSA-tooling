# CI pytest fix

GitHub Actions gaf:

```text
No module named pytest
```

Daarom installeert `scripts\\ci.cmd` nu zelf:

```cmd
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest
```

Daarmee is `ci.cmd` zelfstandig bruikbaar:

```cmd
scripts\\ci.cmd
```

zowel lokaal als in GitHub Actions.
