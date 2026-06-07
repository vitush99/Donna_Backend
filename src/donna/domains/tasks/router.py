from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from donna.api.dependencies import get_current_user_id, get_db
from donna.core.errors import NotFoundError
from donna.domains.tasks.schemas import TaskCreate, TaskListResponse, TaskResponse, TaskUpdate
from donna.domains.tasks.service import TaskService

router = APIRouter()


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    return TaskService(db).create_task(user_id=user_id, payload=payload)


@router.get("", response_model=TaskListResponse)
def list_tasks(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    tasks = TaskService(db).list_tasks(user_id=user_id)
    return {"items": tasks}


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: str,
    payload: TaskUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    try:
        return TaskService(db).update_task(user_id=user_id, task_id=task_id, payload=payload)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    try:
        TaskService(db).delete_task(user_id=user_id, task_id=task_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
