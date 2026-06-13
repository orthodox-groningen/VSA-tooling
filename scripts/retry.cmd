@echo on
cd "C:\Git\orthodox-groningen\VSA-tooling"
if not exist "c:\Users\rj200\Downloads\%1" (
    echo File not found: c:\Users\rj200\Downloads\%1
    exit /b 1
)
cls
tar -xf "c:\Users\rj200\Downloads\%1"
scripts\test.cmd
if %errorlevel% neq 0 (
    echo Test failed - ERRORLEVEL=%errorlevel%
    exit /b 1
)
pause
