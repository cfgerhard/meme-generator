from .animal import Animal


class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str, weight: int):
        """Create a new dog"""
        super().__init__(name, age)
        self.breed = breed
        self.weight = weight

    def speak(self):
        print(f'{self.name} says, wooof')