# Stap 90 - stop build-hugo mutators

Probleem:

Oude apply-scripts herschrijven `scripts\build-hugo.cmd` en voegen regels in midden in het `hugo ^` blok.

Deze stap:

- zet `scripts\build-hugo.cmd` schoon terug;
- deactiveert oude mutators:
  - `apply-step76-regenerate-missing-vsa-images.py`
  - `apply-step84-hugo-link-asset-checker.py`
  - `apply-step86-clean-build-regenerate-check.py`
- past tests aan zodat ze niet meer verwachten dat deze scripts `build-hugo.cmd` muteren.
