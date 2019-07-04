from tkinter import *
import os

class TermPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.grid()
        a=0
        for x in os.listdir("/Users/bdunk/s/grades/Terms"):
           if (x != ".DS_Store"):
                Label(parent, text=x).grid(row=a, column=0)
                open=Button(parent, text="Open", command=lambda : self.openterm(parent,("/Users/bdunk/s/grades/Terms/"+x)))
                open.grid(row=a, column=1)
                a=a+1

        new_file_name=Entry(parent)
        new_file_name.grid(row=a, column=0)

        newfilebutton=Button(parent, text="Create", command= lambda: self.createterm(new_file_name)).grid(row=a, column=1)

    def createterm(self, entry):
        os.mkdir("/Users/bdunk/s/grades/Terms/"+entry.get())
        self.openterm(self.parent,"/Users/bdunk/s/grades/Terms/"+entry.get())

    def openterm(self, parent, term_path):
        print(term_path)


class CoursePage(Frame):
    def __init__(self, parent, termPath):
        Frame.__init__(self, parent)


class AssignmentPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)


window = Tk()
term=TermPage(window)
window.mainloop()