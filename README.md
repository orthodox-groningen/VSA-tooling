# VSA stap 19 - validate op bestanden én mappen

Deze stap breidt `vsa validate` uit.

Voorheen:

```cmd
vsa validate bestand.md
```

Nu ook:

```cmd
vsa validate content
```

Het commando:

- accepteert een bestand of map;
- zoekt recursief naar `.md`, `.markdown` en `.vsa`;
- valideert alle gevonden bestanden;
- verzamelt alle fouten;
- geeft exitcode `0` bij alles OK;
- geeft exitcode `1` bij één of meer fouten.

Dit is belangrijk voor Hugo en GitHub Actions.
