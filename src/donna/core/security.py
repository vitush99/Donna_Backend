import uuid


def get_dev_user_id() -> str:
    """Temporary user identity for local development before auth is implemented."""
    return str(uuid.UUID("00000000-0000-0000-0000-000000000001"))
