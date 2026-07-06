@echo off
cls
setlocal

cd /d "%~dp0\.."

echo %CD%^> %0 %1
echo.

call ".venv\Scripts\activate"

if "%~1"=="" (
    echo Gebruik: import ^<zipfile^>
    exit /b 1
)

if not exist "%USERPROFILE%\Downloads\%~1" (
    echo Bestand "%USERPROFILE%\Downloads\%~1" niet gevonden.
    exit /b 1
)

tar -xf "%USERPROFILE%\Downloads\%~1" -C "."