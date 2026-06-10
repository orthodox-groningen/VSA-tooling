# VSA stap 15 - scope-grid rendering

Deze stap verbetert de SVG-renderer.

Nieuw:

- elke `ScopeNode` krijgt een intern grid;
- samengestelde hoogte-modifiers worden per kolom gerenderd;
- samengestelde lengte-modifiers worden per kolom gerenderd;
- ontbrekende modifiers worden visueel aangevuld met `~`;
- melisma's krijgen daardoor betere horizontale spreiding.

Voorbeeld:

```text
{/&\&/tekst_&~&~}
```

wordt intern:

```text
kolom 1: /   _
kolom 2: \   ~
kolom 3: /   ~
```

Nog niet perfect:

- tekstbreedte wordt nog geschat;
- echte fontmeting komt later;
- regelafbreking is nog niet aanwezig.
