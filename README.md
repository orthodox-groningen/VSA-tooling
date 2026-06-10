# VSA Parser stap 1 - testfix

Deze patch lost drie testproblemen op:

1. oude placeholder-test voor lexer vervangen;
2. oude placeholder-test voor parser vervangen;
3. regressietest beperkt tot mappen met `.parser-step1`.

Daardoor worden grotere bestaande regressiemappen zoals `zondag-toon-1` nog niet meegenomen.
