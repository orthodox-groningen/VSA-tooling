@echo off
setlocal

cd /d "%~dp0\.."

echo === SOURCE ===
dir /s /b "examples\hugo-demo\content-source\praktijk*"

echo.
echo === GENERATED CONTENT CANDIDATES ===
if exist "examples\hugo-demo\content" dir /s /b "examples\hugo-demo\content\praktijk*"
if exist "examples\hugo-demo\content-generated" dir /s /b "examples\hugo-demo\content-generated\praktijk*"
if exist "generated" dir /s /b "generated\*praktijk*"

echo.
echo === LAYOUTS ===
dir /s /b "examples\hugo-demo\layouts\*list.html"
dir /s /b "examples\hugo-demo\layouts\*single.html"
dir /s /b "examples\hugo-demo\layouts\*baseof.html"

echo.
echo === PUBLIC PRAKTIJK HTML ===
if exist "examples\hugo-demo\public\praktijk\index.html" (
  findstr /n /c:"Praktijkvoorbeelden" /c:"Tropaar toon" /c:"Kondak toon" "examples\hugo-demo\public\praktijk\index.html"
) else (
  echo Geen public praktijk index gevonden.
)
