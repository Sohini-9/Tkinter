from tkinter import *
root = Tk()

label1 = Label(root,text="Email")
label2 = Label(root,text="Password")

text1 = Entry(root)
text2 = Entry(root)

label1.grid(row=0,column=0)
text1.grid(row=0,column=1)

label2.grid(row=1,column=0)
text2.grid(row=1,column=1)

button = Button(root,text='Login')
button.grid(row=2,column=1)

root.geometry("300x300")
root.mainloop()

#pack places the widgets one above another as they are written somewhat like a stack but a grid places them side to side and gives more flexibility