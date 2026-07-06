@echo off
setlocal
cd /d "%~dp0\.."
python scripts\check-docs.py
