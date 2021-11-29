class Teacher:
    
    #global variable
    employeeID = 0
    
    #Constructor 
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        self.courses = []   #each teacher will have their own list
        #           Class.variable
        self.employeeID = Teacher.employeeID
        Teacher.employeeID+=1
        

    #toString method
    def __str__(self):
        out = ""
        out += f"{self.employeeID},{self.name},{self.subject}\n"
        for course in self.courses:
            out+=f"\t{course}\n"
        return out
    
    #add a course 
    def addCourse(self,newCourse):
        self.courses.append(newCourse)