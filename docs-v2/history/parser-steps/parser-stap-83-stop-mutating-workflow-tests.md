# Stap 83 - stop muterende workflow-tests

## Probleem

`build-hugo.cmd` draait de test-suite.

Een aantal tests voerde apply-scripts uit die echte bestanden in de repo aanpassen.
Dat is gevaarlijk, omdat een gewone test-run dan de working tree vervuilt.

Voorbeeld:

```text
.github\workflows\*.yml
```

kreeg bij herhaalde runs steeds extra lege regels.

## Besluit

Tests mogen geen `apply-step*.py` scripts op de echte repo uitvoeren.

Wel toegestaan:

- pure functies testen;
- tijdelijke bestanden gebruiken;
- scripts alleen statisch inspecteren.

## Herstel

```cmd
python scripts\normalize-workflow-yaml-whitespace.py
```

ruimt overtollige lege regels in workflow YAML-bestanden op.
