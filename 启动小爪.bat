@echo off
chcp 65001 >nul
title 🐾 小爪控制面板
echo.
echo ╔══════════════════════════════════════════╗
echo ║         正在启动小爪控制面板...         ║
echo ╚══════════════════════════════════════════╝
echo.

python "%~dp0xiaozhua_controller.py"

if errorlevel 1 (
    echo.
    echo 启动失败，请确保已安装 Python
    pause
)
