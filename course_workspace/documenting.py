"""Excercise on DocStrings."""


class Cat():
    """Create a Cat object."""

    def __init__(self, name: str, age: int):
        """Initialize Cat object."""
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Cat speaks.

        >>> kitty.speak()
        Spot says, purrrrrr
        """
        print(f'{self.name} says, purrrrrr')


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'kitty': Cat('Spot', 3)})
    