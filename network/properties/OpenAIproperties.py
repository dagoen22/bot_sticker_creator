from dataclasses import dataclass
from typing import Optional


@dataclass
class OpenAIData:
    model: str
    prompt: str
    size: str
    quality: int
    n: Optional[int] = 1
