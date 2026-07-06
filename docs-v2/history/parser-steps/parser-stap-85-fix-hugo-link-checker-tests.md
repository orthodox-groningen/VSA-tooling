# Stap 85 - fix Hugo linkchecker tests

## Fixes

- `LinkRef` gebruikt `NamedTuple` in plaats van `@dataclass`.
- De testloader registreert de module in `sys.modules`.
- De oude stap-75 test verwacht geen letterlijke `img=` tekst meer.

## Reden

Onder Python 3.14 kan `@dataclass` met postponed annotations mislopen bij import via `spec.loader.exec_module()` wanneer de module niet in `sys.modules` staat.
