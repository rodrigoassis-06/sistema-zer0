import os
import sys

# Garante que o diretório de execução e o sys.path incluam a pasta backend
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")

if os.path.exists(backend_dir):
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)

# Expõe a aplicação FastAPI para runners ASGI (Uvicorn / Gunicorn / Render)
from app.main import app

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    is_prod = bool(os.environ.get("RENDER") or os.environ.get("PRODUCTION"))

    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print("=" * 60)
    print(f"[*] Iniciando Sistema Zero")
    print(f"[*] Endereço: http://{host}:{port}/")
    print(f"[*] Modo: {'Produção (Render)' if is_prod else 'Desenvolvimento Local'}")
    print("=" * 60)

    # Abre o navegador apenas em ambiente local interativo
    if not is_prod and os.environ.get("OPEN_BROWSER") == "1":
        try:
            import webbrowser
            webbrowser.open(f"http://localhost:{port}/")
        except Exception:
            pass

    uvicorn.run("app.main:app", host=host, port=port, reload=not is_prod)
