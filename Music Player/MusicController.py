import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import os

music_player = tkr.Tk()
music_player.title("Music Player @_python.py_")
music_player.geometry("450x350")
music_player.config(bg='#fff')
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='#404042', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

icon1 = tkr.PhotoImage(file='music.png')
icon2 = tkr.PhotoImage(file='stop.png')
icon3 = tkr.PhotoImage(file='pause.png')
icon4 = tkr.PhotoImage(file='play-button-arrowhead.png')

Button1 = tkr.Button(music_player, image=icon1, command=play)
Button2 = tkr.Button(music_player, image = icon2, command=stop)
Button3 = tkr.Button(music_player, image=icon3, command=pause)
Button4 = tkr.Button(music_player, image = icon4, command=unpause)

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 20 bold", textvariable=var, bg='#fff')

play_list.pack(fill="both", expand="no")
song_title.place(x=120, y=230)
Button1.place(x=100, y = 300)
Button2.place(x=170, y = 300)
Button3.place(x=240, y = 300)
Button4.place(x=310, y = 300)
music_player.mainloop()