# TODO addendum stap 66

Toevoegen aan `docs/todo.md`:

## CI font-metrics eindcontrole

Status: `Open`

Controleer vóór release:

- GitHub Actions installeert `fonts-dejavu-core`;
- GitHub Actions installeert `requirements-rendering.txt`;
- `scripts/debug-font-metrics.py` geeft in CI `backend='pillow'`;
- lokale Windows-build en CI-build gebruiken hetzelfde font;
- README vermeldt Pillow, DejaVu Sans en licentiepad;
- documentatie-eindcontrole bevat font/licentiecheck.
