@echo off
echo ============================================================
echo AI Audio-to-Image Pipeline - Setup Script
echo ============================================================
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
echo.

echo Installing dependencies...
echo This may take several minutes...
echo.
python -m pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Make sure LM Studio is running with the local server enabled
echo 2. Run: python main.py
echo.
echo To test individual components, run: python test_components.py
echo.
pause
