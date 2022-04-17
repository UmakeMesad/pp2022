from domains.Student import Student
from domains.Course import Course
import math
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
        
        
def enterMarkForStudent(listStudents, listCourse):    
    for course in listCourse:
        for student in listStudents:
            mark = float(input("Enter mark of student: "+ student.getName() + " for " + course.getName() + ": "))
            student.setCourseMark(course.getName(), math.floor(mark*10)/10)
                
def sortbyaverageofmark(listStudents):
    listStudents.sort(key=lambda student: student.getaverageMark(),reverse = False)