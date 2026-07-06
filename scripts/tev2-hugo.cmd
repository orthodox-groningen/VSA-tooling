@echo off
setlocal
set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"

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
echo [TEv2 check] Verify all generated TermRefs were resolved
"%PY%" scripts\check-tev2-termrefs.py generated\hugo\content
if errorlevel 1 exit /b 1

echo.
echo TEv2 processing complete.
endlocal
