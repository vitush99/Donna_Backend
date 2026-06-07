from enum import StrEnum

from pydantic import BaseModel


class ToolRiskLevel(str, StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ToolDefinition(BaseModel):
    name: str
    description: str
    risk_level: ToolRiskLevel
