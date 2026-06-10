@echo off
setlocal

cd /d %~dp0\..

if "%~1"=="" (
    echo Usage:
    echo.
    echo scripts\run-example.cmd path\to\example.vsa
    echo.
    exit /b 1
)

call .venv\Scripts\activate

echo.
echo === Running VSA example ===
echo.

python -m vsa.cli "%~1"

echo.
