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