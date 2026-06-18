# Stap 89 - clean build artifacts

## Probleem

Oude routes bleven verschijnen doordat generated output niet volledig werd opgeschoond vóór een nieuwe Hugo-build.

Daarnaast was `build-hugo.cmd` kwetsbaar voor patchscripts die regels midden in een `hugo ^` blok invoegden.

## Oplossing

`build-hugo.cmd` is opnieuw compact gemaakt en gebruikt nu:

```cmd
python scripts\clean-hugo-build-artifacts.py
```

De build maakt eerst `generated\site` en kopieert daarna dezelfde output naar:

```text
examples\hugo-demo\public
```

zodat de linkchecker daar handmatig op kan blijven draaien.
