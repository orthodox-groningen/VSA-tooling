@echo off
setlocal
cd /d %~dp0\..
set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"
echo.
echo === Build preview ===
echo.
if exist generated\preview rmdir /s /q generated\preview
if exist examples\hugo-demo\static\vsa rmdir /s /q examples\hugo-demo\static\vsa
"%PY%" -m vsa.cli validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1
"%PY%" scripts\assert-real-font-metrics.py
if errorlevel 1 exit /b 1
"%PY%" -m vsa.cli build-markdown ^
  examples\hugo-demo\content-source ^
  generated\preview\content ^
  examples\hugo-demo\static\vsa ^
  --output-mode shortcode
if errorlevel 1 exit /b 1
"%PY%" -m vsa.cli musicxml ^
  examples\hugo-demo\content-source ^
  examples\hugo-demo\static\vsa\mxl
if errorlevel 1 exit /b 1
"%PY%" scripts\update-nav-placeholders.py generated\preview\content
if errorlevel 1 exit /b 1
"%PY%" scripts\update-spacing-diagnostics-metadata.py generated\preview\content\voorbeelden\rendering\spacing-diagnostiek.md
if errorlevel 1 exit /b 1
hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\preview\content ^
  --destination ..\..\generated\preview\site ^
  --baseURL /
if errorlevel 1 exit /b 1
echo.
echo Preview build OK:
echo generated\preview\site
echo.
