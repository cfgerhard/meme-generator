class QuoteModel():

    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author

    def __str__(self):
        return f'"{self.text}" - {self.author}'