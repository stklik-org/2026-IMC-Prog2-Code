from tests.unit_tests.test_users import TestUsers

mycar = {
    "color": "red",
    "convertible": False,
    "make": "Audi",
    "model": "A3",
    # ...
}

somebodysCar = {
    "color": "blue",
    "convertible": True,
    "make": "Mercedes",
    "model": "Fancy"
}

def description(car):
    print(f"Hey, there's a {car['color']} {car['make']}.")

description(mycar)
description(somebodysCar)

fluffy = {
    "name": "Fluffy",
    "age": 13,
    "species": "cat"
}

def describe(pet):
    print(f"{pet['name']} is my {pet['age']} year old {pet['species']}")

describe(fluffy)
# describe(mycar)


class Person:
    def __init__(self, name, age):   # <-- this is a constructor
        self.name = name
        self.age = age

    def describe(self):
        print(self.name, self.age)

stefan = Person(name="Stefan", age=20)
print("\n"*2, "Printing Stefan:")
# print(stefan.name, stefan.age)
stefan.describe()

franz = Person("Franz", 30)
# print(franz.name, franz.age)
franz.describe()

class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def describe(self):
        print(f"{self.name} is my {self.age} year old {self.species}")


