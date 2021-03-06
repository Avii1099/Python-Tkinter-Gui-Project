"""Here code about Tkinter. We learn How make window
                and set label"""
from tkinter import *

root = Tk()
root.title("Basic")
#Size of your output window width x height
root.geometry("600x400")
#MAxSize of your output window width x height
root.maxsize(900, 900)
#MinSize of your output window width x height
root.minsize(250, 40)
#Set Your label
label1 = Label(text="Hello World")
label1.pack()
root.mainloop()
