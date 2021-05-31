import random
import time
from tkinter import *
from PIL import Image, ImageTk

# data for game
Question = {1: 'Noose Pay Perry Port', 2: 'Pretty Shack Scent', 3: 'Ape Hand Hub Hair', 4: 'Wand Her Womb Hen', 5: 'Whole Imp Pig Gains', 6: 'Sea Yule Hater', 7: 'Why Tail Huff Hunt', 8: 'Mike Ranch Healed Wren', 9: 'Ail Huck Each Arm', 10: 'Canoe Key Pass Egret', 11: 'Fur Chin Ollie Foil', 12: 'Isle of View', 13: 'Jog Clay Die Scream', 14: 'Law Duff There Inks', 15: 'Moe’s Art', 16: 'Pea Sank White', 17: 'Sand Track Laws', 18: 'Up Hair Hush Ooze', 19: 'Wheel Yum Air Ream He', 20: 'Yell Help Hey Jess', 21: 'Zola Reek Lips', 22: 'My Cull Chore Den', 23: 'Kenya Ear Mean How', 24: 'Tie Man Dug Hen', 25: 'Come Pew Turf High Russ', 26: 'Heart Official Ant Heller Gents', 27: 'Free Quaintly As Quest Shuns', 28: 'These Moe King Hun', 29: 'High Issues Home Hutch', 30: 'Lee On Hard Odie Cap Rio', 31: 'Mare Itch Prop Owes All', 32: 'These Hound Doff Moo Sick', 33: 'Nor Thumb Air Reckon', 34: 'Sadder Dane Height', 35: 'Wands Up Pawn Eight I"m', 36: 'Par Keens Pace', 37: 'Rome He Owe Hand Jewelry Yet', 38: 'Hoe Min Proof Mint', 39: 'Ace Heck Hunch Ants', 40: 'Mass Turk Hard', 41: 'Oar He Oak Hooky', 42: 'Lawn Hoarder', 43: 'Talk Toothy And', 44: 'Tack Seed Rye Fur', 45: 'Welk Hum Ohm', 46: 'Foyer Inn Form Hay Shun', 47: 'Kay Belt Ella Fission', 48: 'Weenie Toot Hawk', 49: 'Ewe Nigh Ted Kink Dumb', 50: 'Prey Tee Womb Anne', 51: 'Pay Perk Lips', 52: 'Bee Foreign Halved Her', 53: 'Law San Jail Lust Dimes', 54: 'Freeze Ham Pulse', 55: 'Arrest Mike Ace', 56: 'These Oop Ream Kurt', 57: 'Spar Cling What Her', 58: 'Win Airy Meds Alley', 59: 'fun elle eyes', 60: 'ayyy alex haha', 61 : 'knee code low eon'}

answer = {1: 'Newspaper Report', 2: 'British Accent', 3: 'A Panda Bear', 4: 'Wonder Woman', 5: 'Olympic Games', 6: 'See You Later', 7: 'White Elephant', 8: 'My Grandchildren', 9: 'A Lucky Charm', 10: 'Can You Keep A Secret', 11: 'Virgin Olive Oil', 12: 'I Love You', 13: 'Chocolate Ice Cream', 14: 'Lord of the Rings', 15: 'Mozart', 16: 'Peace and Quiet', 17: 'Santa Clause', 18: 'Up Hair Hush Ooze', 19: 'Will You Marry Me', 20: 'Yellow Pages', 21: 'Solar Eclipse', 22: 'Micheal Jordan', 23: 'Can You Hear Me Now', 24: 'Time and Again', 25: 'Computer Virus', 26: 'Artificial Intelligence', 27: 'Frequently Asked Questions', 28: 'The Smoking Gun', 29: 'I Miss You So Much', 30: 'Leonardo Dicaprio', 31: 'Marriage Proposal', 32: 'The Sound of Music', 33: 'North American', 34: 'Saturday Night Fever', 35: 'Once Upon A Time', 36: 'Parking Place', 37: 'Romeo & Juliet', 38: 'Home Improvement', 39: 'A Second Chance', 40: 'Mastercard', 41: 'Oreo Cookie', 42: 'Law and Order', 43: 'Talk to the Hand', 44: 'Taxi Driver', 45: 'Welcome Home', 46: 'For Your Information', 47: 'Cable Television', 48: 'We Need to Talk', 49: 'United Kingdom', 50: 'Pretty Woman', 51: 'Paperclips', 52: 'Before & After', 53: 'Los Angeles Times', 54: 'Free Samples', 55: 'I Rest My Case', 56: 'The Supreme Court', 57: 'Sparkling Water', 58: 'When Harry Met Sally', 59: 'vanilla ice', 60: 'hey alexa', 61 : 'nickelodeon'}

