# TODO addendum stap 72

Toevoegen aan `docs/todo.md` onder demo-site:

## SVG asset-referenties bij nested content

Status: `In uitvoering`

Controleer dat voor pagina's in subdirectories:

- gegenereerde SVG-bestandsnaam het volledige relatieve pad gebruikt;
- HTML `<img src="/vsa/...">` naar exact die SVG verwijst;
- weekdagen/praktijkvoorbeelden niet naar sibling- of parent-assets verwijzen;
- build-tests dit structureel controleren.
