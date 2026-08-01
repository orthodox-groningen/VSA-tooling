@echo off
setlocal

echo.
echo === TEv2 terminology for docs ===
echo.
echo Tip: volledige docs-build ^(TEv2 + MkDocs^): scripts\docs-build-tev2.cmd
echo.

call scripts\docs-build-tev2.cmd
exit /b %errorlevel%
