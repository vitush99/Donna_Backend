from fastapi import APIRouter

from donna.domains.approvals.router import router as approvals_router
from donna.domains.tasks.router import router as tasks_router

v1_router = APIRouter()
v1_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
v1_router.include_router(approvals_router, prefix="/approvals", tags=["approvals"])
