@echo off
setlocal

cd /d %~dp0\..

echo.
echo === Cleaning temporary files ===
echo.

if exist .pytest_cache rmdir /s /q .pytest_cache
if exist htmlcov rmdir /s /q htmlcov
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

for /d /r %%D in (__pycache__) do @if exist "%%D" rmdir /s /q "%%D"

del /s /q *.pyc >nul 2>nul

echo.
echo Clean completed.
echo.
