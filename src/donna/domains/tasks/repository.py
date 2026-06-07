from sqlalchemy import select
from sqlalchemy.orm import Session

from donna.domains.tasks.models import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: Task) -> Task:
        self.db.add(task)
        self.db.flush()
        self.db.refresh(task)
        return task

    def get_for_user(self, *, task_id: str, user_id: str) -> Task | None:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        return self.db.scalar(statement)

    def list_for_user(self, *, user_id: str, limit: int = 100) -> list[Task]:
        statement = (
            select(Task)
            .where(Task.user_id == user_id)
            .order_by(Task.created_at.desc())
            .limit(limit)
        )
        return list(self.db.scalars(statement).all())

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.flush()
