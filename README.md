# VSA stap 22 - output-mode in vsa.toml

Deze stap breidt `vsa.toml` uit.

Nieuw:

```toml
[hugo]
assets-url-prefix = "/vsa"
output-mode = "img"
```

Mogelijke waarden:

```text
img
shortcode
```

Voorrang:

```text
CLI-optie --output-mode
  ↓
vsa.toml
  ↓
default: img
```

Voor Hugo kun je dus instellen:

```toml
[hugo]
output-mode = "shortcode"
```
