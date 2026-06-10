# VSA stap 5 - validate commando

Deze stap voegt een eerste echt bruikbaar validatiecommando toe:

```cmd
vsa validate bestand.md
```

Het commando:

- herkent Markdownbestanden met `::: vsa-notatie`;
- herkent losse `.vsa` bestanden;
- parseert VSA-inhoud;
- voert semantische validatie uit;
- toont fouten;
- geeft exitcode `0` bij OK;
- geeft exitcode `1` bij fouten.
