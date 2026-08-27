@echo off
REM Shared PATH/version/package check. Call from repo-root scripts after cd.
REM Flags are forwarded to scripts\_ensure.py (see that file).
setlocal EnableExtensions
cd /d "%~dp0.."

echo %PATH% | find /I ".\scripts" >nul
if errorlevel 1 (
  echo NOTE: PATH missing .\scripts; prepended for this command.
  echo Add .\scripts to your user PATH for short names ^(test, serve, build, check^).
  set "PATH=.\scripts;%PATH%"
)

where python >nul 2>&1
if errorlevel 1 (
  echo ERROR: python not found on PATH
  echo Install Python 3.14 and add C:\Python314\ and C:\Python314\Scripts\ to PATH.
  exit /b 1
)

python -c "import sys; raise SystemExit(0 if sys.version_info[:2]==(3,14) else 1)" >nul 2>&1
if errorlevel 1 (
  echo ERROR: python is not version 3.14
  python --version
  echo Expected: Python 3.14.x ^(e.g. C:\Python314\python.exe^), not 3.12 and not the Microsoft Store stub.
  exit /b 1
)

python scripts\_ensure.py %*
exit /b %ERRORLEVEL%
