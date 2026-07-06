@echo off
setlocal
set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"

echo.
"%PY%" scripts\tev2_hugo.py --content-root generated\hugo\content
if errorlevel 1 exit /b 1

endlocal
