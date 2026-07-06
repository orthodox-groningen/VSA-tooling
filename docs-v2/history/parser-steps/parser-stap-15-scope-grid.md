# Stap 15 - scope-grid rendering

Deze stap maakt de SVG-renderer meer in lijn met het VSA-gridmodel.

Een scope wordt niet langer behandeld als één los tekstblok met één modifierlaag, maar als:

```text
bovenrij     EHM per kolom
tekstlaag    zangelement
onderrij     ELM per kolom
```

Voorbeeld:

```text
{/&\&/tekst_&~&~}
```

wordt:

```text
kolom 1: /   _
kolom 2: \   ~
kolom 3: /   ~
```

Dit is belangrijk voor melisma's en samengestelde modifiers.
