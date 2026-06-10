@echo off
setlocal

cd /d %~dp0\..

echo.
echo === Build preview ===
echo.

if exist generated\preview rmdir /s /q generated\preview

vsa validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1

vsa build-markdown ^
  examples\hugo-demo\content-source ^
  generated\preview\content ^
  generated\preview\static\vsa
if errorlevel 1 exit /b 1

hugo ^
  --source examples\hugo-demo ^
  --contentDir ..\..\generated\preview\content ^
  --destination ..\..\generated\preview\site
if errorlevel 1 exit /b 1

echo.
echo Preview build OK:
echo generated\preview\site
echo.
