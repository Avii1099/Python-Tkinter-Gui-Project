"""Making button in  Tkinter"""
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Button")
#define function for button1 and button2
def b1():
    print("Button1")
def b2():
    print("Button2")

#maing frame for button
f1 = Frame(root, borderwidth='8', bg= 'Black',relief = SUNKEN )
f1.pack(side= TOP)

#button making here
b1= Button(f1, fg='red', text= "Button1", command=b1)
b1.pack(side=TOP)
b2= Button(f1, fg='red', text= "Button2", command=b2)
b2.pack(side=TOP)
root.mainloop()