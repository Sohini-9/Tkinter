from tkinter import *
#importing everything from tkinter using *
root=Tk()
root.geometry("300x400")
#to specify the size of the window
#creating object of the clas Tk to create the window
hello=Label(root,text='Hello Tkinter',fg="red",bg="white",font=("Arial",36))
#to add text we are using the widget label,fg is for the foreground means the text and bg is for the background
hello.pack()
#pack is the simplest way of placing the widget
root.mainloop()
#to keep the window running we use the mainloop
