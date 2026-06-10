from fastapi import APIRouter

from donna.domains.health.router import router as health_router
from donna.domains.tasks.router import router as tasks_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(tasks_router, prefix="/api/tasks", tags=["tasks"])