@echo off
setlocal

if not exist docs\terminologie\_index.template (
  echo ERROR: docs\terminologie\_index.template not found.
  exit /b 1
)

copy /y docs\terminologie\_index.template docs\terminologie\_index.md >nul
if errorlevel 1 exit /b 1

endlocal
