from typing import List

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                row = line.split(' - ')
                new_quote = QuoteModel(row[0], row[1])
                quotes.append(new_quote)
        return quotes
