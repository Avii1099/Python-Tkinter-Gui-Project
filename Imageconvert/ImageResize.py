'''Image Resize Project
    By : @_python.py_
     pip install python-resize-image
'''
import tkinter.ttk

from PIL import Image, ImageTk
import PIL.Image
from resizeimage import resizeimage
from tkinter import *
from tkinter import filedialog

# make Windows
root = Tk()
root.geometry('320x480')
root.title('Image Converter @_python.py_')
root.config(bg="#ffffff")

# set image on background
image = PIL.Image.open('img.jpeg')
test = ImageTk.PhotoImage(image)
Label(image = test, bg='#fff').pack()
# defina label for app name and developer name
Label(root, text='Image Converter', font='Verdana 20 bold', fg='#404042', bg="#ffffff").pack()
Label(root, text='@_python.py_', font='Verdana 10 bold', fg='#404042', bg="#ffffff").pack()
# variables for ask image width and height
width = IntVar()
height = IntVar()

# Define Label and Entry box for ask image size
Label(root, text='Size = ', font='Verdana 10 bold', fg='#404042', bg="#ffffff").place(x=10, y=280)
Label(root, text='X', font='Verdana 10 bold', fg='#404042', bg="#ffffff").place(x=166, y=280)
Label(root, text='Width', fg='#404042', bg="#ffffff").place(x=70, y=250)
Label(root, text='height', fg='#404042', bg="#ffffff").place(x=195, y=250)

# Entry Box
Entry(root, textvariable=width, font='Verdana 10 bold', fg='#404042', bg="#ffffff", borderwidth=3, width=9).place(x=70, y=280)
Entry(root, textvariable=height, font='Verdana 10 bold', fg='#404042', bg="#ffffff", borderwidth=3, width=9).place(x=190, y=280)

Label(root, text='Select Target Format', font='Verdana 10 bold', fg='#404042', bg="#ffffff").place(x=10, y= 330)
from1 = StringVar()
jpgto = tkinter.ttk.Combobox(root, width=10, textvariable= from1)
jpgto['values'] = (' PNG', ' GIF', ' ICO')
jpgto.place(x = 190, y = 330)
jpgto.current(0)

# function for select file for browser
def ChooseFile():
    global filename
    # Browse Files
    filename=filedialog.askopenfilename(initialdir="/", title="Select a File",
                                        filetypes=(("JPG File", "*.jpg*"), ("all files", "*.*")))
    # Change label contents
    label_file_explorer.configure(text="File : "+filename)


# function for convert image
def StartConvert():
    WSize = width.get()
    HSize = height.get()

    name = filename.split('/')
    finalname = name[-1].replace('.jpeg', '')

    with open(str(filename), 'r+b') as f:
        with PIL.Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [WSize, HSize])
            cover.save(f'{finalname}.{from1.get().strip().lower()}', image.format)

    Label(root, text='Image Convert Successfully', fg='#404042', bg="#ffffff",font='Verdana 10 bold').place(x=57, y=410)

# label for file explore
label_file_explorer = Label(root, text="File: ", width=50, height=4, fg="#404042", bg="#ffffff")
label_file_explorer.pack()

# design button for call to function
Button(root, text='Choose File',bg='#404042', fg='#ffffff', font='Verdana 10 bold', command=ChooseFile).place(x=40, y=380)
Button(root, text='Start Convert', bg='#404042', fg='#ffffff', font='Verdana 10 bold', command=StartConvert).place(x=180, y=380)
Label(root, text='Here, you can find an image \n converter for your needs, \nfor example, a jpg to png converter.',fg='#404042', bg="#ffffff").place(x = 57, y=430)
root.mainloop()
