#importing Libraries

from tkinter import *
import random, string
import pyperclip

#initialize window

root =Tk()
root.geometry("400x250")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")
root.configure(bg="#FFE873")
root.iconbitmap("password.ico")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR', font ='arial 15 bold', bg="#FFE873").pack()
Label(root, text ='@_python.py_', font ='arial 15 bold', bg="#FFE873").pack(side = BOTTOM)

pass_len = IntVar()
pass_str = StringVar()


###select password length
Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold', bg="#FFE873").place(x = 50, y= 50)
length = Spinbox(root, from_= 8, to_ = 32, textvariable = pass_len, width = 15).place(x = 200, y= 50)
# YOUR PASSWORD
Label(root, text = 'YOUR PASSWORD', font = 'arial 10 bold', bg="#FFE873").place(x = 50, y= 80)
Entry(root, textvariable = pass_str).place(x = 200, y= 80)


#####define function



def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase)+\
                   random.choice(string.ascii_lowercase)+\
                   random.choice(string.digits)+\
                   random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase +
                                          string.ascii_lowercase +
                                          string.digits +
                                          string.punctuation)
    pass_str.set(password)


def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text = "GENERATE PASSWORD", command = Generator).place(x = 50, y= 120)
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).place(x = 200, y= 120)


# loop to run program
root.mainloop()


