from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage
root = Tk()
root.title("NewsPaper")
root.geometry("650x400")
root.maxsize(650,800 )

texts = []
photos = []
for i in range(0,2):
    with open(f"{i+1}.txt") as fw:
        text = fw.read()
        texts.append(text)
    image = Image.open(f"{i+1}.jpg")
    photos1 = resizeimage.resize_cover(image, [150, 150])
    photos.append(ImageTk.PhotoImage(photos1))
f1 = Frame(root, width=800, height=100)
Label(f1, text="Arvind's Newspaper", font= " lucida 28 bold", relief=SUNKEN). pack()
Label(f1, text="27,July 2020", font= " lucida 14 bold"). pack()
f1.pack()

f2 = Frame(root, width=800, height=400)
Label(f2, text=texts[0], padx= 22, pady = 20, relief=SUNKEN).pack(side="left")
Label(f2, image=photos[0], padx= 22, pady = 20, relief=SUNKEN).pack(side="left")
f2.pack(anchor='w')

f3 = Frame(root, width=800, height=200)

Label(f3, text=texts[1], padx= 22, pady = 20, relief=SUNKEN).pack(side="left")
Label(f3, image=photos[1], padx= 22, pady = 20, relief=SUNKEN).pack(side="left")
f3.pack(anchor='w')



root.mainloop()