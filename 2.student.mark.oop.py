from unicodedata import name
from numpy import double, number

class Student:
    def __init__(self,name,id,dob):
        self.name = name
        self.id = id
        self.dob = dob
    
    def getName(self):
        return self.name    
    
    def setCourse(self, course):
        self.course = course
        
    def setMark(self, mark):
        self.mark = mark
     
    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("DOB:", self.dob)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("\n")
class Course:
    def __init__(self,id, name):
            self.id = id
            self.nameofcourse = name
            
    def getName(self):
        return self.nameofcourse
    
    def display(self):
        print("Name of course :", self.nameofcourse)
        print("Number of course:", self.numberofcourse)
        print("\n")

def enterStudents(listStudents):
    numberStudents = int(input("Enter number of student: "))
    
    for index in range(0, numberStudents):
        ID = int(input("ID"+str(index+1)+":"))
        name = str(input("name"+str(index+1)+":"))
        dateofbirth = str(input("dateofbirth"+str(index+1)+":"))
        
        listStudents.append(Student(name, ID, dateofbirth))
        
def enterCourse(listCourse):
    numerOfCourse = int(input("Enter number of course: "))
    
    for index in range(0, numerOfCourse):
        ID = int(input("Enter ID: "))
        name = str(input("Enter Name: "))
        
        listCourse.append(Course(ID, name))
        
def enterMarkForStudent(listStudents, listCourse):
    nameCourse = ''
    k = True
    
    while k :
        nameCourse = str(input("Enter name of course: "))
        for course in listCourse:
            if (nameCourse == course.getName()):
                k = False
                
    for student in listStudents:
        mark = float(input("Enter mark of student "+ student.getName() + ": "))
        student.setCourse(nameCourse)
        student.setMark(mark)
        
def Main():
    listStudents = list()
    listCourse = list()
    enterStudents(listStudents)
    enterCourse(listCourse)
    
    enterMarkForStudent(listStudents, listCourse)

    for student in listStudents:
        student.display()
Main();