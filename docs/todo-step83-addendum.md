# TODO addendum stap 83

Toevoegen aan `docs/todo.md` onder test/CI:

## Tests mogen working tree niet muteren

Status: `In uitvoering`

Regel:

- tests mogen geen apply-scripts op de echte repo uitvoeren;
- tests gebruiken pure functies of tijdelijke mappen;
- build-hugo mag na een schone checkout geen gewijzigde `.github\workflows` opleveren.

Controle:

```cmd
python scripts\normalize-workflow-yaml-whitespace.py
python -m pytest tests\test_no_mutating_apply_scripts_in_tests.py -v
```
