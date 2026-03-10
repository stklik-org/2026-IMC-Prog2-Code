
class Animal:
    def __init__(self, name):
        print("Animal constructor", name)
        self.name = name

    def speak(self):
        print("Generic Sound")

    def jump(self):
        print("Animal Jumped")

    def __str__(self):
        return f"Generic Animal {self.name}"

class Bird(Animal):
    def speak(self):
        super().speak()
        print("Chirping")

class SongBird(Bird):

    def __init__(self, name, song):
        super().__init__(name)
        print("Songbird Constructor", name, song)
        self.song = song

    def speak(self):
        super().speak()
        print("Nice Song: ", self.song)

    def __str__(self):
        return f"This is a special Songbird named {self.name} singing {self.song}"

class Cat(Animal):
    pass

class Kitten(Cat):

    def jump(self):
        print("Kitten Jumped")


# sb = SongBird("Whitney", "Always love you")
# sb.speak()  # should print "Generic Sound"
# print("Songbird's name", sb.name)
# kit = Kitten()
# kit.speak()  # should print "Meow"
#
# kit.jump()


# print(sb)

#
# class Person():
#     def __init__(self, name, address, phone, email, socialsecurity, car):
#         self.name = name
#         self.address = address
#         #...
#
# class Student(Person):
#     def __init__(self, studentID, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.studentID = studentID
#
# s = Student("1234", "Stefan", "Street A", email="stefan@stefan.at")

class School():
    def __init__(self):
        self.__students = {}


    def __str__(self):
        return f"School has {len(self.__students)} students: {', '.join(self.__students.values())}"

    def __getitem__(self, item):
        return self.__students[item]

    def __add__(self, other):
        self.__students[other] = other

    def __gt__(self, other):
        return len(self) > other

    def __len__(self):
        return len(self.__students)

s = School()
s + "Susy"
s + "Lisa"
s + "Mary"
print(str(s))
# print(s[2])
s + "Thomas"
print(s)

print("Has more than 10 students:", s > 10)

print(s._School__students)
#
# class MyList():
#     def __init__(self, *args):
#         self.content = args
#
#     def __len__(self):
#         return len(self.content)
#
#
# l = MyList(1, 2, 4, "stefan")


class DatabaseConnection():

    def __init__(self):
        self.__conn = None

    def connect(self, server):
        pass # some connection code
        self.__conn = Connection(...)
        self._conn.connect()

    def disconnect(self):
        self.__conn.disconnect()

    def query(self, query):
        if not self.__conn:
            self.connect()
        self.__conn.query(query)



class Dog:
    num_dogs = 0
    def __init__(self):
        # self.i = 12345
        Dog.num_dogs += 1
        pass

d1 = Dog()
d2 = Dog()
print("Number of Dogs", Dog.num_dogs)