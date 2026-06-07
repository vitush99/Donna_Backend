from fastapi import APIRouter

from donna.api.v1.router import v1_router
from donna.core.config import settings
from donna.domains.health.router import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(v1_router, prefix=settings.api_v1_prefix)
