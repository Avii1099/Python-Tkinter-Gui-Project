#importing modules

from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.configure(bg="#FFE873")

#title of the window
root.title("Message Encode and Decode..@_python.py_")

#label
Label(root, text ='ENCODE DECODE', font = 'arial 20 bold', bg="#FFE873").pack()
Label(root, text ='@_python.py_', font = 'arial 20 bold', bg="#FFE873").pack(side =BOTTOM)


#define variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
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
    if mode.get() =='e':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() =='d':
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
    mode.set("")
    Result.set("")


# Label and Button

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE', bg = '#FFE873').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = '#D5C6FF').place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY', bg = '#FFE873').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key, bg ='#D5C6FF').place(x=290, y = 90)


#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)', bg = '#FFE873').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode, bg= '#D5C6FF').place(x=290, y = 120)



#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='#D5C6FF').place(x=290, y = 150)

#result button
Button(root, font = 'arial 10 bold', text = 'RESULT', padx =2, bg ='Blue', command = Mode).place(x=60, y = 150)
#reset button
Button(root, font = 'arial 10 bold', text ='RESET', width =6, command = Reset, bg = 'LimeGreen', padx=2).place(x=160, y = 190)
#exit button
Button(root, font = 'arial 10 bold', text= 'EXIT', width = 6, command = Exit, bg = 'OrangeRed', padx=2, pady=2).place(x=260, y = 190)
root.mainloop()

