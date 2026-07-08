# Parser stap 3

Deze stap maakt de overgang van AST naar muzikale posities.

Voorbeeld:

```text
{/&\tekst_&_}
```

wordt:

```text
positie 1:
  ehm="/"
  elm="_"

positie 2:
  ehm="\"
  elm="_"
```

Belangrijk:

- impliciete `~` wordt toegevoegd;
- modifier-aantallen worden gecontroleerd;
- semantische validatie staat nu los van parsing.
