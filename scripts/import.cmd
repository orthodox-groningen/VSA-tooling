@echo off
cls
setlocal
cd /d "%~dp0\.."
call scripts\_ensure.cmd --vsa-tool --import vsa
if errorlevel 1 exit /b 1

echo %CD%^> %0 %1
echo.

if "%~1"=="" (
    echo Gebruik: import ^<zipfile^>
    exit /b 1
)

if not exist "%USERPROFILE%\Downloads\%~1" (
    echo Bestand "%USERPROFILE%\Downloads\%~1" niet gevonden.
    exit /b 1
)

tar -xf "%USERPROFILE%\Downloads\%~1" -C "."
