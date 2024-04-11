"""Abstract Interface."""
from abc import ABC, abstractmethod

from typing import List
from .quote import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface."""

    extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested."""
        ext = path.split('.')[-1]
        return ext in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse content into a list."""
        pass
