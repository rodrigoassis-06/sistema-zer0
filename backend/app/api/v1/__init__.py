from fastapi import APIRouter
from app.api.v1.auth import router as auth_router
from app.api.v1.customers import router as customers_router
from app.api.v1.services import router as services_router
from app.api.v1.appointments import router as appointments_router
from app.api.v1.financial import router as financial_router
from app.api.v1.dashboard import router as dashboard_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(customers_router)
api_router.include_router(services_router)
api_router.include_router(appointments_router)
api_router.include_router(financial_router)
api_router.include_router(dashboard_router)

