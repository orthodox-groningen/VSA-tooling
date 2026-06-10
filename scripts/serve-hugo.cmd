@echo off
setlocal

cd /d %~dp0\..

echo.
echo === VSA + Hugo local preview ===
echo.

echo [1/2] Generate Markdown + SVG
vsa build-markdown ^
  examples\hugo-demo\content-source ^
  generated\hugo\content ^
  generated\hugo\static\vsa
if errorlevel 1 exit /b 1

echo.
echo [2/2] Start Hugo server
hugo server ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\hugo\content
