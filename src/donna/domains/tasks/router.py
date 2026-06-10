from typing import Annotated

from fastapi import APIRouter, Depends, status

from donna.domains.tasks.controller import TaskController
from donna.domains.tasks.models import Task
from donna.domains.tasks.repository import TaskRepository
from donna.domains.tasks.schemas import (
    TaskCreate,
    TaskListResponse,
    TaskResponse,
    TaskUpdate,
)
from donna.domains.tasks.service import TaskService

router = APIRouter()

task_repository = TaskRepository()
task_service = TaskService(task_repository)
task_controller = TaskController(task_service)


def get_task_controller() -> TaskController:
    return task_controller


TaskControllerDependency = Annotated[TaskController, Depends(get_task_controller)]


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    controller: TaskControllerDependency,
) -> Task:
    return controller.create(payload)


@router.get("", response_model=TaskListResponse)
def list_tasks(
    controller: TaskControllerDependency,
) -> TaskListResponse:
    items = [TaskResponse.model_validate(task) for task in controller.list_all()]
    return TaskListResponse(items=items)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: str,
    controller: TaskControllerDependency,
) -> Task:
    return controller.get(task_id)


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: str,
    payload: TaskUpdate,
    controller: TaskControllerDependency,
) -> Task:
    return controller.update(task_id, payload)
