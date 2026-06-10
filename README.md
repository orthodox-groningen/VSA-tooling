# VSA stap 13 - testfix

Deze patch past een oude SVG-test aan.

De oude test verwachtte nog dat `_` letterlijk in de SVG stond.
Sinds stap 13 wordt `_` als echte SVG-lijn gerenderd.

Daarom controleert de test nu op `<line>` in plaats van op `_`.
