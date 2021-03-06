from tkinter import *
from PIL import Image , ImageTk

arvind_root = Tk()
# #size of window in width x height
arvind_root.title("Calculator")
arvind_root.geometry("900x400")

# #set minimum width and height
arvind_root.minsize(480, 233)
arvind_root.maxsize(1080, 1080)
#
# #making label
# arvind = Label(text="Hello World")
# arvind.pack()
#
#
# #set image
# # image = Image.open("insta.jpg")
# # photo = ImageTk.PhotoImage(image)
# # arvind_label = Label(image=photo)
# # arvind_label.pack()
#
# # read label function
# title_label = Label(text='''When it comes to Graphical User Interface
#                             \nbased application, image(s) play a vital
#                             \nrole. From the application icon to animation,
#                             \nit's useful.
#                             \nTo display images in labels, buttons, canvases,
#                             \nand text widgets, the PhotoImage class is used,
#                             \nwhich is present in tkinter package.''',
#                     bg="yellow", fg="black", padx=23, pady=94, font=("comicsansms",
#                                 19, "bold"), borderwidth=3, relief=SUNKEN)
# #import pack option
# title_label.pack(side='bottom', fill=X, padx=30, pady=30)
# title_label.pack()

#Making Frame
# f1 = Frame(arvind_root, bg="red", borderwidth= '4', relife=SUNKEN)
# f1.pack(side=TOP, fill=X)
#
# l = Label(f1, text="Hello World - Notepad")
# l.pack()

# def hello():
#     print("Hello Python")
#
# """Making a button"""
# frame = Frame(arvind_root, borderwidth=6, bg='grey', relief= SUNKEN)
# frame.pack(side = LEFT, anchor = 'nw')
#
# b1 = Button(frame, fg= "red", text="Submit", command=hello)
# b1.pack(side=LEFT)
# b2 = Button(frame, fg= "red", text="Submit")
# b2.pack(side=LEFT )
# b3 = Button(frame, fg= "red", text="Submit")
# b3.pack(side=LEFT)



arvind_root.mainloop()



