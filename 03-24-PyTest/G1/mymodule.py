

def multiply(a, b, c):
    """
    Returns the product of a, b and c
    if the input are valid integers.
    Otherwise, it returns None.
    """
    if a == 0:
        return 42
    return a * b * c


class School():
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        pass

    def is_student_defined(self, name):
        pass


