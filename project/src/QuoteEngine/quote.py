"""Quote Model file."""


class QuoteModel:
    """Quote Model Class."""

    def __init__(self, text: str, author: str):
        """Quote Model Constructor."""
        self.text = text
        self.author = author

    def __str__(self):
        """Quote Model String Representation."""
        return f'"{self.text}" - {self.author}'
