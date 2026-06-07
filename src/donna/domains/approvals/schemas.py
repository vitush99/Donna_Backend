from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class ApprovalStatus(str, StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"


class RiskLevel(str, StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ApprovalResponse(BaseModel):
    id: str
    user_id: str
    action_type: str
    risk_level: RiskLevel
    status: ApprovalStatus
    payload_json: str
    created_at: datetime
    expires_at: datetime | None

    model_config = {"from_attributes": True}


class ApprovalListResponse(BaseModel):
    items: list[ApprovalResponse]
