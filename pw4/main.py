from output import *
from input import *

def Main():
    listStudents = list()
    listCourse = list()
    enterStudents(listStudents)
    enterCourse(listCourse)    

    enterMarkForStudent(listStudents, listCourse)
        
    print("before")
    printListStudent(listStudents)
    
    sortbyaverageofmark(listStudents)
    
    print("after sort")
    printListStudent(listStudents)
Main()