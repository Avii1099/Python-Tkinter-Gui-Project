# open cmd and run pip install speedtest
from speedtest import Speedtest
from tkinter.ttk import *
from tkinter import *
import threading


root = Tk()
root.title("Internet Speed Tracker")
root.geometry('380x220')
root.resizable(False, False)
root.configure(bg="#FFE873")
root.iconbitmap('speed.ico')

# design Label
Label(root, text ='INTERNET SPEED', bg='#FFE873', fg='#4B8BBE', font = 'arial 25 bold').pack()
Label(root, text ='@_python.py_', bg='#FFE873', fg='#4B8BBE', font = 'arial 15 bold').pack(side =BOTTOM)

# making label for show internet speed
down_label = Label(root, text="Download Speed - ", bg='#FFE873', font = 'arial 10 bold')
down_label.place(x = 90, y= 50)
up_label = Label(root, text="Upload Speed - ", bg='#FFE873', font = 'arial 10 bold')
up_label.place(x = 90, y= 80)

# function for check spped
def check_speed():
    global download_speed, upload_speed
    speed_test=Speedtest()
    download=speed_test.download()
    upload=speed_test.upload()
    download_speed=round(download / (10 ** 6), 2)
    upload_speed=round(upload / (10 ** 6), 2)

# function for progress bar and update text
def update_text():
    thread=threading.Thread(target=check_speed, args=())
    thread.start()
    progress=Progressbar(root, orient=HORIZONTAL,
                         length=210, mode='indeterminate')
    progress.place(x = 85, y = 110)
    progress.start()
    while thread.isAlive():
        root.update()
        pass
    down_label.config(text="Download Speed - "+str(download_speed)+"Mbps")
    up_label.config(text="Upload Speed - "+str(upload_speed)+"Mbps")

    progress.stop()
    progress.destroy()

# button for call to function
button = Button(root, text="Check Speed", width=30, bd = 0, bg = 'light blue', pady = 5, command=update_text)
button.place(x=85, y = 140)
root.mainloop()

