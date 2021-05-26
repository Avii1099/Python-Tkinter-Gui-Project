from tkinter import *
from tkinter import messagebox as MsgBox
from PIL import Image, ImageTk


# X starts so True


clicked=True
count=0
# disable all buttons when winner is win

def WithPlayer():

    # Design the window
    root = Tk()
    root.geometry("550x390")
    root.title('Tic Tac Toe Friend')
    root.resizable(False, False)
    root.config(bg="yellow")
    root.iconbitmap('tic-tac-toe-icon.ico')

    image1 = Image.open('tic-tac-toe.png')
    test = ImageTk.PhotoImage(image1)
    Label(image=test, bg="yellow").place(x=370, y=10)

    # define variables
    clicked = True
    count = 0
    global playerX, playerO
    playerX=0
    playerO=0
    playerX_var=StringVar()
    playerO_var=StringVar()


    # note the score of player and show on display
    def PlayerScore():
        # Update score of player X and player O
        playerX_var.set('Player X : '+str(playerX))
        playerO_var.set('Player O : '+str(playerO))
        Label(root,text='SCORE',font='Helvetica 20 bold',height=1,width=6,bg="yellow", fg='blue').place(x=380,y=140)
        Label(root,textvariable=playerX_var,font='Helvetica 15 bold',height=1,width=9,bg="yellow").place(x=380,y=180)
        Label(root,textvariable=playerO_var,font='Helvetica 15 bold',height=1,width=9,bg="yellow").place(x=380,y=210)

    # disable all button wif player is win otherwise match is draw
    def disable_all_buttons():
        Label(root, text='Reset Game', font='Helvetica 15 bold', height=1, width=11, bg="yellow").place(x=85, y=360)
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        PlayerScore()

    # check if someone is won
    def CheckifWon():
        global winner, playerX, playerO
        winner=False

        # 1st Row
        global count, clicked
        if b1['text']=='X' and b2['text']=='X' and b3['text']=='X':
            b1.config(bg='red')
            b2.config(bg='red')
            b3.config(bg='red')
            winner=True
            playerX = playerX+1
            MsgBox.showinfo('Tic Tac Toe', 'Player X is win')
            disable_all_buttons()

        # 2nd Row
        if b4['text']=='X' and b5['text']=='X' and b6['text']=='X':
            b4.config(bg='red')
            b5.config(bg='red')
            b6.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe', 'Player X is win')
            playerX+=1
            disable_all_buttons()


        # 3rd Row
        if b7['text']=='X' and b8['text']=='X' and b9['text']=='X':
            b7.config(bg='red')
            b8.config(bg='red')
            b9.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe', 'Player X is win')
            playerX+=1
            disable_all_buttons()


        # 1st column
        if b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
            b1.config(bg='red')
            b4.config(bg='red')
            b7.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe', 'Player X is win')
            disable_all_buttons()
        # 2nd column
        if b2['text']=='X' and b5['text']=='X' and b8['text']=='X':
            b2.config(bg='red')
            b5.config(bg='red')
            b8.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player X is win')
            playerX+=1
            disable_all_buttons()
        # 3rd column
        if b3['text']=='X' and b6['text']=='X' and b9['text']=='X':
            b3.config(bg='red')
            b6.config(bg='red')
            b9.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player X is win')
            playerX+=1
            disable_all_buttons()

        # if 1 , 5, and 9 box is matching
        if b1['text']=='X' and b5['text']=='X' and b9['text']=='X':
            b1.config(bg='red')
            b5.config(bg='red')
            b9.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player X is win')
            playerX+=1
            disable_all_buttons()

        # if 3 , 5, and 7 box is matching
        if b3['text']=='X' and b5['text']=='X' and b7['text']=='X':
            b3.config(bg='red')
            b5.config(bg='red')
            b7.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player X is win')
            playerX+=1
            disable_all_buttons()

        # IF  O PLAYERS WINNER
        # 1st row
        if b1['text']=='O' and b2['text']=='O' and b3['text']=='O':
            b1.config(bg='red')
            b2.config(bg='red')
            b3.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player O is win')
            playerO += 1
            disable_all_buttons()
        # 2ND ROW
        if b4['text']=='O' and b5['text']=='O' and b6['text']=='O':
            b4.config(bg='red')
            b5.config(bg='red')
            b6.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player O is win')
            playerO += 1
            disable_all_buttons()

        if b7['text']=='O' and b8['text']=='O' and b9['text']=='O':
            b7.config(bg='red')
            b8.config(bg='red')
            b9.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player O is win')
            playerO += 1
            disable_all_buttons()

        if b1['text']=='O' and b4['text']=='O' and b7['text']=='O':
            b1.config(bg='red')
            b4.config(bg='red')
            b7.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player O is win')
            playerO += 1
            disable_all_buttons()

        if b2['text']=='O' and b5['text']=='O' and b8['text']=='O':
            b2.config(bg='red')
            b5.config(bg='red')
            b8.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player O is win')
            playerO += 1
            disable_all_buttons()

        if b3['text']=='O' and b6['text']=='O' and b9['text']=='O':
            b3.config(bg='red')
            b6.config(bg='red')
            b9.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe','Player O is win')
            playerO += 1
            disable_all_buttons()

        if b1['text']=='O' and b5['text']=='O' and b9['text']=='O':
            b1.config(bg='red')
            b5.config(bg='red')
            b9.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe', 'Player O is win')
            playerO += 1
            disable_all_buttons()

        if b3['text']=='O' and b5['text']=='O' and b7['text']=='O':
            b3.config(bg='red')
            b5.config(bg='red')
            b7.config(bg='red')
            winner=True
            MsgBox.showinfo('Tic Tac Toe', 'Player O is win')
            playerO += 1
            disable_all_buttons()

        if count > 8:
            MsgBox.showinfo('Tic Tac Toe', 'Match is Tie')
            disable_all_buttons()

    # Button clicked function
    def b_click(b):
        global clicked, count
        if b['text']==" " and clicked==True:
            b['text']='X'
            clicked=False
            count+=1
            Label(root, text='Player O turn ', font='Helvetica 15 bold', height=1, width=11, bg="yellow").place(x=85, y=360)
            CheckifWon()


        elif b['text']==' ' and clicked==False:
            b['text']='O'
            clicked=True
            count+=1
            Label(root, text='Player X turn', font='Helvetica 15 bold', height=1, width=11, bg="yellow").place(x=85, y=360)
            CheckifWon()

        else:
            MsgBox.showerror('Tic Tac Toe','Hey! this box is already selected \n pick Another one')

    # reset all value when user click on reset
    def reset():
        global clicked, count, playerX, playerO
        clicked = True
        count = 0
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, Reset_Button
        Label(root, text='Player X turn ', font='Helvetica 15 bold', height=1, width=11, bg="yellow").place(x=85, y=360)
        b1 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
        b3=Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font='Helvetica 20', height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    reset()
    PlayerScore()


    # reset button
    Reset_Button = Button(root, text = 'RESET', font='Helvetica 13 bold', height=1, width=17, bg="#4e5153", fg='#ffffff', command= reset)
    Reset_Button.place(x=350, y=260)
    # exit button
    Button(root, text='EXIT', font='Helvetica 12 bold', height=1, width=17,bg="#4e5153", fg='#ffffff', command=root.destroy).place(x=350, y=310)



    root.mainloop()



WithPlayer()
