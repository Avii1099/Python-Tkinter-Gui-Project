# from the tkinter library
from tkinter import *
# import filedialog module
from tkinter import filedialog
import moviepy
import moviepy.editor


root=Tk()
root.title('Mp4 to Mp3 @_python.py_')
root.geometry("400x320")
root.config(bg="#FFE873")

Label(root, text = 'Mp4 to Mp3', fg="#4B8BBE", bg="#FFE873", font="Verdana 30 bold").pack()
Label(root, text = '@_python.py_', fg="#4B8BBE", bg="#FFE873", font="Verdana 30 bold").pack()


# Function for opening the
def browseFiles():
    global filename
    filename=filedialog.askopenfilename(initialdir="/", title="Select a File",
                                        filetypes=(("Text files", "*.Mp4*"), ("all files", "*.*")))


    # Change label contents
    label_file_explorer.configure(text="File : "+filename)


# Function for convert Mp4 to Mp3
def changetomp3():
    video=moviepy.editor.VideoFileClip(filename)  # Put your file path in here
    # Convert video to audio
    audio=video.audio
    audio.write_audiofile('new_audio.mp3')



label_file_explorer = Label(root, text="File: ", width=50, height=4, fg="blue")
label_file_explorer.pack(anchor='center', pady=5)
Button(root, text="Browse Files", width=8, command=browseFiles).pack(anchor='center', pady=5)
Button(root, text="Convert", width=8, command=changetomp3).pack(anchor='center', pady=5)
Button(root, text="Exit", width=8, command=exit).pack(anchor='center', pady=5)

root.mainloop()

