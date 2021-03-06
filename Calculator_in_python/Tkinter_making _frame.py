"""Making frame in Tkinter"""
from tkinter import *

root = Tk()
f1 = Frame(root, bg = 'red', borderwidth='10',relief=SUNKEN )
f1.pack(side=TOP, fill=X)

l = Label(f1, text = "Hello World")
l.pack()

root.mainloop()