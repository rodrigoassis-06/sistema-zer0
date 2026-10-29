import os
import sys
import webbrowser

# Garante que o diretório de execução seja a pasta backend
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")

if os.path.exists(backend_dir):
    os.chdir(backend_dir)
    sys.path.insert(0, backend_dir)

try:
    import uvicorn
except ImportError:
    print("\n[!] O pacote 'uvicorn' não foi encontrado no ambiente Python atual.")
    print("[*] Tentando executar com o ambiente virtual (.venv)...")
    venv_python = os.path.join(backend_dir, ".venv", "Scripts", "python.exe")
    if os.path.exists(venv_python):
        os.execv(venv_python, [venv_python, os.path.abspath(__file__)])
    else:
        print("[X] Por favor, instale as dependências com: pip install -r backend/requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print("=" * 60)
    print("[*] Iniciando Sistema 0 (Starter Base)")
    print("[*] Painel Web: http://localhost:8000/")
    print("[*] Swagger Docs: http://localhost:8000/docs")
    print("[*] Login Demo: admin@demo.com | Senha: admin123")
    print("=" * 60)

    # Abre o navegador automaticamente
    try:
        webbrowser.open("http://localhost:8000/")
    except Exception:
        pass

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

