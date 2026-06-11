# Hugo demo praktijk layout fallback fix

Deze overlay pakt twee mogelijke oorzaken aan:

1. `voorbeelden/praktijk.md` botst met `voorbeelden/praktijk/`.
2. Hugo gebruikt geen passende list-template, waardoor `<main class="page"></main>` leeg blijft.

## Na uitpakken

```cmd
scripts\fix-praktijk-navigation.cmd
scripts\build-hugo.cmd
scripts\serve-hugo.cmd
```

## Debug

```cmd
scripts\debug-praktijk-navigation.cmd
```
