
from mymodule import School

def test_createSchool_withName():
    schoolname = "TestSchool"

    myschool = School(schoolname)

    assert myschool.name == schoolname


def test_addNewStudent():
    schoolname = "TestSchool"
    myschool = School(schoolname)

    numStudentsBefore = len(myschool.students)
    myschool.add_student("Tom")

    assert "Tom" in myschool.students
    assert numStudentsBefore + 1 == len(myschool.students)


def test_addNewStudent_Twice():
    schoolname = "TestSchool"
    myschool = School(schoolname)

    numStudentsBefore = len(myschool.students)
    myschool.add_student("Tom")
    myschool.add_student("Tom")

    assert "Tom" in myschool.students
    assert numStudentsBefore + 1 == len(myschool.students)
