@echo off
setlocal
cd /d %~dp0\..
set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"
echo.
echo === VSA + Hugo local preview ===
echo.
echo [1/2] Generate Markdown + SVG
if exist generated\hugo\content rmdir /s /q generated\hugo\content
if exist examples\hugo-demo\static\vsa rmdir /s /q examples\hugo-demo\static\vsa
"%PY%" scripts\assert-real-font-metrics.py
if errorlevel 1 exit /b 1
"%PY%" -m vsa.cli build-markdown ^
  examples\hugo-demo\content-source ^
  generated\hugo\content ^
  examples\hugo-demo\static\vsa ^
  --output-mode shortcode
if errorlevel 1 exit /b 1
"%PY%" -m vsa.cli musicxml ^
  examples\hugo-demo\content-source ^
  examples\hugo-demo\static\vsa\mxl
if errorlevel 1 exit /b 1
"%PY%" scripts\update-nav-placeholders.py generated\hugo\content
if errorlevel 1 exit /b 1
"%PY%" scripts\update-spacing-diagnostics-metadata.py generated\hugo\content\voorbeelden\rendering\spacing-diagnostiek.md
if errorlevel 1 exit /b 1
echo.
echo [2/2] Start Hugo server
hugo server ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\hugo\content ^
  --baseURL / ^
  --disableFastRender ^
  --forceSyncStatic ^
  --noHTTPCache
