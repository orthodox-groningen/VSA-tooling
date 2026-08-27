@echo off
setlocal
cd /d %~dp0\..
call scripts\_ensure.cmd --vsa-tool --import vsa
if errorlevel 1 exit /b 1

if "%~1"=="" (
    echo Usage:
    echo.
    echo run-example path\to\example.vsa
    echo.
    exit /b 1
)

echo.
echo === Running VSA example ===
echo.
python -m vsa.cli "%~1"
echo.
exit /b %ERRORLEVEL%
