@echo off
setlocal

cd /d %~dp0\..

call .venv\Scripts\activate

echo.
echo === Running verbose tests ===
echo.

python -m pytest -v -s

echo.
