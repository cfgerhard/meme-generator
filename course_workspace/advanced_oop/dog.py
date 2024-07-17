class Dog():

    def __init__(self, name:str, age:int,
                 breed:str, weight:int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    @classmethod
    def spawn(cls,new_name, mother, father):
        breed = mother.breed
        if mother.breed != father.breed:
            breed = f'{mother.breed}-{father.breed} Mix.'
        weight = (mother.weight + father.weight)/(2*10)
        return cls(new_name, 0, breed, weight)

if __name__ == "__main__":
    sally = Dog('Sally', 6, 'chihuahua', 7)
    henry = Dog('Henry', 7, 'terrier', 15)
    if sally > henry:
        print(f'{sally} is older than {henry}')
    else:
        print(f'{henry} is older than {sally}')
    trixy = Dog.spawn('Trixy', sally, henry)
    print(trixy.breed)