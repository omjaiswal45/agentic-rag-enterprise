import hashlib
from typing import Any
from pydantic import BaseModel, ConfigDict, Field


class Document(BaseModel):
    """A single parsed source document, normalized to text plus metadata."""
    model_config = ConfigDict(frozen=True)

    doc_id: str
    text: str = Field(min_length=1)
    source_path: str
    file_format: str
    enterprise: str
    title: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    @staticmethod
    def make_id(enterprise: str, source_path: str) -> str:
        """Stable ID: same enterprise + path always gives the same ID."""
        raw = f"{enterprise}:{source_path}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
