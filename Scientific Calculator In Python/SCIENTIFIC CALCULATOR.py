from tkinter import *
import os
import time
from math import *


root=Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title('SCIENTIFIC CALCULATOR')
root.iconbitmap('calculator.ico')



def GetValue(event):
    value = event.widget.cget('text')
    if value=='Clr':
        sc_variable.set('')
    elif value=='=':
        try:
            print(screen.get())
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error8')
            screen.update()
            time.sleep(1)
            sc_variable.set('')
            screen.update()


    else:
        sc_variable.set(f'{sc_variable.get()}{value}')


my_menu=Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label='Exit',command=quit)


sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 27 bold',fg='black',bg='white',borderwidth=7)
screen.pack(pady=30)


f=Frame(root)
f.pack()
b1=Button(f,text='7',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b2=Button(f,text='8',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b3=Button(f,text='9',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b4=Button(f,text='*',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b5=Button(f,text='sin',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b6=Button(f,text='(',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b1.bind('<Button-1>',GetValue)
b2.bind('<Button-1>',GetValue)
b3.bind('<Button-1>',GetValue)
b4.bind('<Button-1>',GetValue)
b5.bind('<Button-1>',GetValue)
b6.bind('<Button-1>',GetValue)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
        buttons[count].grid(row=1,column=i)
        count += 1


f=Frame(root)
f.pack()
b1=Button(f,text='4',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b2=Button(f,text='5',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b3=Button(f,text='6',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b4=Button(f,text='-',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b5=Button(f,text='cos',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b6=Button(f,text=')',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)


b1.bind('<Button-1>',GetValue)
b2.bind('<Button-1>',GetValue)
b3.bind('<Button-1>',GetValue)
b4.bind('<Button-1>',GetValue)
b5.bind('<Button-1>',GetValue)
b6.bind('<Button-1>',GetValue)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=2,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='1',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b2=Button(f,text='2',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b3=Button(f,text='3',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b4=Button(f,text='+',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b5=Button(f,text='tan',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b6=Button(f,text='%',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)


b1.bind('<Button-1>',GetValue)
b2.bind('<Button-1>',GetValue)
b3.bind('<Button-1>',GetValue)
b4.bind('<Button-1>',GetValue)
b5.bind('<Button-1>',GetValue)
b6.bind('<Button-1>',GetValue)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=3,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='.',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b2=Button(f,text='0',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b3=Button(f,text='sinh',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b4=Button(f,text='cosh',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b5=Button(f,text='tanh',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b6=Button(f,text='pi',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b1.bind('<Button-1>',GetValue)
b2.bind('<Button-1>',GetValue)
b3.bind('<Button-1>',GetValue)
b4.bind('<Button-1>',GetValue)
b5.bind('<Button-1>',GetValue)
b6.bind('<Button-1>',GetValue)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=4,column=i)
    count += 1
f=Frame(root)
f.pack()

b1=Button(f,text='log10',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b2=Button(f,text='exp',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b3=Button(f,text='/',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b4=Button(f,text='Clr',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b5=Button(f,text='log',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)

b6=Button(f,text='=',font='lucida 9 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='#FFE873',width=3)


b1.bind('<Button-1>',GetValue)
b2.bind('<Button-1>',GetValue)
b3.bind('<Button-1>',GetValue)
b4.bind('<Button-1>',GetValue)
b5.bind('<Button-1>',GetValue)
b6.bind('<Button-1>',GetValue)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=5,column=i)
    count += 1
root.mainloop()