root = Tk()
root.geometry('380x500')
root.title('Guess the Gibberish')
root.config(bg='#ffff63')
root.resizable(False, False)
root.iconbitmap('game-console.ico')
# image for gibberish background
image1 = Image.open('Gibberish_back.png')
test = ImageTk.PhotoImage(image1)
Label(image= test, bg='#ffff63').place(x=0, y=70)

timer = 15
score = 0
# start game function
def StartGame():
    start_button.config(state=DISABLED, bg = 'grey')
    next_btn.config(state=DISABLED)
    show_ans_l.config(text='')
    RW.config(text='')
    global random_num, timer
    timer = 15
    random_num = random.randint(1,61)
    Question_label.config(text=Question[random_num])
    hint_label.config(text = 'Hint -> Number of words is : '+str(len(answer[random_num].split())))
    startcountdown()
    Ans_entry.bind('<Return>', Checkans)


def startcountdown():
    global timer
    if timer >= 0:
        time_label.config(text=str(timer))
        timer -= 1
        time_label.after(1000, startcountdown)
        if timer == -1:
            next_btn.config(state=NORMAL)
            show_ans_l.config(text='Right answer is : ' + answer[random_num].lower())
            Ans_entry.delete(0,END)

def Checkans(event):
    global score
    user = str(Ans_entry.get())
    if user.lower() == answer[random_num].lower():
        score += 1
        score_label.config(text = 'Your Score : ' + str(score))
        Ans_entry.delete(0, END)
        RW.config(text='RIGHT', fg='green')

    else:
        Ans_entry.delete(0, END)
        RW.config(text='WRONG', fg= 'red')
        show_ans_l.config(text='Right answer is : '+ answer[random_num].lower())

def Reset():
    global timer , score
    timer = 15
    score = 0
    score_label.config(text='Your Score : ' + str(score))
    time_label.config(text='15')
    Question_label.config(text='Guess The Gibberish')
    start_button.config(state=NORMAL)
    next_btn.config(state=DISABLED)
    hint_label.config(text='Hint -> Number of words is : ')
    Ans_entry.delete(0, END)

game_desp= 'Game Description: Guess The Gibberish Game is a free word \n puzzle game that will exercise your brain.it has words that \n are  made up but when spoken/write sound similar to a real word. \n \n After Click start button, Enter the answer in the displyed below \n and press enter.  for next round click on Next button '
Label(root, text=game_desp,fg='grey', bg='#ffff63', font='Helvetica 8').place(x=15, y=0)

Label(root, text='@_python.py_',fg='white', bg='#0597fe', font='Helvetica 12 bold').place(x=130, y=100)
Question_label = Label(root, text='Guess The Gibberish',fg='white', bg='#0597fe', font='Helvetica 15 bold')
Question_label.place(x=50, y=140)

time_label = Label(root, text= '15', font='Helvetica 18 bold', fg='white', bg='black')
time_label.place(x=178, y=216)

score_label = Label(root, text= 'Your Score : '+str(score), font='Helvetica 12 bold', fg='black', bg='#ffff63')
score_label.place(x = 130, y=280)

Ans_entry = Entry(root, width=25, font='Helvetica 12 bold')
Ans_entry.place(x = 35, y= 320)

hint_label = Label(root, text= 'Hint -> Number of words is : ', fg='black', bg='#ffff63')
hint_label.place(x=35, y=350)

next_btn = Button(root, text='Next', width=7, height= 1, bd = 0 , bg='grey', command= StartGame)
next_btn.place(x=270, y=320)

RW = Label(root, text='',fg='white', bg='#ffff63', font='Helvetica 13 bold')
RW.place(x = 150, y = 370)

show_ans_l = Label(root, text= ' ', font='Helvetica 12 bold', fg='black', bg='#ffff63')
show_ans_l.place(x = 40, y = 410)

btn_frame = Frame(root, width=40, height=40)
btn_frame.pack(side=BOTTOM)
start_button = Button(btn_frame, text='Start', width=20, bd = 0 , padx = 10, pady=10, bg='#a3ffc8', command= StartGame)
start_button.grid(row=0, column=0)
Button(btn_frame, text='Reset', width=20, bd = 0 , padx = 10, pady=10, bg='light blue', command = Reset).grid(row=0, column=1)

root.mainloop()



