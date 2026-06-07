from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from donna.core.config import settings


def _connect_args() -> dict[str, object]:
    if settings.database_url.startswith("sqlite"):
        return {"check_same_thread": False}
    return {}


engine = create_engine(settings.database_url, pool_pre_ping=True, connect_args=_connect_args())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
