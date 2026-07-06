# Stap 37 - optie A: semantiek blijft error

We behouden de severity-infrastructuur, maar zetten semantische diagnostics voorlopig terug op `error`.

## Waarom

De bestaande toolchain verwacht:

```text
semantische fout → validate faalt → process stopt
```

Dat geldt voor:

- `validate_path`;
- `process_markdown`;
- `ProcessValidationError`;
- CI;
- expected-fail tests.

## Wat blijft nieuw

Diagnostics hebben nu wel een veld:

```text
severity
```

en de infrastructuur kent:

```python
has_warnings()
has_fatal_errors()
```

## Later

Een volgende stap kan configuratie toevoegen:

```toml
[vsa.validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
```

Maar standaard blijft semantiek voorlopig hard.
