"""Quote Model file."""


class QuoteModel:
    """Quote Model Class."""

    def __init__(self, body: str, author: str):
        """Quote Model Constructor."""
        self.body = body
        self.author = author

    def __str__(self):
        """Quote Model String Representation."""
        return f'"{self.body}" - {self.author}'


# fertig