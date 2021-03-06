"""Tkinter in python
   author : @_python.py_"""

"""1. Create your first GUI application"""
# from tkinter import *
#
# root=Tk()
#
# root.title("_python.py_")
#
# root.mainloop()
#

"""2. Create a label widget"""

# from tkinter import *
# root=Tk()
# root.title("_python.py_")
# lbl = Label(root, text="Hello", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)
# root.mainloop()

"""3. Setting window size """
# from tkinter import *
#
# root=Tk()
# #set height and width of window output
# root.geometry("200x250")
# root.title("_python.py_")
#
# root.mainloop()

"""4. Adding a button widget"""
# from tkinter import *
#
# root = Tk()
# root.title("-python.py_")
# root.geometry('350x200')
# lbl = Label(root, text="Hello")
# lbl.grid(column=0, row=0)
# # add button
# btn = Button(root, text="Click Me", bg="red", fg="black")
# btn.grid(column=1, row=0)
#
# root.mainloop()

"""5. Handle button click event"""
# from tkinter import *
#
# root = Tk()
# root.title("_python.py_")
# root.geometry('350x200')
#
# lbl = Label(root, text="Hello")
# lbl.grid(column=0, row=0)
#
# #define function for event handling
# def clicked():
#
#     lbl.configure(text="Button was clicked !!")
#
# btn = Button(root, text="Click Me", command=clicked)
# btn.grid(column=1, row=0)
# root.mainloop()
