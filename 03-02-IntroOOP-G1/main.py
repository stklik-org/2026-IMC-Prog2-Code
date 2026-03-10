

mycar = {
    "color": "red",
    "year": 1999,
    "make": "Audi",
    "model": "A3",
    "extras": "Sports Edition",
    "tyres": "summer",
    "convertible": False
}

other_car = {
    "color": "blue",
    "year": 2010,
    "brand": "Mercedes",
    "model": "",
    "extras": "Fancy Version",
    "tyres": "winter",
    "convertible": True,
}

def describe(car):
    """This describes a car."""
    print(f"This is a {car['color']} {car['make']} {car['model']} with {car['tyres']} tyres")


mypet = {
    "name": "fluffy",
    "age": 13,
    "type": "dog"
}


class Car(object):
    def __init__(self, color, year, make, model, extras, tyres, convertible):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.extras = extras
        self.tyres = tyres
        self.convertible = convertible

    def describe(self):
        print(f"This is a {self.color} {self.make} {self.model} with {self.tyres} tyres")

class Pet:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def describe(self):
        print(f"This is {self.name}. A {self.age} year old {self.type}.")

    def increase_age(self):
        self.age += 1


# print(mySkoda.color)
# print(mySkoda.year)

class Course:
    def __init__(self, name, objective, course_type):
        self.name = name
        self.objective = objective
        self.course_type = course_type

    def describe(self):
        print(f"Course {self.name} (Type: {self.course_type}): Goal: Learning {self.objective}")


webtech = Course("Web Technologies", "HTML, CSS, JS", "Integrated Lecture")
prog2 = Course("Programming II", "Advanced Programming Concepts", "Lecture with Exam")

webtech.describe()
prog2.describe()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        self.grades = {}

    def add_course(self, course):
        self.courses.append(course)

    def set_grade(self, coursename, grade):
        self.grades[coursename] = grade

    def describe(self):
        print(f"Student {self.name} (age: {self.age})")
        for course in self.courses:
            course.describe()
            print(f"Grade: {self.grades[course.name]}")

student1 = Student("Stefan", 13)
student1.add_course(webtech)
student1.add_course(prog2)
student1.set_grade("Programming II", 3)
student1.set_grade("Web Technologies", 5)


student2 = Student("Suzy", 13)
student2.add_course(webtech)
student2.add_course(prog2)
student2.set_grade("Programming II", 2)
student2.set_grade("Web Technologies", 1)


webtech.objective = "Have fun"


student1.describe()
student2.describe()