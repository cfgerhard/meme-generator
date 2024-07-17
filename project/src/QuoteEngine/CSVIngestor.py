"""CSV file Ingestor."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .quote import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSV file Ingestor Class."""

    extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV files."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
