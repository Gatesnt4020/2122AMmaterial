import tkinter

root=tkinter.Tk()
root.geometry("300x300")

frame1=tkinter.Frame(root,width=200,height=150,bg="blue")
frame1.grid(row=0,column=0)

frame1=tkinter.Frame(root,width=200,height=150,bg="red")
frame1.grid(row=1,column=0)

frame3=tkinter.Frame(root,width=100,height=150,bg="green")
frame3.grid(row=0,column=1)

frame3=tkinter.Frame(root,width=100,height=150,bg="yellow")
frame3.grid(row=1,column=1)

root.mainloop()