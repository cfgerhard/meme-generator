from .animal import Animal


class Frog(Animal):

    def __init__(self, name: str, age: int, color: str):
        """Create a new Frog."""
        super().__init__(name, age)
        self.color = color

    def __str__(self):
        return f'{self.name} is a Frog of color {self.color} and says ribbit'

    def speak(self):
        print(f'{self.name} says, ribbit')