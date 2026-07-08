
# Stap 88 - herstel `build-hugo.cmd`

## Probleem

Een eerdere patch voegde regels in midden in een CMD-regelcontinuatie:

```cmd
hugo ^
python scripts\...
  --source ...
```

Daardoor zag Hugo `python` als subcommand en werden `--source` enzovoort losse CMD-commando's.

## Herstel

`build-hugo.cmd` is volledig vervangen door een schone versie.

De linkchecker wordt voorlopig handmatig gedraaid:

```cmd
python scripts\check-hugo-links-and-assets.py
```
