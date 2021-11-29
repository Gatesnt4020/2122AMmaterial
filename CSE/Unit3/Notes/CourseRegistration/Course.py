class Course:
    
    courseId = 0
    
    #initialization -> Constructor 
    def __init__(self,name,teacher):
        self.name=name
        self.teacher = teacher
        self.courseId = Course.courseId
        Course.courseId+=1
        
    #toString method
    def __str__(self):
        return self.name