from Course import Course
from Student import Student
from Assignment import * #literally import all functions and classes 

cs = Course("Comp Sci")
math = Course("Easy Math")
lunch= Course("Lunch")
chem = Course("Chemistry 1")

stu1 = Student("billy","bob")
stu1.addCourse(cs)
stu1.addCourse(lunch)
stu1.addCourse(chem)
stu1.addCourse(math)

#staticmethod
#ClassName.method()

assignment1()
assignemtn2()




