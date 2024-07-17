"""Ingest DOCX files."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel


class DocxIngestor(IngestorInterface):
    """DOCX ingestor class."""

    extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the DOCX file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        # parse the docx file and return a list of QuoteModel objects.
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
