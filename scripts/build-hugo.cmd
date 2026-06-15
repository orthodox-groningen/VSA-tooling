@echo off
setlocal

cd /d %~dp0\..

call .venv\Scripts\activate

echo.
echo === VSA + Hugo build ===
echo.

echo [1/4] Validate content
vsa validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1

echo.
echo [2/4] Generate Markdown + SVG
python scripts\update-spacing-diagnostics-metadata.py
vsa build-markdown ^
  examples\hugo-demo\content-source ^
  generated\hugo\content ^
  generated\hugo\static\vsa
if errorlevel 1 exit /b 1

echo.
echo [3/4] Run tests
python -m pytest
if errorlevel 1 exit /b 1

echo.
echo [4/4] Build Hugo site
hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\hugo\content ^
  --destination ..\..\generated\site
if errorlevel 1 exit /b 1

echo.
echo Build complete
echo.
