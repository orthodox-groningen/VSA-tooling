@echo off
REM TEv2 preprocess + MkDocs serve op generated/ (TermRefs/hover zoals in CI).
REM Voor snelle edits zonder TEv2: scripts\docs-serve.cmd
setlocal
cd /d "%~dp0.."
set NO_MKDOCS_2_WARNING=1

set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"

call scripts\docs-tev2-run.cmd
if errorlevel 1 exit /b 1

"%PY%" -m pip install -q -r requirements-docs.txt
if errorlevel 1 exit /b 1

pushd generated
copy /y mkdocs.yml mkdocs.yml.serve-bak >nul
if errorlevel 1 (
  popd
  exit /b 1
)

for /f "usebackq delims=" %%I in (`"%PY%" -c "from datetime import datetime; from zoneinfo import ZoneInfo; print(datetime.now(ZoneInfo('Europe/Amsterdam')).strftime('%%Y-%%m-%%d %%H:%%M %%Z'))"`) do set "BUILD_TIME=%%I"
"%PY%" ..\scripts\set-mkdocs-site-url.py "https://orthodox-ronl.github.io/VSA-tooling/" false "%BUILD_TIME%" "local"
if errorlevel 1 (
  copy /y mkdocs.yml.serve-bak mkdocs.yml >nul
  del mkdocs.yml.serve-bak 2>nul
  popd
  exit /b 1
)

echo.
echo MkDocs serve ^(TEv2^) — open http://127.0.0.1:8000/  ^(Ctrl+C om te stoppen^)
echo Gegenereerd-stempel: %BUILD_TIME%
echo Staging: generated\docs  — herhaal dit script na TermRef/glossary-wijzigingen.
echo.
"%PY%" -m mkdocs serve %*
set "SERVE_EXIT=%ERRORLEVEL%"

copy /y mkdocs.yml.serve-bak mkdocs.yml >nul
del mkdocs.yml.serve-bak 2>nul
popd

exit /b %SERVE_EXIT%
