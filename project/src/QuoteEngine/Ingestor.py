"""Ingestor bundle."""
from typing import List

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel


class Ingestor(IngestorInterface):
    """Ingestor class."""



    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return a bool if the parent class has support for file extension in a given path."""
        return cls.file_extension(path) in cls.__base__.extension_support()

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse files."""

        extension = cls.file_extension(path)
        base = cls.__base__

        if not cls.can_ingest(path):
            raise ValueError(f'Unsupported file extension "{extension}" from {path}. '
                             f'Supported types are -> {base.extension_support()}')

        parser = next((c for c in base.__subclasses__() if extension in c.extensions), None)
        return parser.parse(path)
