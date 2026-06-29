@echo off
setlocal

cd /d %~dp0\..

echo.
echo === Build local artifacts ===
echo.

echo [1/5] Sync zondag bronbestanden
call scripts\sync-bron-zondagen.cmd
if errorlevel 1 exit /b 1

echo.
echo [2/5] Clean generated artifacts
if exist generated\artifacts rmdir /s /q generated\artifacts

echo.
echo [3/5] Validate content
vsa validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1

echo.
echo [4/5] Generate Markdown and SVG
vsa build-markdown ^
  examples\hugo-demo\content-source ^
  generated\artifacts\content ^
  generated\artifacts\static\vsa
if errorlevel 1 exit /b 1

echo.
echo [5/5] Done
echo.
echo Generated:
echo - generated\artifacts\content
echo - generated\artifacts\static\vsa
echo.
