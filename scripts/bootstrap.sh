#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python -m pip install --upgrade pip

if [[ -f vendor/bron/pyproject.toml ]]; then
  python -m pip install -e vendor/bron
elif [[ -f ../bron/pyproject.toml ]]; then
  python -m pip install -e ../bron
fi

python -m pip install -e .
python -m pip install pytest
