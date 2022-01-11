from tkinter import *
import random

root = Tk()
canvas = Canvas(root,height=600,width=600,bg="black")  #bg is for the background color
canvas.grid()

stars=[]
for i in range(100):
     centerX = random.randint(0,600)
     centerY = random.randint(0,600)
     stars.append(canvas.create_rectangle(centerX-2,centerY-2,centerX+2,centerY+2,fill="yellow"))

#create_text(x1,y1,text,*options)
canvas.create_text(300,100,text="Hello Space",fill="white",font=32)

from PIL import ImageTk, Image        #libraries that help us render pictures
#open a picture
imgFile = Image.open('falcon.png')
imgFile = imgFile.resize((100,100))  #resize((width,height))
#convert it to a TKpicture
imgTK = ImageTk.PhotoImage(imgFile)
#render the TKpicture
img = canvas.create_image(300,300,image=imgTK) #create_image(x,y,image=)

def animate():
     for s in range(len(stars)):
          #find the coordinates of the star
          x1,y1,x2,y2 = canvas.coords(stars[s])        #this pulls the coords and saves into the var
          # print(x1,y1,x2,y2)
          #reset the coordinates of the star
          canvas.coords(stars[s], x1, y1+1, x2, y2+1)
          if y2 > 600:
               canvas.coords(stars[s],x1, 0, x2, 4)
     #after(howOften,whichCommand)
     canvas.after(1,animate)
     
animate()     

root.mainloop()