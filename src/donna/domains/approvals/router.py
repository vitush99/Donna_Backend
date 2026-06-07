from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from donna.api.dependencies import get_current_user_id, get_db
from donna.domains.approvals.schemas import ApprovalListResponse
from donna.domains.approvals.service import ApprovalService

router = APIRouter()


@router.get("", response_model=ApprovalListResponse)
def list_pending_approvals(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    approvals = ApprovalService(db).list_pending(user_id=user_id)
    return {"items": approvals}
