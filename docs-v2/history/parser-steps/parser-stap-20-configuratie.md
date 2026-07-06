# Stap 20 - projectconfiguratie

Deze stap introduceert:

```text
vsa.toml
```

Voorbeeld:

```toml
[rendering]
max-line-width = 800

[hugo]
assets-url-prefix = "/vsa"
```

## Voorrang

```text
CLI-opties
  ↓
vsa.toml
  ↓
interne defaults
```

Dus dit overschrijft de config:

```cmd
vsa svg input.vsa output.svg --max-line-width 600
```

## Waarom

Voor Hugo en CI wil je stabiele projectinstellingen die niet in elk script herhaald hoeven te worden.
