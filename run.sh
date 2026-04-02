#!/bin/bash
cd "$(dirname "$0")"

# Проверка Python
if command -v python3 &>/dev/null; then
    PY_CMD="python3"
elif command -v python &>/dev/null; then
    PY_CMD="python"
else
    echo "[!] Python 3 not found. Please install Python 3.8+."
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[Yepdex] Starting..."
$PY_CMD export_tracks.py

if [ $? -ne 0 ]; then
    echo ""
    echo "[!] Error occurred during script execution."
    read -p "Press Enter to exit..."
fi
