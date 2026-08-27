@echo off
echo use: _ensure (no separate bootstrap step)
call "%~dp0_ensure.cmd" --catalogus --vsa-tool --import vsa --import pytest --import PIL --pip-r requirements-docs.txt
exit /b %ERRORLEVEL%
