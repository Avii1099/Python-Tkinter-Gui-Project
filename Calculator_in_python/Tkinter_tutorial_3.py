""" 1. Create a MessageBox """
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title("_python.py_")
# root.geometry('350x200')
#
# def clicked():
#
#     messagebox.showwarning('Message title', 'Message content')
#
# btn = Button(root, text='Click here', command=clicked)
# btn.grid(column=0, row=0)
# root.mainloop()


"""2. Add a SpinBox (numbers widget) """
# from tkinter import *
#
# root = Tk()
#
# root.title("_python.py_")
# root.geometry('350x200')
#
# spin = Spinbox(root, from_=0, to=100, width=10)
# spin.grid(column=0, row=0)
#
# root.mainloop()

"""3. Add a Progressbar widget"""
# from tkinter import *
# from tkinter.ttk import Progressbar
# from tkinter import ttk
#
# root = Tk()
#
# root.title("_python.py_")
# root.geometry('350x200')
#
# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='green')
#
# bar = Progressbar(root, length=200, style='black.Horizontal.TProgressbar')
# bar['value'] = 50
# bar.grid(column=0, row=0)
#
# root.mainloop()

""" Add a Menu bar """
# from tkinter import *
# from tkinter import Menu
#
# root = Tk()
#
# root.title("_python.py_")
#
# menu = Menu(root)
#
# new_item = Menu(menu)
# new_item.add_command(label='New')
# new_item.add_separator()
# new_item.add_command(label='Edit')
# menu.add_cascade(label='File', menu=new_item)
#
# root.config(menu=menu)
#
# root.mainloop()

"""Add a Notebook widget (tab control)"""
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title("_python.py_")
# tab_control = ttk.Notebook(root)
#
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='First')
# tab_control.add(tab2, text='Second')
#
# lbl1 = Label(tab1, text='follow, like and share with your friend')
# lbl1.grid(column=0, row=0)
# lbl2 = Label(tab2, text= 'label2')
# lbl2.grid(column=0, row=0)
#
# tab_control.pack(expand=1, fill='both')
#
# root.mainloop()

#
# from tkinter import *
# from tkinter import ttk
#
# window=Tk()
#
# window.title("Welcome to LikeGeeks app")
#
# # Label that act as a "Title" something like an H1
# lbl=Label(window,text="Hello",font=("Arial Bold",50))
#
# lbl.grid(column=0,row=0)
#
# # Tabs
# tab_control=ttk.Notebook(window)
#
# tab1=ttk.Frame(tab_control)
#
# tab2=ttk.Frame(tab_control)
#
# tab_control.add(tab1,text='First')
#
# tab_control.add(tab2,text='Second')
#
# lbl1=Label(tab1,text='label1')
#
# lbl1.grid(column=0,row=2)
#
# lbl2=Label(tab2,text='label2')
#
# lbl2.grid(column=0,row=2)
# tab_control.grid()
#
#
# window.mainloop()



