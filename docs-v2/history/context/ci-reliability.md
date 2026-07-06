# CI-betrouwbaarheid (VSA-tooling)

Spiegel van [docs/architecture/ci-reliability.md](../../../docs/architecture/ci-reliability.md).

Kernpunten:

- Validatie: `vsa-ci.yml` (Windows) + `site-build.yml` (Linux).
- Preview: `pages-preview.yml` op elke push (alle branches).
- Verwijderde dubbele workflows: `python-tests.yml`, `hugo-demo.yml`, `build-artifacts.yml`, `build-target.yml`, `hugo.yml`.
