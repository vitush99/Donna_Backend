from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from donna.core.security import get_dev_user_id
from donna.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user_id() -> str:
    # Replace with real auth once users/auth domain is implemented.
    return get_dev_user_id()
