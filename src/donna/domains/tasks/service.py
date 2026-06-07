from sqlalchemy.orm import Session

from donna.core.errors import NotFoundError
from donna.domains.tasks.models import Task
from donna.domains.tasks.repository import TaskRepository
from donna.domains.tasks.schemas import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = TaskRepository(db)

    def create_task(self, *, user_id: str, payload: TaskCreate) -> Task:
        task = Task(
            user_id=user_id,
            title=payload.title,
            description=payload.description,
            priority=payload.priority.value,
            due_at=payload.due_at,
        )
        created = self.repo.create(task)
        self.db.commit()
        return created

    def list_tasks(self, *, user_id: str) -> list[Task]:
        return self.repo.list_for_user(user_id=user_id)

    def update_task(self, *, user_id: str, task_id: str, payload: TaskUpdate) -> Task:
        task = self.repo.get_for_user(task_id=task_id, user_id=user_id)
        if task is None:
            raise NotFoundError("Task not found")

        updates = payload.model_dump(exclude_unset=True)
        for field, value in updates.items():
            if hasattr(value, "value"):
                value = value.value
            setattr(task, field, value)

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, *, user_id: str, task_id: str) -> None:
        task = self.repo.get_for_user(task_id=task_id, user_id=user_id)
        if task is None:
            raise NotFoundError("Task not found")
        self.repo.delete(task)
        self.db.commit()
