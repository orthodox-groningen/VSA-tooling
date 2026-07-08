# Volgende stap na stap 39

Sluit de validatieconfig aan op de CLI.

Doel:

```cmd
vsa --config vsa.toml validate bestand.vsa
```

waarbij `validate` dezelfde severity-overrides gebruikt als:

```python
validate_file(path, config=config)
```
