# TODO addendum stap 76

Toevoegen aan `docs/todo.md` onder demo-site/build pipeline:

## Primaire SVG-generatie padbewust maken

Status: `Open`

Stap 76 regenereert ontbrekende SVG's als herstelstap.

Later moet de primaire pipeline zelf:

- route/stem uit het actuele relatieve content-source pad afleiden;
- dezelfde stem gebruiken voor Markdown HTML img refs en SVG-bestandsnamen;
- nested directories ondersteunen;
- geen oude `voorbeelden-praktijk-*` assets meer nodig hebben voor nieuwe praktijkroutes.
