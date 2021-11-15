#from file import class
from Post import Post


#creating a post
post1=Post("bob","Hello")  #runs the _init_ function

#post1 is an object

#objects can hold multiple variabels AND have methods
#variabels can store data
username="bob"
message="hello"

print(post1.un)
print(post1.msg)

username="sally"
message="howdy"
post2=Post("sally","howdy")

print(post2.un,post2.msg)


#printing the post
print(post1)                #runs the _str_ function