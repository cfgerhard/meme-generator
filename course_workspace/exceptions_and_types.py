class Cat():
        def __init__(self, name, age, isIndoor=True):
            if age < 0:
                raise ValueError('Age cannot be negative')
            if type(name) is not str:
                raise TypeError('Name must be a string')
            if type(isIndoor) != bool:
                raise TypeError('isIndoor must be a boolean')

            self.name = name
            self.age = age
            self.isIndoor = isIndoor

        def speak(self,greeting: str):
            if(type(greeting) is not str):
                raise TypeError('Greeting must be a string')
            print(f'{self.name} says, "{greeting}"')

try:
    herbert = Cat('3', 3)
    herbert.speak(1)
except Exception:
    print('Bad Cat.')
herbert.speak(1)
