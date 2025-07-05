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
echo 🔨 Starting project build...
python -m build

if %ERRORLEVEL% == 0 (
    echo.
    echo Build succeeded! New packages have been generated in the dist/ directory:
    dir /b dist\
) else (
    echo.
    echo Build failed. Please check the error logs.
)

echo.
@REM pause