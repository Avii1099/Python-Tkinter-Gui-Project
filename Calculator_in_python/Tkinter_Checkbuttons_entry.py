"""Making checkbutton in tkinter"""
from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Form")

def form():
    print("Name = ", namevalue.get())
    print("Phone = ",Phonevalue.get())
    print("Mail = ",Mailvalue.get())


"""Making text form"""
Label(root, text="Welcome to Myclass", font="comicsansms 13 bold", pady=50, padx=25).grid(row=0, column=3)
name = Label(root, text="Name",  padx=5).grid(row=1, column=2)
Phone = Label(root, text="Phone",  padx=5).grid(row=2, column=2)
Mail = Label(root, text="Mail",padx=5).grid(row=3, column=2)

"""Making variable classes for storing entry """
namevalue = StringVar()
Phonevalue = StringVar()
Mailvalue = StringVar()
agree = IntVar()

"""entry for a form """
nameentry = Entry(root, textvariable= namevalue).grid(row=1, column=3)
Phoneentry = Entry(root, textvariable= Phonevalue).grid(row=2, column=3)
Mailentry = Entry(root, textvariable= Mailvalue).grid(row=3, column=3)

"""Check Button"""
agree = Checkbutton(text= "agree Term & Condition", variable = agree, pady=30).grid(row = 4, column=3)
"""MAking submit button"""
Button(text= "submit", command=form).grid(row=5, column=3)

root.mainloop()
