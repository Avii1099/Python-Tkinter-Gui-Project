"""IN This program we know about label function"""
from tkinter import *

root = Tk()
root.geometry("900x900")
#Read label function
#bg = background
#fg = font
l1 = Label(text="""Tkinter is a Python binding to the Tk GUI toolkit. It is the \nstandard Python interface to the Tk GUI toolkit, and is Python's de fact standard \nGUI. Tkinter is included with standard Linux, Microsoft Windows and Mac OS X \ninstalls of Python. The name Tkinter comes from Tk interface."""
           , bg = 'yellow', fg='black', font="19,bold", padx=50, pady=40, relief=
            SUNKEN)
"""Read about pack function"""
l1.pack(side=TOP, fill=Y)
root.mainloop()