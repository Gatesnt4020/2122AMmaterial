from Course import Course
from Student import Student
from Teacher import Teacher
#from Assignment import * #literally imports all functions and classes
teacherList = [Teacher("Banderino","ScienceInSpanish"),Teacher("Anderson","Math"),Teacher("Alexander","Science")]
courseList = [Course("Lunch",teacherList[0]),Course("Alegbra",teacherList[1]),Course("Anatomy",teacherList[2])]
studentList=[]

first=""
last=""
newStudent="y"
#keep looping while you have a newStudent
while newStudent == "n":
    first=input("Student's First: ")
    last=input("Student's Last: ")
    studentList.append(Student(first,last))
    
    newStudent = input("Do you have a new student? (y/n)")

for student in studentList:    
    print(studentList)
    

classToLookUp = "Algebra"
for course in courseList:
    if course.name == classToLookUp:
        print(course.courseId, course.name, course.teacher.name)





