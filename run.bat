@echo off
title Finance Hub — finance.yeahia.uk
cd /d "%~dp0"

echo ============================================
echo   Personal Finance Hub
echo   http://finance.yeahia.uk
echo ============================================
echo.

echo Checking port 8082...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8082" ^| findstr "LISTENING"') do (
    echo Stopping old process PID %%a...
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 2 /nobreak >nul
echo Starting server...
echo.

"C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe" main.py

echo.
echo Server stopped. Press any key to exit...
pause >nul
