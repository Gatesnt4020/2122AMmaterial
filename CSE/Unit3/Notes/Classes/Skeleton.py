#322

"""
This program is intended as a tracer round for the flow of control as 
a user of a social media account makes, deletes, and edits posts. For 
testing, a user should be able to enter their user name, change which 
user name they are currently using, add a post using their current user 
name, remove a post made under their current user name, edit a post 
made under their current user name, print the contents of the list of 
posts, or quit the program.
"""

# This line of code tells the Python interpreter that it needs to 
# reference the post.py file in order to run the rest of the code 
# in this file.
from Post import Post

# How will you save the posts you will create? Review the for loop 
# near the end of this code for an answer.
allPostArchive=[]

# What is the user name they want to use?

# Welcome user to the program 
print("Welcome to the BookFace!")

# Store initial user input in a variable identified by user_input

# You may need to use this statement again to complete the activity.
userinterface=""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

"""
username= input("What is your username? ")
user_input = input(userinterface)

# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":

    # code for adding a post here
    if user_input=="add":
        message=input("What is your message? ")     #obtain message
        post=Post(username,message)                 #createxd our post
        allPostArchive.append(post)                 #saved the post to the archive

    
    # code for removing a post here
    elif user_input=="remove":
        id=int(input("Which post do you want to delete? "))
        #loop through the list using index numbers(0,1,2,3,etc)
        for i in range(len(allPostArchive)):
            #if postwe are on's postId is equal the one we are looking for
            if allPostArchive[i]==id:
        #delete an item in the list
                del allPostArchive[i]
                break

    # code for changing the current user here
    elif user_input=="change user":
        username = input("what is your username? ")
        post.un=username
        #post.setUserName(username)

    # code to display all posts, you can use the code in comments below
    elif user_input == "print":
        # this for loop will print the list
        # and the element itself
        for post in allPostArchive: 
            print (post)
    # code to inform the user that their input was not valid here
    
    # code that will allow the user to make a new selection
    # This code will finish the loop

    user_input = input(userinterface)