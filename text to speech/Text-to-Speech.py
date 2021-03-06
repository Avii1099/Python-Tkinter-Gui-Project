# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initialized window
root = Tk()
root.geometry('320x230')
root.resizable(0, 0)
root.config(bg = '#FFE873')
root.title('TEXT_TO_SPEECH_@python.py_')


##heading
Label(root, text = 'TEXT TO SPEECH', font='arial 20 bold', bg ='#FFE873').pack()
Label(root, text ='@_python.py_', font ='arial 15 bold', bg = '#FFE873').pack(side = BOTTOM)
#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='#FFE873').place(x=20, y=60)
##text variable
Msg = StringVar()
#Entry
entry_field = Entry(root, textvariable =Msg, width ='50')
entry_field.place(x=20, y=100)

#define function
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('python.mp3')
    playsound('python.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY", font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=25, y=140)
Button(root, text = 'EXIT', font = 'arial 15 bold', command = Exit, bg = 'OrangeRed1').place(x=100, y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175, y =140)

#infinite loop to run program
root.mainloop()
