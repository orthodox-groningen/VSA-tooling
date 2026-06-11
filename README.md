# VSA stap 34 - test en link fix

Deze patch herstelt de fouten na de responsive/subpad-fix.

## Opgelost

1. `block_parser` ondersteunt opnieuw:
   - default metadata via `effective_metadata()`;
   - metadataregels zoals `do="C4"`.

2. CLI-demo-subpagina's gebruiken relatieve links.

3. Tests zijn aangepast aan subpad-veilige Hugo-links:
   - `relURL` in templates;
   - geen harde `/voorbeelden/...` links;
   - CSS via `relURL`.
