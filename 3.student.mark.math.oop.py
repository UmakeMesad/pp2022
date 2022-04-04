from audioop import reverse
from itertools import count
from unicodedata import name
from numpy import double, number
import math

class Student:
    def __init__(self,name,id,dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.listCourseMark = list()
    
    def getName(self):
        return self.name    
    
    def setCourseMark(self, course, mark):
        courseMark = {
            "course": course,
            "mark": mark
        }
        self.listCourseMark.append(courseMark)

    def getaverageMark(self):
        sumMark = 0;
        for courseMark in self.listCourseMark:
            sumMark += courseMark["mark"]
            
        average = sumMark/len(self.listCourseMark)
        return math.floor(average*10)/10
     
    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("DOB:", self.dob)
        print("List Course Mark:", self.listCourseMark)
        print("Average GPA:", self.getaverageMark())
        print("Weighted sum of credits:",len(self.listCourseMark))
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
    numberOfCourse = int(input("Enter number of course: "))
    
    for index in range(0, numberOfCourse):
        ID = int(input("Enter ID: "))
        name = str(input("Enter Name: "))
        
        listCourse.append(Course(ID, name))
def list_mark(mark):
    mark.list()
            
def enterMarkForStudent(listStudents, listCourse):    
    for course in listCourse:
        for student in listStudents:
            mark = float(input("Enter mark of student: "+ student.getName() + " for " + course.getName() + ": "))
            student.setCourseMark(course.getName(), math.floor(mark*10)/10)
def sorybyaverageofmark(listStudent,mark):
    return listStudent.sortbyaverageofmark(mark)
              
def sortbyaverageofmark(listStudents):
    listStudents.sort(key=lambda student: student.getaverageMark(),reverse = False)
    
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