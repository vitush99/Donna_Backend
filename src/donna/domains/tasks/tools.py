from pydantic import BaseModel
from sqlalchemy.orm import Session

from donna.domains.tasks.schemas import TaskCreate, TaskPriority
from donna.domains.tasks.service import TaskService


class CreateTaskToolInput(BaseModel):
    title: str
    description: str | None = None
    priority: TaskPriority = TaskPriority.MEDIUM


def tool_create_task(*, db: Session, user_id: str, payload: CreateTaskToolInput) -> dict[str, str]:
    # AI-callable wrapper. Keep tool inputs narrow and auditable.
    task = TaskService(db).create_task(
        user_id=user_id,
        payload=TaskCreate(
            title=payload.title,
            description=payload.description,
            priority=payload.priority,
        ),
    )
    return {"task_id": task.id, "title": task.title}
