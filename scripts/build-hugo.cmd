@echo off
setlocal
echo.
echo === VSA + Hugo build ===
echo.
echo [1/5] Clean generated Hugo artifacts
python scripts\clean-hugo-build-artifacts.py
if errorlevel 1 exit /b 1
echo OK
echo.
echo [2/5] Validate content
vsa validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1
echo OK
echo.
echo [3/5] Generate Markdown + SVG
python scripts\update-nav-placeholders.py
python scripts\update-spacing-diagnostics-metadata.py
vsa build-markdown ^
  examples\hugo-demo\content-source ^
  generated\hugo\content ^
  generated\hugo\static\vsa ^
  --config examples\hugo-demo\vsa-demo-config.yml
if errorlevel 1 exit /b 1
echo OK
echo.
echo [4/5] Prepare Hugo input
if exist examples\hugo-demo\content rmdir /s /q examples\hugo-demo\content
xcopy /e /i /y generated\hugo\content examples\hugo-demo\content >nul
if exist examples\hugo-demo\static\vsa rmdir /s /q examples\hugo-demo\static\vsa
xcopy /e /i /y generated\hugo\static\vsa examples\hugo-demo\static\vsa >nul
echo OK
echo.
echo [5/5] Build Hugo site
hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\hugo\content ^
  --destination ..\..\generated\site
if errorlevel 1 exit /b 1
if exist examples\hugo-demo\public rmdir /s /q examples\hugo-demo\public
xcopy /e /i /y generated\site examples\hugo-demo\public >nul
if errorlevel 1 exit /b 1
echo.
echo Build complete.
endlocal
