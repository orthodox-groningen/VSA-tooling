@echo off
setlocal

cd /d %~dp0\..

if not exist .venv (
    python -m venv .venv
)

call .venv\Scripts\activate

python -m pip install --upgrade pip

REM orthodox-ronl/catalogus (bron) — niet de PyPI-naamgenoot "catalogus".
if exist vendor\bron\pyproject.toml (
    pip install -e vendor\bron
) else if exist ..\bron\pyproject.toml (
    pip install -e ..\bron
) else (
    echo ERROR: bron-repo niet gevonden ^(vendor\bron of ..\bron^).
    echo catalogus moet uit orthodox-ronl/bron komen; PyPI "catalogus" is een ander package.
    exit /b 1
)

pip install -e ".[rendering]"
if errorlevel 1 exit /b 1
pip install pytest
if errorlevel 1 exit /b 1

python -c "from catalogus import ZoekContext; print('catalogus OK:', ZoekContext.__module__)"
if errorlevel 1 (
    echo ERROR: verkeerde of incomplete catalogus-installatie.
    exit /b 1
)
