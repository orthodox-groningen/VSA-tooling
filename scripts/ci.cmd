@echo off
setlocal

cd /d %~dp0\..

echo.
echo === VSA CI ===
echo.

echo [1/5] Install package and test dependencies
python -m pip install --upgrade pip
if errorlevel 1 exit /b 1

python -m pip install -e .
if errorlevel 1 exit /b 1

python -m pip install pytest
if errorlevel 1 exit /b 1

echo.
echo [2/5] Clean generated CI output
if exist generated\ci rmdir /s /q generated\ci

echo.
echo [3/5] Run tests
python -m pytest
if errorlevel 1 exit /b 1

echo.
echo [4/5] Validate demo content directory
vsa validate examples\hugo-demo\content-source
if errorlevel 1 exit /b 1

echo.
echo [5/5] Build demo markdown
vsa build-markdown examples\hugo-demo\content-source generated\ci\content generated\ci\static\vsa
if errorlevel 1 exit /b 1

echo.
echo CI OK
echo.
