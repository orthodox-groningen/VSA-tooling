@echo off
setlocal

cd /d %~dp0\..

echo.
echo === VSA CI ===
echo.

echo [1/5] Install package and test dependencies
call scripts\bootstrap.cmd
if errorlevel 1 exit /b 1

set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"

echo.
echo [2/5] Clean generated CI output
if exist generated\ci rmdir /s /q generated\ci

echo.
echo [3/5] Run tests
"%PY%" -m pytest
if errorlevel 1 exit /b 1

echo.
echo [4/5] Validate consumer-minimal
"%PY%" -m vsa.cli validate --summary examples\consumer-minimal\content-source
if errorlevel 1 exit /b 1

echo.
echo [5/5] Build-markdown consumer-minimal
"%PY%" -m vsa.cli build-markdown examples\consumer-minimal\content-source generated\ci\content generated\ci\static\vsa
if errorlevel 1 exit /b 1

echo.
echo CI OK
echo.
