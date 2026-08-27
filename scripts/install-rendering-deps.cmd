@echo off
setlocal
cd /d "%~dp0.."
call scripts\_ensure.cmd --vsa-tool --import PIL
if errorlevel 1 exit /b 1
python scripts\debug-font-metrics.py
exit /b %ERRORLEVEL%
