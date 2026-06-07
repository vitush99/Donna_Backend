from abc import ABC, abstractmethod
from typing import Any


class LLMProvider(ABC):
    @abstractmethod
    async def generate(
        self,
        *,
        messages: list[dict[str, str]],
        tools: list[dict[str, Any]] | None = None,
    ) -> str:
        pass
