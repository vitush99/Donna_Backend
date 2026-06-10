from donna.domains.tasks.models import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def create(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task

    def get(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def update(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task

    def clear(self) -> None:
        self._tasks.clear()
