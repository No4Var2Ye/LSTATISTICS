@echo off
setlocal

:: Get the directory where this script is located (project root)
cd /d "%~dp0\.."

echo Current directory: %cd%

echo Cleaning dist/ directory...
if exist "dist\" (
    echo Deleting all files and subdirectories in dist/...
    del /q /f dist\* >nul 2>&1
    echo dist/ directory has been cleared.
) else (
    echo dist/ directory does not exist. Skipping cleanup.
)

echo.
@REM pause