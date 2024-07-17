"""Abstract Interface."""
from abc import ABC, abstractmethod

from typing import List
from itertools import chain
from .quote import QuoteModel
import re



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

    def file_extension(path):
        """Return a file extension from path string."""
        return path.split('.')[-1]

    @classmethod
    def extension_support(cls):
        """Return a list of all supported parse extension formats from subclasses."""
        return list(chain(*[c.extensions for c in cls.__subclasses__()]))

    @classmethod
    def text_only(cls, text):
        """Return text free of unwanted and non-printable characters."""
        unwanted_chars = r"[()\"#/@;<>{}`+=~|.!?,]"
        return ''.join(filter(str.isprintable, re.sub(unwanted_chars, "", text).strip()))
# fertig
