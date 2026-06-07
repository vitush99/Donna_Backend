from donna.ai.tools.schemas import ToolRiskLevel


def requires_approval(risk_level: ToolRiskLevel) -> bool:
    return risk_level in {ToolRiskLevel.MEDIUM, ToolRiskLevel.HIGH}
