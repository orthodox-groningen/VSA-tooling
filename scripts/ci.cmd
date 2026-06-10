@echo off
setlocal

cd /d %~dp0\..

echo.
echo === Local CI pipeline ===
echo.

call scripts\clean.cmd
if errorlevel 1 exit /b 1

call scripts\test.cmd
if errorlevel 1 exit /b 1

echo.
echo CI pipeline completed successfully.
echo.
