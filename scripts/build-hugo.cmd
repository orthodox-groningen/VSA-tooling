@echo off
setlocal
set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"
echo.
echo === VSA + Hugo build ===
echo.
echo Python: %PY%
echo.
echo [1/6] Sync zondag bronbestanden
"%PY%" scripts\sync_bron_zondagen.py --bron-root ..\bron
if errorlevel 1 exit /b 1
echo OK
echo.
echo [2/6] Clean generated Hugo artifacts
"%PY%" scripts\clean-hugo-build-artifacts.py
if errorlevel 1 exit /b 1
echo OK
echo.
echo [3/6] Validate content
"%PY%" -m vsa.cli validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1
echo OK
echo.
echo [4/6] Generate Markdown + SVG
"%PY%" -m vsa.cli build-markdown ^
  examples\hugo-demo\content-source ^
  generated\hugo\content ^
  generated\hugo\static\vsa ^
  --config examples\hugo-demo\vsa-demo-config.yml
if errorlevel 1 exit /b 1
"%PY%" -m vsa.cli musicxml ^
  examples\hugo-demo\content-source ^
  generated\hugo\static\vsa\mxl
if errorlevel 1 exit /b 1
"%PY%" scripts\update-nav-placeholders.py generated\hugo\content
if errorlevel 1 exit /b 1
"%PY%" scripts\update-spacing-diagnostics-metadata.py generated\hugo\content\voorbeelden\rendering\spacing-diagnostiek.md
if errorlevel 1 exit /b 1
"%PY%" scripts\assert-real-font-metrics.py
if errorlevel 1 exit /b 1
echo OK
echo.
echo [5/6] Prepare Hugo input
if exist examples\hugo-demo\content rmdir /s /q examples\hugo-demo\content
xcopy /e /i /y generated\hugo\content examples\hugo-demo\content >nul
if exist examples\hugo-demo\static\vsa rmdir /s /q examples\hugo-demo\static\vsa
xcopy /e /i /y generated\hugo\static\vsa examples\hugo-demo\static\vsa >nul
echo OK
echo.
echo [6/6] Build Hugo site
hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\hugo\content ^
  --destination ..\..\generated\site ^
  --baseURL /
if errorlevel 1 exit /b 1
if exist examples\hugo-demo\public rmdir /s /q examples\hugo-demo\public
xcopy /e /i /y generated\site examples\hugo-demo\public >nul
if errorlevel 1 exit /b 1
echo.
echo Build complete.
endlocal
