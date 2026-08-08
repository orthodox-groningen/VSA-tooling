@echo off
REM MkDocs build zonder TEv2 — snelle syntax/link-check.
REM Voor CI-parity met TermRefs: scripts\docs-build-tev2.cmd
setlocal
cd /d "%~dp0.."
set NO_MKDOCS_2_WARNING=1

set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"

"%PY%" -m pip install -q -r requirements-docs.txt
if errorlevel 1 exit /b 1

"%PY%" -m mkdocs build --strict --site-dir site %*
exit /b %errorlevel%
