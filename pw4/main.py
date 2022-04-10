from output import *
from input import *
from domains import *

def Main():
    listStudents = list()
    listCourse = list()
    enterStudents(listStudents)
    enterCourse(listCourse)
    
    enterMarkForStudent(listStudents, listCourse)
    
    print("before")
    for student in listStudents:
        student.display()
    
    sortbyaverageofmark(listStudents)
    
    print("after sort")
    for student in listStudents:
        student.display()
Main();