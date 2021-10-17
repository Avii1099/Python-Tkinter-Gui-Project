from tkinter import *
import smtplib 
from tkinter import messagebox


# making tkinter window  
root = Tk()
root.geometry('500x500')
root.title('Email Sender @_python.py_')
root.resizable(False, False)
root.config(bg="#fff")

# variable for Entry box  
Email = StringVar()
Password = StringVar()
To = StringVar()
Subject = StringVar()

# In this we make layout for sing in mail id 
def emaillogin():
    f = Frame(root, height=480, width=500, bg='#FFF')
    Label(f, text="Sign in", font=("Helvetica", 30, "bold"), bg='#FFF', fg="#2F9DFF").place(x=180, y=120)
    Label(f, text='to continue to Email', font=("Helvetica", 12, "bold"), fg='#666A6C', bg='#FFF').place(x=170, y=170)

    Label(f, text='Email', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=140, y=210)
    email = Entry(f, textvariable=Email, font=('calibre',10,'normal'), width=30, bg="#E2E2E2")
    email.place(x=140, y=230)

    Label(f, text='Password', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=140, y=280)
    password = Entry(f, textvariable=Password, font=('calibre',10,'normal'), width=30, bg="#E2E2E2", show="*")
    password.place(x=140, y=300)

    Button(f, text='NEXT',font=("Helvetica", 10, "bold"), bg='#2F9DFF', 
            fg="#FFF", command=mail_verification).place(x=300,y=330)
    
    Label(f, text='Note:',font=("Helvetica", 10, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=400)
    Label(f, text='1. If Mail Id is not working use different one.',font=("Helvetica", 8, "bold"), 
                    fg='#4C4A49', bg='#FFF').place(x=20, y=420)
    Label(f, text='2. Please remove also email authentication for testing this application.',font=("Helvetica", 8, "bold"), 
                    fg='#4C4A49', bg='#FFF').place(x=20, y=440)
    Label(f, text='   otherwise use fake/temporary Mail Id.',font=("Helvetica", 8, "bold"), 
                    fg='#4C4A49', bg='#FFF').place(x=20, y=460)

    f.place(x=0, y=0)


# here we make send mail layout like from, to, subject and text box
def mail_compose():
    global body
    f = Frame(root, height=480, width=500, bg='#FFF')
    Label(f, text='New Message', font=("Helvetica", 12, "bold"), fg='#fff', bg='#666A6C').place(x=20, y=20)

    Label(f, text='From', font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=60)
    Label(f, text=f"<{Email.get()}>", font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=80)

    Label(f, text='To', font=("Helvetica", 12), fg='#4C4A49', bg='#FFF').place(x=20, y=130)
    to = Entry(f, textvariable=To, font=('calibre',10,'normal'), width=50, bg="#E2E2E2")
    to.place(x=20, y=150)

    Label(f, text='Subject', font=("Helvetica", 12), fg='#4C4A49', bg='#FFF').place(x=20, y=170)
    subject = Entry(f, textvariable=Subject, font=('calibre',10,'normal'), width=50, bg="#E2E2E2")
    subject.place(x=20, y=190)

    Label(f, text='Body', font=("Helvetica", 12), fg='#4C4A49', bg='#FFF').place(x=20, y=210)
    body = Text(f, font=('calibre',10,'normal'), width=50, bg="#E2E2E2", height=12)
    body.place(x=20, y=230)
    
    Button(f, text='Send',font=("Helvetica", 10, "bold"), bg='#2F9DFF', fg="#FFF", command=mail_sending).place(x=20,y=440)
    f.place(x=0, y=0)



# here 1st we verify mail after that we call to
# mail_compose fun otherwise it's show error
def mail_verification():
    global server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:    
        server.login(Email.get(), Password.get())
        mail_compose()
    except Exception:
        messagebox.showerror('Sign in Error!', 'Please check your email id and password\notherwise use different mail id')

# after verfication we send mail from this function 
def mail_sending():
    subject = Subject.get()
    body_text = body.get("1.0", "end-1c")
    msg = f"Subject : {subject} \n\n {body_text}"
    server.sendmail(
        Email.get(), To.get(), msg )
    messagebox.showinfo("Success!", 'mail has been send')

if __name__ == '__main__':
    emaillogin()
    root.mainloop()

