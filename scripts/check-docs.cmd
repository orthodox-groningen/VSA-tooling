@echo off
setlocal
cd /d "%~dp0\.."
python scripts\check-docs.py
if errorlevel 1 exit /b 1
python scripts\sync-docs-walkthrough-svgs.py --check
if errorlevel 1 exit /b 1
