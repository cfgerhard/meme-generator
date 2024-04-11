"""This is a script as part of the Udacity Nanodegree intermediate python."""


class Cat():
    """A class defining parameters of a cat."""

    def __init__(self, name, age, isIndoor=True):
        """Initiate the class with attributes."""
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        """Print the cat's name and says meow."""
        print(f'{self.name} says meow')

    def __str__(self):
        """Print the cat's name and age and if indoor say so."""
        return f'{self.name} is {self.age} years old{" and lives indoor." if self.isIndoor else "."}'


herbert = Cat('Herbert', 2)
herbert.speak()
print(herbert.isIndoor)


class Dog():
    """A class defining parameters of a dog."""

    def __init__(self, name, age, breed):
        """Initiate the class with attributes."""
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        """Print the dog's name and says woof."""
        print(f'{self.name} says woof')

    def __str__(self):
        """Print the dog's name and age and if indoor say so."""
        return f'{self.name} is {self.age} years old and is a {self.breed}'


tiger = Dog('Tiger', 2, 'Labrador')
tiger.speak()
print(tiger.breed)
