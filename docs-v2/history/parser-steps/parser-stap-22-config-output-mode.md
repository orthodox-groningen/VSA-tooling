# Stap 22 - output-mode in vsa.toml

Deze stap voegt toe:

```toml
[hugo]
output-mode = "img"
```

of:

```toml
[hugo]
output-mode = "shortcode"
```

## Voorrang

```text
--output-mode
  ↓
vsa.toml
  ↓
default img
```

Hiermee kun je per project kiezen of de gegenereerde Markdown `<img>` gebruikt of Hugo-shortcodes.
