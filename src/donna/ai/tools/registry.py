from donna.ai.tools.schemas import ToolDefinition, ToolRiskLevel


def get_tool_registry() -> list[ToolDefinition]:
    return [
        ToolDefinition(
            name="create_task",
            description="Create a private task for the current user.",
            risk_level=ToolRiskLevel.LOW,
        )
    ]
