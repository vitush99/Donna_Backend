from sqlalchemy.orm import Session

from donna.domains.approvals.repository import ApprovalRepository


class ApprovalService:
    def __init__(self, db: Session):
        self.repo = ApprovalRepository(db)

    def list_pending(self, *, user_id: str):
        return self.repo.list_pending_for_user(user_id=user_id)
