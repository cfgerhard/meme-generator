class Animal:
    """Define common characteristics for pets."""

    def __init__(self, name: str, age: int, word: str):
        """init function for superclass."""
        self.name = name
        self.age = age
        self.word = word

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, {self.word}')


class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, word, isIndoor=True):
        """Create a new cat"""
        super().__init__(name, age, word)
        self.isIndoor = isIndoor


class Dog(Animal):

    def __init__(self, name: str, age: int, word: str, breed: str, weight: int):
        """Create a new dog"""
        super().__init__(name, age, word)
        self.breed = breed
        self.weight = weight


class Frog(Animal):

    def __init__(self, name: str, age: int, word: str, color: str):
        """Create a new Frog."""
        super().__init__(name, age, word)
        self.color = color

    def __str__(self):
        return f'{self.name} is a Frog of color {self.color} and says {self.word}'


if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3, 'purrrrrr')
    paws = Dog('Mr. Paws', 4, 'woof', 'dachshund', 18)
    crazy = Frog('Frank', 10, 'Ribbit', 'Green')
    wiskers.speak()
    paws.speak()
    crazy.speak()
    print(crazy)
