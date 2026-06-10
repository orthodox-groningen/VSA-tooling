# VSA stap 20 - projectconfiguratie

Deze stap voegt `vsa.toml` ondersteuning toe.

Doel:

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content generated\static\vsa
```

kan defaults gebruiken uit:

```toml
[rendering]
max-line-width = 700

[hugo]
assets-url-prefix = "/vsa"
```

CLI-opties blijven voorrang houden.

## Config zoeken

De tool zoekt standaard naar:

```text
vsa.toml
```

in de huidige werkmap.

Je kunt ook expliciet een configbestand meegeven:

```cmd
vsa build-markdown ... --config vsa.toml
```
