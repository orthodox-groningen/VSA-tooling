# Stap 34 - test en link fix

Deze patch herstelt regressies door de subpad-veilige linkwijziging.

## Block parser

Metadata werkt opnieuw voor:

```text
do="C4"
mode="minor"
```

en defaults via:

```python
effective_metadata()
```

## Tests

Tests verwachten niet langer root-absolute links zoals:

```text
/voorbeelden/basis/
```

maar controleren op subpad-veilige Hugo-oplossingen:

```text
relURL
voorbeelden/basis/
```
