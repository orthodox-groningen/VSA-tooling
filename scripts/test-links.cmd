@echo off
setlocal

cd /d %~dp0\..

call .venv\Scripts\activate

python scripts\check-publication-output.py --site-dir generated\site --url-prefix /VSA-tooling/