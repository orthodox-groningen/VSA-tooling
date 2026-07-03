@echo off
setlocal

cd /d %~dp0\..

if not exist .venv (
    python -m venv .venv
)

call .venv\Scripts\activate

python -m pip install --upgrade pip

if exist vendor\bron\pyproject.toml (
    pip install -e vendor\bron
) else if exist ..\bron\pyproject.toml (
    pip install -e ..\bron
)

pip install -e .
pip install pytest
