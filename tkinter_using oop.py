#we will add all the widgets in the constructor
from tkinter import *
class Demo:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame,text='Click Here',command=self.printmessage) #method is passed in command in place of function
        self.printbutton.pack()

        self.quitbutton = Button(frame,text="Exit",command=frame.quit)   #quit is a default ot exit out of the window
        self.quitbutton.pack()
    def printmessage(self):
        print("Button Clicked")


root = Tk()
b = Demo(root)
root.mainloop()