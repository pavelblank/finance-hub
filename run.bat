@echo off
title Finance Hub
cd /d "%~dp0"

echo ============================================
echo   Personal Finance Hub
echo ============================================
echo.

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python was not found on your PATH.
    echo Install Python 3.10 or higher from https://python.org and try again.
    pause
    exit /b 1
)

echo Checking port 8082...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8082" ^| findstr "LISTENING"') do (
    echo Stopping old process PID %%a...
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 2 /nobreak >nul
echo Starting server...
echo   Open http://localhost:8082 in your browser
echo.

python main.py

echo.
echo Server stopped. Press any key to exit...
pause >nul
