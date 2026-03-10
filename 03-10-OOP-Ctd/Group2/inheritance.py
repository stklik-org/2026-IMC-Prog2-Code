import functools


class Animal():
    def __init__(self, name, weight):
        self.name = name
        self.offspring = []
        self.weight = weight

    def speak(self):
        print("Generic sound")

class Bird(Animal):
    def speak(self):
        super().speak()
        print("Bird is chirping")

class SongBird(Bird):
    def __init__(self, name, weight, song):
        super().__init__(name, weight)
        self.song = song

    def speak(self):
        super().speak()
        print("Singing a song")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow")

class Kitten(Cat):
    pass

sb = SongBird("Whitney Houston", 5, "Always love youuuuuuuuuu")
# print(sb.name)
# print(sb.song)


# b = Bird("Other Bird")
# print(b.name)
#
# sb = SongBird("Birdy")
# # sb.speak()   # should print "Generic Sound"
# print(sb.name)

# c = Cat("Cat")
# c.speak()  # should print "Meow"

# k = Kitten("Kitty")
# k.speak()  # should print "Meow"


# def sum_many_numbers(*args, **kwargs):
#     if multiply:
#         return (functools.reduce(lambda a, b: a * b, args))
#     else:
#         return (sum(args))
#
# print(sum_many_numbers(1, 2, 3, multiply=False, fun=True))
# print(sum_many_numbers(1, 2))
# print(sum_many_numbers(1, 2, 3, 4, 5, 6))



class School():
    def __init__(self, name):
        self.name = name
        self.__students = []

    def __str__(self):
        return f"School {self.name} with {len(self.__students)} students: " + ", ".join(self.__students)

    def __add__(self, other):
        self.__students.append(other)
        return self

    def add(self, other):
        self.__students.append(other)
        return self

    def __getitem__(self, item):
        return self.__students[item]

    def __lt__(self, other):
        self.__students.append(other)
        return True

    def __len__(self):
        return len(self.__students)

s = School("IMC")
s + "Jill" + "Thomas" + "Hugo" + "Ben"
s.add("Sophie").add("Claire")
print(s)


s < "Susy"
print(s)

print(s[1])

print(len(s))

print(s._School__students)

print(s.__class__)

# isinstance(someobj, (Bird, Cat))


class Dog():
    num_dogs = 0
    def __init__(self):
        Dog.num_dogs += 1

d1 = Dog()
d2 = Dog()
d3 = Dog()

print("num_dogs", Dog.num_dogs)