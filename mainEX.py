# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import tkinter as tk
import os

class TermSelect(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        a = 0
        for x in os.listdir("/Users/bdunk/s/grades/Terms"):
            if (x != ".DS_Store"):
                tk.Label(self, text=x).grid(row=a, column=0)
                open = tk.Button(self, text="Open", command= lambda: self.openterm(parent,"/Users/bdunk/s/grades/Terms/"+x))
                open.grid(row=a, column=1)
                a = a + 1

        new_file_name = tk.Entry(self)
        new_file_name.grid(row=a, column=0)

        newfilebutton = tk.Button(self, text="Create",
                                       command=lambda: self.createterm(new_file_name).grid(row=a, column=1))

    def createterm(self, entry):
        os.mkdir("/Users/bdunk/s/grades/Terms/" + entry.get())
        #show_frame(PageOne,"/Users/bdunk/s/grades/Terms/" + entry.get())

    def openterm(self,parent, path):
        parent.grid_forget()


        course = PageOne(parent, path)
        course.grid(row=0, column=0)

        self.destroy()




class PageOne(tk.Frame):

    def __init__(self, parent, path):
        tk.Frame.__init__(self, parent)
        a = 0
        back=tk.Button(self, text="<back", command=lambda: self.goback())
        back.grid(row=0, column=0)


    def goback(self):
        print("back")

    def createcourse(self,parent):
        return 0

    def opencourse(self,parent,path):
        return 0

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(TermSelect))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


root = tk.Tk()
window = tk.Frame(root)
window.grid(row=0, column=0)
term = TermSelect(window)
term.grid(row=0,column=0)
root.mainloop()
