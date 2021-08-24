# install the all package
from bs4 import BeautifulSoup
import requests
from tkinter import *
from PIL import Image

# making tkinter window
root = Tk()
root.geometry("450x300")
root.title('Weather App @_python.py_')
root.resizable(False, False)

# this is our app icon .. download all file from github
root.iconbitmap('cloudy.ico')

# set frames for show different content and color in window
frame1 = Frame(root, bg='#fff', width=450, height=200)
frame1.place(x=0, y=0)

frame2 = Frame(root, bg='#2E2E2E', width=300, height=100)
frame2.place(x=0, y=200)

frame3 = Frame(root, bg='#33FFDD', width=150, height=100)
frame3.place(x=300, y=200)

# here i set gif for make our app more look good
# start animation
file = 'cloud.gif'
info = Image.open(file)
frames = info.n_frames
im = [PhotoImage(file = file, format=f'gif -index {i}') for i in range(frames)]
count = 0
anim = None

def animation(count):
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frames:
        count = 0
    anim = root.after(50, lambda: animation(count))


gif_label = Label(root, image="", bg="#fff")
gif_label.place(x=120, y=15)

# End animation

# weather details - Start
global city
city = StringVar()

# make entry box take city name
Label(root,  text="Enter the City Name", font=("Arial Rounded MT Bold", 12), bg="#fff").place(x=150, y=0)
entry = Entry(root, textvariable=city, width=22, bg='#D0FFBC')
entry.place(x=130, y=25)

# if user agent not work search on chrome my user agent otherwise update chrome
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def Weather():
    global city
    city1 = city.get() + " weather"
    city1 = city1.replace(" ", "+")

    res = requests.get(f'https://www.google.com/search?q={city1}&oq={city1}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
                       headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    print(soup.select('#wob_dts'))
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    Label(root, text=location, font='Caveat 12 bold', bg="#2E2E2E", fg='#fff').place(x=130, y=250)
    Label(root, text=info, font='ROBOTO 15 bold', bg="#2E2E2E", fg='#fff').place(x=130, y=220)
    Label(root, text=f'{weather}°C', font='ROBOTO 35 bold', bg="#2E2E2E", fg='#fff').place(x=5, y=220)

    time = time.split(',')
    Label(root, text=time[0], font='Caveat 20 bold', bg="#33FFDD", fg='#2E2E2E').place(x=330, y=210)
    Label(root, text=time[1].upper(), font='ROBOTO 15 bold', bg="#33FFDD", fg='#2E2E2E').place(x=325, y=240)
    entry.delete('0', END)

Button(root, text='Check', font=("Arial Rounded MT Bold", 8), bg="#D0FFBC", command=Weather).place(x = 280, y=25)

# Weather Details End
animation(count)

root.mainloop()



