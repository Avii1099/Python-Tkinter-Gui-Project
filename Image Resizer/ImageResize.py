"""Image Resize Project
    By : @_python.py_
     pip install python-resize-image
"""
import tkinter.ttk

from PIL import ImageTk
import PIL.Image
from resizeimage import resizeimage
from tkinter import *
from tkinter import filedialog

# color
foreground = "#404042"
background = "#ffffff"
font_max_size = "Verdana 20 bold"
font_min_size = "Verdana 10 bold"
filename = ""


# make Windows
root = Tk()
root.geometry("320x480")
root.title("Image Converter @_python.py_")
root.config(bg=background)


# set image on background
image = PIL.Image.open("crop.png")
test = ImageTk.PhotoImage(image, size=("10", "10"))
Label(image=test, bg="#fff").pack()

# define label for app name and developer name
Label(root, text="Image Converter", font=font_max_size, fg=foreground, bg=background).pack()
Label(root, text="@_python.py_", font=font_min_size, fg=foreground, bg=background).pack()

# variables for ask image width and height
width, height = IntVar(), IntVar()

# Define Label and Entry To enter image resize size
Label(root, text="Size = ", font=font_min_size, fg=foreground, bg=background).place(x=10, y=280)
Label(root, text="X", font=font_min_size, fg=foreground, bg=background).place(x=166, y=280)
Label(root, text="Width", fg=foreground, bg=background).place(x=70, y=250)
Label(root, text="height", fg=foreground, bg=background).place(x=195, y=250)

# Entry Box
Entry(
    root,
    textvariable=width,
    font=font_min_size,
    fg=foreground,
    bg=background,
    borderwidth=3,
    width=9,
).place(x=70, y=280)

Entry(
    root,
    textvariable=height,
    font=font_min_size,
    fg=foreground,
    bg=background,
    borderwidth=3,
    width=9,
).place(x=190, y=280)


combobox_dict = {
    "image_ext": (" PNG", " GIF", " ICO"),
    "predefined_size": (" Instagram Post", " Instagram Story", " IPhone X", " Android 1080p", " Apple Watch"),
}

extension, selected_size = StringVar(), StringVar()
image_ext = tkinter.ttk.Combobox(root, width=10, textvariable=extension)
predefined_size = tkinter.ttk.Combobox(root, width=10, textvariable=selected_size)
image_ext["values"] = combobox_dict.get("image_ext")
predefined_size["values"] = combobox_dict.get("predefined_size")
image_ext.place(x=190, y=330)
predefined_size.place(x=190, y=370)
image_ext.current(0)
predefined_size.current(0)

Label(
    root,
    text="Select Target Format",
    font=font_min_size,
    fg=foreground,
    bg=background,
).place(x=10, y=330)

Label(
    root,
    text="Predefined Size ",
    font=font_min_size,
    fg=foreground,
    bg=background,
).place(x=10, y=370)


# function for select file for browser
def choose_file():
    global filename
    # Browse Files
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("JPG File", "*.jpg*"), ("all files", "*.*")),
    )
    # Change label contents
    label_file_explorer.configure(text="File : " + filename)


# function for convert image
def start_convert():
    sizes = {
        "Instagram Post": "1080x1080",
        "Instagram Story": "1080x1920",
        "IPhone X": "1125x2436",
        "Android 1080p": "1080x1920",
        "Apple Watch": "312x390",
    }

    width_size, height_size = width.get(), height.get()

    if not width_size or not height_size:
        size_list = sizes.get(predefined_size.get().strip(), "1080x1080").split("x")
        width_size, height_size = int(size_list[0]), int(size_list[1])

    if not filename:
        tkinter.messagebox.showwarning("error", "Please select file")

    name = filename.split("/")
    final_name = name[-1].split(".")
    final_name = final_name[0] if len(final_name) > 1 else final_name

    with open(str(filename), "r+b") as f:
        with PIL.Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [width_size, height_size])
            cover.save(f"{final_name}.{extension.get().strip().lower()}", image.format)

    Label(
        root,
        text="Image Convert Successfully",
        fg=foreground,
        bg=background,
        font=font_min_size,
    ).place(x=57, y=450)


# label for file explore
label_file_explorer = Label(root, text="File: ", width=50, height=4, fg=foreground, bg=background)
label_file_explorer.pack()

# design button
Button(
    root,
    text="Choose File",
    bg=foreground,
    fg=background,
    font=font_min_size,
    command=choose_file,
).place(x=40, y=410)
Button(
    root,
    text="Start Convert",
    bg=foreground,
    fg=background,
    font=font_min_size,
    command=start_convert,
).place(x=180, y=410)

root.mainloop()
