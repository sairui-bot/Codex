@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python launcher "py" not found.
    echo Install Python for Windows from https://www.python.org/downloads/
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    py -3 -m venv .venv
    if errorlevel 1 goto :failed
)

".venv\Scripts\python.exe" -m pip install -r requirements-build.txt
if errorlevel 1 goto :failed

".venv\Scripts\python.exe" -m PyInstaller --noconfirm --clean calculator.spec
if errorlevel 1 goto :failed

echo.
echo [SUCCESS] EXE created: "%CD%\dist\Calculator.exe"
pause
exit /b 0

:failed
echo.
echo [ERROR] Build failed. Read the messages above.
pause
exit /b 1
