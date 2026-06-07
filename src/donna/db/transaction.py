from collections.abc import Callable
from typing import TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


def transactional(db: Session, fn: Callable[[], T]) -> T:
    try:
        result = fn()
        db.commit()
        return result
    except Exception:
        db.rollback()
        raise
