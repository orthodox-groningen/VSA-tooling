@echo off
setlocal
cd /d %~dp0\..
set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"
echo.
echo === Build production candidate ===
echo.
if exist generated\production rmdir /s /q generated\production
if exist examples\hugo-demo\static\vsa rmdir /s /q examples\hugo-demo\static\vsa
"%PY%" -m vsa.cli validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1
"%PY%" scripts\assert-real-font-metrics.py
if errorlevel 1 exit /b 1
"%PY%" -m vsa.cli build-markdown ^
  examples\hugo-demo\content-source ^
  generated\production\content ^
  examples\hugo-demo\static\vsa ^
  --max-line-width 900 ^
  --output-mode shortcode
if errorlevel 1 exit /b 1
"%PY%" scripts\update-nav-placeholders.py generated\production\content
if errorlevel 1 exit /b 1
"%PY%" scripts\update-spacing-diagnostics-metadata.py generated\production\content\voorbeelden\rendering\spacing-diagnostiek.md
if errorlevel 1 exit /b 1
hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\production\content ^
  --destination ..\..\generated\production\site ^
  --baseURL / ^
  --minify
if errorlevel 1 exit /b 1
echo.
echo Production candidate build OK:
echo generated\production\site
echo.
