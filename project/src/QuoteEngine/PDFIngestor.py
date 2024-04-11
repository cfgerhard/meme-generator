"""PDF file Ingestor."""
from typing import List
import subprocess
import random
import os

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDF Ingestor class."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF files."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, 'r')
        quotes = []
        for line in file_ref.readlines():
            parse = line.split(' - ')
            new_quote = QuoteModel(parse[0], parse[1])
            quotes.append(new_quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
