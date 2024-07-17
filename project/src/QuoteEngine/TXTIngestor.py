"""Text file Ingestor."""
from typing import List

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel


class TXTIngestor(IngestorInterface):
    """TXT file ingestor class."""

    extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT files."""
        if not cls.can_ingest(path):
            raise ValueError(f"File Type not supported for {path}")
        lines = open(path, 'r').readlines()
        return [QuoteModel(body=cls.text_only(each_line.split("-")[0]), author=cls.text_only(each_line.split("-")[1])) for each_line in lines if cls.text_only(each_line)]
