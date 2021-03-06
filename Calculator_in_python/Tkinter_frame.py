"""Entry Widget & Grid Layout in Tkinter"""

from tkinter import *

root = Tk()
root.geometry("600x600")

def getvalue():
    print("Username =",uservalue.get())
    print("Password =",passvalue.get())
#Making Grid
user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid(row=0)
password.grid(row= 1)

"""Some variables Classes are in tkinter for take input
    That are :
    BooleanVar
    Doublevar
    Intvar
    StringVAr"""
#StringVar for take input
uservalue = StringVar()
passvalue = StringVar()

Userentry = Entry(root, textvariable = uservalue)
Passentry = Entry(root, textvariable = passvalue)

Userentry.grid(row =0, column=1)
Passentry.grid(row =1, column=1)

Button(text="Submit", command=getvalue).grid()
root.mainloop()