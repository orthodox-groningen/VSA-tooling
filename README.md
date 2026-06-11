# Stap 36 - site-demo ending fix

Deze patch herstelt de laatste falende test.

Probleem:

```text
examples\site-demo\zondag\toon-1.md
```

bevatte nog:

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

Dat is sinds stap 36 semantisch ongeldig.

Fix:

```text
[:] {/Hei_}{/lig_} is de Heer. [\\:]
```
