#importing modules

from tkinter import *
import base64
from PIL import Image, ImageTk

#initialize window
root = Tk()
root.geometry('500x400')
root.resizable(0, 0)
root.configure(bg="#FFE873")
root.iconbitmap('shield.ico')

#title of the window
root.title("Message Encode and Decode..@_python.py_")

image1 = Image.open('shield.png')
test = ImageTk.PhotoImage(image1)
Label(image = test, bg='#FFE873').pack()

#label
Label(root, text ='ENCODE DECODE', font = 'arial 20 bold', bg="#FFE873").pack()
Label(root, text ='@_python.py_', font = 'arial 20 bold', bg="#FFE873").pack(side =BOTTOM)


#define variables
Text = StringVar()
private_key = StringVar()
mode_en = StringVar(root, '1')
Result = StringVar()

#define function

#function to encode
def Encode(key, message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key, message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))

    return "".join(dec)

#function to set mode
def Mode():
    if mode_en.get() =='1':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode_en.get() =='2':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')




#Function to exit window

def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode_en.set("")
    Result.set("")


# Label and Button

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE', bg = '#FFE873').place(x= 60, y=180)
Entry(root, font = 'arial 10', textvariable = Text, bg = '#D5C6FF').place(x=290, y = 180)

#key
Label(root, font = 'arial 12 bold', text ='KEY', bg = '#FFE873').place(x=60, y = 210)
Entry(root, font = 'arial 10', textvariable = private_key, bg ='#D5C6FF').place(x=290, y = 210)

values = {
    '1':'Encode',
    '2':'Decode'
}
#mode
Label(root, font = 'arial 12 bold', text ='MODE', bg = '#FFE873').place(x=60, y = 240)
for text, value in values.items():
    if text=='1': Radiobutton(root, text=value, variable=mode_en, value=text,  font = 'arial 10 bold', bg="#FFE873").place(x=290,y=240)
    Radiobutton(root,text=value,variable=mode_en, value=text,  font = 'arial 10 bold', bg="#FFE873").place(x=360,y=240)



#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='#D5C6FF').place(x=290, y = 270)

#result button
Button(root, font = 'arial 10 bold', text = 'RESULT', bg ='white', fg='black', command = Mode).place(x=60, y = 270)
#reset button
Button(root, font = 'arial 10 bold', text ='RESET', width =6, command = Reset, bg = 'LimeGreen', padx=2).place(x=160, y = 310)
#exit button
Button(root, font = 'arial 10 bold', text= 'EXIT', width = 6, command = Exit, bg = 'OrangeRed', padx=2, pady=2).place(x=260, y = 310)
root.mainloop()

