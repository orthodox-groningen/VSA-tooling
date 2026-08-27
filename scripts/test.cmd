@echo off
setlocal
cd /d %~dp0\..
call scripts\_ensure.cmd --catalogus --vsa-tool --import vsa --import pytest --import PIL
if errorlevel 1 exit /b 1
python -m pytest %*
exit /b %ERRORLEVEL%
