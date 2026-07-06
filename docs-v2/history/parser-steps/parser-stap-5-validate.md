# Parser stap 5 - validate commando

Deze stap introduceert:

```cmd
vsa validate bestand.md
```

Bij geldige invoer:

```text
OK
```

Bij fouten:

```text
bestand.md:blok-1:1:1: VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH: Hoogte- en lengte-modifier bevatten niet hetzelfde aantal muzikale posities.
```

## Exitcodes

```text
0 = geldig
1 = fout
```
