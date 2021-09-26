from tkinter import *
import sqlite3
import math 
import random
import smtplib
from tkinter import messagebox

# create databse and table
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    username text, 
                    password text,
                    email text
                )
            ''')
con.commit() 

#create window
root = Tk()
root.geometry('500x450')
root.title('Login Registration form')
root.resizable(False, False)

# variable to hold entry widget data 
fullname = StringVar()
username = StringVar()
password = StringVar()
username_lo = StringVar()
password_lo = StringVar()
email = StringVar()
otp = StringVar()

# insert data on our record 
def insert_record():
    count = 0
    warn = ''

    if fullname.get() == '':
        warn = "Name can't be empty"
    else:
        count += 1
    
    if username.get() == '':
        warn = "Username can't be empty"
    else:
        count += 1
    
    if email.get() == '':
        warn = "Email - id can't be empty"
    else:
        count += 1
    
    if password.get() == '':
        warn = "Password can't be empty"
    else:
        count += 1
    
    if count == 4:
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :username, :password, :email)", {
                'name': fullname.get(),
                'username': username.get(),
                'password': password.get(),
                'email': email.get()

            })
            con.commit()
            otpverficitation()
        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)

# select data from records   
def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            usern = row[1]
            passwo = row[2]

    except Exception as ep:
        messagebox.showerror('', ep)
    count = 0
    if username_lo.get() == "":
        warn = "Username can't be empty"
    else:
       count += 1
    
    if password_lo.get() == "":
        warn = "Password can't be empty"
    else:
       count += 1
    
    if count == 2:
        if usern == username_lo.get() and passwo == password_lo.get():
            messagebox.showinfo('Login Status', 'Logged in Successfully!')

        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)


def login():
    f = Frame(root, height=450, width=500, bg='#FFBA41')
    Label(f, text='Login', font=("Helvetica", 30, "bold"), bg='#FFBA41').place(x=200, y=120)
    Label(f, text='Fill all form field to go to next step', font=("Helvetica", 12, "bold"), fg='#666A6C', bg='#FFBA41').place(x=140, y=170)
    Label(f, text='Username', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=200)
    user = Entry(f, textvariable=username_lo, font=('calibre',10,'normal'), width=30)
    user.place(x=150, y=220)
    Label(f, text='Password', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=250)
    passw = Entry(f, textvariable=password_lo, font=('calibre',10,'normal'), width=30, show="*")
    passw.place(x=150, y=270)
    Button(f, text='Log in',font=("Helvetica", 15, "bold"), bg='#00B6FF', command=login_response).place(x=220,y=300)
    Label(f, text="Don't have account", font=("Helvetica", 12, "bold"), fg='#666A6C', bg='#FFBA41').place(x=140, y=350)
    Button(f, text='Register Here',font=("Helvetica", 8, "bold"), bg='#FFBA41', command=registration).place(x=300,y=350)
    f.place(x=0, y=0)


def registration():
    f = Frame(root, height=450, width=500, bg='#FFBA41')
    Label(f, text='Registration',  font=("Helvetica", 30, "bold"), bg='#FFBA41').place(x=140, y=60)

    Label(f, text='Full Name', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=120)
    Entry(f, textvariable=fullname, font=('calibre',10,'normal'), width=30).place(x=150, y=140)

    Label(f, text='Username', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=170)
    Entry(f, textvariable=username, font=('calibre',10,'normal'), width=30).place(x=150, y=190)

    Label(f, text='Email Id', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=220)
    Entry(f, textvariable=email, font=('calibre',10,'normal'), width=30).place(x=150, y=240)

    Label(f, text='Password', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=270)
    Entry(f, textvariable=password, font=('calibre',10,'normal'), width=30).place(x=150, y=290)

    Button(f, text='Register',font=("Helvetica", 15, "bold"), bg='#00B6FF', command = insert_record).place(x=200,y=330)

    Label(f, text="Already have account", font=("Helvetica", 12, "bold"), fg='#666A6C', bg='#FFBA41').place(x=120, y=380)
    Button(f, text='Login Here',font=("Helvetica", 8, "bold"), bg='#FFBA41', command=login).place(x=300,y=380)
    f.place(x=0, y=0)

def otpverficitation():
    global OTP
    digits = "0123456789"
    OTP = ""
 
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    print(OTP)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your email', 'password')
    subject = 'Your OTP is: '
    body = OTP

    msg = f"Subject : {subject} \n\n {body}"

    server.sendmail(
        'your mail', 'sender mail', msg )

    print('Mail has been send')

    f = Frame(root, height=450, width=500, bg='#FFBA41')
    Label(f, text='OTP Verification', font=("Helvetica", 30, "bold"), bg='#FFBA41').place(x=100, y=120)

    Label(f, text='OTP is send please check your mail', font=("Helvetica", 12, "bold"), fg='#666A6C', 
    bg='#FFBA41').place(x=120, y=170)

    Label(f, text='Verfy Code:', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFBA41').place(x=150, y=200)
    Entry(f, textvariable=otp, font=('calibre',10,'normal'), width=30).place(x=150, y=230)

    Button(f, text='Verify',font=("Helvetica", 12, "bold"), bg='#00B6FF', 
            command=lambda : verify(otp.get())).place(x=150,y=260)
    Button(f, text='Resend',font=("Helvetica", 12, "bold"), bg='#00B6FF').place(x=230,y=260)
    f.place(x=0, y=0)

def verify(entryotp):
    
    global OTP
    
    if entryotp == OTP:
        messagebox.showinfo('confirmation', 'Record Saved')
        login()
    else:
        messagebox.showerror('Wrong', 'Please Enter Valied OTP')


login()
root.mainloop()