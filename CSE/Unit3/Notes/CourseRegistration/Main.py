from Course import Course
from Student import Student
from Teacher import Teacher
#from Assignment import * #literally imports all functions and classes
teacherList=[]
courseList = []
studentList=[]

#loadin the teacgers
with open("Data/teacher.csv","r") as file:
    #readlines returns a list
    teacherFile= file.readlines()

for line in teacherFile:
    name,course,junk = line.split("\t",2)
    
    #create a teacher object
    teacherList.append(Teacher(name,course))
    #save the teachers in the teacherList
    
#delete the headers
teacherList.pop(0)

i=-1
for line in teacherFile:
    nameOfTeacher,nameOfCourse,junk = line.split("\t",2)
    if i!= -1:
        courseList.append(Course(nameOfCourse,teacherList[i]))
    i+=1
print(courseList[0].name)


def loadStudent():
    newStudent="y"
    #keep looping while you have a newStudent
    while newStudent == "n":
        first=input("Student's First: ")
        last=input("Student's Last: ")
        studentList.append(Student(first,last))
        
        newStudent = input("Do you have a new student? (y/n)")

    for student in studentList:    
        print(studentList)
    
def courseLookup():
    classToLookUp = "Algebra"
    for course in courseList:
        if course.name == classToLookUp:
            print(course.courseId, course.name, course.teacher.name)
