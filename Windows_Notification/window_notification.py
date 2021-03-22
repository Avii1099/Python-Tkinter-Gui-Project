from plyer import notification
import tkinter as tk
from tkinter import *
from tkinter import filedialog


# making window
root = tk.Tk()
root.geometry("490x270")
root.title('Notification App')
root.configure(bg="#FFE873")
root.resizable(False, False)

# making variable
title_v = StringVar()
message_v = StringVar()

# design Label
Label(root, text="Windows Notification App", bg="#FFE873", fg='#4B8BBE', font="Verdana 20 bold").pack()
Label(root, text="Title", bg="#FFE873", font="Verdana 10 bold").place(x=60, y=50)
Entry(text="Title", width=50,  textvariable = title_v).place(x=150, y=50)

Label(root, text="Message", bg="#FFE873", font="Verdana 10 bold").place(x=60, y=80)
Entry(root, width=50, textvariable = message_v).place(x=150, y=80)

Label(root, text="Icon Path", bg="#FFE873", font="Verdana 10 bold").place(x = 60, y = 120)
label_file_explorer=Label(root, text="Icon: ", width=44, fg= "blue")
label_file_explorer.place(x = 150, y=120)

# Making Function for select icon
def select_icon():
    global filename
    filename=filedialog.askopenfilename(initialdir="/", title="Select a File",
                                        filetypes=(("ICO file ", "*.ico*"), ("all files", "*.*")))
    # Change label contents
    label_file_explorer.configure(text="Icon : "+filename)

# Making Function for send notification
def send_Notification():

    notification.notify(
        title=str(title_v.get()),
        message=str(message_v.get()),
        app_icon= filename,
        timeout=10,  # seconds
     )

# def clear
def clear():
    title_v.set('')
    message_v.set('')


# design button
Button(root, text="Select Icon", width=15, command=select_icon).place(x = 60, y = 190)
Button(root, text="Send Notification", width=15, command= send_Notification).place(x = 190, y = 190)
Button(root, text="Clear", width=15, command= clear).place(x = 320, y = 190)

root.mainloop()

