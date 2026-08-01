# Verouderde eenmalige scripts

Deze scripts waren eenmalige migratie-/patchscripts en mogen geen broncontent meer
wijzigen. Ze zijn uit `scripts/` verwijderd (fase-4-opruiming).

Om ze opnieuw te wissen als ze ergens terugkomen:

```cmd
scripts\remove-obsolete-scripts.cmd
```

## Verwijderd (historisch)

- `apply-step51-force.py` … `apply-step86-*.py` (eenmalige stap-patches)
- `apply-step68-todo-and-navigation.py` / `revert-step68-navigation.py`
- `stabilize-hugo-navigation.py`, `hide-legacy-hugo-routes.py`, …
- `fix-praktijk-navigation.cmd`, `debug-praktijk-navigation.cmd`
- `retry.cmd` — gebruik `scripts\test.cmd`

Geschiedenis: zie `docs/history/parser-steps/`.
