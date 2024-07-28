from tkinter import *

def function1():
    print('Menu item clicked')


root = Tk()
my_menu = Menu(root)
root.config(menu=my_menu)

sub_menu = Menu(my_menu)

my_menu.add_cascade(label='File',menu=sub_menu)

sub_menu.add_command(label='Project',command=function1)
sub_menu.add_command(label='Save',command=function1)

#in tkinter we don't have any such widget like the status bar so, we would create the lebel such that it is positioned below
status = Label(root,text='This is the current status',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

toolbar = Frame(root,bg='green')
insertbutton = Button(toolbar,text='Insert Files',command=function1)
deletebutton = Button(toolbar,text='Delete Files',command=function1)

insertbutton.pack(side=LEFT,padx=2,pady=3)
deletebutton.pack(side=LEFT,padx=2,pady=3)
toolbar.pack()

root.mainloop()