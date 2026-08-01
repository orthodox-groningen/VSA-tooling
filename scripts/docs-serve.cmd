@echo off
setlocal

cd /d %~dp0\..

set "PY=python"
if exist .venv\Scripts\python.exe set "PY=.venv\Scripts\python.exe"

REM Onderdruk Material for MkDocs "MkDocs 2.0"-banner (zelfde als docs-pages CI).
set "NO_MKDOCS_2_WARNING=1"

"%PY%" -m pip install -q -r requirements-docs.txt
if errorlevel 1 exit /b 1

copy /y mkdocs.yml mkdocs.yml.serve-bak >nul
if errorlevel 1 exit /b 1

REM Zelfde tijdstempel-patroon als docs-pages.yml (lokaal: huidige UTC-tijd).
for /f "usebackq delims=" %%I in (`"%PY%" -c "from datetime import datetime, timezone; print(datetime.now(timezone.utc).strftime('%%Y-%%m-%%d %%H:%%M UTC'))"`) do set "BUILD_TIME=%%I"
"%PY%" scripts\set-mkdocs-site-url.py "https://orthodox-groningen.github.io/VSA-tooling/docs/" false "%BUILD_TIME%" "local"
if errorlevel 1 (
  copy /y mkdocs.yml.serve-bak mkdocs.yml >nul
  del mkdocs.yml.serve-bak 2>nul
  exit /b 1
)

echo.
echo MkDocs serve — open http://127.0.0.1:8000/  (Ctrl+C om te stoppen)
echo Gegenereerd-stempel: %BUILD_TIME%
echo.
"%PY%" -m mkdocs serve %*
set "SERVE_EXIT=%ERRORLEVEL%"

copy /y mkdocs.yml.serve-bak mkdocs.yml >nul
del mkdocs.yml.serve-bak 2>nul

exit /b %SERVE_EXIT%
