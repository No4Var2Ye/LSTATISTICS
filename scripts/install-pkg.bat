@echo off
setlocal

:: Go to project root directory (assuming this script is in a subfolder like scripts/)
cd /d "%~dp0\.."

echo Current directory: %cd%

echo.
echo Searching for .whl file in dist/...

:: Check if dist folder exists
if not exist "dist\" (
    echo Error: dist/ directory does not exist. Please build the package first.
    goto end
)

:: Find the first .whl file in dist/
set WHL_FILE=
for /r "dist" %%f in (*.whl) do (
    set WHL_FILE=%%f
    goto :found
)

:found
if defined WHL_FILE (
    echo.
    echo Found wheel file: %WHL_FILE%
    echo.
    echo Installing package...
    pip install "%WHL_FILE%" --force-reinstall
    if %ERRORLEVEL% == 0 (
        echo Installation succeeded.
    ) else (
        echo Error: Installation failed.
    )
) else (
    echo Error: No .whl file found in dist/. Please build the package first.
)

:end
echo.
@REM pause