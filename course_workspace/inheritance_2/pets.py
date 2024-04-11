from animals import Cat, Dog, Frog

if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    crazy = Frog('Frank', 10,  'Green')
    wiskers.speak()
    paws.speak()
    crazy.speak()
    print(crazy)
