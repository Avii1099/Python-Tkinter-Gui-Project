""" Making Image Viewer In Tkinter
    author : @_python.py_
            """
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer @_python.py_')
root.resizable(False, False)
root.iconbitmap('photo.ico')

#add image
my_img1 = ImageTk.PhotoImage(Image.open('img/1.1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('img/1.2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('img/1.3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('img/1.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('img/2.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('img/3.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('img/4.jpg'))
my_img8 = ImageTk.PhotoImage(Image.open('img/5.jpg'))
my_img9 = ImageTk.PhotoImage(Image.open('img/6.jpg'))
my_img10 = ImageTk.PhotoImage(Image.open('img/7.jpg'))

#add all image in list
image_list = [my_img1,  my_img3, my_img2, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10]

#making lapel for image
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# action on button for back , exit, forward
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image= image_list[image_number-1])
    button_forward = Button(root, text=" >> ", command= lambda:forward(image_number+1), font='Helvetica 15 bold')
    button_back = Button(root, text=" << ", command= lambda : back(image_number-1), font='Helvetica 15 bold')

    if image_number == 10:
        button_forward = Button(root, text=" >> ", state=DISABLED, font='Helvetica 15 bold')

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

    # Update Status bar
    status=Label(root, text='Image '+ str(image_number) +' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root, text=" >> ", command=lambda:forward(image_number+1) ,font='Helvetica 15 bold')
    button_back=Button(root, text=" << ", command=lambda:back(image_number-1), font='Helvetica 15 bold')

    if image_number == 1:
        button_back=Button(root, text=" << ", state=DISABLED)

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

    # Update Status bar
    status=Label(root, text='Image '+ str(image_number) +' of '+str(len(image_list)), bd=1, relief=SUNKEN,    anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#set button on the root screen
button_back = Button(root, text=" << ",  command=back, state=DISABLED , font='Helvetica 15 bold').grid(row=1, column=0)
button_exit = Button(root, text=" EXIT ", command= exit , font='Helvetica 15 bold').grid(row=1, column=1, pady=10)
button_forward = Button(root, text=" >> ",  font='Helvetica 15 bold', command=lambda: forward(2)).grid(row=1, column=2)

root.mainloop()


