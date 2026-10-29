@echo off
title Sistema 0 - Starter Base
cd /d "%~dp0backend"

echo ======================================================
echo    Iniciando Sistema 0 (Starter Base)
echo ======================================================
echo.

if exist ".venv\Scripts\python.exe" (
    echo [*] Usando ambiente virtual .venv...
    start http://localhost:8000/
    ".venv\Scripts\python.exe" -m uvicorn app.main:app --reload --port 8000
) else (
    echo [!] Ambiente virtual nao encontrado. Usando python global...
    start http://localhost:8000/
    python -m uvicorn app.main:app --reload --port 8000
)

pause

