from abc import ABC, abstractmethod


class Animal(ABC):
    """Define common characteristics for pets."""

    def __init__(self, name: str, age: int):
        """init function for superclass."""
        self.name = name
        self.age = age


    @abstractmethod
    def speak(self):
        pass