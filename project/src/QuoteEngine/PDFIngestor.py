"""PDF file Ingestor."""
from typing import List
import subprocess
import tempfile

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel
from .TXTIngestor import TXTIngestor


class PDFIngestor(IngestorInterface):
    """PDF Ingestor class."""

    extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF files."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = tempfile.NamedTemporaryFile(suffix='.txt')
        sub_p = subprocess.run(['pdftotext', path, tmp.name], check=True)

        if sub_p.returncode:
            raise RuntimeError("Subprocess 'pdftotext' did not return successfully.")
        return TXTIngestor.parse(tmp.name)
