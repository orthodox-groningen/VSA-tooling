@echo off
REM Dit is een script om voor de lokale site te testen of links kloppen.
REM volgens mij werkt dat nog niet helemaal...
setlocal

cd /d %~dp0\..

call .venv\Scripts\activate

python scripts\check-publication-output.py --site-dir generated\site --url-prefix /