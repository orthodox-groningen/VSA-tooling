# Stap 83 - stop muterende workflow-tests

Probleem:

`build-hugo.cmd` draait de test-suite. Sommige tests voerden `apply-step*.py` scripts uit.
Daardoor werden echte repo-bestanden aangepast tijdens tests, o.a.:

```text
.github\workflows\*.yml
```

Dat veroorzaakte steeds extra lege regels in workflow-bestanden.

Oplossing:

- stap-70 test voert het apply-script niet meer uit op de echte repo;
- test alleen nog de pure patchfunctie op tekst;
- workflow YAML-bestanden kunnen eenmalig opgeschoond worden.
