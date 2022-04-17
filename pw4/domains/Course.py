
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
