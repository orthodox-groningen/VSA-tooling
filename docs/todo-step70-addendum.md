# TODO addendum stap 70

Toevoegen aan `docs/todo.md` onder CI/GitHub Actions:

## Platformspecifieke CI-stappen controleren

Status: `Open`

Controleer bij toekomstige workflowwijzigingen:

- Linux-commando's zoals `sudo`, `apt-get` alleen op Linux runners;
- Windows jobs gebruiken geen Linux shell aannames;
- rendering dependencies zijn platformonafhankelijk;
- fontinstallatie is reproduceerbaar op Linux en acceptabel op Windows.
