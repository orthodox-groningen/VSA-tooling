# Stap 21 fix - shortcode opt-in

De standaardoutput van `build-markdown` blijft `<img>`.

Shortcodes zijn opt-in:

```cmd
vsa build-markdown ... --output-mode shortcode
```

Waarom:

- bestaande tests blijven geldig;
- bestaande workflow blijft stabiel;
- Hugo-shortcodes blijven beschikbaar.
