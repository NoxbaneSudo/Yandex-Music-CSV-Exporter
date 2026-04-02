@echo off
title Yepdex Music Exporter
cd /d "%~dp0"

:: Проверка версии Python (кратко)
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Please install Python 3.8+ from python.org
    pause
    exit /b
)

echo [Yepdex] Starting...
python export_tracks.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Script crashed. Check your internet or token.
    pause
)
