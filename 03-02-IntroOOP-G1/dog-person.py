class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # self.owner = None

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pet = None

p = Person("Mr Smith", 45)
d = Dog("Lassie", "brown")
p.pet = d
# d.owner = p

d2 = Dog("Hugo", "white")
# d2.owner = p
