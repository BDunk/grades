from tkinter import *
from tkinter import filedialog
import os

def selectTerm():
    term = Tk()

    frame = Frame(term)
    frame.grid()

    Label(term, text="Open Existing Term").grid(row=0)
    Label(term, text="Create New Term").grid(row=1)

    openButton = Button(term, text="Open", command=openTerm)
    newtermname = Entry(term)
    newTermButton = Button(term, text="Create", command=createTerm)

    openButton.grid(row=0, column=1)
    newtermname.grid(row=1, column=1)
    newTermButton.grid(row=1, column=2)

    term.mainloop()

def createTerm():
    path = "/Users/bdunk/s/grades/Terms/"+newtermname.get()
    os.mkdir(path)
    selectCourse(path)

def openTerm():
    while True:
        path = filedialog.askopenfilename(initialdir="/Users/bdunk/s/grades/Terms/")
        if(path!=""):
            break
    print(path)
    selectCourse(path)

def selectCourse(path):
    course = Toplevel()


selectTerm()