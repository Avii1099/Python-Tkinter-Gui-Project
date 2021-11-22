import sqlite3
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# ____________ SQLLite database connection _______________-
cnt = sqlite3.connect("To_DO.db")
cnt.execute('''CREATE TABLE IF NOT EXISTS to_do_data ( task TEXT, date DATE, time TIME TEXT)''')
cnt.cursor()

#__________ function for add task in database _____________
def add_task():
    global entry_box
    date_time = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = date_time.strftime("%d/%m/%Y %H:%M")
    if len(entry_box.get()) != 0:
        cnt.execute("INSERT INTO to_do_data VALUES (:task, :date, :time)", {
                        'task': str(entry_box.get()).strip(),
                        'date': str(dt_string[:10]),
                        'time': str(dt_string[10:])})
        cnt.commit()
        entry0.delete(0, 'end')
        task_list()
    else:
        messagebox.showerror('Add Task', 'Please write your task name')

#__________ delete task acording select task in listbox___
def delete_task():
    try: 
        val = int(list1.curselection()[0])
        data_list = (list1.get(val)).split("    ")
        cnt.execute("DELETE FROM to_do_data WHERE task='%s'"% str(data_list[1]))
        cnt.commit()
        task_list()
    except:
        messagebox.showerror('Select Task', 'Please select task from task List')

# ___________ design window _______________
window = Tk()
window.geometry("700x400")
window.configure(bg = "#ffffff")
window.title("To-Do @_python.py_")


global entry_box
entry_box = StringVar()

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#____ create ractangle blue color and add text/image __________

canvas.create_rectangle( 0, 0, 0+250, 0+400, 
    fill = "#50A0FF", outline = "")

canvas.create_text( 110, 36.0, text = "To-Do GUI",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(32.0)))

canvas.create_text( 88, 73.0, text = "Application",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(24.0)))

canvas.create_text(88.0, 110.5, text = "@_python.py_",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(18.0)))

canvas.create_text( 55.0, 150.5, text = "To-Do: ",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(18.0)))
canvas.create_text( 120.0, 180.5, text = "FOLLOW, LIKE, COMMENT",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(12.0)))

image = Image.open('image/img3.png')
image1 = ImageTk.PhotoImage(image)
Label(canvas, image=image1 , bg="#50A0FF").place(x=15, y=200)

#______________ add task list entry box  _____________

canvas.create_text( 305, 50.5, text = "Create a to-do",
    fill = "#000000",
    font = ("None", int(8.0)))

canvas.create_text( 310.0, 28.0, text = "Add Task",
    fill = "#000000",
    font = ("Roboto-Medium", int(14.0)))

entry0_img = PhotoImage(file = f"image/img_textBox0.png")
entry0_bg = canvas.create_image( 382.5, 78.0,
    image = entry0_img)

entry0 = Entry( bd = 0, bg = "#e5e5e5",
    highlightthickness = 0,
    textvariable= entry_box)

entry0.place( x = 274.0, y = 65, width = 217.0,
    height = 24)


img0 = PhotoImage(file = f"image/img0.png")
b0 = Button(image = img0, borderwidth = 0,
    highlightthickness = 0,
    command = add_task, relief = "flat")

b0.place( x = 510, y = 64, width = 31,
    height = 28)

# _____________________Delete Task Button________________
  
img_delete = PhotoImage(file = f"image/img_delete.png")
b1 = Button(image=img_delete, borderwidth = 0, highlightthickness = 0,
    relief = "flat", 
    command=delete_task,
    bg='#65daff', fg='#fff',
    font= ("Roboto-Medium", int(12.0)))

b1.place( x = 567, y = 120,)

##______________ SHOW TASK LIST ___________
canvas.create_text( 310.0, 130.0, text = "Task List",
    fill = "#000000",
    font = ("Roboto-Medium", int(14.0)))

def task_list():
    global list1
    records = cnt.execute("SELECT * FROM to_do_data")
    show = ""

    scrollbar = Scrollbar(canvas, width=15)
    scrollbar.place(x = 645, y=155,  relheight=0.5)
    list1 = Listbox(canvas,  bg = "#fff", font = ("None", 13), relief='flat', 
                    width=40, selectmode=SINGLE, 
                    yscrollcommand=scrollbar.set)
    list1.place(x=272, y=155)
    scrollbar.config(command=list1.yview)
    id1 = 0
    for task, date, time in records:
        id1 += 1 
        show = str(id1)+"    "+task+"       "+date+"  "+time +"\n"
        list1.insert(END, show)
    

task_list()
 
window.resizable(False, False)
window.mainloop()
