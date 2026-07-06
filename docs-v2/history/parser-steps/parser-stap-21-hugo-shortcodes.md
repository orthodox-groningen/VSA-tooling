# Stap 21 - Hugo shortcodes

Deze stap voegt shortcode-output toe.

## Output modes

### img

```html
<img src="/vsa/demo.svg">
```

### shortcode

```go-html-template
{{< vsa src="/vsa/demo.svg" >}}
```

## Waarom shortcodes?

Shortcodes maken het makkelijker om:

- centrale styling toe te passen;
- responsive gedrag toe te voegen;
- lazy loading toe te voegen;
- toekomstige interactieve rendering te ondersteunen.
