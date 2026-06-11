# Stap 36 - compatibele pitch-marker eindcontrole

De eerdere stap 36 paste niet bij de bestaande validator-architectuur.

Bestaande code gebruikt:

```python
SemanticValidator(document).validate()
```

en verwacht:

```python
diagnostics.items
```

Deze patch behoudt die API.

## Nieuwe foutcodes

```text
VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
```

## Ongeldig

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

```text
[:] {/Hei_}{/lig_} is de Heer.
```

## Geldig

```text
[:] {/Hei_}{/lig_} is de Heer. [\\:]
```
