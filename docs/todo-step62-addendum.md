# TODO addendum stap 62

Toevoegen aan `docs/todo.md` onder SVG-rendering:

## Echte tekstmeting / font metrics

Status: `Open`

Stap 62 gebruikt een betere maar nog steeds geschatte tekstmeting.

Later onderzoeken:

- Pillow/fonttools;
- browser-compatible SVG text measurement;
- cachebare metrics per font/fontsize;
- exacte width-engine voor:
  - wrapping;
  - SVG rendering;
  - scope layout;
  - filler-lines.

Doel:

- geen overlap;
- stabiele spacing;
- voorspelbare line-breaks.
