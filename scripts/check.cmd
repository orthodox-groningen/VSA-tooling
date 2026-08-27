@echo off
setlocal
cd /d %~dp0\..
echo.
echo === VSA check (CI-spiegel) ===
echo.
call scripts\_ensure.cmd --catalogus --vsa-tool --pip-e ".[dev,rendering]" --import vsa --import pytest --import PIL
if errorlevel 1 exit /b 1

if exist generated\ci rmdir /s /q generated\ci

python -m pytest
if errorlevel 1 exit /b 1

python -m vsa.cli validate --summary examples\consumer-minimal\content-source
if errorlevel 1 exit /b 1

python -m vsa.cli build-markdown examples\consumer-minimal\content-source generated\ci\content generated\ci\static\vsa
if errorlevel 1 exit /b 1

echo.
echo Check OK
echo.
exit /b 0
