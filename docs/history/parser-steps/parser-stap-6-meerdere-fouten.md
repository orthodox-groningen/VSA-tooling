# Parser stap 6 - meerdere fouten

Deze stap maakt `vsa validate` geschikter voor echt gebruik.

Voorbeeld:

```text
{}
{te kst}
tekst}
{open
```

leidt niet meer tot alleen de eerste fout, maar tot een lijst.

## Pipeline

```text
RecoverableSyntaxValidator
  ↓
alle syntaxdiagnostics verzamelen
  ↓
alleen bij syntax OK:
Parser
  ↓
SemanticValidator
```

Semantische validatie kan meerdere fouten verzamelen zolang de AST geldig is.

## Waarom syntax eerst?

Bij syntaxfouten is de AST mogelijk onbetrouwbaar. Daarom wordt semantische validatie pas uitgevoerd wanneer de syntaxscan geen errors heeft.
