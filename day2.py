from tkinter import *
from tkinter import ttk

window = Tk()

#Declaring Window Title

window.title ("Registration Screen")

#Declaring Window size

window.geometry  ("700x500")

#Declaring Window Color

window.configure(background  =  "green");

#below four fields are declared

Firstname = Label(window  ,text = "First name").   grid (row=0,column=0)
Lastname  =  Label(window  ,text = "Last name").grid (row=1, column=0)
Email = Label(window,text = "Email Id").grid(row=2,column=0)
Mobile = Label(window,text = "Contact Number").grid(row=3,column=0)
Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)

#function declaration

def clicked():
	     res="Welcome to" + txt.get()
	     lbl.configure (text = res)
btn = ttk.Button(window,text="Submit").grid(row=4,column=0)
window.mainloop()
