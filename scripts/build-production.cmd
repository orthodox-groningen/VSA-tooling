@echo off
setlocal

cd /d %~dp0\..

echo.
echo === Build production candidate ===
echo.

if exist generated\production rmdir /s /q generated\production
if exist examples\hugo-demo\static\vsa rmdir /s /q examples\hugo-demo\static\vsa

vsa validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1

vsa build-markdown ^
  examples\hugo-demo\content-source ^
  generated\production\content ^
  examples\hugo-demo\static\vsa ^
  --max-line-width 900 ^
  --output-mode shortcode
if errorlevel 1 exit /b 1

hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\production\content ^
  --destination ..\..\generated\production\site ^
  --minify
if errorlevel 1 exit /b 1

echo.
echo Production candidate build OK:
echo generated\production\site
echo.
