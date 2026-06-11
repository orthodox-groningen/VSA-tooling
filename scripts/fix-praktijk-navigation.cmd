@echo off
setlocal

cd /d "%~dp0\.."

if exist "examples\hugo-demo\content-source\voorbeelden\praktijk.md" del "examples\hugo-demo\content-source\voorbeelden\praktijk.md"
if exist "examples\hugo-demo\content\voorbeelden\praktijk.md" del "examples\hugo-demo\content\voorbeelden\praktijk.md"
if exist "examples\hugo-demo\content-generated\voorbeelden\praktijk.md" del "examples\hugo-demo\content-generated\voorbeelden\praktijk.md"
if exist "examples\hugo-demo\public" rmdir /s /q "examples\hugo-demo\public"
if exist "generated\hugo" rmdir /s /q "generated\hugo"
if exist "generated\preview" rmdir /s /q "generated\preview"

echo Praktijk cleanup OK
