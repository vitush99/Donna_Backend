from sqlalchemy import select
from sqlalchemy.orm import Session

from donna.domains.approvals.models import ApprovalRequest, ApprovalStatus


class ApprovalRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_pending_for_user(self, *, user_id: str) -> list[ApprovalRequest]:
        statement = (
            select(ApprovalRequest)
            .where(
                ApprovalRequest.user_id == user_id,
                ApprovalRequest.status == ApprovalStatus.PENDING.value,
            )
            .order_by(ApprovalRequest.created_at.desc())
        )
        return list(self.db.scalars(statement).all())
