@echo off
setlocal

if not exist ".venv\Scripts\python.exe" (
  echo ERROR: .venv\Scripts\python.exe niet gevonden.
  exit /b 1
)

.venv\Scripts\python.exe -m pip install -r requirements-rendering.txt
if errorlevel 1 exit /b 1

echo Rendering dependencies installed.
.venv\Scripts\python.exe scripts\debug-font-metrics.py
