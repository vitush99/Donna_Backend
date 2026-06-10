from pydantic import BaseModel

from donna.domains.tasks.repository import TaskRepository
from donna.domains.tasks.schemas import TaskCreate
from donna.domains.tasks.service import TaskService


class CreateTaskToolInput(BaseModel):
    title: str
    description: str | None = None


def tool_create_task(
    *,
    repository: TaskRepository,
    payload: CreateTaskToolInput,
) -> dict[str, str]:
    # AI-callable wrapper. Keep tool inputs narrow and auditable.
    task = TaskService(repository).create_task(
        TaskCreate(title=payload.title, description=payload.description)
    )
    return {"task_id": task.id, "title": task.title}
