
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
        # functionality to check whether the student can take the course
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


webtech.objective = "HTML, JS, CSS and Bootstrap"

print("* - " * 10)
student1.describe()
student2.describe()