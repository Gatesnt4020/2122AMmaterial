class Student:
    
    studentID = 0
    
    #initialization -> Constructor 
    def __init__(self,firstName,lastName):
        self.first= firstName
        self.last = lastName
        self.courses = []   #each student will have their own list
        #           Class.variable
        self.studentID = Student.studentID
        Student.studentID+=1
        

    #toString method
    def __str__(self):
        out = ""
        out += f"{self.last}, {self.first}\n"
        for course in self.courses:
            out+=f"\t{course}\n"
        return out
    
    #set the name
    def setName(self,newFirst,newLast):
        self.first = newFirst
        self.last = newLast
        
    #get the id
    def getStudent(self):
        return self.studentID
    
    #add a course 
    def addCourse(self,newCourse):
        self.courses.append(newCourse)