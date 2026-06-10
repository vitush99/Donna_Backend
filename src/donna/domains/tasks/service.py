from datetime import UTC, datetime
from uuid import uuid4

from donna.core.errors import NotFoundError
from donna.domains.tasks.models import Task, TaskStatus
from donna.domains.tasks.repository import TaskRepository
from donna.domains.tasks.schemas import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, payload: TaskCreate) -> Task:
        now = datetime.now(UTC)
        task = Task(
            id=str(uuid4()),
            title=payload.title,
            description=payload.description,
            status=TaskStatus.PENDING.value,
            source=payload.source.value,
            created_at=now,
            updated_at=now,
        )
        return self.repository.create(task)

    def list_tasks(self) -> list[Task]:
        return self.repository.list_all()

    def get_task(self, task_id: str) -> Task:
        task = self.repository.get(task_id)

        if task is None:
            raise NotFoundError("Task not found")

        return task

    def update_task(self, task_id: str, payload: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        updates = payload.model_dump(exclude_unset=True)

        for field, value in updates.items():
            if hasattr(value, "value"):
                value = value.value
            setattr(task, field, value)

        task.updated_at = datetime.now(UTC)
        return self.repository.update(task)
