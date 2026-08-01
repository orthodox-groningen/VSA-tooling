# Recovered docs — afgerond

Staging na delete-commit `9ff66f94` (2026-07-08).

## Wat er gebeurd is

1. Inventaris: 229 verwijderd → 35 echt weg + archief-extra.
2. Categorie A (doublures / al in `specification/` of **bron**) verwijderd uit de tree.
3. Categorie B herplaatst:
   - `docs/guides/` — user-guide, musicxml-export, reuse, parochie-lokaal-vsa, hugo-*, liturgikon, testing, tev2
   - `docs/plans/` — polyphony-voorstel, uitgaveprofielen
   - `docs/history/process/` — AI-REVIEW-PROMPT

## Terughalen van categorie A (git)

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
git show 9ff66f94^:docs/spec/vsa-spec-v1.0.1.md
```

Zie ook [RELOCATION-PROPOSAL.md](RELOCATION-PROPOSAL.md) (uitgevoerd; paden naar `docs/plans/` i.p.v. `history/proposals`).
