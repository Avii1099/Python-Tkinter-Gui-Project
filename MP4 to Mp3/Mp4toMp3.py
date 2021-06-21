# from the tkinter library
from tkinter import *
# import filedialog module
from tkinter import filedialog
# install moviepy using pip install moviepy
import moviepy
import moviepy.editor
from PIL import Image, ImageTk


root=Tk()
root.title('Mp4 to Mp3 @_python.py_')
root.geometry("400x380")
root.config(bg="#ffffff")
root.iconbitmap("audio-converting.ico")

image1 = Image.open('MP4toMP3.png')
test = ImageTk.PhotoImage(image1)
Label(image = test, bg='#ffffff').pack()

Label(root, text = 'MP4 to MP3', fg="#404042", bg="#ffffff", font="Verdana 20 bold").pack()
Label(root, text = '@_python.py_', fg="#404042", bg="#ffffff", font="Verdana 10 bold").pack()


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

    audio.write_audiofile(f'{filename}.mp3')



label_file_explorer = Label(root, text="Choose File", width=50, height=2, fg="blue")
label_file_explorer.pack(anchor='center', pady=5)
Button(root, text="Browse Files", command=browseFiles, fg="#ffffff", bg="#404042", 
    font="Verdana 10 bold").place(x = 50, y= 250)
Button(root, text="Convert", width=12, command=changetomp3, fg="#ffffff", bg="#404042", 
    font="Verdana 10 bold").place(x = 210, y= 250)
Button(root, text="Exit",  width=12,command=exit, fg="#ffffff", bg="#404042", 
    font="Verdana 10 bold").place(x = 130, y= 290)

root.mainloop()

