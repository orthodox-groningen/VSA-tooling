@echo off
setlocal

echo.
echo === TEv2 terminology for docs ===
echo.
echo [1/3] Prepare terminologie index template
call scripts\prepare-docs-glossary.cmd
if errorlevel 1 exit /b 1

echo [2/3] Generate machine-readable glossary
call npx.cmd mrgt -c docs\tev2-config.yaml
if errorlevel 1 exit /b 1

echo [3/3] Generate terminologie index glossary
call npx.cmd hrgt -c docs\tev2-config.yaml
if errorlevel 1 exit /b 1

echo.
echo Docs TEv2 processing complete.
endlocal
