# Stap 36 - semantic validator import fix

De vorige stap introduceerde:

```python
from .ast import DocumentNode, PitchMarkerNode, ScopeNode
```

Maar `DocumentNode` bestaat niet in deze repo.

De validator gebruikt nu geen directe AST-class imports meer.

In plaats daarvan kijkt hij naar:

```python
type(node).__name__
```

en naar bestaande node-eigenschappen zoals:

```python
height_modifier
length_modifier
text
```

Daardoor blijft de validator minder kwetsbaar voor kleine naamverschillen in de AST-implementatie.
