#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python -m pip install --upgrade pip

# orthodox-groningen/catalogus (bron) — niet de PyPI-naamgenoot "catalogus".
if [[ -f vendor/bron/pyproject.toml ]]; then
  python -m pip install -e vendor/bron
elif [[ -f ../bron/pyproject.toml ]]; then
  python -m pip install -e ../bron
else
  echo "ERROR: bron-repo niet gevonden (vendor/bron of ../bron)."
  echo "catalogus moet uit orthodox-groningen/bron komen; PyPI \"catalogus\" is een ander package."
  exit 1
fi

python -m pip install -e ".[rendering]"
python -m pip install pytest

python -c "from catalogus import ZoekContext; print('catalogus OK:', ZoekContext.__module__)"
