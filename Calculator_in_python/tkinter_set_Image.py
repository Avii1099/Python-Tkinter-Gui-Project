"""Here code about how set image in tkinter
                output window"""
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("900x900")
image = Image.open("insta.jpg")
photo = ImageTk.PhotoImage(image)

image_label = Label(image = photo)
image_label.pack(side= TOP, padx=10, pady=10)

root.mainloop()