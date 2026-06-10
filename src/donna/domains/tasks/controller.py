from donna.domains.tasks.models import Task
from donna.domains.tasks.schemas import TaskCreate, TaskUpdate
from donna.domains.tasks.service import TaskService


class TaskController:
    def __init__(self, service: TaskService):
        self.service = service

    def create(self, payload: TaskCreate) -> Task:
        return self.service.create_task(payload)

    def list_all(self) -> list[Task]:
        return self.service.list_tasks()

    def get(self, task_id: str) -> Task:
        return self.service.get_task(task_id)

    def update(self, task_id: str, payload: TaskUpdate) -> Task:
        return self.service.update_task(task_id, payload)