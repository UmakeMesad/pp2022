 
Number_of_student = 0
tupleStudent = ()
Number_of_Course = 0
tupleCourse = ()
def numberofstufdent():
    global Number_of_student
    Number_of_student = int(input("Enter number of students: "))
    
def input_student():
    global tupleStudent
    for count in range (0, Number_of_student):
        ID = int(input("ID"+str(count+1)+":"))
        name = str(input("name"+str(count+1)+":"))
        dateofbirth = str(input("dateofbirth"+str(count+1)+":"))
        dict = {
            "ID": ID,
            "Name": name,
            "DoB": dateofbirth
        }
        tupleStudent = list(tupleStudent)
        tupleStudent.append(dict)
        tupleStudent = tuple(tupleStudent)
def input_course():
    global Number_of_Course
    Number_of_Course = int(input("Number of course :"))
    

def inputInforMationOfCourse():
    global tupleCourse
    global Number_of_Course
    
    for count in range(0, Number_of_Course):
        idOfCourse = str(input("Enter Id: "))
        nameOfCourse = str(input("Enter Name: "))
        
        dictCourse = {
            idOfCourse,
            nameOfCourse
        }
        tupleCourse = list(tupleCourse)
        tupleCourse.append(dictCourse)
        tupleCourse = tuple(tupleCourse)
        

def selectCourseToEnterMark():
    global tupleStudent
    nameCourse = str(input("Name of seleted course: "))
    
    for i in range(len(tupleStudent)):
        tempMark = float(input("Enter mark of " + str(tupleStudent[i]["Name"]) + ": "))
        tupleStudent[i][str(nameCourse)] = tempMark
        
    tupleStudent = tuple(tupleStudent)
        

numberofstufdent()
input_student()

input_course()
inputInforMationOfCourse()
selectCourseToEnterMark()

print(tupleStudent)
      
 