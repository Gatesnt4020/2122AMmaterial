#declaere that we have a class
from datetime import datetime

class Post:
    #everthing indented is in the class

    #"global" variables
    postId = 0

    #initialize an object -> Constructor
    #defining when initialize, we need username and message
    def __init__(self,username,message):
        #object's username = usernamePassedIn
        self.un = username
        self.msg = message
        #each object needs a unique number for the post
        self.postId = Post.postId
        Post.postId+=1
        #datetime.now() pulls the current time from the computer
        self.timestamp = datetime.now()


    #string printing format
    #define the string format  ---  toString function
    def __str__(self):
        return str(self.postId)+" "+self.un +" "+ self.timestamp.__str__()+":\n\t"+self.msg

    #other methods
    #function to reset the username 
    def setUserName(self,username):
        self.un=username