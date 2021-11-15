class Course:
    
    #initialization -> Constructor 
    def __init__(self,name):
        self.name=name
        
    #toString method
    def __str__(self):
        return self.name