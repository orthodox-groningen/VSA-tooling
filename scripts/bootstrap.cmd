@echo off
setlocal

cd /d %~dp0\..

echo.
echo === VSA Tooling bootstrap ===
echo.

if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

call .venv\Scripts\activate

echo.
echo Installing/updating pip...
python -m pip install --upgrade pip

echo.
echo Installing project in editable mode...
pip install -e .

echo.
echo Installing pytest...
pip install pytest

echo.
echo Bootstrap completed.
echo.
