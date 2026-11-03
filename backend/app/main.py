import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.core.config import settings
from app.core.database import engine, Base
import app.models # Registers all models with Base.metadata
from app.api.v1 import api_router

# Auto-create tables on startup (especially convenient for local SQLite / rapid setup)
Base.metadata.create_all(bind=engine)

# Auto-seed initial demo & test data on startup (creates demo/teste accounts automatically)
try:
    from app.seed import seed_database
    seed_database()
except Exception as e:
    print(f"[*] Aviso ao semear banco inicial: {e}")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Sistema 0: Base Starter com Agendamento e Controle Financeiro Multi-tenant",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for frontend integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/")
    def serve_frontend_root():
        index_file = os.path.join(frontend_path, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return health_check()

    @app.get("/catalogo")
    @app.get("/revista")
    def serve_catalogo():
        catalogo_file = os.path.join(frontend_path, "catalogo.html")
        if os.path.exists(catalogo_file):
            return FileResponse(catalogo_file)
        return serve_frontend_root()

    @app.get("/catalogo.pdf")
    @app.get("/docs/CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf")
    def serve_catalogo_pdf():
        docs_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf"))
        if os.path.exists(docs_pdf):
            return FileResponse(docs_pdf, media_type="application/pdf", filename="CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf")
        return {"error": "PDF not found"}
else:
    @app.get("/")
    def health_check():
        return {
            "status": "online",
            "app": settings.PROJECT_NAME,
            "docs": "/docs",
            "version": "1.0.0"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
