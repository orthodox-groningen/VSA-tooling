@echo off
setlocal

echo.
echo === TEv2 terminology for Hugo demo ===
echo.

echo [TEv2 1/3] Generate machine-readable glossary
call npx mrgt -c examples\hugo-demo\terminology-config.yaml
if errorlevel 1 exit /b 1

echo.
echo [TEv2 2/3] Generate human-readable glossary fragments
call npx hrgt -c examples\hugo-demo\terminology-config.yaml
if errorlevel 1 exit /b 1

echo.
echo [TEv2 3/3] Resolve term references in generated Hugo markdown
call npx trrt -c examples\hugo-demo\terminology-config.yaml
if errorlevel 1 exit /b 1

echo.
echo TEv2 processing complete.
endlocal
