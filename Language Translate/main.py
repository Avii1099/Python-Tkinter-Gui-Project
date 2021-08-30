from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  # pip install pillow
from googletrans import Translator  # pip install googletrans==3.1.0a0
from tkinter import messagebox

root = Tk()
root.title('Langauge Translator')
root.geometry('530x330')
root.resizable(False, False)
root.config(bg='#6495ED')
root.iconbitmap('translate.ico') # this is for set app icon

# function for translate the language and set in t2 box
def translate():
    language_1 = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'please fill the box')
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(language_1, dest=cl)
        t2.insert('end', output.text)

# for clear the both t1 and t2 box
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')


img = ImageTk.PhotoImage(Image.open('translate.png'))
label = Label(image=img, bg='#6495ED')
label.place(x=230, y=3)

a = StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold') )

auto_detect['values'] = ('Auto Detect', )

auto_detect.place(x=30, y=70)
auto_detect.current(0)

l = StringVar()
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))

choose_langauge['values'] = (
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', ' Azerbaijani',
    'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', ' Catalan',
    'Cebuano', 'Chichewa', 'Chinese', 'Corsican', 'Croatian',' Czech',
    'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish',
    'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole',
    'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic',
    'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda',
    'Korean','Kurdish','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malagasy',
    'Malay','Malayalam','Maltese','Maori','Marathi','Mongolian','Myanmar','Nepali','Norwegian''Odia',
    'Pashto','Persian','Polish','Portuguese','Punjabi','Romanian','Russian','Samoan','Scots Gaelic','Serbian','Sesotho',
    'Shona','Sindhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik','Tamil','Tatar',
    'Telugu','Thai','Turkish','Turkmen','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa'
    'Yiddish','Yoruba','Zulu',
)

choose_langauge.place(x=290, y=70)
choose_langauge.current(0)

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root, text="Translate", width=10, font=('verdana', 10, 'bold'), cursor="hand2",
                command=translate, bg= '#323233' , fg='#fff')
button.place(x=150, y=280)

clear = Button(root, text="Clear", width=10, font=('verdana', 10, 'bold'), cursor="hand2",
               command=clear, bg= '#323233' , fg='#fff')
clear.place(x=280, y=280)

root.mainloop()