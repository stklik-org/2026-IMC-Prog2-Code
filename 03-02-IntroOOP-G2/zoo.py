class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

class Person:
    def __init__(self, name):
        self.name = name

    def feed(self, animal, food):
        print(f"{self.name} just fed {animal.name}: {food}")


animals = [
    Animal("Tiger32", 12, 121),
    Animal("Lion42", 4, 131),
    Animal("Zebra 12", 12, 11),
    Animal("Bison 23", 4, 121),
    # add more
]

caretaker = Person("Joe")

for animal in animals:
    caretaker.feed(animal, "Apple")

