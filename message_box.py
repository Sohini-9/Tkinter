from tkinter import *
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo("Title","This is a messagebox")
response = tkinter.messagebox.askquestion("Question1","Do you like coffee?")

if response=="yes":
    print("Uhuuu!!! Here is your coffee")

root.mainloop()