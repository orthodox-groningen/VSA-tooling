# Stap 39 - validation config integration

Deze stap sluit severity-overrides aan op de validatielaag.

## Nieuw

```python
config = load_config("vsa.toml")

validate_file("bestand.vsa", config=config)
validate_path("map", config=config)
```

## Config

```toml
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
```

## Gedrag

Zonder config:

```text
semantic diagnostics = error
```

Met override:

```text
specifieke code = warning
```

## Nog niet

CLI-integratie is nog niet gedaan.

Dus dit werkt nog niet automatisch via:

```cmd
vsa --config vsa.toml validate ...
```

Dat is de volgende stap.
