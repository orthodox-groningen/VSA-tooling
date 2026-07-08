# Stap 65 - DejaVu font policy

Deze stap standaardiseert het renderfontbeleid rond DejaVu Sans.

## Default

```text
DejaVu Sans
```

## Preferred project-local path

```text
assets/fonts/DejaVuSans.ttf
```

## Fallbacks

- Linux DejaVu Sans paths;
- Windows `C:\Windows\Fonts\DejaVuSans.ttf`, als aanwezig;
- Arial;
- Segoe UI;
- estimator fallback.

## Licentie

Als `DejaVuSans.ttf` in de repo wordt opgenomen, moet de complete upstream licentie
worden opgenomen in:

```text
licenses/DejaVu-Fonts.txt
```

Deze patch levert bewust geen `.ttf` mee.
