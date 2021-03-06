from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube video downloader @_python.py_")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
Label(root,text = '@_python.py_', font ='arial 15 bold').pack()

#enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 70)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 110)

#function to download video

def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
