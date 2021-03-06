from tkinter import *

root = Tk()
root.title("Event Handling")
root.geometry("200x100")

def avii(event):
    print("Hello User",event.x, event.y)
Widget = Button(root, text = "click")
Widget.pack()

Widget.bind('<Button-1>', avii)
Widget.bind('<Double-1>', quit)

root.mainloop()

