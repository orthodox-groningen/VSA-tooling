@echo off
setlocal

cd /d %~dp0\..

echo.
echo === VSA CI ===
echo.

echo [1/4] Clean generated CI output
if exist generated\ci rmdir /s /q generated\ci

echo.
echo [2/4] Run tests
python -m pytest
if errorlevel 1 exit /b 1

echo.
echo [3/4] Validate demo content
vsa validate examples\hugo-demo\content-source\zondag\toon-1.md
if errorlevel 1 exit /b 1

echo.
echo [4/4] Build demo markdown
vsa build-markdown examples\hugo-demo\content-source generated\ci\content generated\ci\static\vsa
if errorlevel 1 exit /b 1

echo.
echo CI OK
echo.
