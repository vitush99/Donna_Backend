import pytest
from pydantic import ValidationError

from donna.domains.tasks.schemas import TaskCreate


def test_task_create_requires_title() -> None:
    with pytest.raises(ValidationError):
        TaskCreate(title="")
