class Course:
    
    #Constructor 
    def __init__(self,name):
        self.name=name
        
    #toString
    def __str__(self):
        return self.name
    
math = Course("Algebra")    #running the constructor
print(math)                 #running the toString